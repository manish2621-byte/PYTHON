number=100
while number<=999:
 temp = number
 sum =0
 while temp!=0:
    rem = temp%10 
    sum+= rem**3 
    temp = temp//10

 if sum == number:
    print(number,"armstrong")
 else:
    print(number,"not armstrong")
 number+=1
