import redis
import json
import random

r = redis.Redis(host='localhost', port=6379, db=0)

random_list = [random.randrange(1000000000, 9999999999, 1) for i in range(5)]
random_list.append(1234567890)
random_list.append(9876543210)
print(random_list)

for i in range(6):
    data = {
        "metadata": {
            "from": random_list[random.randrange(0, 7, 1)],
            "to": random_list[random.randrange(0, 7, 1)]
        },
        "amount": random.randrange(-100000, 100001, 1)
    }

    json_data = json.dumps(data)
    r.publish('my-channel-1', json_data)