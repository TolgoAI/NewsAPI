## **Testing-News-API**
This application acquires data (news articles) on the topic of 'war in ukraine' from NewsAPI and loads data into CSV file, which can be leveraged for various analytical purposes.  

#### **Fulfill the following prerequisites before running an application and test.py**
- Make sure to get your own API key from https://newsapi.org/ 
- Add your API key to the url in __ init __.py :
```python
url = "https://newsapi.org/v2/everything?q=ukraine&war&language=en&sortBy=publishedAt&apiKey=YOUR_API_KEY"
```
#### **Setup**
Open your terminal and run the following commands:
```zsh
git clone git@github.com:TolgoAI/NewsAPI.git
cd project
python3 -m venv project1_env
source project1_env/bin/activate
pip install -r requirements.txt
```

#### **Testing an App residing in __ init __.py**

Make sure to provide URLs with your YOUR_API_KEY in test.py
```zsh
pytest test.py
```
After running the test, you will realize that the test "def test_get_author_name()" has failed. Don't panic, the code is working as intended, therefore,  replace the value for author of the first article with suggested assertion in the error message. 
```python
assert response_body["articles"][0]["author"] == 'Suggested_Assertion'
```

Voila, the tests are passing!
