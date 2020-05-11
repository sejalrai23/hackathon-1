print("Enter your identity")
print("1. Admin");
print("2. User");

n=int(input())

if n==1 :
	print("Select : ")
	print("1. Add hospitals having blood banks and blood donation camps")
	print("2. view the list of donors of a particular area with proper Blood group details")
	m=int(input())
	
	if m==1 :
		print("Enter name of hospital :",end="")
		h_name=input();
		file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\hos.txt','a+')
		#file.write("1. ")
		file.write(h_name)
		file.write("\n")
		file.close()
		
	elif m==2:
		print("\nList of donors : ")
		file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\don.txt','r')
		print(file.read())
		file.close()
	
elif n==2 :
	print("1. Register")
	print("2. Login")
	a=int(input())
	
	if a==1 :
		print("Enter :")
		print("New ID : ",end="")
		ID=input()
		print("Name : ",end="")
		name=input()
		print("Age : ",end="")
		age=input()
		print("Blood group : ",end="")
		blood=input()
		print("Address : ",end="")
		add=input()
		file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\us.txt','a+')
		file.write(ID)
		file.write(" ")
		file.write(name)
		file.write(" ")
		file.write(age)
		file.write(" ")
		file.write(blood)
		file.write(" ")
		file.write(add)
		file.write("\n")		
		file.close()
	
	elif a==2 :
		print("Enter ID")
		ID=input()		
		print("Enter : ")
		print("1. Donate")
		print("2. Requesting")
		b=int(input())
		if b==1 :
			file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\don.txt','a+')
			#file.write("1. ")
			file.write(ID)
			file.write("\n")		
			file.close()
			
			
		elif b==2 :
			print("Hospitals : ")
			file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\hos.txt','r')
			print(file.read())
			file.close()
			print("Donors : ")
			file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\don.txt','r')
			print(file.read())
			file.close()
			print("Users : ")
			file=open('‪C:\\Users\\Dell\\Desktop\\bloodbank\\us.txt','r')
			print(file.read())
			file.close()
	
	
			 				
	
else :
	print("Wrong option")
	

