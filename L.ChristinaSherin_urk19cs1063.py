import re


#Step 1:Input 10 Ip address
Ip = input("Input 1st ipv4 address:")
Ip1= input("Input 2nd ipv4 address:")
Ip2 = input("Input 3rd ipv4 address:")
IP3  = input("Input 4th ipv4 address:")
IP4  = input("Input 5th ipv4 address:")
Ip6  = input("Input 6th ipv4 address:")
Ip7  = input("Input 7th ipv4 address:")
Ip8  = input("Input 8th ipv4 address:")
Ip9  = input("Input 9th ipv4 address:")
Ip10 = input("Input 10th ipv4 address:")
           

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
ip_list = []
if(re.search(regex, Ip)):
    
   print("Valid Ip address")

   ipv4 = Ip.split(".")
   s = [str(i) for i in ipv4]
   res = int("".join(s))
   
   a = bin(res)
   ip_list.append("Binary Form of 1st ip address:\n")
   ip_list.append(a)
   print("\n") 
   a1 = oct(res)
   ip_list.append("\nOctal Form of 1st ip address:\n")
   ip_list.append(a1)
   
   a2= oct(res)
   ip_list.append("\nHexadecimal Form of 1st ip address:\n")
   
   ip_list.append(a2)
   
else:
   print("Invalid Ip address")
   

if(re.search(regex, Ip1)):
   print("Valid Ip address")
   ipv40 = Ip1.split(".")
   r = [str(i) for i in ipv40]
   res0 = int("".join(r))
   b = bin(res0)
   ip_list.append("\n Binary form of 2nd ip address")
   ip_list.append(b)
   b1=  oct(res0)
   ip_list.append("\nOctal Form of 2nd ip address:\n")
   ip_list.append(b1)
   b2  =  hex(res0)
   ip_list.append("\nHexadecimal Form of 2nd ip address:\n")
   ip_list.append(b2)
   
else:
   print("Invalid Ip address")
   
if(re.search(regex, Ip2)):
   print("Valid Ip address")
 
   
   
   ipv41 = Ip2.split(".")
   s = [str(i) for i in ipv41]
   res1 = int("".join(s))
   c = bin(res1)
   ip_list.append("\n Binary form of 3rd ip address")
   ip_list.append(c)
   c1=  oct(res1)
   ip_list.append("\nOctal Form of 3rd ip address:\n")
   ip_list.append(c1)
   c2=  hex(res1)
   ip_list.append("\nHexadecimal Form of 3rd ip address:\n")
   ip_list.append(c2)
 
else:
   print("Invalid Ip address")
   
if(re.search(regex, IP3)):
   print("Valid Ip address")
   
   
   ipv42 = IP3.split(".")
   t = [str(i) for i in ipv42]
   res2 = int("".join(t))
   d = bin(res2)
   ip_list.append("\n Binary form of 4th ip address")
   ip_list.append(d)
   d1=  oct(res2)
   ip_list.append("\nOctal Form of 4th ip address:\n")
   ip_list.append(d1)
   d2=  hex(res2)
   ip_list.append("\nHexadecimal Form of 4th ip address:\n")
   ip_list.append(d2)
   
else:
   print("Invalid Ip address")
   
if(re.search(regex, IP4)):
   print("Valid Ip address")
   
   
   ipv43 = IP4.split(".")
   u = [str(i) for i in ipv43]
   res3 = int("".join(u))
   e = bin(res3)
   ip_list.append("\n Binary form of 5th ip address")
   ip_list.append(e)
   e1= oct(res3)
   ip_list.append("\nOctal Form of 5th ip address:\n")
   ip_list.append(e1)
   e2 = hex(res3)
   ip_list.append("\nHexadecimal Form of 5th ip address")
   ip_list.append(e2)
else:
   print("Invalid Ip address")
   
if(re.search(regex, Ip6)):
   print("Valid Ip address")
 
   
   
   ipv44 = Ip6.split(".")
   v = [str(i) for i in ipv44]
   res4 = int("".join(v))

   f = bin(res4)
   ip_list.append("\n Binary form of 6th ip address")
   ip_list.append(f)
   f1= oct(res4)
   ip_list.append("\nOctal Form of 6th ip address:\n")
   ip_list.append(f1)
   
   f2    = hex(res4)
   ip_list.append("\nHexadecimal Form of 6th ip address\n")
   ip_list.append(f2)
else:
   print("Invalid Ip address")
if(re.search(regex, Ip7)):
   print("Valid Ip address")
   
   
   ipv45 = Ip7.split(".")
   w = [str(i) for i in ipv45]
   res5 = int("".join(w))
     
   g = bin(res5)
   
  
   ip_list.append("\n Binary form of 7th ip address")
   ip_list.append(g)
   
  
   g1 = oct(res5)
   
    
  
   ip_list.append("\nOctal Form of 7th ip address:\n")
   ip_list.append(g1) 
   
   g2 = hex(res5)
   ip_list.append("\nHexadecimal Form of 7th ip address\n")
   ip_list.append(g2)
if(re.search(regex, Ip8)):
   print("Valid Ip address")
   
   
   ipv46 = Ip8.split(".")
   x = [str(i) for i in ipv46]
   res6 = int("".join(x))
   h = bin(res6)
   ip_list.append("\n Binary form of 8th ip address")
   ip_list.append(h)
   h1= oct(res6)
   ip_list.append("\nOctal Form of 8th ip address:\n")
   ip_list.append(h1)
   h2   = oct(res6)
   ip_list.append("\nHexadecimal Form of 8th ip address \n")
   ip_list.append(h2)
else:
   print("Invalid Ip address")
if(re.search(regex, Ip9)):
   print("Valid Ip address")
   
   ipv7 = Ip9.split(".")
   y = [str(i) for i in ipv7]
   res7 = int("".join(y))

   i = bin(res7)
    
   ip_list.append("\n Binary form of 9th ip address")
   ip_list.append(i)
   
   
   i1= oct(res7)
   
   ip_list.append("\nOctal Form of 9th ip address:\n")
   ip_list.append(i1)
    
   i2   = hex(res7)
   
   ip_list.append("\nHexadecimal Form of 9th ip address\n")
   ip_list.append(i2)
   
else:
   print("Invalid Ip address")
if(re.search(regex, Ip10)):
   print("Valid Ip address")
   ipv8 = Ip10.split(".")
   z =  [ str(i) for i in ipv8]
   res8 = int("".join(z))
   j = bin(res8)
   ip_list.append("\n Binary form of 10th ip address")
   ip_list.append(j)
   j1= oct(res8)
   ip_list.append("\nOctal Form of 10th ip address:\n")
   ip_list.append(j1)
   print("\n")
   j2   = hex(res8)
   ip_list.append("\nHexadecimal Form of 10th ip address\n")
   ip_list.append(j2)
   f = open("conversion.txt","w")
    
   f.writelines(ip_list)
   f.close()
   f = open("conversion.txt","r")
   print(f.read())
   print()
   f.close()
else:
   print("Invalid Ip address")
    
        
