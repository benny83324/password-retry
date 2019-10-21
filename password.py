password ="a123456"
i = 3
while i >0:
	answer = input("What is your password:")
	
	if answer == password:
		print("you have logged in successfully")
		break
	else:
		i = i-1
		if i == 0:
			print("wrong password! you can try your password later")
		if i > 0:
			print("wrong password! you still got",i," more time to enter your password")