# googlesheets

Hi, in today's example a client would like to read in data from a google sheets data structure, because the data he wishes to access is in a read-only mode. However, one columns of data comprises links to other google drive websites that have pdfs. Now, while extracting data from a standard spreadsheet is not too difficult (the most direct way I know of would be to download the data, then use read_xl), the linked pdfs present something of a challenge. Each pdf might have a lot of data on it's own and when there are thousands of entry having to manually read all that information would be quite time consuming. We might need help! 

Also, sometimes pdfs aren't texts, they are images, which makes trying to extract information significantly more challenging. Could we use a machine tool to help us? Well good news! We can!.

## **Table of Contents**
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Install Dependencies](#1-install-dependencies)
  - [2. Set Up Google API](#2-set-up-google-api)
  - [3. Download PDFs and Run OCR](#3-download-pdfs-and-run-ocr)
- [Usage](#usage)
  - [1. Extracting Google Drive Links](#1-extracting-google-drive-links)
  - [2. Download PDFs](#2-download-pdfs)
  - [3. Run OCR](#3-run-ocr)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## **Prerequisites**
Before running this script, make sure you have the following installed and configured:

1. **Python 3.6+**: You should have Python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. **Google Sheets API**: The script accesses a Google Sheet to extract links, so you’ll need to set up a Google Sheets API and Google Drive API.
3. **Tesseract OCR**: This project uses Tesseract for **Optical Character Recognition** to extract text from PDF files.
4. **Required Python Libraries**:
   - `gspread`: For accessing and interacting with Google Sheets.
   - `requests`: For downloading PDFs.
   - `pytesseract`: For extracting text using OCR.
   - `pdf2image`: For converting PDF pages into images that Tesseract can process.
   - `pillow`: For image processing.


## **Setup Instructions**

### **1. Install Dependencies**

Install the necessary Python libraries using `pip`:

```bash
pip install gspread requests oauth2client pytesseract pdf2image pillow

You may need to check if you can run pip. If you do not, this is a sign that your device does not have Python installed.



### **2. Google API**


To access Google Sheets and download files from Google Drive, you'll need to set up a Google API project.

First,go to the Google Cloud Console, and create a new project. "https://cloud.google.com/cloud-console?utm_source=google&utm_medium=cpc&utm_campaign=japac-SG-all-en-dr-BKWS-all-super-trial-PHR-dr-1710102&utm_content=text-ad-none-none-DEV_c-CRE_649003149322-ADGP_Hybrid+%7C+BKWS+-+BRO+%7C+Txt+-Management+Tools-Cloud+Console-google+cloud+console-main-KWID_43700075888673448-kwd-296393718382&userloc_9062522-network_g&utm_term=KW_google+cloud+console&gad_source=1&gad_campaignid=1039894279&gclid=CjwKCAjw6NrBBhB6EiwAvnT_rq8NdEeJRi5SgeF5RfjIs898jHcXOyQY3hHLg1SJSOyjdcVCMFCzNBoCfGsQAvD_BwE&gclsrc=aw.ds" may be useful link. If unwilling to pay there is an option for free use. Enable the Google Sheets and Drive API.


Share Google Sheet with Service Account: Ensure that the service account's email address is shared with access to your Google Sheet.




## **How It Works: Line-by-Line Explanation**

### **Step 1: Authenticate with Google Sheets API**
The first thing the script does is authenticate with the Google Sheets API. This is done using the **service account credentials** that you generated in the Google Cloud Console.

```python
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials_json = "path_to_your_credentials.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json, scope)
client = gspread.authorize(creds)


First we set the urls required for Sheets and Drive authentication. We have compiled them in a list for easy access, which is a thing that you may consider on other projects that may involved accessing multiple links. Then we set the credentials (which are the client's, very imprt). Finally we use gspread.authorise to gain authorisation from the google services.


If at this stage errors are encountered, check that the link is valid and that permissions are set to public for the pertinent resources.


After authentication we are free to open the url.
sheet = client.open_by_url("YOUR_GOOGLE_SHEET_URL")
#gets the worksheet.
worksheet = sheet.get_worksheet(0)

data = worksheet.get_all_values()
retrieve all rows of data.

To make the folders to store the pdf data, we can use a simple check. If not checks if our files exist, and if one hasn't been created we use os.makedirs to write one ourselves. The condition also prevents us from inadvertently writing duplicates everytime we run the code.


We then iteratively take out the links in the sheet with row[i]. i depends on which specific column . We then use the open() function set to 'wb' to read in the pdfs and then transcribe the contents to a new file with f.write. Should the pdfs involve images , we use pytesseract.image_to_string() to read the image for us.

Lastly it may be wise to ask the program to sleep for sometime so it doesn't tax the download limit for google.




## **Troubleshooting**

### **"Google API Access Denied" Error**:
- Double-check that the **Service Account** email has been shared with the correct Google Sheet.
- Ensure that you’ve provided the correct path to the **credentials JSON** file in the script.
- Verify that both **Google Sheets API** and **Google Drive API** are enabled in the **Google Cloud Console**.

### **"Failed to Download PDF" Error**:
- Ensure the **Google Drive link** is valid and accessible.
- Check if the file is **publicly shared** or if the service account has permission to access it.

---

## **License**

This project is licensed under the **MIT License** 
