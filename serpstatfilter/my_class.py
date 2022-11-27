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
        self.complex_filter = self.select_filter(row=MyData['complex_filter_row'],
                                                 text=MyData['complex_filter_text'],
                                                 select_data=MyData['complex_filter_select']
                                                 )

        self.dict_complex_filter = {}
        self.count_custom_filter = 0
        self.value_between = None

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
        print('999', self.complex_filter.get())
        print ('dict_complex_filter',self.dict_complex_filter)

        for items, values in self.dict_complex_filter.items():
            print('000', items, values)
            #print ('111', values['links_external'][0].get(), values['links_external'][1].get())
            print ('links_external',values['links_external'][0].get(), values['links_external'][1].get())

    def select_filter(self, row, text, select_data):
        self.set_label(f'{text}', row=row, bg='light gray')
        n = tk.StringVar()
        select_filter = ttk.Combobox(width=70, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row)
        select_filter.current()
        return select_filter


    def complex_select_filter(self, row, text, select_data):

        lab = ttk.Label(text=f"{text}", width=30)
        lab.grid(column=0, row=row, padx=0, pady=0)
        n = tk.StringVar()

        select_filter = ttk.Combobox(width=26, textvariable=n)
        select_filter['values'] = select_data
        select_filter.grid(column=1, row=row, padx=5, pady=5, sticky='w')
        select_filter.current()

        value = tk.Entry(root, width=10)
        value.grid(row=row, column=1, sticky='E', padx=190, pady=0)

        def del_grid():
            select_filter.grid_remove()
            btn.grid_remove()
            lab.grid_remove()
            value.grid_remove()
            self.dict_complex_filter.pop(str(select_filter))

        btn = tk.Button(text='x', command=del_grid, width=1, height=1, bg='red')
        btn.grid(row=row, column=1, padx=5, pady=0, sticky='E')

        return select_filter, value


    def add_complex_filter(self):
        rows = 10
        self.count_custom_filter += 1
        if '{url_from}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter, f'{self.count_custom_filter} URL from complexFilter:', MyData['complex_filter_url_from_select'])
            self.dict_complex_filter[str(data_grid)] = {'url_from':data_grid}
        elif '{anchor}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter, f'{self.count_custom_filter} Anchor from complexFilter:', MyData['complex_filter_anchor_select'])
            self.dict_complex_filter[str(data_grid)] = {'anchor':data_grid}
        elif '{links_external}' in self.complex_filter.get():
            data_grid = self.complex_select_filter(rows + self.count_custom_filter, f'{self.count_custom_filter} Links_external:', MyData['complex_filter_links_external_select'])
            self.dict_complex_filter[str(data_grid)] = {'links_external':data_grid}


    def draw_save_button(self):
        tk.Button(text="Apply", command=self.validate, bg='black', fg='white').grid(row=6, column=1, padx=10, pady=10, sticky='W')
        tk.Button(text="Add Complex Filter", command=self.add_complex_filter, bg='green', fg='white').grid(row=7, column=1, padx=0, pady=0, sticky='WE')


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
    complex_filter_select_url_from = '{url_from} - the referring page', '{anchor} - the anchor of the backlink', '{links_external} - the number of external links from the referring page', '{link_type} - the type of the backlink. Possible values: text, redirect, iframe, form, canonical, rss, alternate, image'
    complex_filter_select_anchor = '{contains} - contains (text value)', '{notContains} - does not contain (text value)', '{startsWith} - starts with (text value)','{endsWith} - ends with (text value)'
    complex_filter_select_links_external = '{gt} - greater than (number value)', '{lt} - less than (number value)', '{gte} - greater than or equal (number value)', '{lte} - less than or equal (number value)', '{eq} - exact match (number or text value)', '{between} - between (number value):'

    MyData = {'link_per_domain_row': 2, 'link_per_domain_text': 'Select the order of the backlinks:',
              'link_per_domain_select': link_per_domain_select,
              'param_search_type_row': 3, 'param_search_type_text': 'Select the type of search:',
              'param_search_type_select': param_search_type_select,
              'params_sort_row': 4, 'params_sort_text': 'Select the sorting parameter:',
              'params_sort_select': params_sort_select, 'order_sort_row': 5,
              'order_sort_text': 'Select the order of sorting:', 'order_sort_select': order_sort_select,
              'complex_filter_row': 8, 'complex_filter_text': 'Select the complex filter:', 'complex_filter_select': complex_filter_select,
              'complex_filter_url_from_select': complex_filter_select_url_from,
              'complex_filter_anchor_select': complex_filter_select_anchor,
              'complex_filter_links_external_select': complex_filter_select_links_external
              }

    # print(MyData['link_per_domain_select'])
    MyFrame = FrameSearch(MyData)
    input_init = MyFrame.draw_selection_txt()

    #ttk.Label(root, text="Complex Filter",
              #background='green', foreground="white",
              #font=("Times New Roman", 15)).grid(row=8, column=1)
    cmb = ttk.Combobox(root, width="10", values=("prova", "ciao", "come", "stai"))

    root.mainloop()
