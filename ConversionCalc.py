userConversionType = input('1: Inches to mm 2: mm to inches?')

conversionTypeInt = int(userConversionType)

userNumber = input("What is your number?")
userNumberFloat = float(userNumber)

# 1 convert inches to mm
if conversionTypeInt == 1:
    print("convert inches to mm")
    convertedNumber = userNumberFloat * 25.4
    convertedString = "{0:.4f} inches is = {1:.4f} mm"
    

# 2 convert mm to inches
if conversionTypeInt == 2:
    print("convert mm to inches")
    convertedNumber = userNumberFloat / 25.4
    convertedString = "{0:.4f} mm is = {1:.4f} inches"


# 1 in = 25.4 mm
# Convert from in to mm
#       userNumber *25.4 mm = converted number

# 25.4 mm = 1 in
# Convert from mm to in
#       userNumber / 25.4 mm = converted number

print(convertedString.format(userNumberFloat, convertedNumber))