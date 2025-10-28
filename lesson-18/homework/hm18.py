import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
stack=pd.DataFrame(df)
stack
stack['creationdate']=pd.to_datetime(df['creationdate'])
before_2014=df[df['creationdate']<'2014-01-01']
before_2014


stac=stack[stack['score']>50]
stac
stac=stack[stack['score'].between(50,100)]
stac
stac=stack[stack['ans_name']=='Scott Boston']
stac

gender_checking = df['Gender'] == "Male"
salary_checking = df['Salary'].between(50000, 150000)
team_checking = df['Team'].isin(['Sales', 'Product'])


stack['creationdate']=pd.to_datetime(df['creationdate'])
before_2014=df[df['creationdate']<'2014-01-01']

stac=stack[stack['score'].between(50,100)]
stac

df[gender_checking & salary_checking & team_checking]

#Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.



stack['creationdate']=pd.to_datetime(df['creationdate'])
time_check=stack['creationdate'].between('2014-03-01','2014-10-01')
name_check=stack['ans_name']=='Unutbu'
score_check=stack['score']>5
result=stack[time_check& name_check&score_check]
result
# ...existing code...
# stack['creationdate'] = pd.to_datetime(df['creationdate'])
# time_check = stack['creationdate'].between('2014-03-01', '2014-10-01')
# name_check = stack['ans_name'] == 'Unutbu'
# score_check = stack['score'] < 5   # <5, task talabiga ko'ra

# result = stack[time_check & name_check & score_check]
# result
# ...existing code...
#Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
stac
# stac=stack[stack['score'].between(5,10)]
# view=stack['viewcount']>10000
# result=stack[stac |view]

# ...existing code...
mask_score = stack['score'].between(5, 10)     # boolean Series
mask_view = stack['viewcount'] > 10000        # boolean Series
result = stack[mask_score | mask_view]        # OR: score between 5-10 OR viewcount > 10000
result
# ...existing code...
#Find all questions that are not answered by Scott Boston
stac=stack[stack['ans_name']!='Scott Boston']
stac

import pandas as pd
df=pd.read_csv('titanic.csv')
data=pd.DataFrame(df)
data
# ...existing code...
mask = (data['Sex'].str.lower() == 'female') & (data['Pclass'] == 1) & (data['Age'].between(20, 30))
female_p1_20_30 = data.loc[mask]
female_p1_20_30
# ...existing code...
# ...existing code...
mask_high_fare = data['Fare'] > 100
high_fare = data.loc[mask_high_fare].reset_index(drop=True)
high_fare
# ...existing code...
#Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
alone=data['Survived']<1
alone
mask = (data['Embarked']=='C') & (data['Fare'] > 50 )
female_p1_20_30 = data.loc[mask]
female_p1_20_30

# ...existing code...
mask = (data['SibSp'] > 0) & (data['Parch'] > 0)
both_relatives = data.loc[mask].reset_index(drop=True)
both_relatives
# ...existing code...
mask = (data['Age'] <15) & (data['Survived'] == 0)
both_relatives = data.loc[mask].reset_index(drop=True)
both_relatives
data
