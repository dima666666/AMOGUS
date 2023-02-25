#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# задание №1
a=int(input())
b=int(input())
print(a + b)
print(a * b)
print(a ** b)
print(a / b)
print(a % b)
print(a // b)
print(a - b)


# In[ ]:


a=int(input())
b=int(input())
c=int(input())

result=((a+2)/(b+5))**4 - 0.001*c


print(result)


# In[29]:


a=int(input())
b=int(input())
c=int(input())

result=((a+2)/(b+5))**4 - 0.001*c


print(result)


# In[6]:


#задание №3
print('мяч'*9)


# In[10]:


#задание №3
a=input()
print('='*40)
print('\t   сообщение: ' + a)
print('='*40)


# In[14]:


#задание №4
a=("лимоны,апельсины,мандарины")
b=["лимоны","апельсины","мандарины"]
print(a[15])
print(b[1])


# In[20]:


#задание №5
a=[15,78,96,13,25,43,]
del(a[3])
print(a)
a.append(15)
print(a)


# In[27]:


#задание №6
a={"китай" : "пекин", "Россия" :"москва","белорусь" : "минск","ОвощЬ" : "помидор","фрукт" : "апельсин"}
del(a["Овощь"])
print(a)


# #задание №7
# a=int(input())
# 

# In[51]:


a=int(input())
if(a==1):
    print("Понидельник")
elif(a==2):
    print("Вторник")
elif(a==3):
    print("Среда")
elif(a==4):
    print("Четверг")
elif(a==5):
    print("Пятница")
elif(a==6):
    print("Суббота")
elif(a==7):
    print("Воскресенье")
else:
    print("неверный ответ")


# In[48]:


a=int(input())
print(str(a) + " киллометр это " +   str(a*1000)  + " метров ")


# In[ ]:




