import parser
import logging

message = "Program that will take in files and create a file with a summary of the current TODO's in the listed files."

logMessages = {
    'warning' : {
        'nofile' : "File '{0}' does not exist on this system."
    }
}


def main():
    import argparse

    ap = argparse.ArgumentParser(description=message)
    ap.add_argument("files",
                    nargs=argparse.REMAINDER,
                    metavar="[file1, file2, ...]",
                    help="The list of files that the program will process TODOs from.")
    ap.add_argument("-o", "--out",
                    action='store_true',
                    help="Output the raw text to standard out")
    ap.add_argument("-g", "--gui",
                    action='store_true',
                    help="Enable the GUI")
    ap.add_argument("-w", "--write",
                    nargs=1,
                    dest="outFile",
                    metavar="dest",
                    type=argparse.FileType('w'),
                    help="Write the output to file specified by 'dest'.")
    args = ap.parse_args()

    if args.gui:
        logging.critical("GUI not yet supported.")
        exit(1)

    listconfs = []
    for fileName in args.files:
        try:
            with open(fileName) as f:
                listconfs.append(parser.TODOconf(f, fileName))

        except IOError:
            logging.warning(logMessages['warning']['nofile'].format(fileName))

    if args.out:
        for i in listconfs:
            print(i)

    if args.outFile:
        for i in listconfs:
            args.outFile[0].write(str(i))

    exit(0)


if __name__ == '__main__':
    main()
