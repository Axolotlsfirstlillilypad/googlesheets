import os
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from pdf2image import convert_from_path
import pytesseract
from time import sleep

#Authenticate with Google Sheets API using the service account credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials_json = "path_to_your_credentials.json"  # Path to your service account credentials
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json, scope)
client = gspread.authorize(creds)
#get the URL
sheet_url = "YOUR_GOOGLE_SHEET_URL"  
sheet = client.open_by_url(sheet_url)
worksheet = sheet.get_worksheet(0)  #Only 1 sheet exists, so we can just extract the links from the first sheet indexed at 0.
#Fetch all rows of data from the worksheet
data = worksheet.get_all_values()


#the linked pdfs will have their info stored here
if not os.path.exists( "downloaded_pdfs"):
    os.makedirs( "downloaded_pdfs")
  #for non-link infor
if not os.path.exists("extracted_text"):
    os.makedirs("extracted_text")


for row in data:
    pdf_link = row[i]
  #build the link for each specific link, by strining together terms. This can be really use if the links have common folders.
    file_id = pdf_link.split("/d/")[1].split("/")[0]  # Extract file ID from the URL
    response = requests.get( f"https://drive.google.com/uc?id={file_id}&export=download")
    pdf_path = os.path.join(download_folder, f"{file_id}.pdf")

  #write in the info
    with open(pdf_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {pdf_path}")    
    pages = convert_from_path(pdf_path)
    extracted_text = ""
    for i, page in enumerate(pages):
        print(f"Processing page {i + 1}...")
      #write in if pdf is stored in images, read the images
        text = pytesseract.image_to_string(page)
        extracted_text += text + "\n\n"
    text_file_path = os.path.join(text_folder, f"{file_id}.txt")
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)
    
    
    sleep(2)
