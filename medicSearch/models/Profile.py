from medicSearch.models import *   # Importa todas as models de dentro do diretório medicSearch/models


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
    
