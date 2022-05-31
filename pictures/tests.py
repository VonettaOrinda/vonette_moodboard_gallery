from django.test import TestCase
from .models import *
# Create your tests here.

class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.Europe = Location.objects.create(name='Europe')
        self.fashion = categories.objects.create(name='fashion')
        self.travel = categories.objects.create(name='travel')

        # self.pizza = Image.objects.create(name='drinks', location=self.Europe  description='picture of pizza')

        # self.pizza.categories.add(self.foodie)
        # self.pizza.categories.add(self.music)

    # def a testcase for instance of the drinks class
    def test_instance(self):
        self.pizza.save()
        self.assertTrue(isinstance(self.pizza, Image))

    def test_delete_image(self):
        self.pizza.save()
        self.pizza.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.pizza.save()
        self.pizza.name = 'MorePizza'
        self.assertTrue(self.pizza.name == 'MorePizza')

    def test_all_images(self):
        self.pizza.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)

    def test_search_by_category(self):
        self.pizza.save()
        images = Image.search_by_category('fun')
        self.assertTrue(len(images) > 0)

    def test_view_location(self):
        self.pizza.save()
        location = Image.view_location(self.nairobi)
        self.assertTrue(len(location) > 0)

    def test_view_category(self):
        self.pizza.save()
        categories = Image.view_category(self.food)
        self.assertTrue(len(categories) > 0)

class categoriesTest(TestCase):
    def setUp(self):
        self.nature = categories(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, categories))

class LocationTest(TestCase):
    def setUp(self):
        self.Europe = Location(name='Europe')

    def test_instance(self):
        self.Europe.save()
        self.assertTrue(isinstance(self.Europe, Location))

# Create your tests here.

