def search_by_date(transactions):
  date=input("enter date: ")
  for transaction in transactions:
    if transaction['date']==date:
      return transaction
  return "Transaction Not Found"

def sort_amount(transactions):
  n=len(transactions)
  for i in range(n):
    for j in range(n-1):
      if transactions[j]["amount"]>transactions[j+1]["amount"]:
        transactions[j],transactions[j+1]=transactions[j+1],transactions[j]
  return transactions

def add_data(transactions):
  dic={"date": input("enter date: "),
       "amount": int(input("enter amount: ")),
       "desc":input("enter desc: ")}
  transactions.append(dic)
  return transactions

def dele_dic(transactions):
  date=input("enter date: ")
  for transaction in transactions:
    if date in transaction["date"]:
      transactions.remove(transaction)
  return transactions

def sum_amount(transactions):
  year=input("enter year: ")
  sum=0
  for transaction in transactions:
    if transaction["date"][0:4]==year:
        sum+=transaction["amount"]
  return sum