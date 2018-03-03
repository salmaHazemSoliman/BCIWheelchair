import gspread
import GooglespreadSheetConfig as GSC

class GSpreadPrintingUtilities():
    @staticmethod
    def getEmptyRowIndex(colToCheck):
        #gc = gspread.login( GSC.email , GSC.password)
	json_key = json.load(open('/tmp/mozilla_root0/BCIWheelChair2018-eef792bad9a5.json'))
	scope = ['https://spreadsheets.google.com/feeds']

	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

	gc = gspread.authorize(credentials)

	#wks = gc.open("Where is the money Lebowski?").sheet1

        sh = gc.open(GSC.title) 
        worksheet = sh.worksheet(GSC.sheet_title)

        #investigate the followin columns
        prev_index = -1
        index = -1
        for i in colToCheck:
            values_list = worksheet.col_values(i)
            curr_index = len(values_list)

            if (curr_index > prev_index):
                index = curr_index

#            print "---- getEmptyRowIndex test ----"
#            print "--------"
#            print index
#            print "--------"


            prev_index = curr_index

        return index + 1
