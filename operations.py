# Number of hours in a year
def multiply() :
    oneDayHours=24
    oneYearsDays=365
    print( oneDayHours * oneYearsDays)
multiply()     


# number of hours in a week
def multiply() :
    oneDaysHours=24
    daysOfWeek=7
    print(oneDaysHours * daysOfWeek)
multiply()    


# waking hours per week
def wakingHour() :
    sleepingHours=8
    daysOfWeek=7
    totalHoursInWeek=168
    print(sleepingHours * daysOfWeek)
    print( totalHoursInWeek - (sleepingHours * daysOfWeek))
     
wakingHour()


# spend money in a month
def leftOverMoney() :
    houserent=4000
    electricity=2000
    water=4566
    homeAppliances=4000
    totalSalary=40000
    print(totalSalary - (houserent + electricity + water + homeAppliances))

leftOverMoney()


# subratcton
def subtract() :
    tax=5679
    debt=20000
    totalsalary=100000
    print(totalsalary - tax - debt)   

subtract()    


# percentage of annual scores
def  percentageOfScores() :
     numberOfSubjects=6
     english=95
     mathematic=85
     chemistry=90
     physic=89
     biology=96
     history=90
     print((english + mathematic + chemistry + physic + biology + history) /  numberOfSubjects)

percentageOfScores()
