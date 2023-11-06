from win32com import client
import sys, getopt, os 

def showHelp():
    helpText = ''
    helpText += '\nUSAGE: loki.py [file] [args]\n\n'
    helpText += 'DESCRIPTION: Exports or transforms XLS files to PDF\n\n'
    helpText += 'OPTIONS: \n'
    helpText += '\t-f --file\t\tFull location.\n'
    helpText += '\t\t\t\t\t- [string] [required]\n'
    helpText += '\t-s --size\t\tSet paper size.\n'
    helpText += '\t\t\t\t\t- [string] [choices: "a4", "legal"] [default: "a4"]\n\n'
    helpText += 'EXAMPLE: loki.py --size=legal --file=C:\\location\\to\\your\\file.ext\n\n'
    print(helpText)

def main(argv):
    targetFile = ''
    targetPaperSize = 1
    exportedFilename = ''

    try:
        opts, args = getopt.getopt(argv,"hs:f:",["size=","file=", "help"])
    except getopt.GetoptError:
        print('Error in usage. Please see below:\n\n')
        showHelp()
        sys.exit(2) 
    for opt, arg in opts:
        if opt in('-h', '--help'):
            showHelp()
            sys.exit()
        elif opt in ("-s", "--size"):
            if(arg == 'legal'):
                 targetPaperSize = 5 # legal 8.5 x 14
        elif opt in ("-f", "--file"):
            if(arg == ''):
                print('Error in usage. Please see below:\n\n')
                showHelp()
            targetFile = arg
            exportedFilename = os.path.splitext(os.path.basename(targetFile))[0]+'.pdf'

    try:
        xlApp = client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open(targetFile)
        ws = books.Worksheets[0]

        # constant parameters
        ws.Visible = 1
        ws.PageSetup.Zoom = False
        ws.PageSetup.Orientation = 2
        ws.PageSetup.RightMargin = 25
        ws.PageSetup.TopMargin = 25
        ws.PageSetup.BottomMargin = 25
        ws.PageSetup.FitToPagesTall = 1
        ws.PageSetup.FitToPagesWide = 1
        ws.PageSetup.CenterHorizontally = True
        ws.PageSetup.CenterVertically = True

        # input parameters
        ws.PageSetup.PaperSize = targetPaperSize
    except :
        print('ERROR: There\'s a problem opening the target excel file: ', targetFile)
        print('\nPlease see usage below:\n\n')
        showHelp()
        sys.exit()

    try:
        # export function
        ws.ExportAsFixedFormat(0, os.path.join(os.getcwd(), exportedFilename))
    except :
        print('There\'s a problem exporting the file : ', targetFile)

if __name__ == "__main__":
    main(sys.argv[1:])