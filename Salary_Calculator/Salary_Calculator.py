from tkinter import *

#Create Window object
app = Tk()

#Hours Worked Per Week
hoursWorkedWeek_text = IntVar()
hoursWorkedWeek_label = Label(app, text="Hours worked per week: ", font=("bold", 13), pady = 20)
hoursWorkedWeek_label.grid(row=0,column=0, sticky=W)
hoursWorkedWeek_entry = Entry(app, textvariable=hoursWorkedWeek_text)
hoursWorkedWeek_entry.grid(row=0,column=1)

#Rate Earned Per Hour
rateEarnedPH_text = IntVar()
rateEarnedPH_label = Label(app, text="Rate earned per hour: ", font=("bold", 13))
rateEarnedPH_label.grid(row=0,column=2, sticky=W)
rateEarnedPH_entry = Entry(app, textvariable=rateEarnedPH_text)
rateEarnedPH_entry.grid(row=0,column=3)

#Overtime Hours
overtimeHours_text = IntVar()
overtimeHours_label = Label(app, text="Overtime hours: ", font=("bold", 13))
overtimeHours_label.grid(row=1,column=0, sticky=W)
overtimeHours_entry = Entry(app, textvariable=overtimeHours_text)
overtimeHours_entry.grid(row=1,column=1)

#Rate for Overtime
rateForOvertime_text = IntVar()
rateForOvertime_label = Label(app, text="Rate for overtime: ", font=("bold", 13))
rateForOvertime_label.grid(row=1,column=2, sticky=W)
rateForOvertime_entry = Entry(app, textvariable=rateForOvertime_text)
rateForOvertime_entry.grid(row=1,column=3)

#Calculation
def calculate():
    try:
        hpw_str = hoursWorkedWeek_entry.get()
        hpw = int(hpw_str)
    except:
        errorMessage = StringVar()
        errorMessage_label = Label(app, text="Please enter a whole \n number in the Hours worked box", font=("bold", 11),)
        errorMessage_label.grid(row=3,column=0)
        
        

    rph_str = rateEarnedPH_entry.get()
    rph = float(rph_str)

    try:
        oh_str = overtimeHours_entry.get()
        oh = int(oh_str)
    except:
        errorMessage = StringVar()
        errorMessage_label = Label(app, text="Please enter a whole number \n in the Hours worked box", font=("bold", 11))
        errorMessage_label.grid(row=4,column=0)
        
        

    rot_str = rateForOvertime_entry.get()
    rot = float(rot_str)

    try:
        _salaryPerWeek = hpw * rph + oh * rot
        format_salaryPerWeek = "{:.2f}".format(_salaryPerWeek)
        _salaryPerWeek = float(format_salaryPerWeek)

        _salaryPerMonth = _salaryPerWeek * 4
        format_salaryPerMonth = "{:.2f}".format(_salaryPerMonth)
        _salaryPerMonth = float(format_salaryPerMonth)

        _salaryPerYear = _salaryPerMonth * 12
        format_salaryPerYear = "{:.2f}".format(_salaryPerYear)
        _salaryPerYear = float(format_salaryPerYear)

        salaryPerWeek = str(_salaryPerWeek)
        salaryPerMonth = str(_salaryPerMonth)
        salaryPerYear = str(_salaryPerYear)

        salaryPerWeek_text = "Your Weekly Salary is $" + salaryPerWeek
        salaryPerMonth_text = "Your Monthly Salary is $" + salaryPerMonth
        salaryPerYear_text = "Your Yearly Salary is $" + salaryPerYear

        #Show Wages
        salaryPerWeek_text_str = StringVar()
        salaryPerWeek_label = Label(app, text=salaryPerWeek_text, font=("bold", 13), pady = 20)
        salaryPerWeek_label.grid(row=3,column=0)

        salaryPerMonth_text_str = StringVar()
        salaryPerMonth_label = Label(app, text=salaryPerMonth_text, font=("bold", 13), pady = 20)
        salaryPerMonth_label.grid(row=4,column=0)

        salaryPerYear_text_str = StringVar()
        salaryPerYear_label = Label(app, text=salaryPerYear_text, font=("bold", 13), pady = 20)
        salaryPerYear_label.grid(row=5,column=0)
    except:
        errorMessage = StringVar()
        errorMessage_label = Label(app, text="Fix the issue(s) \n to continue", font=("bold", 11))
        errorMessage_label.grid(row=5,column=0)

#Buttons
calculate_btn = Button(app, text="Calculate", width=12, command=calculate)
calculate_btn.grid(row=2,column=1, pady=20)

app.title("Salary Calculator")
app.geometry("700x400")

#Start program
app.mainloop()