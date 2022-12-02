import tkinter as tk
from tkinter import Tk
from tkinter import ttk

from tkinter import messagebox
import re
import json
from tkinter.filedialog import askopenfilename


def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

class FrameSearch(Tk):

    def __init__(self, MyData):
        self.check_gird_create = []
        self.draw_save_button()
        self.num_link = self.static_select
        self.link_domain = self.static_select(row=MyData['link_per_domain_row'],
                                              text=MyData['link_per_domain_text'],
                                              select_data=MyData['link_per_domain_select']
                                              )
        self.param_search_type = self.static_select(row=MyData['param_search_type_row'],
                                                    text=MyData['param_search_type_text'],
                                                    select_data=MyData['param_search_type_select']
                                                    )
        self.params_sort = self.static_select(row=MyData['params_sort_row'],
                                              text=MyData['params_sort_text'],
                                              select_data=MyData['params_sort_select']
                                              )
        self.order_sort = self.static_select(row=MyData['order_sort_row'],
                                             text=MyData['order_sort_text'],
                                             select_data=MyData['order_sort_select']
                                             )
        self.complex_filter = self.select_filter(row=10,
                                                 text=MyData['complex_filter_text'],
                                                 select_data=MyData['complex_filter_select']
                                                 )
        self.complex_filter_and = False
        self.dict_complex_filter = {}
        self.count_custom_filter = 0
        self.count_group = 0
        self.group_name = ''
        self.select_or_and = ''
        self.draw_selection_txt()

    def draw_selection_txt(self):
        self.set_label('How many backlinks can you get?:', row=1, bg='light gray')
        self.num_link = tk.Entry(width=10)
        self.num_link.grid(row=1, column=1, sticky='w')
        if self.num_link.get() == '':
            self.num_link.insert(0, 100)
        return self.num_link.get()

    @staticmethod
    def save_result(save_data):
        try:
            with tk.filedialog.asksaveasfile(mode='w', defaultextension=".json") as file:
                save_file = json.dump(save_data, file, indent=4)
        except AttributeError:
            # if user cancels save, filedialog returns None rather than a file object, and the 'with' will raise an error
            print("The user cancelled save")
    @staticmethod
    def set_label(text, row, bg):
        return ttk.Label(text=f"{text}", background=f'{bg}', width=30).grid(column=0, row=row, padx=1, pady=5)

    @staticmethod
    def clear_params_select(my_str):
        if len(my_str) >= 5:
            my_str = re.findall(r'\{(.+?)\}', my_str)[0]
            return my_str
        else:
            pass

    def validate(self):

        try:
            int(self.num_link.get())
        except ValueError:
            self.set_label('Numerical values only:', row=1, bg='red')
        else:
            rest = str(int(self.num_link.get()) / 100).split('.')
            if int(self.num_link.get()) <= 99:
                self.set_label('How many backlinks can you get?:', row=1, bg='light gray')
            elif int(rest[1]) == 0:
                self.set_label('How many backlinks can you get?:', row=1, bg='light gray')
            else:
                self.set_label('Only numbers divisible by 100:', row=1, bg='red')

        max_size = 100
        if int(self.num_link.get()) <= 100:
            page = 1
            size = int(self.num_link.get())
        elif self.num_link.get() >= 101:
            size = 100
            page = int(self.num_link.get()) // max_size

        print('order_sort', self.order_sort.get())
        print('dict_complex_filter', self.dict_complex_filter)
        list_or = []
        list_and = []
        link_per_domain = {self.clear_params_select(self.link_domain.get())}
        link_per_domain = str(link_per_domain).replace('\'','').replace('{','').replace('}','')
        my_json = {
            "id": 1,
            "method": "SerpstatBacklinksProcedure.getNewBacklinks",
            "params": {
                "query": "{domain}",
                "searchType": f"{self.clear_params_select(self.param_search_type.get())}",
                "sort": f"{self.clear_params_select(self.params_sort.get())}",
                "order": f"{self.clear_params_select(self.order_sort.get())}",
                "page": f"{int(page)}",
                "size": f"{int(size)}",
                "linkPerDomain": f"{int(link_per_domain)}"
            }
        }
        for items, values in self.dict_complex_filter.items():
            name_filter = list(values.keys())[2]
            compareType = self.clear_params_select(values[f'{name_filter}'][0].get())
            values_filter = values[f'{name_filter}'][1].get()
            print('compareType', compareType)
            print('compareTypesafsafs', values[f'{name_filter}'][0].get())
            if 'between' in str(compareType) or 'link_nofollow' in str(values[f'{name_filter}'][0].get()):
                values_filter = values_filter.split(':')
                values_filter = [x.strip() for x in values_filter]
            else:
                values_filter = [values_filter]

            if values['Type'] == 'OR':
                if len(values_filter) != 0:
                    t = {"field": f"{name_filter}", "compareType": f"{compareType}", "value": values_filter}
                    list_or.append(t)
            elif values['Type'] == 'AND':
                if len(values_filter) != 0:
                    t = {"field": f"{name_filter}", "compareType": f"{compareType}", "value": values_filter}
                    list_and.append(t)
        if list_and:
            my_json['params']['complexFilter'] = [list_or,list_and]
        elif list_or:
            my_json['params']['complexFilter'] = [list_or]

        save_file_button = tk.Button(root, text='Save file', command=lambda: self.save_result(my_json), bg='green',
                                     fg='white')
        save_file_button.grid(column=1, row=7, padx=80, pady=10, sticky='w')
        return my_json

    def static_select(self, row, text, select_data):
        self.set_label(f'{text}', row=row, bg='light gray')
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=70, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row)
        select_filter.current()
        return select_filter

    def select_filter(self, row, text, select_data):
        self.set_label(f'{text}', row=row, bg='light gray')
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=70, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row)

        def callback(event):
            if len(self.check_gird_create) == 0:
                self.add_complex_filter(Type='OR')
            else:
                pass

        select_filter.bind("<<ComboboxSelected>>", lambda event: callback(event))
        select_filter.current()

        def callback_and():
            if len(self.check_gird_create) == 0:
                self.groups_filter()
            else:
                pass

        tk.Button(text="AND", command=callback_and, bg='blue', fg='white').grid(row=10, column=3, padx=0, pady=0,
                                                                                sticky='W')
        return select_filter

    def select_filter_and(self, row, select_data):

        # self.set_label(f'{text}', row=row, bg='light gray')
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=70, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row)

        select_filter.bind("<<ComboboxSelected>>", lambda event: self.add_complex_filter(Type='AND'))
        select_filter.current()
        return select_filter

    def groups_filter(self):

        self.count_group += 1
        self.check_gird_create.append(self.count_group)
        self.group_name = f'group_{self.count_group}'
        print('AAAA', self.count_group, self.group_name, self.count_custom_filter)

        # self.set_label(f'Group {self.count_group}', row=10+self.count_custom_filter, bg='light gray')
        def del_grid():
            # self.select_or_and.grid_remove()
            self.complex_filter_and.grid_remove()
            lab.grid_remove()
            btn.grid_remove()
            self.check_gird_create.pop()
            # self.count_custom_filter = self.count_custom_filter - 1
            # self.count_group = self.count_group - 1

        lab = ttk.Label(text=f"Add Select AND", width=30, background='green')
        lab.grid(column=0, row=11 + self.count_custom_filter + self.count_group, padx=1, pady=5)
        self.complex_filter_and = self.select_filter_and(row=11 + self.count_custom_filter + self.count_group,
                                                         select_data=MyData['complex_filter_select']
                                                         )
        print('Gde', 11 + self.count_custom_filter)
        btn = tk.Button(text='x', command=lambda: del_grid(), width=1, height=1, bg='red')
        btn.grid(row=11 + self.count_custom_filter + self.count_group, column=2, padx=5, pady=0, sticky='E')

    def complex_select_filter(self, row, text, select_data, Type):

        lab = ttk.Label(text=f"{text} {Type} ", width=30)
        lab.grid(column=0, row=row, padx=0, pady=0)
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=30, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row, padx=5, pady=5, sticky='w')
        value = tk.Entry(root, width=35)
        value.grid(row=row, column=1, sticky='E', padx=20, pady=0)

        def callback(event):
            if 'between' in event.widget.get():
                value.config(background="yellow", foreground="red")
                value.insert('end', 'Start:End')
            elif 'link_nofollow' in event.widget.get():
                value.config(background="yellow", foreground="red")
                value.insert('end', 'follow:nofollow:ugc:sponsored')
            elif 'link_type' in event.widget.get():
                value.config(background="yellow", foreground="red")
                value.insert('end', 'Only one parameter or: text, redirect, iframe, form, canonical, rss, alternate, image')
            else:
                value.config(background="white", foreground="black")
                value.delete(0, 'end')



        select_filter.bind("<<ComboboxSelected>>", callback)

        def del_grid():
            select_filter.grid_remove()
            btn.grid_remove()
            lab.grid_remove()
            value.grid_remove()
            btn.grid_remove()
            self.count_custom_filter = self.count_custom_filter - 1

        btn = tk.Button(text='x', command=del_grid, width=1, height=1, bg='red')
        btn.grid(row=row, column=1, padx=5, pady=0, sticky='E')
        return select_filter, value

    def add_complex_filter(self, Type='OR'):
        rows = 11
        self.count_custom_filter += 1
        # print ('self.complex_filter_and',self.complex_filter_and)
        print('self.check_gird_create', self.check_gird_create, len(self.check_gird_create))

        if '{url_from}' in self.complex_filter.get():

            data_grid = self.complex_select_filter(rows + self.count_custom_filter + self.count_group,
                                                   f'{self.group_name} Url from:',
                                                   MyData['complex_filter_url_from_select'], Type)
            print('data_gridfffff', data_grid)
            self.dict_complex_filter[str(data_grid)] = {'Type': Type, 'Group': self.group_name, 'url_from': data_grid}

        elif '{anchor}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter + self.count_group,
                                                   f'{self.group_name} Anchor from:',
                                                   MyData['complex_filter_anchor_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type': Type, 'Group': self.group_name, 'anchor': data_grid}
        elif '{link_nofollow}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter + self.count_group,
                                                   f'{self.group_name} Link nofollow:',
                                                   MyData['complex_filter_select_link_nofollow_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type': Type, 'Group': self.group_name, 'link_nofollow': data_grid}


        elif '{links_external}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter + self.count_group,
                                                   f'{self.group_name} Links_external:',
                                                   MyData['complex_filter_links_external_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type': Type, 'Group': self.group_name,
                                                        'links_external': data_grid}
        elif '{link_type}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter + self.count_group,
                                                   f'{self.group_name} Link_type:',
                                                   MyData['complex_filter_link_type_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type': Type, 'Group': self.group_name, 'link_type': data_grid}
        elif '{check}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter + self.count_group,
                                                   f'{self.group_name} Detection date:',
                                                   MyData['complex_filter_date_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type': Type, 'Group': self.group_name, 'check': data_grid}

    def draw_save_button(self):
        tk.Button(text="Apply", command=self.validate, bg='black', fg='white').grid(row=7, column=1, padx=10, pady=10,
                                                                                    sticky='W')


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrollbar Test")
    root.geometry("800x400")
    root.bind_all("<Key>", _onKeyRelease, "+")

    root.configure(background="light gray")

    link_per_domain_select = '{0} - in the ascending order', '{1} - in the descending order'
    param_search_type_select = '{url} - the specific URL (site.com/path/)', '{part_url} - URL starts with (site.com/path/*)', '{domain} - only domain (site.com)', '{domain_with_subdomains} - domain with subdomains (subdomain.site.com)'
    params_sort_select = '{check} - date of the first detection', '{url_from} - the referring page', '{anchor} - the anchor of the backlink', '{link_nofollow} - link attributes', '{links_external} - a number of outgoing links from the referring page', '{link_type} - the type of incoming link', '{url_to} - a landing page'
    order_sort_select = '{asc} - in the ascending order', '{desc} - in the descending order'

    complex_filter_select = '{url_from} - the referring page', '{anchor} - the anchor of the backlink','{link_nofollow} - link attributes. Possible values: follow, nofollow, ugc, sponsored', '{links_external} - the number of external links from the referring page', '{link_type} - the type of the backlink. Possible values: text, redirect, iframe, form, canonical, rss, alternate, image',  '{check} - link detection date. Value format: DD.MM.YYYY (01.01.2001)'
    complex_filter_select_url_from = '{contains} - contains (text value)', '{notContains} - does not contain (text value)', '{startsWith} - starts with (text value)', '{endsWith} - ends with (text value)'
    complex_filter_select_anchor = '{contains} - contains (text value)', '{notContains} - does not contain (text value)', '{startsWith} - starts with (text value)', '{endsWith} - ends with (text value)'
    complex_filter_select_links_external = '{gt} - greater than (number value)', '{lt} - less than (number value)', '{gte} - greater than or equal (number value)', '{lte} - less than or equal (number value)', '{eq} - exact match (number or text value)', '{between} - between (number value):'
    complex_filter_select_link_nofollow = '{contains} - contains (text value) link_nofollow', '{notContains} - does not contain (text value) link_nofollow'
    complex_filter_select_link_type = '{eq} - exact match (number or text value) link_type', '{neq} - does not meet the requirement (number or text value) link_type'
    complex_filter_select_date = '{gt} - greater than (number value)', '{lt} - less than (number value)', '{gte} - greater than or equal (number value)', '{lte} - less than or equal (number value)', '{eq} - exact match (number or text value)', '{between} - between (number value):'

    MyData = {'link_per_domain_row': 2, 'link_per_domain_text': 'Select the order of the backlinks:',
              'link_per_domain_select': link_per_domain_select,
              'param_search_type_row': 3, 'param_search_type_text': 'Select the type of search:',
              'param_search_type_select': param_search_type_select,
              'params_sort_row': 4, 'params_sort_text': 'Select the sorting parameter:',
              'params_sort_select': params_sort_select, 'order_sort_row': 5,
              'order_sort_text': 'Select the order of sorting:', 'order_sort_select': order_sort_select,
              'complex_filter_row': 9, 'complex_filter_text': 'Select the complex filter OR:',
              'complex_filter_select': complex_filter_select,
              'complex_filter_url_from_select': complex_filter_select_url_from,
              'complex_filter_anchor_select': complex_filter_select_anchor,
              'complex_filter_links_external_select': complex_filter_select_links_external,
              'complex_filter_select_link_nofollow_select': complex_filter_select_link_nofollow,
              'complex_filter_link_type_select': complex_filter_select_link_type,
              'complex_filter_date_select': complex_filter_select_date,
              'groups_filter_row': 10, 'groups_filter_text': 'Create_group_filter:',
              }

    MyFrame = FrameSearch(MyData)

    ttk.Label(root, text="Complex Filter",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=6, column=1)
    # cmb = ttk.Combobox(root, width="10", values=("prova", "ciao", "come", "stai"))
    root.mainloop()
