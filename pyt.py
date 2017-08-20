def divide(str1,num):
	liste=list()
	temp=""
	for i in range(len(str1)):
		if i % int(num)==0 and i!=0:
			liste.append(temp)
			temp=""
		temp+=str1[i]
		if i==len(str1)-1:
			liste.append(temp)
	return liste

def addinselect(liste,str1,choise):
	for i in range(len(liste)):
		if int(choise) == 0:
			liste[i]=str1+liste[i]
		elif int(choise)==1:
			liste[i]=liste[i]+str1
		else:
			print("Error! Selected unknown choise")
			exit(0)
	return liste
 
print divide("saasdasd",3)
liste1=["sadasd","asdasd"]
print addinselect(liste1,r"/x",1)
print addinselect(liste1,r"/x",0)
