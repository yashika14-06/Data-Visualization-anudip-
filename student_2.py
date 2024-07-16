
student = {'stdid':['std101','std102','std103','std104','std105','std106','std107','std108','std109','std110']
,'stdname':['Ashish Kumar','Abhishek Kumar','aman','rahul','ruby','suman','saurabh','sumit','kamlesh','rohan'],
'standard':['10th','10th','10th','10th','10th','10th','10th','10th','10th','10th'],
'age':[15,14,15,14,13,13,15,14,15,15],
'hindi':[67,85,23,45,89,90,45,23,45,34],
'english':[89,45,56,67,67,46,23,45,56,12],
'maths':[87,48,78,45,89,67,34,67,78,24],
'science':[89,90,78,45,93,67,45,78,99,45],
'computer':[90,45,67,56,65,67,34,90,67,56],
'total':[422,313,302,258,403,337,181,303,345,171]
}
for i in range(len(student['stdid'])):
    print(student['stdid'][i],"--",student['stdname'][i],"--",student['standard'][i],"--",student['age'][i],"--",student['hindi'][i],"--",student['english'][i],"--",student['maths'][i],"--",student['science'][i],"--",student['computer'][i],"--",student['total'][i])


for i in range(len(student['stdid'])):
    if(student['english'][i]>50):
        print(student['stdname'][i])

print(student['stdid'][7],"--",student['stdname'][7],"--",student['standard'][7],"--",student['age'][7],"--",student['hindi'][7],"--",student['english'][7],"--",student['maths'][7],"--",student['science'][7],"--",student['computer'][7],"--",student['total'][7])

print(student['stdid'][8],"--",student['stdname'][8],"--",student['standard'][8],"--",student['age'][8],"--",student['hindi'][8],"--",student['english'][8],"--",student['maths'][8],"--",student['science'][8],"--",student['computer'][8],"--",student['total'][8])

print(student['stdid'][9],"--",student['stdname'][9],"--",student['standard'][9],"--",student['age'][9],"--",student['hindi'][9],"--",student['english'][9],"--",student['maths'][9],"--",student['science'][9],"--",student['computer'][9],"--",student['total'][9])


new = list(zip(student['stdname'],student['maths']))
sorting = sorted(new,key=lambda x:x[1] ,reverse = True)

top = sorting[:4]
for name , marks in top:
    print(name,"  ",marks)



# students = [
#     {'stdid': 'std101', 'stdname': 'Ashish Kumar', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 89, 'maths': 87, 'science': 89, 'computer': 90, 'total': 422},
#     {'stdid': 'std102', 'stdname': 'Abhishek Kumar', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 89, 'maths': 87, 'science': 89, 'computer': 90, 'total': 422},
#     {'stdid': 'std103', 'stdname': 'Aman', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 56, 'maths': 78, 'science': 78, 'computer': 45, 'total': 302},
#     {'stdid': 'std104', 'stdname': 'Rahul', 'standard': '10th', 'age': 14, 'hindi': 67, 'english': 49, 'maths': 56, 'science': 45, 'computer': 78, 'total': 295},
#     {'stdid': 'std105', 'stdname': 'Ruby', 'standard': '10th', 'age': 13, 'hindi': 89, 'english': 67, 'maths': 45, 'science': 45, 'computer': 56, 'total': 258},
#     {'stdid': 'std106', 'stdname': 'Suman', 'standard': '10th', 'age': 15, 'hindi': 90, 'english': 90, 'maths': 56, 'science': 78, 'computer': 89, 'total': 403},
#     {'stdid': 'std107', 'stdname': 'Saurabh', 'standard': '10th', 'age': 15, 'hindi': 45, 'english': 45, 'maths': 23, 'science': 67, 'computer': 67, 'total': 247},
#     {'stdid': 'std108', 'stdname': 'Sumit', 'standard': '10th', 'age': 14, 'hindi': 23, 'english': 56, 'maths': 78, 'science': 78, 'computer': 78, 'total': 313},
#     {'stdid': 'std109', 'stdname': 'Kamlesh', 'standard': '10th', 'age': 15, 'hindi': 67, 'english': 78, 'maths': 67, 'science': 78, 'computer': 78, 'total': 368},
#     {'stdid': 'std110', 'stdname': 'Rohan', 'standard': '10th', 'age': 15, 'hindi': 12, 'english': 24, 'maths': 45, 'science': 56, 'computer': 56, 'total': 171}
# ]
# for i in students:
#     for j in i:
#         if(student.values('english') > 50):
