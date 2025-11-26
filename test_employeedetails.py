import pytest
from employeedetails import get_employee_info

def test_get_employee_info():
    # Sample data
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 60000

    # Expected result (dictionary)
    expected_output = "Employee Name: Alice Smith,Employee ID: E202,Department: HR,Salary: 60,000.00"


    # Assertion
    #print(get_employeedetails_info(name, emp_id, department, salary))
    assert get_employee_info(name, emp_id, department, salary) == expected_output