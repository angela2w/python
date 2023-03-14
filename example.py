#example of if else elif statements
admission=int(input("Write down your admision number:"))

if admission>9800 and admission<=9900:
    print("Moi Hostel")
elif admission>9600 and admission<=9800:
    print("Ruwenzori hostel")
elif admission>9400 and admission<=9600:
    print("Everest Hostel")
elif admission>9200 and admission<=9400:
    print("Mt Kenya Hostel")
elif admission>=9000 and admission<=9200:
    print("MTN Hostel")
else:
    print("Invalid admission number")