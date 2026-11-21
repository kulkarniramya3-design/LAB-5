
from employee import employee_details

def test_employee_details():
    expected = (
        "Employee Name: Ramya\n"
        "Employee ID: 162\n"
        "Department: IT\n"
        "Salary: 30000"
    )

    result = employee_details("Ramya", 162, "IT", 30000)

    assert result == expected
