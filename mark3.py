#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mask(binr, var):
    
    ans = ""
    
    for i in range(len(var)):
        if binr[i] == '0': 
            ans+=var[i].lower()
        else:
            ans+=var[i] 
            
    return ans

no_of_1s = 0

def take_input(n):
    
    minterms = []
    input_by_user = []
    variables = [chr(i) for i in range(65, 65+n)]

    print("enter truth table output:")

    for i in range(2**n):

        bin_str = (bin(i)[2:].zfill(n))
        bin_wrd = mask(bin_str, variables)
        minterms.append(bin_wrd)

        x = int(input(bin_wrd + ":"))
        
        if x == 1:
            global no_of_1s
            no_of_1s += 1
            goal_state.append(bin_str)
        
        input_by_user.append(x)

    return zip(minterms, input_by_user)


# In[2]:


from itertools import combinations
def list_all_possible_variables(n):
    
    all_variables=[]
    all_comb = []
    variables = [chr(i) for i in range(65, 65+n)]
    
    for i in range(1, n+1):
        all_comb+= list(combinations(variables, i))
    
    for x in all_comb:
        k = len(x)
        
        for i in range(2**k):
            bin_str = (bin(i)[2:].zfill(k))
            bin_wrd = mask(bin_str, x)
            all_variables.append(bin_wrd)
            
    return all_variables


# In[3]:


def convert_wrd_to_bin(bin_wrd):
    
    length = len(bin_wrd)
    ans =["1"]*length;

    for i in range(length):
        
        x = chr(65+i)
        ind = bin_wrd.find(x)
        
        if ind == -1:
            ans[i] = "0"
            
    return "".join(ans)


# In[4]:


def exp_(s, rem, l):
    
    if not rem: 
        l.append(s)
        return

    x = rem[0]

    str1 = s+x
    str2 = s+x.lower()

        
    exp_(str1, rem[1:], l)
    exp_(str2, rem[1:], l)


# In[5]:


def wrd_to_bin_mapping(s, n):
    
    l = []
    not_in_s = []
    temp = s.upper()
    
    for i in range(65, 65+n):
        if chr(i) not in temp: 
            not_in_s.append(chr(i))

    exp_(s, not_in_s, l)
    ans = list(map(convert_wrd_to_bin, l))
    
    return ans


# In[6]:


def all_literals_maping(n):
    
    poss_var = list_all_possible_variables(n)
    map={};
    for i in poss_var:
        map[i] = wrd_to_bin_mapping(i, n)
    
    return map


# In[7]:


"""start search"""

"""
Every state is divided into 2 parts- 
1 - the part with the addition of literals : eg [ "a'b'", "a'b"],
2 - the part with the combination of 0s1s : eg [ "00", "01"].
3 - fn --> cost + heuristics

So, 1 node can be expressed as a 2d list: [ [literals], [0s1s] ]
                                    eg : [ [ "a'b'", "a'b"], [ "00", "01"], fn ]
"""

#goal_state = ['11',"01"]
from math import sin

def cost(i, n, all_com,l):

    global no_of_1s
    global goal_state

    a = 2*i/all_com -1
    
    c = all_com*(sin( (3.145/(n-1)) * ((i-1) + a) ) + 1)

    h = all_com/( len( set(goal_state).difference( set(l) )) + 1)
    f = c+h

    return f

def goal_test(s, g):
    
    print("GT",s, "g=",g)
    
    if sorted(list(dict.fromkeys(s[1]))) == sorted(g):
        return True
    else:
        return False

def select_s(OPEN_LIST):

    sorted_OPEN_LIST = sorted(OPEN_LIST, key=lambda x: x[2], reverse = True)

    return sorted_OPEN_LIST[0]

def generate_successors(s,state_space, n, all_com):
    #consider for now that we have all literals instead of search state space to save memory
    next_s = []
    
    temp = all_literals.copy()
    
#     print("GS1", all_literals)
#     print("GS1",temp)
#     print("GS1",s)
    
    for i in s[0]:
        temp.pop(i)
        
    #print(temp)

    for i in temp:
        temp2 = [[],[],0]
        temp2[0] = s[0] + [i]
        temp2[1] = s[1] + temp[i]
        temp2[2] = cost( len(i.replace("'", "")), n, all_com,temp2[1])
        next_s.append(temp2)

#     print("GS2")
#     for i in next_s:
#         print(i)
        
    return next_s
    
def search(STATE_SPACE, OPEN_LIST, CLOSED_LIST, GOAL_STATE,n, all_com):
    
    if not OPEN_LIST:
        return
    else:
        s = select_s(OPEN_LIST);
#         print("SS",s)
        if goal_test(s,GOAL_STATE):
            print("Goal has been reached")
            print(s[0])
            print(s[1])
            return
        else:
            
            next_s = generate_successors(s,STATE_SPACE, n, all_com)
            
            CLOSED_LIST.append(s)
            
#             print("op1",OPEN_LIST)
            
            for si in next_s:
                if (si[0] not in list( i[0] for i in OPEN_LIST)) and (si[0] not in list( i[0] for i in CLOSED_LIST)):
                    OPEN_LIST = OPEN_LIST + [si]
                    
            OPEN_LIST.remove(s)
            
#             print("op2",OPEN_LIST)
            
            search(STATE_SPACE, OPEN_LIST, CLOSED_LIST, GOAL_STATE, n, all_com)

def search_start( STATE_SPACE, GOAL_STATE, n, all_com, OPEN_LIST = [], CLOSED_LIST = []):
    
    """initialize the open list"""
    OPEN_LIST = [[['0'], [], 0]]
    
    search(STATE_SPACE, OPEN_LIST, CLOSED_LIST, GOAL_STATE, n, all_com)
    
    return


# # Test the search algorithm from below :

# In[8]:


n = int(input("Enter no. of Variables"))


# In[13]:


goal_state = []

for i in take_input(n):
    print(i)


# In[14]:



all_literals = all_literals_maping(n)
temp_l = [bin(i)[2:].zfill(n) for i in range(2**n)]
all_literals.update({"1":temp_l, "0":[]})

search_start(STATE_SPACE=[],  GOAL_STATE = goal_state, n = n, all_com = 2**n)


