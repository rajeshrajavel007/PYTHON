alpha = [0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
encryp_msg = ""
capital = ""
init = 1
while(init):
 normsg = input("Enter the Message:")
 for b,i in enumerate(normsg):
     if (normsg[b].islower()) == True:
         capital += normsg[b].upper()
     else:
         capital += normsg[b]
 for d,i in enumerate(capital):
     for c,j in enumerate(alpha):
         if i == alpha[c]:
             encryp_key = c*(c-1) - c*c
             encryp_msg += alpha[encryp_key]
     if (i == " "):
         encryp_msg += capital[d]
 print(encryp_msg.lower())
 encryp_msg = ""
 capital = ""
 init = int(input("Do you want to continue(1/0):"))



