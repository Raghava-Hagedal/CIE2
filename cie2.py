import sys.argv
if len(sys.argv) == 6:
    script_to_item = sys.argv[0]
    name = sys.argv[1]
    branch = sys.argv[2]
    fees_paid = int(sys.argv[3])
    balance = sys.argv[4]
    total_fees = int(sys.argv[5])
else:
    name = "Raghava"
    branch = "BCA"
    fees_paid = "87000"
    balance = "NULL"
    total_fees = "87000"

if fees_paid == total_fees:
    print("Your fees is paid completely")
else:
    print("Your fees is Pending")

print(f"Name: {name}")
print(f"Branch: {branch}")
print(f"Fees Paid: {fees_paid}")
print(f"Balance Fees: {balance}")