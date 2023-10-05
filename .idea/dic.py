dis={
    "1234567890":"murugan",
    "0987654321":"mani",
    "4178198176":"sasi",
    "2467617878":"prithive"
}
#num=input("enter number:")
#print(dis.get(num, 'sorry contact not found'))
#print(dis['82942649248924'])#error
name=input("enter contact:")
for key,value in dis.items():
    if value==name:
        print(key)
