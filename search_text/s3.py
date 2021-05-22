import boto3
from PyPDF2 import PdfFileReader
from io import BytesIO
from search_text.settings import AWS_ACCESS_KEY_ID, AWS_S3_PUBLIC_URL, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_PUBLIC_URL

def fetchFromS3():
    pdf_files = []
    s3 = boto3.resource('s3', region_name=AWS_S3_REGION_NAME, 
            aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
    bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)
    for item in bucket.objects.all():
        obj = s3.Object(AWS_STORAGE_BUCKET_NAME, item.key)
        fs = obj.get()['Body'].read()
        pdfFile = PdfFileReader(BytesIO(fs))
        file_json = {"pdfFile" : pdfFile, "url" : AWS_S3_PUBLIC_URL + item.key, "file_name" : item.key}
        pdf_files.append(file_json)
    
    return pdf_files


def readTextFromFile(pdfFile):
    text = ""
    for page in range(pdfFile.getNumPages()):
        text = text + pdfFile.getPage(page).extractText()
    return text


