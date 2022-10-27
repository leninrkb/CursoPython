#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ejemplo1_c2.py


# In[ ]:


"""Comparación de enteros mediante sentencias If"""


# In[ ]:


print('Ingresa tu edad y la de tu mejor amigo, para decirte la relación qué hay entre ellas ')


# In[ ]:


#Lee la primera edad 


# In[ ]:


edad1=int(input('Ingresa tu edad: '))


# In[ ]:


#Lee la segunda edad


# In[ ]:


edad2=int(input('Ingresa la edad de tu mejor amigo: '))


# In[ ]:


if edad1==edad2:
    print(edad1,'es igual',edad2,'\n Tu amigo y tú, tienen la misma edad.')
if edad1 !=edad2:
    print(edad1,' es diferente de',edad2,'\n Tu amigo y tú tienen edades diferentes.')
if edad1 < edad2:
    print(edad1,' es menor que',edad2,'\n Tu amigo es mayor que tú.')
if edad1 > edad2:
    print(edad1,' es mayor que',edad2,'\n Tu amigo es menor que tú.')
if edad1 <= edad2:
    print(edad1,' es menor o igual a',edad2,'\n Tu amigo tiene al menos, tu edad.')
if edad1 > edad2:
    print(edad1,' es mayor que',edad2,'\n Tu amigo tiene a lo más, tu edad.')


# In[ ]:




