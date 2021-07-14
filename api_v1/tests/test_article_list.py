from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api_v1.factories import UserFactory, CategoryFactory, ArticleFactory


class ArticleListTest(APITestCase):
    def test_article_list(self):
        user = UserFactory()
        category = CategoryFactory()
        article = ArticleFactory(user=user, category=category)
        response = self.client.get(
            reverse('api_v1:categories'),
        )
        data = [
                    {
                        "id": 1,
                        "title": category.title,
                        "articles": [
                            {
                                "id": 1,
                                "title": article.title,
                                "description": article.description,
                                "user": user.id,
                                "category": category.id,
                                "image": None,
                            }
                        ]
                    }
        ]
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertListEqual(response.json(), data)