import tkinter as tk
from tkinter import ttk
import serpstatfilter.anchor as anchor
import serpstatfilter.url_from as url_from
import serpstatfilter.params_searchtype as params_searchtype
import serpstatfilter.params_sort as params_sort
import serpstatfilter.order_sort as order_sort
import serpstatfilter.parametr_link_per_domain as parametr_link_per_domain
import serpstatfilter.params_num_link as params_num_link
import serpstatfilter.custum_filter_choice as custum_filter_choice
import serpstatfilter.links_external as links_external
import serpstatfilter.link_nofollow as link_nofollow
import serpstatfilter.link_type as link_type
import tkinter as tk
import json
import re
from tkinter.filedialog import askopenfilename



list_custom_filter = []
count_custom_filter = 0
cunt_uniq_link_nofollow = 0

def Look_Custum_Filter():
    global cunt_uniq_link_nofollow
    global count_custom_filter
    num_colum = 10
    MAX_NUM = 24  # Maximum number of entries
    if count_custom_filter < MAX_NUM:
        if '{url_from}' in custum_filter_select.get():
            type_filer = 'url_from'
            list_custom_filter.append(url_from.CustumFileter_url_from(root,num_colum,count_custom_filter,type_filer))
            list_custom_filter[-1]
            count_custom_filter += 1
        elif '{anchor}' in custum_filter_select.get():
            type_filer = 'anchor'
            list_custom_filter.append(anchor.CustumFileter_anhor(root,num_colum,count_custom_filter,type_filer))
            list_custom_filter[-1]
            count_custom_filter += 1
        elif '{links_external}' in custum_filter_select.get():
            type_filer = 'links_external'
            list_custom_filter.append(links_external.CustumFileter_links_external(root,num_colum,count_custom_filter,type_filer))
            list_custom_filter[-1]
            count_custom_filter += 1
        elif '{link_type}' in custum_filter_select.get():
            type_filer = 'link_type'
            list_custom_filter.append(link_type.CustumFileter_link_type(root,num_colum,count_custom_filter,type_filer))
            list_custom_filter[-1]
            count_custom_filter += 1

        elif '{link_nofollow}' in custum_filter_select.get():
            cunt_uniq_link_nofollow += 1
            print (cunt_uniq_link_nofollow)
            if cunt_uniq_link_nofollow == 1:
                type_filer = 'link_nofollow'
                list_custom_filter.append(link_nofollow.CustumFileter_link_nofollow(root, num_colum, count_custom_filter,type_filer))
                list_custom_filter[-1]
                count_custom_filter += 1
            else:
                pass

def clear_params_select(string):
    if len(string) >= 5:
        str = re.findall(r'\{(.+?)\}', string)[0]
        return str
    else:
        pass


def get_data():
    # SET how links domain we need
    num = params_num_link.Num_link.get()
    num_backlinks =  params_num_link.get_link_per_domain(num)
    page = num_backlinks['page']
    size = num_backlinks['size']
    searchType = clear_params_select(params_searchtype.searchTypechoosen.get())
    sort = clear_params_select(params_sort.sortchoosen.get())
    order = clear_params_select(order_sort.orderchoosen.get())
    linkPerDomain = int(clear_params_select(parametr_link_per_domain.linkperdomainchoosen.get()))
    global my_json
    my_json = {
        "id": 1,
        "method": "SerpstatBacklinksProcedure.getNewBacklinks",
            "params": {
                "query": "{domain}",
                "searchType": f"{searchType}",
                "sort": f"{sort}",
                "order": f"{order}",
                "page":f"{page}",
                "size": f"{size}",
                "linkPerDomain": f"{int(linkPerDomain)}"
            }
    }

    print (my_json)
    #for i in Look_Url_From_Filter:
        #print ('Url_From',i[0].get(),i[1].get())
    #for i in entries_anhor:
        #print ('Anhor',i[0].get(),i[1].get())


    Format_List_Custom_Filter = []
    for custup_filter in list_custom_filter:
        print ('custup_filtervvvvvvvvvvv',custup_filter)
        field = custup_filter[0]
        try:
            value = custup_filter[2].get()
        except IndexError:
            value = None
        compareType =  clear_params_select(custup_filter[1].get())

        if value:
            data_CompexFilter =  {"field": f"{field}","compareType": f"{compareType}", f"value": [f"{value.strip()}"]}
            Format_List_Custom_Filter.append(data_CompexFilter)

    if Format_List_Custom_Filter:
        my_json['params']['complexFilter'] = [Format_List_Custom_Filter]
        print (my_json)
    save_file_button = tk.Button(root, text='Save file', command=lambda:save_result(my_json), bg='green', fg='white')
    save_file_button.grid(column=1, row=23, padx=80, pady=10, sticky='w')





def default_params():
    pass
    #Num_link.insert(0,"100")
    #linkperdomainchoosen.insert(0,"{0} - in the ascending order")
    #print ('entries_url_from',entries_url_from)
    #if len(entries_url_from) > 1:
        #print ('ffffffffffff')
        #for i in entries_url_from:
            #print ('ooo',i)
            #i[0].insert(0,"{contains} - contains (text value)")
            #i[1].insert(0,"{contains} - contains (text value)")
def update_scrollregion(event):
    photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

def save_result(save_data):
    try:
        with tk.filedialog.asksaveasfile(mode='w', defaultextension=".json") as file:
            save_file = json.dump(save_data, file, indent=4)
    except AttributeError:
        # if user cancels save, filedialog returns None rather than a file object, and the 'with' will raise an error
        print("The user cancelled save")


def app():
    global root
    root = tk.Tk()
    #windows.title("Backlinks Exstractor Serpstat API")
    #windows.geometry("900x600")




    photoFrame = tk.Frame(root, width=11, height=1, bg="#EBEBEB")
    photoFrame.grid()
    photoFrame.rowconfigure(0, weight=1, )
    photoFrame.columnconfigure(0, weight=1)

    global photoCanvas
    photoCanvas = tk.Canvas(photoFrame, bg="#EBEBEB", width=900, height=600)
    photoCanvas.grid(row=0, column=0, sticky="nsew")

    root = tk.Frame(photoCanvas, bg="#EBEBEB")
    photoCanvas.create_window(0, 0, window=root, anchor='nw')

    # label text for title

    ttk.Label(root, text="Creating a request to the Serpastat API",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=0, column=1)




    params_num_link.params_num_link(root, num_colum=1, num_row=2)

    parametr_link_per_domain.parametr_link_per_domain(root, num_colum=1, num_row=3)

    params_searchtype.params_searchtype(root, num_colum=1, num_row=4)

    params_sort.params_sort(root, num_colum=1, num_row=5)
    order_sort.order_sort(root, num_colum=1, num_row=6)

    # label text for title
    ttk.Label(root, text="Complex Filter",
              background='green', foreground="white",
              font=("Times New Roman", 15)).grid(row=7, column=1)

    #complexfilter_add(root, num_colum=1, num_row=8)

    #custum_fileter_url_from()



    #tk.Button(root, text="default_params", command=default_params).grid(row=24, column=1, padx=10, pady=10)


    tk.Button(root, text="Aply Filter", command=get_data, bg='red', fg='white').grid(row=23, column=1, padx=10, pady=10, sticky='w')




    photoScroll = tk.Scrollbar(photoFrame, orient=tk.VERTICAL)
    photoScroll.config(command=photoCanvas.yview)
    photoCanvas.config(yscrollcommand=photoScroll.set)
    photoScroll.grid(row=0, column=1, sticky="ns")




    #Custup Filter Choice
    global custum_filter_select


    tk.Button(root, text="Get Filter", command=Look_Custum_Filter, bg='black', fg='white', width=25).grid(row=8, column=1, padx=10, pady=10)
    custum_filter_select = custum_filter_choice.custum_filter_choice(root, num_colum=1, num_row=9)

    root.bind("<Configure>", update_scrollregion)

    root.mainloop()



if __name__ == "__main__":
    app()
