has_good_credit = True
has_criminal_record = True

if has_good_credit and has_criminal_record:
    print("Not Eligible for Loan")

elif has_good_credit or has_criminal_record:
    print("Again not eligible")

elif has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
