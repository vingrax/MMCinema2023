from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.dashboard_url = reverse('dashboard')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123'
        )

    def test_dashboard_view_with_authenticated_user(self):
        """Test that authenticated users can access the dashboard."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index2.html')
    
    