from django.db import models

COLOR_CHOISES = (
        ('black', 'Черный'),
        ('white', 'Белый'),
        ('blue', 'Синий'),
        ('red', 'Красный'),
        ('yellow', 'Желтый'),
        ('green', 'Зеленый'),
        ('purple', 'Фиолетовый'),
        ('orange', 'Оранжевый'),
        ('brown', 'Коричневый'),
        ('gray', 'Серый'),
        ('pink', 'Розовый'),
        ('gold', 'Золотой'),
        ('silver', 'Серебряный'),
        ('platinum', 'Платиновый')
    )

MOVEMENT_CHOISES = (
        ('quartz', 'Кварц'),
        ('automatic', 'Автоматический'),
        ('solar', 'Солнечный'),
        ('mechanic', 'Механический'), 
        ('elect', 'Электронные'),

        )

GENDER_CHOISE = (
    ('male', 'Мужские'),
    ('female', 'Женские'),
    ('unisex', 'Универсальные')
)

class Watch(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    case_material = models.CharField(max_length=50)
    color = models.CharField(max_length=20, choices=COLOR_CHOISES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    base_image = models.ImageField(upload_to='images/', blank=True, null=True)
    movement = models.CharField(max_length=50, choices=MOVEMENT_CHOISES)
    gender = models.CharField(max_length=50, choices=GENDER_CHOISE, default='male')

    def __str__(self):
        return self.brand + ' ' + self.model
    

class WatchImage(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image/')

    def __str__(self) -> str:
        return self.watch.brand + ' ' + self.watch.model + ' ' + str(self.id)
    

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name 