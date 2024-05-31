INPUT_SCHEMA = {
    "text": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["There is a fine house in the forest"]
    },
    'candidate_labels': {
        'datatype': 'STRING',
        'required': True,
        'example': [ "Happy", "Sad"],
        'shape': [-1]
    },
}
