from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AddCouponViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )

    def test_add_coupon_without_active_order(self):
        self.client.login(username="tester", password="pass")
        response = self.client.post(reverse("core:add-coupon"), {"code": "TEST"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("core:checkout"))
