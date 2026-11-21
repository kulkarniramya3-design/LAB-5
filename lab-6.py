
def employee_details(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )


print(employee_details("Ramya", 162, "IT", 30000))
