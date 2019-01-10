import argparse
import spyder
from util import *

parser = argparse.ArgumentParser(description='subject timetable retriver',
                                    usage='%(prog)s [options]')

parser.add_argument('codes', nargs='+', help="subject code (only support one now)")
parser.add_argument('-s', dest='sem',help='manually set the semester info', default=smart_semester())
parser.add_argument('-r',dest='series', help='whether their is a series among the subject (default = None)', default=None)
parser.add_argument('--start', help='Starting date (default = 1)', default=1)
parser.add_argument('--end', help='Ending date (default = 7)', default=7)
parser.add_argument('-y', dest='year', default=smart_year(), help="currently only support the most recent year, achieve support may be added later")

args = parser.parse_args()
spyder = spyder.Spyder(args.codes[0], args.year, args.sem, args.series, args.start, args.end)
spyder.get()