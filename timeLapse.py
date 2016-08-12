import sys, getopt
from time import sleep

arguments = {
    'shots': 300,
    'freq': 5,
    'path': './',
    'filename': 'image.jpg',
    'verbose': True
}

def testShot():
    while True:
        testShot = input("> Do you want to take a test shot [Y/N]: ")
        if testShot.upper() == 'Y':
            takeShots(1, 1)
        else:
            break

def takeShots(freq, shots): 
    for i in range(1, shots+1):
        sleep(freq)
        sys.stdout.flush()
        if i % 5 != 0:
            print('.', end=" ")
        else:
            print(i, end=" ")

        if i % 100 == 0:
            print('\n')
    
    print('\n')
    print("[Done]")

def confirmDetails(freq, shots, path, filename):
    time = freq * shots
    print("\tShot Frequency: %s seconds" %freq )
    print("\tNumber of Shots: %s" %shots )
    print("\tTotal time (freq x shots): \n\t\t%.1f seconds \n\t\t%.1f minutes \n\t\t%.1f hours" % (time, time / 60, time / (60*60) ) )
    print("\tPath: %s" %path )
    print("\t Filename: %s" % filename )
    confirm = input("> Confirm details [Y/N]: ")
    print("------------")

    if confirm.upper() == 'Y':
        return True
    else:
        return False;

def verboseInput():
    global arguments
    arguments['shots'] = int( input("> Enter number of shots: ") )
    arguments['freq'] = float( input("> Enter shot frequency in seconds: ") )
    arguments['path'] = input("> Enter path to store the image: ")
    arguments['filename']= input("> Enter filename of the image. Date and time will be appended: ")
    return


def printManual():
    print("\t -f \t frequency of shots (in seconds)")
    print("\t -s \t number of shots")
    print("\t -o \t output filename of image")
    print("\t -p \t path of image files")

def parseArgs(opts):
    global arguments
    for opt, arg in opts:
        if opt in ('-f', '--freq'):
            arguments['freq'] = float( arg )
        elif opt in ('-s', '--shots'):
            arguments['shots'] = int( arg )
        elif opt in ('-o', '--output'):
            arguments['filename'] = arg;
        elif opt in ('-p', '--path'):
            arguments['path'] = arg;
        elif opt == '-v':
            arguments['verbose'] = True
        elif opt == '-h':
            printManual()

    #print(freq, shots, filename, path)

def prompt(argv):
    print("~~~~~~~Time Lapse Program~~~~~~~")
    print("Press Ctrl-C to kill program")

    try:
        opts, args = getopt.getopt(argv,"hf:s:o:p:v",["freq=","shots=", "output=", "path="])
    except:
        return

    if not opts:
        verboseInput()
    else:
        parseArgs(opts)

    while True:
        if confirmDetails(
                arguments['freq'], 
                arguments['shots'], 
                arguments['path'], 
                arguments['filename']
            ) == True: 
            testShot()
            takeShots(arguments['freq'], arguments['shots'])
            break
        else:
            verboseInput()



if __name__ == "__main__":
    prompt(sys.argv[1:])
