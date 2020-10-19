import argparse, os, time, datetime
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help = "name of the file")
parser.add_argument("-m", "--mtime", help = "modification time (use 1 or 2 to choose format)")
parser.add_argument("--rename", help = "rename file")
parser.add_argument("-s", "--size", help = "print the size of the file", action = "store_true")
args = parser.parse_args()
if args.rename:
    os.rename(args.filename, args.rename)
if args.mtime:
    st = os.stat(args.filename)
    if args.mtime == '1':
        print("last modified: %s" % time.ctime(st.st_mtime))
    elif args.mtime == '2':
        dt = datetime.datetime.fromtimestamp(st.st_mtime)
        print("last modified: %s" % dt.isoformat())
    else:
        print("Wrong input")
if args.size:
    st = os.stat(args.filename)
    print(f"size is {st.st_size}")
