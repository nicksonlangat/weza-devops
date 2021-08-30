from django.test import TestCase
from .models import Employee
# Create your tests here.

class EmployeeTest(TestCase):
    def create_employee(self, first_name='Steve', last_name='Hoober', email='stevehoober@gmail.com', salary=40000):
        return Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            salary=salary
        )
    def test_employee_creation(self):
        x=self.create_employee()
        self.assertTrue(isinstance(x,Employee))
        self.assertEqual(x.__str__(), x.first_name)

