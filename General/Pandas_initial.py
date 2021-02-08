import pandas
import xlrd

df1 = pandas.DataFrame([[1,2,3],[40,50,60]],columns=['one','two','three'],index=['first','second'])
print(df1)
type(df1.one.max())

df2 = pandas.DataFrame([{"Name":"John","age":23},{"Name":"Jack","age":45}],index=['first','second'])
print(df2)

df3 = pandas.read_csv("D:\\Python_Automation\\AutomationCourse\\General\\data\\supermarkets.csv")
print(df3)


df4 = pandas.read_json("D:\\Python_Automation\\AutomationCourse\\General\\data\\supermarkets.json")
print(df4)

df5 = pandas.read_excel("D:\\Python_Automation\\AutomationCourse\\General\\data\\supermarkets.xlsx",sheet_name=0)
print(df5)


df6 = pandas.read_csv("D:\\Python_Automation\\AutomationCourse\\General\\data\\supermarkets-commas.txt")
print(df6)

df7 = pandas.read_csv("D:\\Python_Automation\\AutomationCourse\\General\\data\\supermarkets-semi-colons.txt",sep=';',header=None)
print(df7)

df7.columns = ['ID','Address','City','State','Country','Name','Employees']
df7.set_index('ID',inplace = True)
print(df7)

print(df7.loc[2:5,"City":"Employees"])

print(df7.iloc[2:5,2:5])