import pytest
from unittest.mock import Mock, patch

class TestRegistration:
    def test_register_page_loads(self, client):
        """Test that registration page loads successfully"""
        response = client.get('/register')
        assert response.status_code == 200

    def test_login_page_loads(self, client):
        """Test that login page loads successfully"""
        response = client.get('/')
        assert response.status_code == 200

    def test_register_new_user(self, client, mock_db):
        """Test registering a new user"""
        mock_connect, mock_connection, mock_cursor = mock_db
        
        #Mock database responses
        mock_cursor.fetchone.side_effect = [
            None,  # No existing user
            (5,)   # Max user ID is 5
        ]
        
        response = client.post('/register', data={
            'username': 'newuser',
            'email': 'test@example.com', 
            'password': 'password123'
        })
        
        #redirect after successful registration
        assert response.status_code == 302
        assert response.location.endswith('/')  #CHATGPT FIXED: Check if location ends with /

    def test_login_process(self, client, mock_db):
        """Test login process"""
        mock_connect, mock_connection, mock_cursor = mock_db
        
        #mock successful login
        mock_cursor.fetchall.return_value = [(1,)]  # User ID
        
        response = client.post('/process', data={
            'usernameInput': 'testuser',
            'passwordInput': 'password123'
        })
        
        assert response.status_code == 200

    def test_register_new_user_success(self, client, mock_db):
        """Test successful user registration"""
        mock_connect, mock_connection, mock_cursor = mock_db
        
        #mock no existing user, max ID is 5
        mock_cursor.fetchone.side_effect = [None, (5,)]
        
        response = client.post('/register', data={
            'username': 'newuser',
            'email': 'test@example.com',
            'password': 'password123'
        })
        
        #Redirect to index after successful registration
        assert response.status_code == 302
        assert response.location.endswith('/')  #CHATGPT FIXED: Check if location ends with /
    #CHATGPT FIXED ISSUES
    def test_register_existing_user(self, client, mock_db):
        """Test registration with existing username"""
        mock_connect, mock_connection, mock_cursor = mock_db
        
        #mock user already exists - provide both fetchone calls
        mock_cursor.fetchone.side_effect = [
            (1,),  # First call: user exists (user ID 1)
            None   # Second call: max_id_query won't be reached due to early return, but need to provide a value
        ]
        
        response = client.post('/register', data={
            'username': 'existinguser',
            'email': 'test@example.com',
            'password': 'password123'
        })
        
        assert response.status_code == 200
        assert b'Username already exists' in response.data