#Match case for month with embedded if then for date

BirthMonth = input("What month were you born?").lower()
BirthDay = int(input("What date were you born?"))

match BirthMonth:
    case "january":
        if BirthDay <= 21:
            sign = "Capricorn"
        else:
            sign = "Aquarius"
    case "february":
        if BirthDay <= 21:
            sign = "Aquarius"
        else:
            sign = "Pisces"
    case "march":
        if BirthDay <= 21:
            sign = "Pisces"
        else:
            sign = "Aries"
    case "april":
        if BirthDay <= 21:
            sign = "Aries"
        else:
            sign = "Taurus"
    case "may":
        if BirthDay <= 21:
            sign = "Taurus"
        else:
            sign = "Gemini"
    case "june":
        if BirthDay <= 21:
            sign = "Gemini"
        else:
            sign = "Cancer"
    case "july":
        if BirthDay <= 21:
            sign = "Cancer"
        else:
            sign = "Leo"
    case "august":
        if BirthDay <= 21:
            sign = "Leo"
        else:
            sign = "Virgo"
    case "september":
        if BirthDay <= 21:
            sign = "Virgo"
        else:
            sign = "Libra"
    case "october":
        if BirthDay <= 21:
            sign = "Libra"
        else:
            sign = "Scorpio"
    case "november":
        if BirthDay <= 21:
            sign = "Scorpio"
        else:
            sign = "Sagittarius"
    case "december":
        if BirthDay <= 21:
            sign = "Sagittarius"
        else:
            sign = "Capricorn"

if sign in ["Aries", "Aquarius"]:
    print("You are an " + sign)
else:
    print("You are a " + sign)


