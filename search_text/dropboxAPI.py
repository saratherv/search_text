##################################################################################################
# These are set of failed approaches which didn't work
# Major reason is apache tika not working properly for python

##################################################################################################






# import dropbox
# from search_text.settings import access_token
# from search_text.settings import folder_path
# # from tika import parser
# import requests, PyPDF2
# from io import BytesIO


# def getFilesFromDropBoxFolder():
#     dbx = dropbox.Dropbox(access_token)
#     links = []
#     for entry in dbx.files_list_folder(folder_path).entries:
#         print(entry.name)
#         file_path = folder_path + "/" + entry.name
#         shared_link_metadata = dbx.sharing_create_shared_link(file_path)
#         links.append(shared_link_metadata.url)
#     return links

# def getTextFromLinks(link):
#     print("xxxxxxxxxxxxxxxxxx", link)
#     try:
#         response = requests.get(link)
#         my_raw_data = response.content
#         text = " "
#         with BytesIO(my_raw_data) as data:
#             read_pdf = PyPDF2.PdfFileReader(data)

#             for page in range(read_pdf.getNumPages()):
#                 print(read_pdf.getPage(page).extractText())
#                 text = text + " " + read_pdf.getPage(page).extractText()
#         return text
#     except Exception as e:
#         print("error", e)
#         return ""



#     #     md, response = dbx.files_download(file_path)
#     #     out = open(entry.name)
#     #     # file_contents.append(response.content)
#     # return file_contents


#         # parsed = parser.from_buffer(file_contents)
#         # print("Aaaaaaaaaaaaaaaaaaaaaaaa", file_contents)
#         # print("Xxxxxxxxxxxxxxxxxxxxxxxx", parsed)
#         ##### Need to add text reading functionality here ####




# # file_path = "/borneo/document.pdf"
# # shared_link_metadata = dbx.sharing_create_shared_link(file_path)
# # shared_link_metadata.url




# def test():
#     print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
#     url = 'https://www.dropbox.com/s/cr5aszzjsawrk2b/test.pdf?dl=0'
#     response = requests.get(url)
#     my_raw_data = response.content

#     with BytesIO(my_raw_data) as data:
#         read_pdf = PyPDF2.PdfFileReader(data)

#         for page in range(read_pdf.getNumPages()):
#             print(read_pdf.getPage(page).extractText())



# import boto3

# # boto3 client
# client = boto3.client(
#     'textract', 
#     region_name='us-west-2', 
#     aws_access_key_id='xxxxxxx', 
#     aws_secret_access_key='xxxxxxx'
# )

# # Read image
# with open('slika2.png', 'rb') as document:
#     img = bytearray(document.read())

# # Call Amazon Textract
# response = client.detect_document_text(
#     Document={'Bytes': img}
# )

# # Print detected text
# for item in response["Blocks"]:
#     if item["BlockType"] == "LINE":
#         print ('\033[94m' +  item["Text"] + '\033[0m')







# {'status': 200, 'content': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDropbox - document.pdf - Simplify your life\n\n \n\n\n\n\n\n\n\n\n   \n', 
# 'metadata': {'Content-Encoding': 'ISO-8859-1', 'Content-Type': 'application/xhtml+xml; charset=ISO-8859-1', 
# 'Content-Type-Hint': 'text/html; charset=UTF-8', 'X-Parsed-By': ['org.apache.tika.parser.DefaultParser', 
# 'org.apache.tika.parser.html.HtmlParser'], 'X-TIKA:parse_time_millis': '119', 'dc:title': 
# 'Dropbox - document.pdf - Simplify your life', 'description': 
# 'Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily.
#  Never email yourself a file again!', 'fb:app_id': '210019893730', 'google-site-verification': 
#  ['TnuSyOnBMNmtugbpL1ZvW2PbSF9LKvoTzrvOGS9h-b0', 'EZKIczQcM1-DVUMz8heu1dIhNtxNbLqbaA9-HbOnCQ4'], 
#  'msapplication-TileColor': '#ffffff', 'msapplication-TileImage': 
#  'https://cfl.dropboxstatic.com/static/images/logo_catalog/logo_m1.png', 'norton-safeweb-site-verification': 
#  'tz8iotmk-pkhui406y41y5bfmfxdwmaa4a-yc0hm6r0fga7s6j0j27qmgqkmc7oovihzghbzhbdjk-uiyrz438nxsjdbj3fggwgl8oq2nf4ko8gi7j4z7t78kegbidl4', 'og:description': 'Shared with Dropbox', 'og:image': 'https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-pdf-large.png', 'og:image:height': '160', 'og:image:width': '160', 'og:site_name': 'Dropbox', 'og:title': 'document.pdf', 'og:type': 'website', 'og:url': 'https://www.dropbox.com/s/xnjwvhsru57wfxh/document.pdf?dl=0', 'referrer': 'origin-when-cross-origin', 'resourceName': 'https-www-dropbox-com-s-xnjwvhsru57wfxh-document-pdf-dl-0', 'robots': 'noindex, nofollow, noimageindex', 'slack-app-id': 'AES7B2V7D', 'title': 'Dropbox - document.pdf - Simplify your life', 
#  'twitter:card': 'summary', 'twitter:description': 'Shared with Dropbox', 'twitter:image': 
#  'https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-pdf-large.png', 
#  'twitter:site': '@Dropbox', 'twitter:title': 'document.pdf', 'twitter:url': 
#  'https://www.dropbox.com/s/xnjwvhsru57wfxh/document.pdf?dl=0'}}
