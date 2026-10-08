Book = [
    ("Python 101", "John Doe", 2020),
    ("Data Science Basics", "Jane Smith", 2014),
    ("AI for Everyone", "Alex Turner", 2017),
]

while True:
    menuInput = input("""
========== Library Organizer ===========
1. Tampilkan Buku (Tahun Terbit >= 2015)
2. Tambah buku baru
3. Hapus buku
4. Tampilkan Semua Buku
5. Exit
>> """)
    if menuInput == "1":
        for Judul, Penulis, TahunTerbit in Book:
            if TahunTerbit >= 2015:
                print(f"\nJudul: {Judul}\nPenulis: {Penulis}\nTahun Terbit: {TahunTerbit}")
            else:
                continue
        input("\nPress ENTER to continue...")
    if menuInput == "2":
        BukuBaru = input("Input Data Buku Baru dengan format Judul/Penulis/TahunTerbit:\n>> ")
        split_BukuBaru = BukuBaru.split("/")

        Judul, Penulis, TahunTerbit = split_BukuBaru[0:]
        Book.append((Judul,Penulis,int(TahunTerbit)))
    if menuInput == "3":
        index = 0
        DeletedBook = ""
        JudulBuku = input("Input judul buku yang ingin dihapus: ")
        for dataBuku in Book:
            if dataBuku[0].lower().find(JudulBuku.lower()) >= 0:
                confirmation = input(f"Targeted Book: {dataBuku[0]} by {dataBuku[1]} ({dataBuku[2]}), Continue Delete? (Y/N): ").upper()
                if confirmation == "Y":
                    DeletedBook = Book.pop(index)
                    break
                else:
                    print("Continue finding targeted book...")
            index += 1

        if DeletedBook != "":
            print(f"Sucessfully removed {DeletedBook}")
        else:
            print("Book Title to delete not found!")
        input("\nPress ENTER to continue...")
    elif menuInput == "4":
        for Judul, Penulis, TahunTerbit in Book:
            print(f"\nJudul: {Judul}\nPenulis: {Penulis}\nTahun Terbit: {TahunTerbit}")
        input("\nPress ENTER to continue...")
    elif menuInput == "5":
        break