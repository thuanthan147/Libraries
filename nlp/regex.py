
# coding: utf-8

# In[1]:


import csv


# In[2]:


with open("Data/utf-8_1.csv", 'r') as f:
    reader = csv.reader(f)
    utf8_list = list(reader)


# In[3]:


with open("Data/utf-8_2.csv", 'r') as f:
    reader = csv.reader(f)
    utf8_list_2 = list(reader)


# In[4]:


utf2 = utf8_list_2[1:]
utf2 = [i[1:] for i in utf2]


# In[5]:


utf = utf8_list[1:]


# In[6]:


utf = [i[1:] for i in utf]


# In[7]:


utf = utf + utf2


# In[16]:


print(utf[500])


# In[28]:


utf = [i for i in utf if "RING" not in i[1]]
utf = [i for i in utf if "MACRON" not in i[1]]
utf = [i for i in utf if "STROKE" not in i[1]]
utf = [i for i in utf if "TILDE AND ACUTE" not in i[1]]
utf = [i for i in utf if "DIAERESIS" not in i[1]]
utf = [i for i in utf if "BARRED" not in i[1]]
utf = [i for i in utf if "MIDDLE TILDE" not in i[1]]

utf = [i for i in utf if "CEDILLA" not in i[1]]


# In[29]:


for i in utf:
    if "RING" in i[1]:
        print(i)


# In[30]:


huyen = [i for i in utf if "GRAVE" in i[1] and "DOUBLE" not in i[1]]
sac = [i for i in utf if "ACUTE" in i[1] and "DOUBLE" not in i[1]]
hoi = [i for i in utf if "HOOK ABOVE" in i[1]]
nga = [i for i in utf if "TILDE" in i[1]]
nang = [i for i in utf if "DOT BELOW" in i[1]]
mu = [i for i in utf if "CIRCUMFLEX" in i[1]]
moc = [i for i in utf if "HORN" in i[1]]
cong =[i for i in utf if "BREVE" in i[1]]


# In[39]:


len(huyen)


# In[40]:


word_check = [" A ", " E ", " I ", " O ", " U ", " Y "]


# In[41]:


huyen = [i for i in huyen if any(j in i[1] for j in word_check) ] 
sac = [i for i in sac if any(j in i[1] for j in word_check) ] 
hoi = [i for i in hoi if any(j in i[1] for j in word_check) ] 
nga = [i for i in nga if any(j in i[1] for j in word_check)] 
nga = [i for i in nga if i not in [i for i in nga if "TILDE BELOW" in i[1]]] + hoi
nang = [i for i in nang[1:] if any(j in i[1] for j in word_check) ]
mu = [i for i in mu if any(j in i[1] for j in word_check) and "CIRCUMFLEX BELOW" not in i[1]]
moc = [i for i in moc if any(j in i[1] for j in word_check) ]
cong = [i for i in cong if any(j in i[1] for j in word_check) ]


# In[42]:


final_list = sac + huyen + nga + nang + mu + moc + cong


# In[43]:


A_char = [i for i in final_list if " A " in i[1]] 
E_char = [i for i in final_list if " E " in i[1]]
I_char = [i for i in final_list if " I " in i[1]]
O_char = [i for i in final_list if " O " in i[1]]
U_char = [i for i in final_list if " U " in i[1]]
Y_char = [i for i in final_list if " Y " in i[1]]


# In[44]:


E_char


# In[45]:


list_A = [list(set([i[0].lower() for i in A_char]))+["ấ"], 'a']
list_O = [list(set([i[0].lower() for i in O_char])), 'o']
list_E = [list(set([i[0].lower() for i in E_char])), 'e']
list_I = [list(set([i[0].lower() for i in I_char])), 'i']
list_U = [list(set([i[0].lower() for i in U_char])), 'u']
list_Y = [list(set([i[0].lower() for i in Y_char])), 'y']


# In[46]:


list_sac = [list(set([i[0].lower() for i in sac])) + ["ấ"], 'sac']
list_huyen = [list(set([i[0].lower() for i in huyen])), 'huyen']
list_hoi = [list(set([i[0].lower() for i in hoi])), 'hoi']
list_nga = [list(set([i[0].lower() for i in nga])), 'nga']
list_nang = [list(set([i[0].lower() for i in nang])), 'nang']

list_mu = [list(set([i[0].lower() for i in mu])) + ["ǻ"],'mu']
list_moc = [list(set([i[0].lower() for i in moc])),'moc']
list_cong = [list(set([i[0].lower() for i in cong])),'cong']


# In[47]:


character = []
character.extend((list_A, list_O, list_U, list_E, list_I, list_Y))


# In[48]:


dau = []
dau.extend((list_sac, list_huyen, list_hoi, list_nga, list_nang))


# In[49]:


dau[2]


# In[50]:


dau_temp = [j[0] for j in dau]


# In[51]:


other = []
other.extend((list_mu, list_moc, list_cong))


# In[52]:


import inspect
def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]


# In[61]:


def check_properties(word, character, dau , other):
    char_name=[]
    holder = [[]]
    holder_dau = [[]]
    dau_temp = [j[0] for j in other]
    flat_list = [item for sublist in dau_temp for item in sublist]
    dau_2_temp = [j[0] for j in dau]
    flat_2_list = [item for sublist in dau_2_temp for item in sublist]
    for i in other:
        if word in i[0]:
            holder = i
    for i in dau:
        if word in i[0]:
            holder_dau = i
    for i in character:
        if word in i[0]:
            if holder == []:
                temp_1 = [j for j in i[0] if j not in flat_list]
                #try:
                temp_2 = [j for j in temp_1 if j in holder_dau[0]]
                #except:
                #    temp_2 = [j for j in temp_1]
                char_name = [i[1]]+temp_2
                break
            else:
                
                temp_1 = [j for j in i[0] if j in holder_dau[0]]
                   #temp_1 = [j for j in i[0]]
                temp_2 = [j for j in temp_1 if j in holder[0]]
                #try:
                temp_none_dau = [j for j in i[0] if j not in flat_list and j in holder_dau[0]]
                #except:
                #    temp_none_dau = [j for j in i[0] if j not in flat_list]
                temp_none_mu = [j for j in i[0] if j in holder[0] and j not in flat_2_list]
                char_name = [i[1]]
                char_name = char_name + temp_2 + temp_none_dau + temp_none_mu
                break

    return list(set(char_name))


# In[62]:


temp = check_properties("ể", character, dau ,other)


# In[63]:


print(temp)


# In[64]:


list_D = [['đ','Đ'],'d']


# In[65]:


complete_list = []
complete_list.extend((list_A, list_O, list_E, list_U, list_I, list_Y))


# In[66]:


def replace_word(inputString, complete_list, character, dau, other):
    temp_string = ""
    
    for word in inputString:
        flag = 0
        for i in complete_list:
            if word == "đ" or word == "Đ":
                temp_string = temp_string + "[" + "dđ" + "]"
                flag = 1
                break
            elif word in i[0]:
                temp_string = temp_string + "["+"".join(check_properties(word, character, dau, other))+"]"
                flag = 1
                break
        if flag == 0:
            temp_string = temp_string + word
    return temp_string


# In[67]:


string = "chế không biết điều này nặng hay nhẹ mà cớ sao thợ sửa tàu nâng nó lên đệ"
print(replace_word(string, complete_list, character, dau, other))

