from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from authapp.models import ShopUser
from django.core.management import call_command


class TestUserManagement (TestCase):
    def setUp(self):
        # call_command('flush' , '--noinput')
        # call_command('loaddata', 'test_db.json')
        self.client = Client()
        self.superuser = ShopUser.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')
        self.user = ShopUser.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')
        self.user_with__first_name = ShopUser.objects.create_user('umaturman', 'umaturman@geekshop.local', 'geekbrains', first_name='Uma')


    def test_user_login(self):
        # главная без логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title'], 'home')
        self.assertNotContains(response, 'User', status_code= 200)
        # self.assertNotIn('User', response.content.decode())
        # данные пользователя
        self.client.login(username='tarantino', password= 'geekbrains')
        # логинимся
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)
        # главная после логина
        response = self.client.get('/')
        self.assertContains(response, 'User', status_code=200 )
        self.assertEqual(response.context['user'], self.user)
        # self.assertIn('Пользователь', response.content.decode())

    class TestUserManagement(TestCase):
        ...

    def test_basket_login_redirect(self):

        # без логина должен переадресовать
        response = self.client.get('/basket/')
        self.assertEqual(response.url, '/auth/login/?next=/basket/')
        self.assertEqual(response.status_code, 302)
        # с логином все должно быть хорошо
        self.client.login(username='tarantino', password='geekbrains')
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['basket']), [])
        self.assertEqual(response.request['PATH_INFO'], '/basket/')
        self.assertIn('Your cart', response.content.decode())

    def test_user_logout(self):
        # данные пользователя
        self.client.login(username='tarantino', password='geekbrains')
        # логинимся
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)
        # выходим из системы
        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 302)
        # главная после выхода
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

    def test_user_register(self):
        # логин без данных пользователя
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'register')
        self.assertTrue(response.context['user'].is_anonymous)
        new_user_data = {
            'username': 'samuel',
            'first_name': 'Samuel',
            'last_name': 'Jackson',
            'password1': 'geekbrains',
            'password2': 'geekbrains',
            'email': 'sumuel@geekshop.local',
            'age': '21'}
        response = self.client.post('/auth/register/', data=new_user_data)
        self.assertEqual(response.status_code, 302)
        new_user = ShopUser.objects.get(username=new_user_data['username'])
        activation_url = f"{settings.DOMAIN_NAME}/auth/verify/{new_user_data['email']}/{new_user.activation_key}"
        # print(activation_url)
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 302)
        # данные нового пользователя
        self.client.login(username=new_user_data['username'], password=new_user_data['password1'])
        # логинимся
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)
        # проверяем главную страницу
        response = self.client.get('/')
        self.assertContains(response, text=new_user_data['first_name'], status_code=200)

    def test_user_wrong_register(self):
        new_user_data = {
            'username': 'teen',
            'first_name': 'Mary',
            'last_name': 'Poppins',
            'password1': 'geekbrains',
            'password2': 'geekbrains',
            'email': 'merypoppins@geekshop.local',
            'age': '17'}

        response = self.client.post('/auth/register/', data=new_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'register_form', 'age', 'Your are too young')

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')