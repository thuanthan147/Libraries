
# coding: utf-8

# In[59]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import argparse
import ast


# In[60]:


class get_page_table:
# Crawling data info in a webpage
    
    def __init__(self, url):
        # Initialize 
        self.url = url
        html_doc = requests.get(self.url)
        self.soup = bs(html_doc.text, 'lxml')
        
    def extract_table(self, flag=None):
        """
        Return a table in the page
        flag: a list contain 2 element: attribute and value
        
        Return:
            table: list
            table from the url with given flag
        """
        return_list = []
        
        if flag != None:
            try:
                table = self.soup.find('table',{flag[0]: flag[1]})
            except:
                print("Can't find table with given attribute")
                return []
        else:
            table = self.soup.findAll('table')
            if not table:
                print("Page doesn't have any table!")
                return []
        
        if str(type(table)) == "<class 'bs4.element.Tag'>":
            temp_table = []
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all('td')
                cols = [element.text.strip() for element in cols]  
                temp_table.append(cols)
            return_list.append(temp_table)
        else:
            for tabl in table:
                temp_table = []
                rows = tabl.find_all("tr")
                for row in rows:
                    cols = row.find_all('td')
                    cols = [element.text.strip() for element in cols]  
                    temp_table.append(cols)
                return_list.append(temp_table)
        return return_list
    
    def extract_page_table(self, write_down = False, flag=None):
        """ Extract all tables in a webpage, return list or write to csv
            write_down: bool
                if True, write to csv file
                else return a list
            flag: list of lists, which contain 2 element
                find all table contraining given attribute and value
        """
        final_table = []
        if flag != None:
            for pair in flag:
                table = self.extract_table(pair)
                if table:
                    count = 0
                    for tab in table:
                        count += 1
                        if write_down:
                            df = pd.DataFrame(tab)
                            df.to_csv(str(count) + ".csv")
                        else:
                            final_table.append(tab)
        else:
            table = self.extract_table(flag)
            if table:
                count = 0
                for tab in table:
                    count += 1
                    if write_down:
                        df = pd.DataFrame(tab)
                        df.to_csv(str(count) + ".csv")
                    else:
                        final_table.append(tab)
        if not write_down:
            return final_table
        else:
            return []


# In[69]:


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",help="Url you want to get the tables", type=str)
    parser.add_argument("--write_down",help="True: write down to file", type=bool)
    parser.add_argument("--flag",help="List of pairs of attribute and value of a specific table, ex: \[\['class','something'\]\], type=str",default=None)                    
    args = parser.parse_args()
    url = args.url
    write_down = args.write_down
    table_parser = get_page_table(url)
    try:
        flag = args.flag
        table_parser.extract_page_table(write_down, ast.literal_eval(flag))
    except:
        flag = None
        table_parser.extract_page_table(write_down, flag)


# In[70]:


if __name__ == "__main__":
    main()

