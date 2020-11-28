import requests

how_many_last = str(100)
print('\n-----------------Welcome to Client Program----------------\n')
while True:
    print('Press q to exit!')
    inp = input().strip()
    if inp =='q':
        break
    try:
        id = int(inp)
    except ValueError:
        print('Please, input valid integer id')
        continue

    id = str(id)
    response = requests.get('http://localhost:8000/supply_order/count/?supply_id='+id + \
                            '&how_many_last='+how_many_last)
    print(response.status_code)
    if response.status_code == 404:
        print(response.json()['error_message'])
        continue
    json_data = response.json()
    percent = json_data['percent']
    msg = json_data['message']
    print('Completion rate for driver', id, ' = ', percent)
    print(msg)



