import pickle
import sys

class Employee:
    def __init__(self, str1, str2, make, model, year, mileage):
        self.EmpName = str1
        self.EmpAdrs = str2
        self.Vdata = Vehicle(make, model, year, mileage)

    def getempname(self):
        return self.EmpName

    def setempname(self, empname):
        self.EmpName = empname
        print("Name changed successfully!")

    def getempadrs(self):
        return self.EmpAdrs

    def setempadrs(self, address):
        self.EmpAdrs = address

    def getvdata(self):
        return self.Vdata

    def __str__(self):
        return f'\nEmployee Name: {self.EmpName} Employees Address: {self.EmpAdrs} Vehicle\'s Data: {self.Vdata}'


class FullTimeEmployee(Employee):
    def __init__(self, str1, str2, make, model, year, mileage, salary):
        super().__init__(str1, str2, make, model, year, mileage)
        self.salary = salary

    def getsal(self):
        return self.salary

    def setsal(self, sal):
        self.salary = sal

    def CompensationFTE(self):
        if self.salary <= 40000:
            tax = self.salary * 16 / 100
        elif 40000 < self.salary <= 75000:
            t1 = 40000 * 16 / 100
            t2 = (self.salary - 40000) * 26 / 100
            tax = t1 + t2
        else:
            t1 = 40000 * 16 / 100
            t2 = 35000 * 26 / 100
            t3 = (self.salary - 75000) * 33 / 100
            tax = t1 + t2 + t3
        return self.salary - tax

    def __str__(self):
        return f'\nEmployee name: {self.EmpName} Employee address: {self.EmpAdrs} {self.Vdata} Salary of employee: {self.salary}'


class HourlyEmployee(Employee):
    def __init__(self, str1, str2, make, model, year, mileage, hworked, hrate):
        super().__init__(str1, str2, make, model, year, mileage)
        self.hoursWorked = hworked
        self.hourlyRate = hrate

    def gethwork(self):
        return self.hoursWorked

    def sethwork(self, hwork):
        self.hoursWorked = hwork

    def gethrate(self):
        return self.hourlyRate

    def sethrate(self, hrate):
        self.hourlyRate = hrate

    def CompensationHE(self):
        if self.hoursWorked <= 40:
            c = self.hoursWorked * self.hourlyRate
        else:
            c = (40 * self.hourlyRate) + ((self.hoursWorked - 40) * self.hourlyRate * 1.7)
        return c

    def __str__(self):
        return f'\nEmployee name: {self.EmpName} Employee address: {self.EmpAdrs} {self.Vdata} Hours worked: {self.hoursWorked} Hourly Rate: {self.hourlyRate}'


class Consultant(Employee):
    def __init__(self, str1, str2, make, model, year, mileage, hworked, Ptype):
        super().__init__(str1, str2, make, model, year, mileage)
        self.hoursWorked = hworked
        self.ProjectType = Ptype

    def getchworked(self):
        return self.hoursWorked

    def setchworked(self, hworked):
        self.hoursWorked = hworked
        print('Hours updated successfully!')

    def getPtype(self):
        return self.ProjectType

    def setPtype(self, Pt):
        self.ProjectType = Pt

    def CompensationC(self):
        rates = {1: 55.00, 2: 70.00, 3: 85.00}
        return self.hoursWorked * rates.get(self.ProjectType, 0)

    def __str__(self):
        return f'\nEmployee name: {self.EmpName} Employee address: {self.EmpAdrs} {self.Vdata} Worked Hours: {self.hoursWorked} Project type: {self.ProjectType}'


class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f'\nVehicle make: {self.make} Vehicle Model: {self.model} Vehicle Year: {self.year} Mileage: {self.mileage}'


def add_employee():
    while True:
        try:
            b=int(input('Type of Employee?(1-Full Time;2-Hourly;3-Consultant) : '))
            if b in [1, 2, 3]:
                break
            else:
                print("Invalid input, Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid choice. Please enter 1, 2 or 3")  
    if b==1:
        print("Adding an Employee")
        str1=input("Enter the Employee's name: ")
        str2=input("Enter the employee's address: ")
        make=input("Enter the vehicle's make: ")
        model=input("Enter the vehicle's model: ")
        while True:
            year = input("Enter the year of manufacture: ")
            try:
                year = int(year)
                break
            except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        while True:
            mileage = input("Enter the mileage: ")
            try:
                mileage = int(mileage)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        while True:
            salary = input("Enter the salary: ")
            try:
                salary = float(salary)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        FTE1=FullTimeEmployee(str1, str2, make, model, year, mileage, salary)
        with open('empdata.dat', 'ab') as fb: 
               pickle.dump(FTE1, fb) 
               print("Employee added to database\n")
               return
    elif b==2:
            print("Adding an Employee")
            str1=input("Enter the Employee's name: ")
            str2=input("Enter the employee's address: ")
            make=input("Enter the vehicle's make: ")
            model=input("Enter the vehicle's model: ")
            while True:
                year = input("Enter the year of manufacture: ")
                try:
                    year = int(year)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            while True:
                mileage = input("Enter the mileage: ")
                try:
                    mileage = int(mileage)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            while True:
                hworked= input("Enter the hours worked: ")
                try:
                    hworked = int(hworked)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            while True:
                hrate= input("Enter the hourly rate: ")
                try:
                    hrate = float(hrate)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            HE1=HourlyEmployee(str1, str2, make, model, year, mileage, hworked, hrate)
            with open('empdata.dat', 'ab') as fb: 
                pickle.dump(HE1, fb) 
                print("Employee added to database\n")
                return
    elif b==3:
            print("Adding an Employee")
            str1=input("Enter the Employee's name: ")
            str2=input("Enter the employee's address: ")
            make=input("Enter the vehicle's make: ")
            model=input("Enter the vehicle's model: ")
            while True:
                year = input("Enter the year of manufacture: ")
                try:
                    year = int(year)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            while True:
                mileage = input("Enter the mileage: ")
                try:
                    mileage = int(mileage)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            while True:
                hworked= input("Enter the hours worked: ")
                try:
                    hworked = int(hworked)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            while True:
                try:
                    Ptype = int(input("Project Type? (Enter a number between 1-3): "))
                    if Ptype in [1, 2, 3]:
                        break
                    else:
                        print('Invalid input. Please enter a number between 1-3.')
                except ValueError:
                    print("Invalid input. Please enter a numeric value between 1-3.")
            C1=Consultant(str1, str2, make, model, year, mileage, hworked, Ptype)
            with open('empdata.dat', 'ab') as fb: 
                pickle.dump(C1, fb) 
                print("Employee added to database\n")
                return

def print_all_employees():
    try:
        with open('empdata.dat', 'rb') as fb:
                print("\n==================================================================================================================================================")
                print("Data of all Full Time Employees in the database")
                print("====================================================================================================================================================")
                print(f"{'Emp Name':<20} {'Address':<35} {'Veh Make':<15} {'Veh Model':<15} {'Year Manf':<15} {'Mileage':<15} {'Salary':<15}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                try:
                        while True:
                            emp = pickle.load(fb)
                            if isinstance(emp, FullTimeEmployee):
                                print(f"{emp.EmpName:<20} {emp.EmpAdrs:<35} {emp.Vdata.make:<15} {emp.Vdata.model:<15} {emp.Vdata.year:<15} {emp.Vdata.mileage:<15} {emp.salary:<15}")
                except EOFError:
                    pass    
                print("\n==================================================================================================================================================")
                print("Data of all Hourly Employees in the database")
                print("====================================================================================================================================================")
                print(f"{'Emp Name':<20} {'Address':<35} {'Veh Make':<15} {'Veh Model':<15} {'Year Manf':<15} {'Mileage':<15} {'Hrs worked':<15} {'Hrly Rate':<15}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------")    
        with open('empdata.dat', 'rb') as fb:
            try:
                while True:
                    emp = pickle.load(fb)
                    if isinstance(emp, HourlyEmployee):
                        print(f"{emp.EmpName:<20} {emp.EmpAdrs:<35} {emp.Vdata.make:<15} {emp.Vdata.model:<15} {emp.Vdata.year:<15} {emp.Vdata.mileage:<15} {emp.hoursWorked:<15} {emp.hourlyRate:<15}")
            except EOFError:
                pass
                print("\n=================================================================================================================================================")
                print("Data of all Consultants in the database")
                print("===================================================================================================================================================")
                print(f"{'Emp Name':<20} {'Address':<35} {'Veh Make':<15} {'Veh Model':<15} {'Year Manf':<15} {'Mileage':<15} {'Hours worked':<15} {'Proj Type':<15}")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")    
        with open('empdata.dat', 'rb') as fb:
            try:
                while True:
                    emp = pickle.load(fb)
                    if isinstance(emp, Consultant):
                        print(f"{emp.EmpName:<20} {emp.EmpAdrs:<35} {emp.Vdata.make:<15} {emp.Vdata.model:<15} {emp.Vdata.year:<15} {emp.Vdata.mileage:<15} {emp.hoursWorked:<15} {emp.ProjectType:<15}")
            except EOFError:
                print()
                return
    except FileNotFoundError:
        print("No employee data found. The database file 'empdata.dat' does not exist.")
        
def print_compensation():
    try:
        with open('empdata.dat', 'rb') as fb:
            print("\n===========================================================================")
            print("Employee name and Compensation of all Employees")
            print("===========================================================================")
            print(f"{'Employee Name':<20} {'Compensation':<20}")
            print("-----------------   -------------------")
            try:
                while True:
                    employee = pickle.load(fb)
                    if isinstance(employee, FullTimeEmployee):
                        compensation = employee.CompensationFTE()
                        print(f"{employee.EmpName:<20} ${compensation:,.2f}")
                    elif isinstance(employee, HourlyEmployee):
                        compensation = employee.CompensationHE()
                        print(f"{employee.EmpName:<20} ${compensation:,.2f}")
                    elif isinstance(employee, Consultant):
                        compensation = employee.CompensationC()
                        print(f"{employee.EmpName:<20} ${compensation:,.2f}")
            except EOFError:
                print()
                return
    except FileNotFoundError:
        print("No employee data found. The database file 'empdata.dat' does not exist.")


def print_high_mileage():
    try:    
        with open('empdata.dat', 'rb') as fb:
            print("===========================================================================")
            print("Employee name and Vehicle Data For High Mileage Vehicles")
            print("===========================================================================")
            print(f"{'Employee':<25} {'Make':<10} {'Model':<10} {'Year':<10} {'Mileage':<10}")
            print("---------------------    ---------  --------   ------     ---------")
            try:
                while True:
                    employee = pickle.load(fb)
                    if employee.Vdata.mileage > 78000:
                        print(f"{employee.EmpName:<25} {employee.Vdata.make:<10} {employee.Vdata.model:<10} {employee.Vdata.year:<10} {employee.Vdata.mileage:,.0f}")
            except EOFError:
                print()
                return
    except FileNotFoundError:
        print("No employee data found. The database file 'empdata.dat' does not exist.")
        
def main():
    running=True
    while running:
        print('====Menu====')
        print('1. To add an Employee')
        print('2. To print employee data for all employees')
        print('3. To print the employee name and compensation of all employees')
        print('4. To print the employee name with vehicle information for high mileage vehicles')
        print('5. To exit the program')

        try:
            choice = int(input("Your Selection: "))
            if choice == 1:
                add_employee()
            elif choice == 2:
                print_all_employees()
            elif choice == 3:
                print_compensation()
            elif choice == 4:
                print_high_mileage()
            elif choice == 5:
                while True:
                    exit_input = input("Are you sure you want to exit? (Y/N): ").strip().lower()
                    if exit_input == 'y':
                        print("Exiting the program. Goodbye!")
                        running = False  #not able to use sys.exit(0) as it is giving error in jupyter notebook!
                        break
                    elif exit_input == 'n':
                        print("Returning to the main menu...")
                        break
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 5.")

main()
