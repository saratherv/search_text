from django.http import response
from elasticsearch import Elasticsearch
import logging


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


def insertDocuments(documents):
    es = connect_elasticsearch()
    es.indices.delete(index='s3_data', ignore=[400, 404])
    if es == None:
        return {"success" : False, "error" : "unable to connect to elastic search"}
    try:
        for data in documents:
            es.index(index="s3_data", doc_type="text_files", body=data)
        return {"success" : True, "message" : "documents indexed with Elastic Search"}
    except Exception as e:
        return {"success" : False, "error" : repr(e)}


def searchText(text):
    es = connect_elasticsearch()
    if es == None:
        return {"success" : False, "error" : "unable to connect to elastic search"}
    res= es.search(index='s3_data',doc_type='text_files',body={
        'query':{
            'match':{
                "text":text
            }
        }
    })

    if "timed_out" in res and res["timed_out"] == False:
        return {"success" : True, "data" : res["hits"]["hits"]}
    else:
        return {"success" : False, "error" : "unable to fetch results"}
    







if __name__ == '__main__':
  logging.basicConfig(level=logging.ERROR)