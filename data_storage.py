storage = {}

def store_data(data):
    storage['processed_data'] = data

def get_data():
    return storage.get('processed_data', [])
