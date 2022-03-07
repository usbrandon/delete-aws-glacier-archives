#!/usr/bin/env python3

import json
import subprocess
import time

json_file = 'output.json'
account_id = '120858456456'
vault_name = 'arq_1B1A2BEF-9F13-41BA-86AA-2229C737BBB4'

with open(json_file) as f:
    data = json.load(f)

for item in data['ArchiveList']:
    cmd = "aws glacier delete-archive --profile produser --account-id %s --vault-name %s --archive-id=\'%s\'" % (
    account_id, vault_name, item['ArchiveId'])
    returned_value = subprocess.call(cmd, shell=True)
    print('cmd: %s || returned value: %s' % (cmd, str(returned_value)))
    time.sleep(0.1)
