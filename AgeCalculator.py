from time import sleep

while True:
    By = int(input("Birth Year? "))
    Bm = int(input("Birth Month? "))
    Bd = int(input("Birth Day? "))

    Cy = int(input("\nCurrent Year? "))
    Cm = int(input("Current Month? "))
    Cd = int(input("Current Day? "))

    y = Cy-By
    m = Cm-Bm
    d = Cd-Bd

    if y >= 4:
        x = y//4
        z = (x*366)+(y-x)*365
        a = m*30.4375
        total = int((z+a+d)+1)
        print("\n→",((total*24)*60)*60, " Seconds")
        print("→",(total*24)*60, " Minutes")
        print("→",total*24, " Hours")
        print("→",total, " Days")
        print("→",int(total//30.4375), " Months")
        print("→",int((total//30.4375)/12), " Years\n")
    elif y<=4:
        z = y*365
        a = m*30.4375
        total = int((z+a+d))
        print("\n→",((total*24)*60)*60, " Seconds")
        print("→",(total*24)*60, " Minutes")
        print("→",total*24, " Hours")
        print("→",total, " Days")
        print("→",int(total//30.4375), " Months")
        print("→",int((total//30.4375)/12), " Years\n")
    else:
        print("\n\"","Error!!!\"\n")

    print("\n\n\nPlease wait for 10 seconds...\n\n")
    sleep(10)
    continue
