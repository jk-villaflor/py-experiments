from win32com import client
import sys, getopt, os

productionMode = False


def showHelp():
    helpText = ''
    helpText += '\nUSAGE: loki.py [file] [args]\n\n'
    helpText += 'DESCRIPTION: Exports or transforms XLS files to PDF\n\n'
    helpText += 'OPTIONS: \n'
    helpText += '\t-f --file\t\tFull location.\n'
    helpText += '\t\t\t\t\t- [string] [required]\n'
    helpText += '\t-s --size\t\tSet paper size.\n'
    helpText += '\t\t\t\t\t- [string] [choices: "a4" | "legal"] [default: "a4"]\n\n'
    helpText += '\t-i --index\t\tSelect worksheet. Accepts index or worksheet name.\n'
    helpText += '\t\t\t\t\t- [number | string] [default: "0" | 0]\n\n'
    helpText += '\t-o --orientation\t\tOrientation between landscape and portrait.\n'
    helpText += '\t\t\t\t\t- [string] [choices: "portrait" | "landscape"] [default: "portrait"]\n\n'
    helpText += 'EXAMPLE: loki.py --size=legal --file=C:\\location\\to\\your\\file.ext\n\n'
    print(helpText)

def main(argv):
    targetFile = ''
    targetPaperSize = 1 # legal 8.5 x 11
    exportedFilename = ''
    worksheetIndex = 0
    zoomValue = False
    margins = 15

    try:
        opts, args = getopt.getopt(argv,"s:f:i:z:o:m:h",["size=","file=", "index=", "zoom=","orientation=", "margins=","help"])
    except getopt.GetoptError:
        print('Error in usage. Please see below:\n\n')
        showHelp()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in('-h', '--help'):
            showHelp()
            sys.exit(2)
        elif opt in ("-o", "--orientation"):
            if(arg == 'landscape'):
                orientation = 2
            elif(arg == 'portrait'):
                orientation = 1
            else:
                print('Unrecognized orientation parameter\n\n')
                showHelp()
                sys.exit(2)
        elif opt in ("-z", "--zoom"):
            zoomValue = int(arg)
        elif opt in ("-m", "--margins"):
            margins = int(arg)
        elif opt in ("-s", "--size"):
            if(arg == 'legal'):
                targetPaperSize = 5 # legal 8.5 x 14
        elif opt in ("-f", "--file"):
            if(arg == ''):
                print('Error in usage. Please see below:\n\n')
                showHelp()
                sys.exit(2)
            targetFile = arg
            exportedFilename = os.path.splitext(os.path.basename(targetFile))[0]+'.pdf'
        elif opt in ("-i", "--index"):
            worksheetIndex = arg

    try:
        xlApp = client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open(targetFile)
        ws = books.Worksheets[worksheetIndex]

        # excel parameters
        ws.Visible = 1
        ws.PageSetup.Zoom = zoomValue
        ws.PageSetup.Orientation = orientation
        # ws.PageSetup.LeftMargin = 5
        # ws.PageSetup.RightMargin = 5  
        # ws.PageSetup.TopMargin = 5
        # ws.PageSetup.BottomMargin = 5
        ws.PageSetup.LeftMargin = margins
        ws.PageSetup.RightMargin = margins
        ws.PageSetup.TopMargin = margins
        ws.PageSetup.BottomMargin = margins
        ws.PageSetup.FitToPagesTall = 3
        ws.PageSetup.FitToPagesWide = 1
        ws.PageSetup.CenterHorizontally = True
        # ws.PageSetup.CenterVertically = True

        # input parameters
        ws.PageSetup.PaperSize = targetPaperSize
    except Exception as err:
        print('ERROR: ', err)
        print('ERROR: There\'s a problem opening the target excel file: ', targetFile)
        print('\nPlease see usage below:\n\n')
        showHelp()
        sys.exit()

    try:
        # export function
        exportedFilename = os.path.join(os.getcwd(), exportedFilename)
        ws.ExportAsFixedFormat(0, exportedFilename)
    except :
        print('There\'s a problem exporting the file : ', exportedFilename+"\n")

if __name__ == "__main__":
    main(sys.argv[1:])