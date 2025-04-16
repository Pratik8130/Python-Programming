'''write a program to check datatype of given values
d = {}
d1 = {"pratik" : "rcb"}
d2 = {7}
print(type(d))
print(type(d1))
print(type(d2))'''

'''write a program to create a set and add the elements as 1,'xyz','abc','m','c'
s = set()
s.add(1)
s.add('xyz')
s.add('abc')
s.add('m')
s.add('c')

print(s)
print(type(s))'''

'''Dictionary: 
           It is a datatype which contains key and value pairs as data

It is oredered
          
'''

'''Write a program to create a dictionary with 3 key and value pair which contains employee id employee name and employee deparatment as key value and display the dictionary value'''

# Employee = {"Id":"18","Name":"Pratik","Department":"Electronics"}

# # print(Employee["Id"])
# # print(Employee.get("Name"))
# # print(Employee.get("City","Not found"))
# print(Employee.keys())
# print(Employee.values())
# print(Employee.items())

'''Write a program to create customer dictionary which is containing keys Account number ,Account holder name, Balance and branch name
display all the keys present inside customer dictionary 
display all the values present in customer dictionary
display all the items or key and value pairs present in a dictionary'''

customer_dict = {"Account number":1419,
                 "Account holder name":"Pratik M",
                 "Balance":500,
                 "Branch name":"SBI CKD"}

print(customer_dict.keys())
print(customer_dict.values())
print(customer_dict.items())