def get_employee_info(name, emp_id, department, salary):

    """Returns a formatted string containing employee details."""

    return (f"Employee Name: {name},"
            f"Employee ID: {emp_id},"
            f"Department: {department},"
            f"Salary: {salary:,.2f}")



if __name__ == "__main__":

    print(get_employee_info("John Doe","E108","cs",59000))