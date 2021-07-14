import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from factory import Sequence

from articles.models import Article
from categories.models import Category

faker = factory.faker.Faker._get_faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = Sequence(lambda n: f'djangopython{n}')
    password = factory.LazyFunction(lambda: make_password('H@rdpass123'))


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.LazyFunction(faker.company)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.LazyFunction(faker.company)
    description = factory.LazyFunction(faker.company)
    category = factory.SubFactory(CategoryFactory)
    user = factory.SubFactory(UserFactory)



