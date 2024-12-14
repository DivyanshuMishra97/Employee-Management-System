# Employee Management System

## Overview

The Employee Management System is a Python-based application designed to manage employee data efficiently. It supports adding, retrieving, and analyzing employee information, including compensation and vehicle data. The system handles multiple employee types (Full-Time, Hourly, Consultant) and stores data persistently using Python's `pickle` module.

---

## Features

1. **Add Employee**:
   - Supports adding Full-Time, Hourly, and Consultant employees.
   - Captures details like name, address, salary/hourly rate/project type, and vehicle data.

2. **View All Employees**:
   - Displays employee details categorized by type (Full-Time, Hourly, Consultant).

3. **Calculate Compensation**:
   - Calculates employee compensation based on:
     - Tax brackets (Full-Time Employees).
     - Overtime (Hourly Employees).
     - Project type rates (Consultants).

4. **High Mileage Vehicles**:
   - Lists employees with vehicles that have mileage greater than 78,000.

5. **Persistent Data Storage**:
   - Stores employee data in a binary file (`empdata.dat`) for future retrieval.

## How to Use

1. Run the script using Python.
2. Choose an option from the menu:
   - **1**: Add a new employee.
   - **2**: Display all employee details.
   - **3**: Calculate and display employee compensation.
   - **4**: Display high-mileage vehicle information.
   - **5**: Exit the program.
3. Follow the prompts to input employee or vehicle details.

---

## Classes and Structure

### **Employee**:
- **Parent class** for shared attributes and methods:
  - `EmpName`, `EmpAdrs`, and `Vdata` (Vehicle object).
- **Methods**:
  - Getters and setters for employee name and address.
- **Inheritance**:
  - Base class for `FullTimeEmployee`, `HourlyEmployee`, and `Consultant`.

### **FullTimeEmployee**:
- **Inherits from**: `Employee`.
- **Additional Attributes**:
  - `salary` (float).
- **Methods**:
  - `CompensationFTE`: Calculates net salary based on tax brackets.

### **HourlyEmployee**:
- **Inherits from**: `Employee`.
- **Additional Attributes**:
  - `hoursWorked` (int), `hourlyRate` (float).
- **Methods**:
  - `CompensationHE`: Calculates pay, including overtime.

### **Consultant**:
- **Inherits from**: `Employee`.
- **Additional Attributes**:
  - `hoursWorked` (int), `ProjectType` (int).
- **Methods**:
  - `CompensationC`: Calculates pay based on project type rates.

### **Vehicle**:
- **Captures and manages vehicle information**.
- **Attributes**:
  - `make`, `model`, `year`, `mileage`.

---

## Example Outputs

### Adding an Employee
```
Type of Employee?(1-Full Time;2-Hourly;3-Consultant): 1
Adding an Employee
Enter the Employee's name: John Doe
Enter the employee's address: 123 Main St
Enter the vehicle's make: Toyota
Enter the vehicle's model: Corolla
Enter the year of manufacture: 2015
Enter the mileage: 65000
Enter the salary: 50000
Employee added to database
```


## Viewing All Employees

```
=====================================================================
Data of all Full-Time Employees
=====================================================================
Emp Name          Address                        Veh Make   Veh Model
John Doe          123 Main St                   Toyota      Corolla
```

## Viewing High Mileage Vehicles
```
=====================================================================
High Mileage Vehicles (Mileage > 78,000)
=====================================================================
Employee           Make        Model       Year        Mileage
Jane Smith         Honda       Civic       2012        82,000
...
```
## Viewing Compensation
```
=====================================================================
Employee Name      Compensation
=====================================================================
John Doe           $42,500.00
Jane Smith         $3,400.00
...
```
### Key Features and Highlights

- Object-Oriented Design
- Modular structure using inheritance for flexibility.
- Input Validation
- Robust checks for numeric inputs and project types.
- Compensation Calculations
- Handles tax brackets, overtime, and project type-based rates.
- Persistent Storage
- Uses pickle to save and retrieve data.
- Interactive Menu
- Simplifies navigation through features.


