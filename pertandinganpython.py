import random

#permainan tekaan nombor proton dan nama elemen
rahsia = random.randint(19,25)
teka = True
while teka:
    nombor = int(input("masukkan nombor proton tekaan anda(19,25):"))
    #input nombor proton
    if nombor == rahsia:
        print ("tahniah tekaan anda tepat")
        #nama elemen berdasarkan nombor
        if rahsia == 19:
            print("nama elemen berdasarkan nombor yang diteka ialah kalium")
            teka=False
        elif rahsia == 20:
            print("nama elemen berdasarkan nombor yang diteka ialah kalsium")
            teka=False
        elif rahsia == 21:
            print("nama elemen berdasarkan nombor yang diteka ialah skandium")
            teka=False
        elif rahsia == 22:
            print("nama elemen berdasarkan nombor yang diteka ialah titanium")
            teka=False
        elif rahsia == 23:
            print("nama elemen berdasarkan nombor yang diteka ialah vanadium")
            teka=False
        elif rahsia == 24:
            print("nama elemen berdasarkan nombor yang diteka ialah kromium")
            teka=False
        elif rahsia == 25:
            print("nama elemen berdasarkan nombor yang diteka ialah mangan")
            teka=False
        teka = False
        
    elif nombor > rahsia:
        print ("nombor tekaan lebih daripada nombor sebenar")
    else:
        print ("nombor tekaan anda kurang daripada nombor sebenar")
          
          
else:
    print("jumpa lagi!!><")

