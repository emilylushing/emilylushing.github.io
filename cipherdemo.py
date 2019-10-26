#cipher 

message = input("enter a message: ")
message.lower() #changes all the characters in your message to lowercase - easier for shifting

newmessage = [] #creates a list that you can keep the characters of your new message in

for ch in message: #for each character in the message you are deciphering 
	
	##if the character is a space, a period, or a comma: 
		#need to take into account that these are also considered characters/have unicodes!!!
		
	##else:
		#lowercase 'a' unicode is 97
		#lowercase 'z' unicode is 122
		#shift is 5!! 
		
#to print a message from a list

for ch in newmessage:
        print(ch, end = "")	
		
		
#message: 
#czggj. ht ivhz dn zhdgt. dh wzdib czgy cjnovbz di ocdn mjjh. nziy czgk viy ajjy. d gdfz npncd.
