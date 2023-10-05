entries = int(input("enter no. of entries"))
phone_book = {}
for x in range(entries):
    user_input = input("Enter number, name:").split(',')
    phone_book[user_input[0]] = user_input[1]
print(phone_book)
