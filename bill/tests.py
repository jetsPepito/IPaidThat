from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from bill.models import *
from datetime import datetime
from .utils import *

class RetObjTest(TestCase):
    def setUp(self):
        dat = datetime.strptime("10/08/12", "%d/%m/%y")
        RetObject.objects.create(email = "toto@gmail.com",
                                 invoice_number="Project 1",
                                 date= dat.date(),
                                 client_name= "Titi",
                                 total_ttc = "2000 €",
                                 total_vat = "2500 €")

    def test_emailandclient_name(self):
        em = RetObject.objects.get(email="toto@gmail.com")
        client_name = RetObject.objects.get(client_name="Titi")
        self.assertEqual(em.email, 'toto@gmail.com')
        self.assertEqual(client_name.client_name, 'Titi')

class TestBack(TestCase):
    def test_back(self):
        back("legatt.poubelle@gmail.com", "indo")
        list = RetObject.objects.filter(invoice_number="legatt.poubelle@gmail.com")
        for el in list:
            self.assertEqual(el.email, "legatt.poubelle@gmail.com")