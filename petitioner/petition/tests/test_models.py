from petition.models import Petition, Signature

from django.test import TestCase


class PetitionTestCase(TestCase):

    def test_name_of_petition(self):
        petition = Petition.objects.create(name="bread lover", description="Eating bread 1 slice a day")
        self.assertEqual(2, 1 + 1)
        self.assertEqual(petition.name, "bread lover")


