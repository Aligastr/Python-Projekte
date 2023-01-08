import requests
import telegram_token

global requestURL

requestURL = "http://api.telegram.org/bot" + telegram_token.token + "/getUpdates"


def extract_result (dict):
    result_array = dict['result']
    result_dict = result_array[0]

    if result_array == []:
        return False
    else:
        result_dict = result_array[0]
        return result_dict

update_raw = requests.get(requestURL)
update = update_raw.json()

final_result = extract_result(update)

print(final_result['message']['text'])