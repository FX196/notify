import sys
import requests

def notify(message):
    with open('/Users/yuhongc/Projects/ifttt/token', 'r') as file:
        token = file.readline()[:-1]
    report = {}
    report['value1'] = message
    requests.post('https://maker.ifttt.com/trigger/job_done/with/key/%s' % token, data=report)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        message = sys.argv[1]
        notify(message)
    else:
        message = "Job %s done on %s" % (sys.argv[1], sys.argv[2])
        notify(message)
        # e.g. "Job upload done on local"
    print("Sent message: %s" % message)

