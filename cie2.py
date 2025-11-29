import sys
if len(sys.argv) == 6:
    script_to_item = sys.argv[0]
    name = sys.argv[1]
    branch = sys.argv[2]
    fees_paid = int(sys.argv[3])
    balance = sys.argv[4]
    total_fees = int(sys.argv[5])
else:
    name = ""
    branch = ""
    fees_paid = ""
    balance = ""
    total_fees = ""

if fees_paid == total_fees:
    print("Your fees is paid completely")
else:
    print("Your fees is Pending")

print(f"Name: {name}")
print(f"Branch: {branch}")
print(f"Fees Paid: {fees_paid}")
print(f"Balance Fees: {balance}")
