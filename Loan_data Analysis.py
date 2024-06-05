#!/usr/bin/env python
# coding: utf-8

# ## Understanding data

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("C:/Users/purva/Downloads/Loan_data_analysis_project/Loan_data_analysis_project/Loan_dataset.csv")


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.info()


# ## Null Treatment 

# In[6]:


df.isna().sum()


# ## Null treatment

# In[7]:


df.isna().sum().plot(kind='bar')


# In[8]:


for i in df.columns:
    if df[i].dtypes==object:
        df[i]=df[i].fillna(df[i].mode()[0])
    else:
        df[i]=df[i].fillna(df[i].mean())


# In[9]:


df.isna().sum().plot(kind='bar')


# ## Descriptive Statics

# In[10]:


for i in df.columns:
    if df[i].dtypes!=object:
        print(i)
        print()
        print(df[i].describe())
        print('******************************************************')


# ## Analysis

# In[11]:


#1.What is the average current loan amount for each loan status?
avg_loan = df.groupby('Loan Status')['Current Loan Amount'].mean()
avg_loan


# In[12]:


avg_loan.plot(kind='line')


# In[13]:


#2.How does the credit score vary with the annual income?
credit_vs_annual = df.groupby('Credit Score')['Annual Income'].sum()
credit_vs_annual


# In[14]:


sns.scatterplot(data=df,y='Credit Score',x='Annual Income')


# In[15]:


#3.Is there a correlation between the number of open accounts and the current credit balance?
sns.heatmap(df[['Current Credit Balance','Number of Open Accounts']].corr(),annot=True)


# In[16]:


df[['Current Credit Balance','Number of Open Accounts']].corr()


# In[17]:


df[['Current Credit Balance','Number of Open Accounts']].corr().plot(kind='bar')


# In[18]:


#4.What is the distribution of credit scores across different home ownership types?
plt.figure(figsize=(10, 5))
sns.barplot(x='Home Ownership', y='Credit Score', data=df)
plt.title('Credit Scores Distribution by Home Ownership Type')


# In[19]:


sns.boxplot(x='Home Ownership', y='Credit Score', data=df)


# In[20]:


#5.How does the annual income differ for different purposes of loans?
plt.figure(figsize=(29,10))
sns.barplot(x='Purpose', y='Annual Income', data=df)


# In[21]:


distribution = df.groupby('Purpose')['Annual Income'].mean()
distribution


# In[22]:


#6.What is the average monthly debt for each term (short-term vs. long-term)?
average_monthly = df.groupby('Term')['Monthly Debt'].mean()
average_monthly


# In[23]:


plt.pie(average_monthly, labels=average_monthly.index, autopct='%1.1f%%')


# In[37]:


#7.Is there a correlation between years of credit history and the current credit balance?
correlation = df['Years of Credit History'].corr(df['Current Credit Balance'])
correlation


# In[25]:


sns.heatmap(df[['Current Credit Balance','Years of Credit History']].corr(),annot=True)


# In[26]:


#8.How does the credit score vary with the years in the current job?
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Years in current job', y='Credit Score', data=df)


# In[27]:


#9.What is the relationship between the number of credit problems and the number of open accounts?
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Number of Credit Problems', y='Number of Open Accounts', data=df)


# In[28]:


#10.What is the distribution of annual income across different loan statuses?
sns.barplot(x='Loan Status', y='Annual Income', data=df)


# In[29]:


#11.Is there a correlation between the current loan amount and the number of open accounts?
sns.heatmap(df[['Number of Open Accounts','Current Loan Amount']].corr(),annot=True)


# In[30]:


#12.How does the monthly debt vary with the years of credit history?
sns.scatterplot(x='Years of Credit History', y='Monthly Debt', data=df)


# In[31]:


#13.What is the average annual income for each purpose of loan?
avg_income = df.groupby('Purpose')['Annual Income'].mean()
avg_income


# In[32]:


#14.How does the credit score vary with the number of credit problems?
score_vs_problems = df.groupby('Credit Score')['Number of Credit Problems'].sum()
score_vs_problems


# In[33]:


sns.scatterplot(data=df,x='Number of Credit Problems',y='Credit Score')


# In[34]:


#15.Is there a correlation between the number of credit problems and the current credit balance?
sns.heatmap(df[['Number of Credit Problems','Current Credit Balance']].corr(),annot=True)


# In[38]:


#16.What is the distribution of current loan amounts across different home ownership types
plt.figure(figsize=(10, 5))
sns.barplot(x='Home Ownership', y='Current Loan Amount', data=df)


# In[41]:


#17.How does the annual income vary with the years in the current job
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df,x='Years in current job',y='Annual Income')


# In[42]:


#18.Is there a correlation between the current loan amount and the monthly debt?
sns.heatmap(df[['Monthly Debt','Current Loan Amount']].corr(),annot=True)


# In[44]:


#19.What is the average monthly debt for each home ownership type?
avg_monthly_debt = df.groupby('Home Ownership')['Monthly Debt'].mean()
avg_monthly_debt


# In[49]:


plt.pie(avg_monthly_debt, labels=avg_monthly_debt.index, autopct='%1.1f%%')


# In[54]:


#20.How does the credit score vary with the number of open accounts
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df,y='Number of Open Accounts',x='Credit Score')


# In[64]:


#21.What is the distribution of credit scores across different loan statuses?
distribution = df.groupby('Loan Status')['Credit Score'].sum()
distribution
plt.figure(figsize=(10, 5))
sns.barplot(data=df,x='Loan Status',y='Credit Score')


# In[66]:


#22.Is there a correlation between the current loan amount and the years of credit history?
sns.heatmap(df[['Years of Credit History','Current Loan Amount']].corr(),annot=True)


# In[68]:


#23.How does the monthly debt vary with the number of credit problems?
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df,y='Monthly Debt',x='Number of Credit Problems')


# In[69]:


#24.What is the average current loan amount for each purpose of loan?
avg_loan = df.groupby('Purpose')['Current Loan Amount'].mean()
avg_loan


# In[70]:


avg_loan.plot(kind='barh')


# In[77]:


#25.How does the credit score vary with the current credit balance?
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df,x='Credit Score',y='Current Credit Balance')


# In[78]:


#26.Is there a correlation between the annual income and the current credit balance?
sns.heatmap(df[['Annual Income','Current Credit Balance']].corr(),annot=True)


# In[79]:


#27.What is the distribution of annual income across different terms (short-term vs. long-term)?
average_income = df.groupby('Term')['Annual Income'].mean()
average_income


# In[80]:


plt.pie(average_income, labels=average_income.index, autopct='%1.1f%%')


# In[81]:


#28.How does the credit score vary with the number of credit problems
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df,y='Credit Score',x='Number of Credit Problems')


# In[83]:


#29.Is there a correlation between the current loan amount and the number of credit problems?
sns.heatmap(df[['Number of Credit Problems','Current Loan Amount']].corr(),annot=True)


# In[85]:


#30.What is the relationship between the number of open accounts and the years of credit history
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Years of Credit History', y='Number of Open Accounts', data=df)


# In[ ]:




