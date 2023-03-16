#https://my-json-server.typicode.com/typicode/demo/posts
import requests
import json
from jsonschema import validate
# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]

from configuration import SERVICE_URL
# from src.scheme.post import POST_SCHEMA
from src.base_class.response import Response
from  src.pydantic_schemas.post import Post

def test_get_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    # validadion via pydantic
    response.assert_status_code(200).validate(Post)


# #validadion via scheme
#     response\
#         .assert_status_code(200)\
#         .validate(POST_SCHEMA)

