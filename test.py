from unittest import mock
from unittest.mock import patch
import pytest
import requests

# Test for a successful response status

def test_status():
     response = requests.get("https://newsapi.org/v2/everything?q=ukraine&war&language=en&sortBy=publishedAt&apiKey=YOUR_API_KEY")
     assert response.status_code == 200

#Check if the response content is in json

def test_content_type_equals_json():
     response = requests.get("https://newsapi.org/v2/everything?q=ukraine&war&language=en&sortBy=publishedAt&apiKey=YOUR_API_KEY")
     assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_get_author_name():
     response = requests.get("https://newsapi.org/v2/everything?q=ukraine&war&language=en&sortBy=publishedAt&apiKey=YOUR_API_KEY")
     response_body = response.json()
     assert response_body["articles"][0]["author"] == 'Yves Smith' # after running, this test will throw
     # an error with an assertion suggestion, that needs to be replaced with the correct value to make the test pass

# Raise an HTTPError using mock.patch

@mock.patch('requests.get')
def test_verify(mock_request):
    mock_resp = requests.models.Response()
    mock_resp.status_code = 404
    mock_request.return_value = mock_resp
    res = requests.get()
    with pytest.raises(requests.exceptions.HTTPError) as errc:
        res.raise_for_status()
    print(errc)
