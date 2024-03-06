import concurrent.futures.process

import requests

import json

# saving file name
file_name = 'My_Products'
# creating blank list for urls
urls = []


# clear all data in my json file if there is any from previous test
with open(file_name, 'w') as json_file:
    json_file.write('')


def get_product_data(url):
    try:
        # making get request to server
        response = requests.get(url)

        # checking if request is successful
        if response.status_code == 200:
            # making json content
            data = response.json()

            # converting data to single-line json format
            json_data = json.dumps(data)

            # writing data in json file
            with open(file_name, 'a') as json_file:
                json_file.write(json_data + '\n')
                print('data form {} is written in your file {}'.format(url, file_name))
        else:
            print('error geting data from {} , with status code {}'.format(url, response.status_code))

        pass

    except Exception as e:
        print('An error occurred: {}'.format(e))


# generating urls
for i in range(1, 101):
    urls.append('https://dummyjson.com/products/{}'.format(i))


def main():

    with concurrent.futures.process.ProcessPoolExecutor() as process_executor:
        for i in range(0, 100, 20):
            p_f = [process_executor.submit(process_urls, urls[i:i + 20])]


def process_urls(urls):
    with concurrent.futures.ProcessPoolExecutor() as thread_executor:
        for url in urls:
            t_f = thread_executor.submit(get_product_data, url)


if __name__ == '__main__':
    main()


print('all information saved in {}'.format(file_name))
