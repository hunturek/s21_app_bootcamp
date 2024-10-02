import redis
import time
import logging
import argparse
import json

parser = argparse.ArgumentParser(description='cash_flow')
parser.add_argument('-e', '--evil', type=str, help='List of evil nums')
args = parser.parse_args()

logging.basicConfig(level=logging.INFO)

evil = args.evil.split(',')
print(evil)

r = redis.Redis(host='localhost', port=6379, db=0)

p = r.pubsub()
p.subscribe('my-channel-1')

try:
    while True:
      message = p.get_message()
      if message and message['type'] == 'message':
        data = message['data']
        if isinstance(data, bytes):
            decoded_data = json.loads(data.decode('utf-8'))
            if str(decoded_data['metadata']['to']) in evil \
                and decoded_data['amount'] > 0:
                tmp: int = decoded_data['metadata']['to']
                decoded_data['metadata']['to'] = \
                    decoded_data['metadata']['from']
                decoded_data['metadata']['from'] = tmp
                logging.warning('swap')
            logging.info(decoded_data)
      time.sleep(0.01)

except KeyboardInterrupt:
    print('exit')