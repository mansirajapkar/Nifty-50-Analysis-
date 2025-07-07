import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('NIFTY 50_Data.csv')
# print(df.info())
# print(df.head())
df['Date']=pd.to_datetime(df['Date'])
# print(df.info())
# new=df.dropna()
# print(new.info())
df['Year']=pd.DatetimeIndex(df['Date']).year
year_list=df['Year'].unique()
#print(year_list)
#1 day of each year 
date_list=[]
for i in year_list:
    include=df[df['Date'].dt.year==i].min()
    date_list.append(include['Date'])
print(date_list)
date_closelist=[]
close_list=[]
for i in date_list:
    cl=df.where(df['Date']==i)
    cl=cl.dropna()  
    date_closelist.append(cl[['Date','Close']])
    close_list.append(cl['Close'].values[0])
close_list.reverse()
date_closelist.reverse()
print("Close List")
print(close_list)
# print('length of close list',len(close_list))
# total=0
# for i in range(0,5):
#     total=total+close_list[i]
# print("1st five's close list amount group",total)
# percentage1=(total/5)*100
# print(f'{percentage1} 1st percentage')
# total2=0
# for i in range(5,10):
#     total2=total2+close_list[i]
# print("2nd five's close list amount group",total2)
# percentage2=(total2/5)*100
# print(f'{percentage2} 2nd percentage')
# total3=0
# for i in range(10,15):
#     total3=total3+close_list[i]
# print("3rd five's close list amount group",total3)
# percentage3=(total2/5)*100
# print(f'{percentage3} 3rd percentage')
# total4=0
# for i in range(15,20):
#     total4=total4+close_list[i]
# print("4th group of five's close list amount group",total4)
# percentage4=(total/5)*100
# print(f'{percentage4} 4th percentage')
# total5=0
# for i in range(20,len(close_list)):
#     total=total+close_list[i]
# print("Last group of five's close list amount group",total)
# percentage5=(total5/5)*100
# print(f'{percentage5} 1st percentage')
# print('Date:close')
# print(date_closelist)
print('Here is ret list')
ret_list=[]
for i in range(len(close_list)-5):
    ret=close_list[i+5]-close_list[i]
    perc=(ret/close_list[i])*100
    ret_list.append(perc)
year_list=list(year_list)
year_list.reverse()
#print(year_list)
group_of_five=[]
print("Here is output:",ret_list)
for i in range(len(year_list)-5):
    gof=year_list[i],'-',year_list[i+5]
    group_of_five.append(gof)
    print(year_list[i],'-',year_list[i+5],ret_list[i])

return_list=[]
print('Here is return list')
for i in range(len(ret_list)):
    returns=(ret_list[i]*50000)/100
    return_list.append(returns)
    print(year_list[i],'-',year_list[i+5],"--",ret_list[i],"==",return_list[i])

total=0
for i in range(0,len(return_list)):
    total+=return_list[i]

print("Here is final Anaswer: ",total)

# for i in range(len(cl)):
#     print(df[['Date','Close']])
#print(cl[['Date','Close']])
#print(cl.info())
#print(cl.head(174))
# #apply function on 2 columns 
# df['Sum']=df[['Low','Close']].apply(lambda row:row['Low']+row['Close'],axis=1)
# print(df)
# # df[['Low','Close']]=df[['Low','Close']].apply(lambda x:x*2)
# # print(df)
print(group_of_five)
years=[]
for i in range(len(year_list)-5):
    year=f"{year_list[i]}-{year_list[i+5]}"
    years.append(year)
plt.figure(figsize=(10,5))
plt.plot(years, ret_list, color='Blue', linestyle="--")
plt.xlabel("5-Years Periods")
plt.ylabel("Return(%)")
plt.title("Nifty 50-5 Years Returns Over Time")
plt.show()
# plt.plot(group_of_five,ret_list,marker='s',linestyle='--',color='green')
# plt.show()