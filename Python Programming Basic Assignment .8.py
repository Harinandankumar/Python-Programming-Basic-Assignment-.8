#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Add Two Matrices?
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def addMatrices(a,b):
    print(f'Inputs: {a},{b}')
    if len(a) == len(b):
        out_matrix = []
        for ele in range(len(a)):
            if len(a[ele]) == len(b[ele]):
                out_matrix.append([])
                for sub_ele in range(len(a[ele])):
                    out_matrix[ele].append(a[ele][sub_ele]+b[ele][sub_ele])
            else:
                print('Both Matrices must contains same no of rows and columns') 
    else:
        print('Both Matrices must contains same no of rows and columns')
    print(f'Output: {out_matrix}')

addMatrices([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]])
addMatrices([[2,3,5],[1,1,1],[2,2,2]],[[4,3,5],[1,2,3],[3,2,1]])


# 2. Write a Python Program to Multiply Two Matrices?
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,4,7],[2,5,8],[3,6,9]]

def multiply_matrice(a,b):
    output = []
    if len(a[0]) == len(b):
        for ele in range(len(a[0])):
            output.append([0 for ele in range(len(b[0]))])
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    output[i][j] += a[i][k]*b[k][j]
        print(output)     
    else:
        print('Matrix Multiplication is Not Possible')
        
multiply_matrice(a,b)


# 3. Write a Python Program to Transpose a Matrix?
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2],[4,5],[7,8]]
c = [[1,2,3],[4,5,6]]

def generate_transpose(in_matrix):
    out_matrix = []
    for ele in range(len(in_matrix[0])):
        out_matrix.append([0 for i in range(len(in_matrix))])
    for i in range(len(in_matrix)):
        for j in range(len(in_matrix[i])):
            out_matrix[j][i] = in_matrix[i][j]
    print(f'{in_matrix} -> {out_matrix}')
        
generate_transpose(a)
generate_transpose(b)
generate_transpose(c)


# 4. Write a Python Program to Sort Words in Alphabetic Order?
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def sortString():
    in_string = input("Enter a String: ").title()
    sorted_list = sorted(in_string.split(' '))
    print(' '.join(sorted_list))

sortString()


# 5. Write a Python Program to Remove Punctuation From a String?
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def removePunctuatuions():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    in_string = input('Enter a String: ')
    out_string = ''
    for ele in in_string:
        if ele not in punctuations:
            out_string += ele
    print(out_string)
    
removePunctuatuions()

