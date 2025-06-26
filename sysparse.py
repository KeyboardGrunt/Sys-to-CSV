import sys
import csv

def get_place(log_line, jumps):
    jump = 0
    j = 0
    for i in log_line:
        if i == " ":
            jump += 1
            if jump == jumps:
                    return j
        j += 1    


syslog = sys.argv[1]

# Insert validation and error handling.

if sys.argv[1] == "-help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
     print("Syslog to CSV parser.")
     print("Using this on files other than syslog will have unexpected effects.")
     print("python3 sysparse.py <syslog file> <output file>")
     exit()

outfile = sys.argv[2]

try:
    with open(syslog) as sl:
        with open(outfile, 'w', newline='') as csvfile:
            csvwrite = csv.writer(csvfile, delimiter=';', escapechar='\\', quoting=csv.QUOTE_NONE)
            csvwrite.writerow(['datetime'] + ['hostname'] + ['appname'] + ['message'])
            for l in sl:
                sl_date = l[0:15]
                host_end = get_place(l, 4)
                sl_hostname = l[16:host_end]
                app_end = get_place(l, 5)
                sl_appname = l[host_end + 1:app_end]
                message = l[app_end + 1:]
                csvwrite.writerow([sl_date] + [sl_hostname] + [sl_appname] + [message])
except:
    print("Error: Make sure you are selecting a syslog file.")
