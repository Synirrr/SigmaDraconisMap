from oauth2client.service_account import ServiceAccountCredentials

import gspread


def main():
    ########################## Setup google credentials and API access ##########################################
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('src/main/starmap-310623-baf93c6b9991.json', scope)

    gc = gspread.authorize(credentials)
    #############################################################################################################

    # Get records from spread sheet
    wks = gc.open('CSV-SDW-GPS').sheet1

    records_dict = wks.get_all_records()
    objects = []
    for record in records_dict:
        # Make solar bodies
        print(record)