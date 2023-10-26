from medicSearch.models import *   # Importa todas as models de dentro do diretório medicSearch/models
from django.db.models import Sum, Count

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True) 
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')  # ALTERAÇÕES REALIZADAS
    specialties = models.ManyToManyField(Speciality, blank=True, related_name='specialties')  # ALTERAÇÕES REALIZADAS
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')  # ALTERAÇÕES REALIZADAS


    # Metodo para exibir o objeto quando quisermos acessar através de sua instância
    def __str__(self):
        return f'{self.user.username}'
    


    # Metodo para criar o perfil do usuário (vide pg.34, 35, ...)
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass



    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
    
    
    def show_scoring_average(self):
        from .Rating import Rating
        try:
            ratings = Rating.objects.filter(user_rated=self.user).aaggregate(Sum('value'), Count('user'))
            if ratings['user__count'] > 0:
                scoring_average = ratings['value__sum'] / ratings['user__count']
                scoring_average = round(scoring_average, 2) # Arredonda o valor para 2 casas decimais
                return scoring_average
            return 'Sem avaliações'
        except:
            return 'Sem avaliações'
     
        
    def show_favorites(self):
        ids = [result.id for result in self.favorites.all()]
        return Profile.objects.filter(user__id__in=ids)
    
    def show_ratings(self):
        from .Rating import Rating
        return Rating.objects.filter(user_rated=self.user)