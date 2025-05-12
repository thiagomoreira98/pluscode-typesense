
import typesense

from typing import Dict, Any, List
from app.config import settings

class Typesense:
    def __init__(self, collection_name: str):
        self.client = typesense.Client({
            'nodes': [{
                'host': settings.TYPESENSE_HOST,
                'port': settings.TYPESENSE_PORT,
                'protocol': 'http'
            }],
            'api_key': settings.TYPESENSE_API_KEY,
            'connection_timeout_seconds': 2
        })
        self.collection_name = collection_name
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        try:
            self.client.collections[self.collection_name].retrieve()
        except typesense.exceptions.ObjectNotFound:
            schema = {
                'name': self.collection_name,
                'fields': [
                    {'name': 'id', 'type': 'string'},
                    {'name': 'name', 'type': 'string'},
                    {'name': 'price', 'type': 'float'},
                    {'name': 'zipcode', 'type': 'int32'},
                    {'name': 'lat', 'type': 'float'},
                    {'name': 'lon', 'type': 'float'},
                    {'name': 'pluscode', 'type': 'string'},
                ],
                'default_sorting_field': 'zipcode'
            }
            self.client.collections.create(schema)

    def save(self, document: Any) -> Dict[str, Any]:
        return self.client.collections[self.collection_name].documents.upsert(document)

    def search(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        return self.client.collections[self.collection_name].documents.search(params)