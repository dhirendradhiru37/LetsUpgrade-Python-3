#Assignment-1 Day3

Altitude=int(input("Enter the input as Altitude(in ft)= "))

if Altitude>=0 and Altitude<=1000:
    print("Altitude is ",Altitude,",Safe to land")
elif Altitude>1000 and Altitude<5000:
    print("Altitude is ",Altitude,",Bring down to 1000")
else:
    print("Altitude is ",Altitude,",Turn around and try later") 