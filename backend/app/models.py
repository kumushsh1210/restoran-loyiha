from django.db import models

# 1. Menyu (Taomlar) uchun model
class Taom(models.Model):
    nomi = models.CharField(max_length=100)
    tavsifi = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    turi = models.CharField(max_length=50) # Masalan: Milliy taomlar, Ichimliklar
    chegirma_foizi = models.IntegerField(default=0)
    chegirma_kuni = models.CharField(max_length=20, blank=True, null=True)
    rasm = models.ImageField(upload_to='taomlar/', blank=True, null=True)
    def __str__(self):
        return f"{self.nomi} - {self.narxi} so'm"

# 2. Buyurtmalar uchun model
class Buyurtma(models.Model):
    HOLAT_CHOICES = [
        ('Kutilmoqda', 'Kutilmoqda'),
        ('Tayyorlanmoqda', 'Tayyorlanmoqda'),
        ('Yakunlandi', 'Yakunlandi'),
    ]
    taom = models.ForeignKey(Taom, on_delete=models.CASCADE)
    miqdori = models.PositiveIntegerField(default=1)
    vaqti = models.DateTimeField(auto_now_add=True)
    holati = models.CharField(max_length=20, choices=HOLAT_CHOICES, default='Kutilmoqda')

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.taom.nomi}"

# 3. To'lovlar tarixi uchun model
class Tolov(models.Model):
    buyurtma = models.OneToOneField(Buyurtma, on_delete=models.CASCADE)
    umumiy_summa = models.DecimalField(max_digits=12, decimal_places=2)
    tolov_vaqti = models.DateTimeField(auto_now_add=True)
    tolov_turi = models.CharField(max_length=50) # Masalan: Naqd yoki Karta

    def __str__(self):
        return f"To'lov #{self.id} - {self.umumiy_summa} so'm"

