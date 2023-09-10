import datetime as dt

def hari_lahir():
    tahun = int(input("enter your year of birth: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    hari_lahir = dt.date(tahun,bulan,tanggal)
    print(f"Your days birthday is {hari_lahir:%A}")

def umur_tahun():
    tahun = int(input("enter your year of birth: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    birthday= dt.date(tahun,bulan,tanggal)
    today= dt.date.today()
    umur_tahun= today - birthday
    print(f"Your age is {umur_tahun.days // 365} years old")

def umur_bulan():
    tahun = int(input("enter your year of birth: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    birthday= dt.date(tahun,bulan,tanggal)
    today= dt.date.today()
    umur_bulan= today - birthday
    print(f"Your age is {umur_bulan.days // 30} month.")

def umur_minggu():
    tahun = int(input("enter your year of birth: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    today = dt.date.today()
    birthday = dt.date(tahun,bulan,tanggal)
    umur_minggu = today - birthday
    print(f"Your age in weeks is {umur_minggu.days // 7} weeks.")

def umur_hari():
    tahun = int(input("enter your year of birth: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    birthday= dt.date(tahun,bulan,tanggal)
    today= dt.date.today()
    umur_hari= today - birthday
    print(f"Your age is {umur_hari}")

def umur_lengkap():
    tahun = int(input("enter your year of birth: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    birthday = dt.date(tahun,bulan,tanggal)
    today = dt.date.today()
    umur_hari = today - birthday
    umur_tahun = umur_hari.days // 365
    umur_bulan_sisa = (umur_hari.days % 365) // 30
    umur_sisa_hari = (umur_hari.days % 365) % 30 % 7
    umur_sisa_minggu = (umur_hari.days % 365) % 30 // 7
    print(f"Your age is {umur_tahun} years,{umur_bulan_sisa} month,{umur_sisa_minggu} weeks,{umur_sisa_hari} days.")

def future_birthday():
    tahun = int(input("enter the year: \t"))
    bulan = int(input("enter your month of birth: \t"))
    tanggal = int(input("enter your date of birth: \t"))
    future_birthday = dt.date(tahun,bulan,tanggal)
    print(f"your birthday in {tahun} is {future_birthday:%A}")

print("Choose the Option".center(37,"="))

while True:
    
    userinput = int(input(" 1.See your birthday\n 2.See your age(in years)\n 3.See your age(in month)\n 4.See your age(in weeks)\n 5.See your age(in days)\n 6.See your age(Years to Days)\n 7.See your future birthday\n"))
    if userinput == 1:
        hari_lahir()
    elif userinput == 2:
        umur_tahun()
    elif userinput == 3:
        umur_bulan()
    elif userinput == 4:
        umur_minggu()
    elif userinput == 5:
        umur_hari()
    elif userinput == 6:
        umur_lengkap()
    elif userinput == 7:
        future_birthday()
    else:
        break
