import datetime
import random
import calendar

while True:
    menuInput = input("""=== SwiftParcel Delivery ===
1. Register Shipment
2. Exit Program
-> """)
    if menuInput == "1":
        while True:
            customerID = input("Input Customer ID: ")
            if not customerID.isnumeric():
                print("Customer ID must be numeric!")
                continue
            break

        while True:
            customerName = input("Input Customer Name: ")
            nospaceName = customerName.replace(" ","")

            if len(nospaceName) < 5 or len(nospaceName) > 20:
                print("Name must only contain 5-20 characters!")
                continue
            elif not nospaceName.isalpha():
                print("Name must only contain alphabetical characters!")
                continue
            break

        while True:
            parcelType = input("Input Parcel Type (Document/Package/Food): ")
            if parcelType not in ("Document", "Package", "Food"):
                print("Parcel Type must be Document/Package/Food!")
                continue
            break

        while True:
            parcelName = input("Input Parcel Name: ")
            if len(parcelName) < 3 or len(parcelName) > 30:
                print("Parcel Name must be 3-30 characters inclusive")
                continue
            break

        while True:
            try:
                Qt = int(input("Input quantity: "))
            except ValueError:
                print("Quantity must be numeric!")
                continue

            if Qt < 1 or Qt > 50:
                print("Quantity must be 1-50 inclusive")
                continue
            break

        while True:
            try:
                pricePerParcel = int(input("Input Price per Parcel: "))
            except ValueError:
                print("Price per parcel must be numeric!")
                continue

            if pricePerParcel < 1000:
                print("Price per parcel must be >Rp1.000")
                continue
            break

        while True:
            branchCode = input("Input branch code: ")
            if not branchCode.startswith("BR"):
                print("Branch code must start with 'BR'!")
                continue
            break

        while True:
            try:
                shipmentMonth = int(input("Input shipment month (1-12): "))
            except ValueError:
                print("Shipment month must be numeric! (1-12)")
                continue

            if shipmentMonth < 0 or shipmentMonth > 12:
                print("Shipment month must be inputted between 1-12")
                continue
            break

        while True:
            try:
                shipmentYear = int(input("Input shipment year: "))
            except ValueError:
                print("Shipment year must be numeric!")
                continue

            if shipmentYear < 2020 or shipmentYear > datetime.datetime.now().year:
                print(f"Shipment year must be inputted between 2020 - {datetime.datetime.now().year}!")
                continue
            break

        while True:
            deliveryNote = input("Input delivery note: ")
            if deliveryNote.replace(" ","") == "":
                print("Delivery note cannot be empty!")
                continue
            elif len(deliveryNote) > 40:
                print("Delivery note cannot contain more than 40 characters!")
                continue
            break

        ShipmentID = "SP" + str(random.randint(100,999))
        ShipmentMonthName = calendar.month_name[shipmentMonth]
        TotalPayment = Qt * pricePerParcel
        shipmentAge = datetime.datetime.now().year - shipmentYear

        print("="*10 + " SHIPMENT SUMMARY " + "="*10)
        print(f"""Shipment ID : {ShipmentID}
Customer ID : CS{customerID}
Customer Name : {customerName}
Parcel Type : {parcelType}
Parcel Name : {parcelName}
Quantity : {Qt}
Price per Parcel: Rp{pricePerParcel:,}
Branch Code : {branchCode}
Shipment Period : {ShipmentMonthName} {shipmentYear}
Shipment Age : {shipmentAge}
Delivery Note : {deliveryNote}
Total Payment : Rp{TotalPayment:,}""")
        print("="*38)
        print("Shipment registered successfully!")
        input("Press ENTER to return to the main menu...")
        continue
    elif menuInput == "2":
        print("Thank you for using SwiftParcel!")
        break
    else:
        print("Choice must be 1 or 2")
        continue