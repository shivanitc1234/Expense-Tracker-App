from features import search_by_date,sort_amount,add_data,dele_dic,sum_amount
transactions=[{"date":"2022-10-13",
              "amount":5000,
              "desc":"fruits"
              },{"date":"2023-10-15",
              "amount":7000,
              "desc":"vegetables"},
               {"date":"2023-12-22",
              "amount":4000,
              "desc":"clothes"},
             {"date":"2024-01-23",
              "amount":10000,
              "desc":"Dry Fruits"},
             {"date":"2024-02-12",
              "amount":50000,
              "desc":"Laptop"}]
flag=True
while flag:
  print("Expense Tracker App:\n 1.Adding\n 2.Searching\n 3.Sorting\n 4.Deleting\n 5.display\n 6.Stop Application\n 7.sum of amount\n ")
  choice=int(input("Choose feature: "))
  if choice==1:
    print("-"*50)
    print("adding data")
    print("-"*50)
    print(add_data(transactions))
    print("-"*50)
  elif choice==2:
    print("-"*50)
    print("Searching Data")
    print("-"*50)
    print(search_by_date(transactions))
    print("-"*50)
  elif choice==3:
    print("-"*50)
    print("Sorting data")
    print("-"*50)
    print(sort_amount(transactions))
    print("-"*50)
  elif choice==4:
    print("-"*50)
    print("deleting data")
    print("-"*50)
    print(dele_dic(transactions))
    print("-"*50)
  elif choice==5:
    print("-"*50)
    print(transactions)
    print("-"*50)
  elif choice==6:
    print("-"*50)
    print("Application Stopped")
    flag=False
    print("-"*50)
  elif choice==7:
    print("-"*50)
    print("Sum of amount of a given year")
    print("-"*50)
    print(sum_amount(transactions))
    print("-"*50)
  else:
    print("-"*50)
    print("Please enter correct feature")
    print("-"*50)
