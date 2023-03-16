# {'id': 1, 'title': 'Post 1'}

POST_SCHEMA = {
    #'type': 'object',
    'properties': {
        'id':{'type': 'number'},
        'title':{'type': 'string'}
    },
    'required':['id']
}

#'title':{'type': 'string', 'enum': ['POST']}