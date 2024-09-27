import pandas as pd


path = './data/emp.csv'
emp = pd.read_csv(path, encoding='cp949')
print(emp)
print()

empCopy  =  emp

pay = emp['Pay']    #객체['컬럼명'] 객체.pay
for i, v in enumerate(pay):
    if v<=400:
        empCopy = empCopy.drop(i)

print(empCopy)
print()
print()

#empCopy파일
emp_table = pd.DataFrame(empCopy)
emp_table.to_csv('./data/empCopy.csv')
print('empCopy.csv파일 저장 test')
print()



#empTest파일
empTest = emp
data = empTest[emp['Pay']>400].index
remove = empTest.drop(data)
print(remove)
fname = './data/empTest.csv'
remove.to_csv(fname)
print('empTest.csv 파일 저장 test')




'''
 No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  까사노  350
4  105  아이유  400
5  106  고길동  450
6  107  빈센조  500

    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
5  106  고길동  450
6  107  빈센조  500
'''