import pytest
import sys
import os
from unittest.mock import Mock, patch

# Add the parent directory to Python path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as flask_app

@pytest.fixture
def app():
    """Fixture to create Flask app for testing"""
    flask_app.config.update({
        'TESTING': True,
        'SECRET_KEY': 'test-secret-key',
        'WTF_CSRF_ENABLED': False
    })
    yield flask_app

@pytest.fixture
def client(app):
    """Fixture to create test client"""
    return app.test_client()

@pytest.fixture
def mock_db():
    """Fixture to mock database connections"""
    with patch('mysql.connector.connect') as mock_connect:
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.side_effect = [None]
        mock_cursor.fetchall.side_effect = [[]]
        yield mock_connect, mock_connection, mock_cursor
