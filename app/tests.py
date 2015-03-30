from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from app.models import Article, Label


class NoArticleViewTests(TestCase):
    def test_list_view_with_no_articles(self):
        """
        If no articles exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('app:article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No articles found.')
        self.assertQuerysetEqual(response.context['articles'], [])


class ArticleViewTests(TestCase):
    def setUp(self):
        """ Need at least one article """
        user = User.objects.create_user(username='admin',
                                        email='admin@gmail.com',
                                        password='top_secret')

        label = Label.objects.create(name='label1')

        article = Article.objects.create(headline='First Topic',
                                         content='Content for 1st topic',
                                         pub_date=timezone.now(),
                                         reporter=user)
        article.labels.add(label.id)

    def test_article_list_view(self):
        date = timezone.now()
        response = self.client.get(reverse('app:article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Topic')
        response = self.client.get(reverse('app:article_detail',
                                           kwargs=dict(
                                               year=date.year,
                                               month=date.month,
                                               day=date.day,
                                               slug='first-topic'
                                           )))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Topic')

    def test_article_list_fail_view(self):
        """ If no articles exist """
        date = timezone.now()
        response = self.client.get(reverse('app:article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Topic')
        response = self.client.get(reverse('app:article_detail',
                                           kwargs=dict(
                                               year=date.year,
                                               month=date.month,
                                               day=date.day,
                                               slug='fake-topic'
                                           )))
        self.assertEqual(response.status_code, 404)

    def test_article_search_view(self):
        """ Search existing headline """
        response = self.client.get('%s?search=%s'
                                   % (reverse('app:article_list')
                                      , 'First Topic'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First Topic')

        response = self.client.get('%s?search=%s'
                                   % (reverse('app:article_list')
                                      , '1st'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1st')

        """ Search existing content """
        response = self.client.get('%s?search=%s'
                                   % (reverse('app:article_list')
                                      , 'Content for 1st'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Content for 1st')

        response = self.client.get('%s?search=%s'
                                   % (reverse('app:article_list')
                                      , '1st'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1st')

    def test_article_search_fail_view(self):
        """ Search fake headline or content """
        response = self.client.get('%s?search=%s'
                                   % (reverse('app:article_list')
                                      , 'Fake data'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No articles found.')

    def test_article_label_view(self):
        """ List of existing ar """
        response = self.client.get(reverse('app:article_label',
                                           kwargs=dict(name='label1')))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'label1')

    def test_article_label_fail_view(self):
        """ Test for fake label """
        response = self.client.get(reverse('app:article_label',
                                           kwargs=dict(name='Fake')))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No articles found.')
