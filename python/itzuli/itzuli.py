# Itzuli API module
# (c) 2020 Vicomtech

import requests
import json

class Itzuli:
    itzuli_url = "https://api.itzuli.vicomtech.org/"
    translate_path = "translation/get"
    feedback_path = "translation/feedback"
    quota_path = "quota/get"

    def __init__(self, authcode):
        self.auth = authcode

    # Get translation
    def getTranslation(self, text, fromlang, tolang):
        reqJson = {'sourcelanguage':fromlang, "targetlanguage":tolang, "text":text}
        r = requests.post(url = self.itzuli_url+self.translate_path, data = json.dumps(reqJson), headers = {'Authorization': 'Bearer '+self.auth })

        if (r.status_code == 401):
            raise Exception('Invalid API key or expired')
            return
        elif (r.status_code != 200):
            raise Exception('Invalid status code: '+str(r.status_code))
            return

        return r.json()

    # Get quota
    def getQuota(self):
        r = requests.get(url = self.itzuli_url+self.quota_path, headers = {'Authorization': 'Bearer '+self.auth })

        if (r.status_code == 401):
            raise Exception('Invalid API key or expired')
            return
        elif (r.status_code != 200):
            raise Exception('Invalid status code: '+str(r.status_code))
            return

        return r.json()

    # Send feedback
    def sendFeedback(self, id, correction, evaluation):
        reqJson = { 'id':id, "evaluation":evaluation, "correction":correction }

        r = requests.post(url = self.itzuli_url+self.feedback_path, data = json.dumps(reqJson), headers = {'Authorization': 'Bearer '+self.auth })

        if (r.status_code == 401):
            raise Exception('Invalid API key or expired')
            return
        elif (r.status_code != 200):
            raise Exception('Invalid status code: '+str(r.status_code))
            return

        return r.json()
