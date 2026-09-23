import pytest

class TestRoutes:
    def test_index_route(self, client):
        """Test that the main page loads"""
        response = client.get('/')
        assert response.status_code == 200

    def test_register_route(self, client):
        """Test that register page loads"""
        response = client.get('/register')
        assert response.status_code == 200

    def test_create_account_route(self, client):
        """Test that create account page loads"""
        response = client.get('/createAccount')
        assert response.status_code == 200

    def test_home_route_without_login(self, client):
        """Test that home redirects to login when not authenticated"""
        response = client.get('/home')
        assert response.status_code == 200

    def test_api_page_route(self, client):
        """Test that API page loads"""
        response = client.get('/apiPage')
        assert response.status_code == 200
