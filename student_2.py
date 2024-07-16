
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



