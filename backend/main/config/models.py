from django.db import models


class Company(models.Model):
    """
    Represents a company entity with a name, code, and timestamps for when the
    company was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the company as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the company name is saved in title case.
        """
        self.name = self.name.title()
        super(Company, self).save(*args, **kwargs)

    class Meta:
        db_table = 'company'


class Location(models.Model):
    """
    Represents a location entity with a name, code, and timestamps for when the
    location was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the location as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the location name is saved in title case.
        """
        self.name = self.name.title()
        super(Location, self).save(*args, **kwargs)

    class Meta:
        db_table = 'location'


class Department(models.Model):
    """
    Represents a department entity with a name, code, and timestamps for when the
    department was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the department as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the department name is saved in title case.
        """
        self.name = self.name.title()
        super(Department, self).save(*args, **kwargs)

    class Meta:
        db_table = 'department'


class Designation(models.Model):
    """
    Represents a designation entity with a name, code, and timestamps for when the
    designation was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the designation as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the designation name is saved in title case.
        """
        self.name = self.name.title()
        super(Designation, self).save(*args, **kwargs)

    class Meta:
        db_table = 'designation'


class Division(models.Model):
    """
    Represents a division entity with a name, code, and timestamps for when the
    division was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the division as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the division name is saved in title case.
        """
        self.name = self.name.title()
        super(Division, self).save(*args, **kwargs)

    class Meta:
        db_table = 'division'


class SubDivision(models.Model):
    """
    Represents a subdivision entity with a name, code, and timestamps for when the
    subdivision was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the subdivision as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the subdivision name is saved in title case.
        """
        self.name = self.name.title()
        super(SubDivision, self).save(*args, **kwargs)

    class Meta:
        db_table = 'subdivision'


class Shopfloor(models.Model):
    """
    Represents a shopfloor entity with a name, code, and timestamps for when the
    shopfloor was created and last updated.
    """
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the name of the shopfloor as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the shopfloor name is saved in title case.
        """
        self.name = self.name.title()
        super(Shopfloor, self).save(*args, **kwargs)

    class Meta:
        db_table = 'shopfloor'


class Shift(models.Model):
    """
    Represents a work shift with attributes for shift timings, grace periods,
    lunch breaks, overtime thresholds, and whether the shift is a night shift.
    """
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    grace_period_at_start_time = models.DurationField()
    grace_period_at_end_time = models.DurationField()
    half_day_threshold = models.DurationField()
    full_day_threshold = models.DurationField()
    overtime_threshold_before_start = models.DurationField()
    overtime_threshold_after_end = models.DurationField()
    lunch_in = models.TimeField(blank=True, null=True)
    lunch_out = models.TimeField(blank=True, null=True)
    lunch_duration = models.DurationField(blank=True, null=True)
    night_shift = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_night_shift(self):
        """
        Determines if the shift qualifies as a night shift based on its start and end time.
        """
        return self.start_time > self.end_time

    def calculate_lunch_duration(self):
        """
        Calculates the duration between lunch start and lunch end times.
        """
        if self.lunch_in and self.lunch_out:
            return self.lunch_out - self.lunch_in
        return None

    def __str__(self):
        """
        Returns the name of the shift as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the shift name is saved in uppercase.
        """
        self.name = self.name.upper()
        super(Shift, self).save(*args, **kwargs)

    class Meta:
        db_table = 'shift'


class AutoShift(models.Model):
    """
    Represents an auto shift with attributes for shift timings, tolerance periods,
    lunch breaks, overtime thresholds, and whether the shift is a night shift.
    """
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    tolerance_start_time = models.DurationField()
    tolerance_end_time = models.DurationField()
    # grace_period_at_start_time = models.DurationField()
    # grace_period_at_end_time = models.DurationField()
    half_day_threshold = models.DurationField()
    full_day_threshold = models.DurationField()
    overtime_threshold_before_start = models.DurationField()
    overtime_threshold_after_end = models.DurationField()
    lunch_in = models.TimeField()
    lunch_out = models.TimeField()
    lunch_duration = models.DurationField()
    night_shift = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_night_shift(self):
        """
        Determines if the shift qualifies as a night shift based on its start and end time.
        """
        return self.start_time > self.end_time

    def calculate_lunch_duration(self):
        """
        Calculates the duration between lunch start and lunch end times.
        """
        return self.lunch_out - self.lunch_in

    def __str__(self):
        """
        Returns the name of the auto shift as its string representation.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Custom save method that ensures the auto shift name is saved in uppercase.
        """
        self.name = self.name.upper()
        super(AutoShift, self).save(*args, **kwargs)

    class Meta:
        db_table = 'auto_shift'
