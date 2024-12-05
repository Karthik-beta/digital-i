from django.test import TestCase
from .models import Company, Location, Department, Designation, Division, SubDivision, Shopfloor, Shift, AutoShift
from datetime import time, timedelta

class ModelTestCase(TestCase):
    def setUp(self):
        """
        Set up data for each test case.
        """
        self.company = Company.objects.create(name="Test Company", code="TC01")
        self.location = Location.objects.create(name="Test Location", code="LOC01")
        self.department = Department.objects.create(name="Test Department", code="DEPT01")
        self.designation = Designation.objects.create(name="Test Designation", code="DES01")
        self.division = Division.objects.create(name="Test Division", code="DIV01")
        self.subdivision = SubDivision.objects.create(name="Test Subdivision", code="SUBDIV01")
        self.shopfloor = Shopfloor.objects.create(name="Test Shopfloor", code="SF01")
        self.shift = Shift.objects.create(
            name="Morning Shift", 
            start_time=time(8, 0), 
            end_time=time(17, 0),
            grace_period_at_start_time=timedelta(minutes=10),
            grace_period_at_end_time=timedelta(minutes=10),
            half_day_threshold=timedelta(hours=4),
            full_day_threshold=timedelta(hours=8),
            overtime_threshold_before_start=timedelta(minutes=30),
            overtime_threshold_after_end=timedelta(minutes=30),
            lunch_in=time(12, 0),
            lunch_out=time(13, 0),
            lunch_duration=timedelta(hours=1),
            night_shift=False
        )
        self.auto_shift = AutoShift.objects.create(
            name="Auto Morning Shift", 
            start_time=time(8, 0), 
            end_time=time(17, 0),
            tolerance_start_time=timedelta(minutes=5),
            tolerance_end_time=timedelta(minutes=5),
            half_day_threshold=timedelta(hours=4),
            full_day_threshold=timedelta(hours=8),
            overtime_threshold_before_start=timedelta(minutes=30),
            overtime_threshold_after_end=timedelta(minutes=30),
            lunch_in=time(12, 0),
            lunch_out=time(13, 0),
            lunch_duration=timedelta(hours=1),
            night_shift=False
        )

    def test_company_creation(self):
        """
        Test if a Company instance is created successfully and its name is capitalized.
        """
        self.assertEqual(self.company.name, "Test Company")
        self.assertEqual(self.company.code, "TC01")
    
    def test_location_creation(self):
        """
        Test if a Location instance is created successfully.
        """
        self.assertEqual(self.location.name, "Test Location")
        self.assertEqual(self.location.code, "LOC01")

    def test_department_creation(self):
        """
        Test if a Department instance is created successfully.
        """
        self.assertEqual(self.department.name, "Test Department")
        self.assertEqual(self.department.code, "DEPT01")

    def test_designation_creation(self):
        """
        Test if a Designation instance is created successfully.
        """
        self.assertEqual(self.designation.name, "Test Designation")
        self.assertEqual(self.designation.code, "DES01")

    def test_division_creation(self):
        """
        Test if a Division instance is created successfully.
        """
        self.assertEqual(self.division.name, "Test Division")
        self.assertEqual(self.division.code, "DIV01")

    def test_subdivision_creation(self):
        """
        Test if a SubDivision instance is created successfully.
        """
        self.assertEqual(self.subdivision.name, "Test Subdivision")
        self.assertEqual(self.subdivision.code, "SUBDIV01")

    def test_shopfloor_creation(self):
        """
        Test if a Shopfloor instance is created successfully.
        """
        self.assertEqual(self.shopfloor.name, "Test Shopfloor")
        self.assertEqual(self.shopfloor.code, "SF01")

    def test_shift_creation(self):
        """
        Test if a Shift instance is created successfully and if is_night_shift works.
        """
        self.assertEqual(self.shift.name, "MORNING SHIFT")
        self.assertFalse(self.shift.is_night_shift())
        self.assertEqual(self.shift.lunch_duration, timedelta(hours=1))

    def test_auto_shift_creation(self):
        """
        Test if an AutoShift instance is created successfully and if is_night_shift works.
        """
        self.assertEqual(self.auto_shift.name, "AUTO MORNING SHIFT")
        self.assertFalse(self.auto_shift.is_night_shift())
        self.assertEqual(self.auto_shift.lunch_duration, timedelta(hours=1))

    def test_shift_lunch_duration(self):
        """
        Test if the calculate_lunch_duration method returns correct lunch duration.
        """
        lunch_duration = self.shift.calculate_lunch_duration()
        self.assertEqual(lunch_duration, timedelta(hours=1))

    def test_auto_shift_lunch_duration(self):
        """
        Test if the calculate_lunch_duration method returns correct lunch duration.
        """
        lunch_duration = self.auto_shift.calculate_lunch_duration()
        self.assertEqual(lunch_duration, timedelta(hours=1))
