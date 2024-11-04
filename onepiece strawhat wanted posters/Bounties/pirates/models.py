from django.db import models

class Bounty(models.Model):
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    amount_type = models.CharField(max_length=20, default='berries')

    def __str__(self):
        return f"Bounty: {self.amount} {self.amount_type}"

class Pirate(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    HAKI_CHOICES = [
        ("Y", "Yes"),
        ("N", "No"),
    ]

    DEVIL_FRUIT_CHOICES = [
        ("Y", "Yes"),
        ("N", "No"),
    ]

    SPECIES_CHOICES = [
        ("H", "Human"),
        ("F", "Fishman"),
        ("A", "Animal"),
        ("C", "Cyborg"),
        ("O", "Other"),
    ]

    pirate_name = models.CharField(max_length=100)
    special_name = models.CharField(max_length=100, blank=True)
    species = models.CharField(choices=SPECIES_CHOICES, max_length=1)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    position_in_crew = models.CharField(max_length=10)
    work_done_by_them = models.TextField(max_length=100)
    powers = models.TextField(max_length=100, blank=True)
    spec_power = models.TextField(max_length=1000, blank=True)
    devil_fruit = models.CharField(choices=DEVIL_FRUIT_CHOICES, max_length=1)
    devil_fruit_name = models.CharField(max_length=100, blank=True)
    haki = models.CharField(choices=HAKI_CHOICES, max_length=1)
    haki_type = models.CharField(max_length=1000, blank=True)
    first_bounty = models.DecimalField(max_digits=100, decimal_places=2)  
    current_bounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)   
    date_of_birth = models.DateField()
    age = models.IntegerField()
    dream = models.TextField(max_length=1000)
    wanted_poster = models.ImageField(upload_to='wanted_posters/', default='wanted_posters/default_image.png')

    def __str__(self):
        return self.pirate_name





