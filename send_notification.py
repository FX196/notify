import sys
import requests

def notify(message):
    with open('token', 'r') as file:
        token = file.read()
    report = {}
    report['value1'] = message
    requests.post('https://maker.ifttt.com/trigger/job_done/with/key/%s' % token, data=report)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        notify(sys.argv[1])
    else:
        message = "Job %s done on %s" % (sys.argv[1], sys.argv[2])
        notify(message)
        # e.g. "Job upload done on local" 
