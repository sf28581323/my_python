month = {"一月": "January",
         "二月": "February",
         "三月": "March",
         "四月": "April",
         "五月": "May",
         "六月": "June",
         "七月": "July",
         "八月": "August",
         "九月": "September",
         "十月": "October",
         "十一月": "November",
         "十二月": "December"}
n = input()

if  n in month:
    print(month[n])
else :
    print("Error")
