#Utility tests 
def test_get_username_function():
    """Test the getUsername function from app.py"""
    #test by importing and checking it returns the string
    from app import getUsername
    result = getUsername(123)
    assert "SELECT username FROM login WHERE userId = '123'" in result
#CHATGPT MADE
def test_basic_assertion():
    """Simple test to verify the file is working"""
    assert True

def test_homepage(client):
    """test that homepage returns 200 status"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_accessible(client):
    """Test that home page returns 200 status"""
    response = client.get('/')
    assert response.status_code == 200
#CHATGPT MADE REST
def test_register_page_accessible(client):
    """Test that register page returns 200 status"""  
    response = client.get('/register')
    assert response.status_code == 200

def test_create_account_page_accessible(client):
    """Test that create account page returns 200 status"""
    response = client.get('/createAccount')
    assert response.status_code == 200