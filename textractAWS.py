#########
# This files is currently nor being used but I am keeping it for refrence i we plan to use AWS textract.textract
# It works well with png and jpg formats
#########



import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from search_text.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def indexDocument(bucketName, objectName, text):

    # Update host with endpoint of your Elasticsearch cluster
    #host = "search--xxxxxxxxxxxxxx.us-east-1.es.amazonaws.com
    host = "search-index-pdf-data-f6t5yv4cf7pdd2fhxi26j7lcza.ap-southeast-1.es.amazonaws.com"
    region = 'ap-southeast-1'

    if(text):
        service = 'es'
        # ss = boto3.Session()
        # credentials = ss.get_credentials()
        # region = ss.region_name

        awsauth = AWS4Auth(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, region, service)

        es = Elasticsearch(
            hosts = [{'host': host, 'port': 443}],
            http_auth = awsauth,
            use_ssl = True,
            verify_certs = True,
            connection_class = RequestsHttpConnection
        )

        document = {
            "name": "{}".format(objectName),
            "bucket" : "{}".format(bucketName),
            "content" : text
        }

        es.index(index="textract", doc_type="document", id=objectName, body=document)

        print("Indexed document: {}".format(objectName))

# Document
s3BucketName = "borneodatabucket"
documentName = "index.png"

# Amazon Textract client


textract = boto3.client("textract", region_name="ap-southeast-1", aws_access_key_id = aws_key, aws_secret_access_key = aws_secret)

# Call Amazon Textract
response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })


text = ""
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print ('\033[94m' +  item["Text"] + '\033[0m')
        text += item["Text"]

indexDocument(s3BucketName, documentName, text)