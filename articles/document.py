from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import YourModel



class YourModelDocument(Document):
    class Index:
        name = 'yourmodel_index'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = YourModel

    # Add fields you want to index
    field_name = fields.TextField(attr='name')
    field_description = fields.TextField(attr='description')