from django.contrib.auth.models import User
user = User.objects.create_user('testuser', 'test@thebeatles.com', 'testuser')
