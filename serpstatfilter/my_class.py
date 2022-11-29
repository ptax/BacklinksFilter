import tkinter as tk
from tkinter import Tk
from tkinter import ttk

from tkinter import messagebox


class CreateSearch:
    def __init__(self):
        self.num_links = int(self.num_links)

    def get_num_links(self):
        max_size = 100
        if self.num_links <= 100:
            page = 1
            size = self.num_links
        elif self.num_links >= 101:
            size = 100
            page = self.num_links // max_size
        return {'page': page, 'size': size}


class FrameSearch(Tk):

    def __init__(self, MyData):
        self.draw_save_button()
        self.num_link = self.draw_selection_txt
        self.link_domain = self.select_filter(row=MyData['link_per_domain_row'],
                                              text=MyData['link_per_domain_text'],
                                              select_data=MyData['link_per_domain_select']
                                              )
        self.param_search_type = self.select_filter(row=MyData['param_search_type_row'],
                                                    text=MyData['param_search_type_text'],
                                                    select_data=MyData['param_search_type_select']
                                                    )
        self.params_sort = self.select_filter(row=MyData['params_sort_row'],
                                              text=MyData['params_sort_text'],
                                              select_data=MyData['params_sort_select']
                                              )
        self.order_sort = self.select_filter(row=MyData['order_sort_row'],
                                             text=MyData['order_sort_text'],
                                             select_data=MyData['order_sort_select']
                                             )


        self.dict_complex_filter = {}
        self.count_custom_filter = 0
        self.count_group = 0
        self.group_name = ''
    def draw_selection_txt(self):
        self.set_label('How many backlinks can you get?:', row=1, bg='light gray')
        self.num_link = tk.Entry(width=10)
        self.num_link.grid(row=1, column=1, sticky='w')
        if self.num_link.get() == '':
            self.num_link.insert(0, 100)
        return self.num_link.get()

    @staticmethod
    def set_label(text, row, bg):
        return ttk.Label(text=f"{text}", background=f'{bg}', width=30).grid(column=0, row=row, padx=1, pady=5)

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

        print('333', self.num_link.get())
        print('555', self.link_domain.get())
        print('666', self.param_search_type.get())
        print('777', self.params_sort.get())
        print('888', self.order_sort.get())
        #print('999', self.complex_filter.get())
        print('dict_complex_filter', self.dict_complex_filter)
        dict_or = {}
        list_or = []
        list_and = []
        #dict_or[f'{name_group}'] =
        print ('dddddddddddd',self.dict_complex_filter)
        for items, values in self.dict_complex_filter.items():
            print('values,LEN', len(values))
            name_filter = list(values.keys())[2]

            compareType = values[f'{name_filter}'][0].get()
            name_group = values['Group']
            print ('name_group',name_group)

            values_filter = values[f'{name_filter}'][1].get()
            print ('valuessssssssssssssss', values['Type'])

            t = {"field": f"{name_filter}", "compareType": f"{compareType}", "value": [f"{values_filter}"]}
            print ('select_or_and',select_or_and.get())
            print ('ttttttttt',t)
            list_or.append({name_group:t})
            #dict_or[f'{name_group}'] = t
            try:
                dict_or[f'{name_group}'].append([t])
            except KeyError:
                dict_or[f'{name_group}'] = [t]
        print ('dict_or', dict_or)

    def select_filter(self, row, text, select_data):
        self.set_label(f'{text}', row=row, bg='light gray')
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=70, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row)
        select_filter.bind("<<ComboboxSelected>>", lambda event:self.add_complex_filter(event))
        select_filter.current()
        return select_filter

    def groups_filter(self):

        self.count_group += 1
        self.group_name = f'group_{self.count_group}'
        print ('AAAA',self.count_group ,self.group_name ,self.count_custom_filter)
        #self.set_label(f'Group {self.count_group}', row=10+self.count_custom_filter, bg='light gray')

        if self.count_group == 1:
            self.complex_filter = self.select_filter(row=10+self.count_custom_filter,
                                                     text=MyData['complex_filter_text'],
                                                     select_data=MyData['complex_filter_select']
                                                     )
        if self.count_group > 1:
            self.set_label(f'Group {self.count_group} Choose [OR AND]', row=11+self.count_custom_filter+self.count_group, bg='light gray')
            global select_or_and
            select_or_and = ttk.Combobox(width=70)
            select_or_and['values'] = ['AND', 'OR']
            select_or_and.grid(column=1, row=11+self.count_custom_filter+self.count_group)
            print ('Gde',11+self.count_custom_filter)

        #self.add_complex_filter

    def complex_select_filter(self, row, text, select_data, Type='OR'):
        lab = ttk.Label(text=f"{text}", width=30)
        lab.grid(column=0, row=row, padx=0, pady=0)
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=26, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row, padx=5, pady=5, sticky='w')
        value = tk.Entry(root, width=10)
        value.grid(row=row, column=1, sticky='E', padx=190, pady=0)

        def callback(event):
            if 'between' in event.widget.get():
                value.config(background="yellow", foreground="red")
                value.insert('end', 'Start:End')
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
            btn_plus.grid_remove()
            #self.dict_complex_filter.pop(str(select_filter))

        btn_plus = tk.Button(text='+', command=lambda: self.add_complex_filter(Type='OR'), width=1, height=1, bg='red')
        btn_plus.grid(row=row, column=1, padx=50, pady=0, sticky='E')
        btn = tk.Button(text='x', command=del_grid, width=1, height=1, bg='red')
        btn.grid(row=row, column=1, padx=5, pady=0, sticky='E')
        return select_filter, value

    def add_complex_filter(self, Type='OR'):
        rows = 10
        self.count_custom_filter += 1
        if '{url_from}' in self.complex_filter.get():

            data_grid = self.complex_select_filter(rows + self.count_custom_filter+self.count_group,
                                                   f'{self.group_name} Url from:',
                                                   MyData['complex_filter_url_from_select'], Type)
            print ('data_gridfffff',data_grid)
            self.dict_complex_filter[str(data_grid)] = {'Type':Type, 'Group': self.group_name, 'url_from': data_grid}

        elif '{anchor}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter+self.count_group,
                                                   f'{self.group_name} Anchor from:',
                                                   MyData['complex_filter_anchor_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type':Type, 'Group':self.group_name, 'anchor': data_grid}
        elif '{links_external}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter+self.count_group,
                                                   f'{self.group_name} Links_external:',
                                                   MyData['complex_filter_links_external_select'], Type)
            self.dict_complex_filter[str(data_grid)] = {'Type':Type, 'Group':self.group_name, 'links_external': data_grid}

    def draw_save_button(self):
        tk.Button(text="Apply", command=self.validate, bg='black', fg='white').grid(row=7, column=1, padx=10, pady=10,
                                                                                    sticky='W')
        tk.Button(text="Add New filtets", command=self.groups_filter, bg='blue', fg='white').grid(row=8,
                                                                                                     column=1,
                                                                                                     padx=0,
                                                                                                     pady=0,
                                                                                                     sticky='W')




if __name__ == "__main__":
    # MySearch = CreateSearch(num_links='200')
    # print(MySearch.get_num_links())

    root = tk.Tk()
    root.title("Scrollbar Test")
    root.geometry("800x400")
    root.configure(background="light gray")

    link_per_domain_select = '{0} - in the ascending order', '{1} - in the descending order'
    param_search_type_select = '{url} - the specific URL (site.com/path/)', '{part_url} - URL starts with (site.com/path/*)', '{domain} - only domain (site.com)', '{domain_with_subdomains} - domain with subdomains (subdomain.site.com)'
    params_sort_select = '{check} - date of the first detection', '{url_from} - the referring page', '{anchor} - the anchor of the backlink', '{link_nofollow} - link attributes', '{links_external} - a number of outgoing links from the referring page', '{link_type} - the type of incoming link', '{url_to} - a landing page'
    order_sort_select = '{asc} - in the ascending order', '{desc} - in the descending order'
    complex_filter_select = '{url_from} - the referring page', '{anchor} - the anchor of the backlink', '{links_external} - the number of external links from the referring page', '{link_type} - the type of the backlink. Possible values: text, redirect, iframe, form, canonical, rss, alternate, image'
    complex_filter_select_url_from = '{contains} - contains (text value)', '{notContains} - does not contain (text value)', '{startsWith} - starts with (text value)', '{endsWith} - ends with (text value)'
    complex_filter_select_anchor = '{contains} - contains (text value)', '{notContains} - does not contain (text value)', '{startsWith} - starts with (text value)', '{endsWith} - ends with (text value)'
    complex_filter_select_links_external = '{gt} - greater than (number value)', '{lt} - less than (number value)', '{gte} - greater than or equal (number value)', '{lte} - less than or equal (number value)', '{eq} - exact match (number or text value)', '{between} - between (number value):'

    MyData = {'link_per_domain_row': 2, 'link_per_domain_text': 'Select the order of the backlinks:',
              'link_per_domain_select': link_per_domain_select,
              'param_search_type_row': 3, 'param_search_type_text': 'Select the type of search:',
              'param_search_type_select': param_search_type_select,
              'params_sort_row': 4, 'params_sort_text': 'Select the sorting parameter:',
              'params_sort_select': params_sort_select, 'order_sort_row': 5,
              'order_sort_text': 'Select the order of sorting:', 'order_sort_select': order_sort_select,
              'complex_filter_row': 9, 'complex_filter_text': 'Select the complex filter:',
              'complex_filter_select': complex_filter_select,
              'complex_filter_url_from_select': complex_filter_select_url_from,
              'complex_filter_anchor_select': complex_filter_select_anchor,
              'complex_filter_links_external_select': complex_filter_select_links_external,
              'groups_filter_row': 10, 'groups_filter_text': 'Create_group_filter:',
              }

    # print(MyData['link_per_domain_select'])
    MyFrame = FrameSearch(MyData)
    input_init = MyFrame.draw_selection_txt()

    print(MyFrame)
    ttk.Label(root, text="Complex Filter",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=6, column=1)
    # cmb = ttk.Combobox(root, width="10", values=("prova", "ciao", "come", "stai"))
    root.mainloop()
