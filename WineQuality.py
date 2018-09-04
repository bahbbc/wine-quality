
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[4]:


wine = pd.read_csv('winequality.csv', sep=';')


# In[5]:


wine.head()


# In[8]:


wine.shape


# ## Exploratory Data Analysis

# Primeiro vamos verificar a variável resposta: `quality`

# ### Quality

# In[11]:


wine.quality.describe()


# In[10]:


sns.kdeplot(wine.quality);


# Apesar da descrição do desafio dizer que os valores estão entre 0 e 10, o dataset só possui valores entre 3 e 9. Percebemos também que existem apenas notas com valores inteiros.

# ### type

# In[13]:


wine.type.value_counts()


# In[18]:


sns.countplot(x="type", data=wine)


# In[20]:


sns.stripplot(x="type", y="quality", data=wine);


# Percebemos que há um número maior de vinhos Vermelhos do que vinhos Brancos. Comparando-se com a variável resposta vemos que o tipo do vinho branco possui notas 9, o que não acontece com o vinho vermelho. 

# ### fixed acidity
