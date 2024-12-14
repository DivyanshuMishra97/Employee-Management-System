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
