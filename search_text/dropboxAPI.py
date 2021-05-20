import dropbox
from search_text.settings import access_token
from search_text.settings import folder_path


def getFilesFromDropBoxFolder():
    dbx = dropbox.Dropbox(access_token)
    for entry in dbx.files_list_folder(folder_path).entries:
        print(entry.name)
        file_path = folder_path + "/" + entry.name
        md, response = dbx.files_download(file_path)
        file_contents = response.content
        ##### Need to add text reading functionality here ####
