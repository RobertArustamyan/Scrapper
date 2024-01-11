from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

EUR_TO_DOL = 1.1
DRAM_TO_DOL = 0.0025
MILE_TO_KM = 1.6
class ListRequest:
    cookies = {
        '_ga': 'GA1.1.1126743256.1704731670',
        '_ym_uid': '170473167427204818',
        '_ym_d': '1704731674',
        '_fbp': 'fb.1.1704731675547.1887017835',
        '_ym_visorc': 'w',
        '_ym_isad': '2',
        'XSRF-TOKEN': 'eyJpdiI6Ik55ZHhneCtyOEU5SVFcL3BYc1RBUFpnPT0iLCJ2YWx1ZSI6InpYcWlKVHdQS056M3R6d3RzcFJ2UnVXTXBSelRRSEJxaVlyNGFpQzJBam5ZWXVwWjdWcFVES051cEtKZEl6OFhzM1IzTE5Bc1RjYWdHNTZ5dnhTYis2dk9oSTc4T1ZzNXk0TEpJQUh1RklWNFdnN0lTbE9Ta0FCSXMzaStIU3RTIiwibWFjIjoiMWRlNDJhNTA5NDJhNjMyZTEzZjQ1MWUyN2EwNTM3N2YyMmVhZGU3NzVlODI5NTczNjQwNTcyNWYyOTA0OWNlOCJ9',
        'autoam_session': 'eyJpdiI6ImJ4NE5IMExwaE5iNGJFc3pBZDVtTHc9PSIsInZhbHVlIjoiZjJnMUdVSjFYemZERFl2VUlcL1hWY1wvWnNaZjJjanZ3NStXK0twU1Azc3FIVnU4ejlrRXk3NjRtNUlrUmJvYnI0bUxGMnlpR3JsOUd5cE5qOWlUMkI0aDdmc1h5WUFcL3FpUWJ4dGMxQzJ2a1VtU0RBM3FiNUNzaEN2RWdTQ2RSeWIiLCJtYWMiOiJjY2RmYWY5ZTI4NWRjZjM1Njk5Yjg3YTA0NjVkNGU4MGYzNWI1OWViYzBkOWM0YWI0MTIzYzNhMzlkMmZhMDU4In0%3D',
        '_ga_FP90EBRFYF': 'GS1.1.1704891967.5.1.1704892650.37.0.0',
    }

    headers = {
        'authority': 'auto.am',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.1126743256.1704731670; _ym_uid=170473167427204818; _ym_d=1704731674; _fbp=fb.1.1704731675547.1887017835; _ym_visorc=w; _ym_isad=2; XSRF-TOKEN=eyJpdiI6Ik55ZHhneCtyOEU5SVFcL3BYc1RBUFpnPT0iLCJ2YWx1ZSI6InpYcWlKVHdQS056M3R6d3RzcFJ2UnVXTXBSelRRSEJxaVlyNGFpQzJBam5ZWXVwWjdWcFVES051cEtKZEl6OFhzM1IzTE5Bc1RjYWdHNTZ5dnhTYis2dk9oSTc4T1ZzNXk0TEpJQUh1RklWNFdnN0lTbE9Ta0FCSXMzaStIU3RTIiwibWFjIjoiMWRlNDJhNTA5NDJhNjMyZTEzZjQ1MWUyN2EwNTM3N2YyMmVhZGU3NzVlODI5NTczNjQwNTcyNWYyOTA0OWNlOCJ9; autoam_session=eyJpdiI6ImJ4NE5IMExwaE5iNGJFc3pBZDVtTHc9PSIsInZhbHVlIjoiZjJnMUdVSjFYemZERFl2VUlcL1hWY1wvWnNaZjJjanZ3NStXK0twU1Azc3FIVnU4ejlrRXk3NjRtNUlrUmJvYnI0bUxGMnlpR3JsOUd5cE5qOWlUMkI0aDdmc1h5WUFcL3FpUWJ4dGMxQzJ2a1VtU0RBM3FiNUNzaEN2RWdTQ2RSeWIiLCJtYWMiOiJjY2RmYWY5ZTI4NWRjZjM1Njk5Yjg3YTA0NjVkNGU4MGYzNWI1OWViYzBkOWM0YWI0MTIzYzNhMzlkMmZhMDU4In0%3D; _ga_FP90EBRFYF=GS1.1.1704891967.5.1.1704892650.37.0.0',
        'origin': 'https://auto.am',
        'referer': 'https://auto.am/search/passenger-cars?q={%22category%22:%221%22,%22page%22:%222%22,%22sort%22:%22latest%22,%22layout%22:%22list%22,%22user%22:{%22dealer%22:%220%22,%22official%22:%220%22,%22id%22:%22%22},%22year%22:{%22gt%22:%221911%22,%22lt%22:%222025%22},%22usdprice%22:{%22gt%22:%220%22,%22lt%22:%22100000000%22},%22mileage%22:{%22gt%22:%2210%22,%22lt%22:%221000000%22}}',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-csrf-token': 'FEyCWVimu0S63G9Jdx5xgFojOszk6sJR5V8guUd9',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'search': '{"category":"1","page":"1","sort":"latest","layout":"list","user":{"dealer":"0","official":"0","id":""},"year":{"gt":"1911","lt":"2025"},"usdprice":{"gt":"0","lt":"100000000"},"mileage":{"gt":"10","lt":"1000000"}}',
    }

    url = "https://auto.am/search"
    def post_response(self, data):
        return requests.post(self.url, cookies=self.cookies, headers=self.headers, data=data)

    def making_data(self,page_num):
        data = {}
        data["search"] = self.data['search'].replace('"page":"1"', f'"page":"{page_num}"')
        return data

    def text_response(self, page_num):
        data = self.making_data(page_num)
        response = self.post_response(data)

        if response is not None:
            return response.text

class Car:
    def __init__(self, name, year, distance, price, add_info, region,cstm_cleared):
        self.name = name
        self.year = year
        self.distance = distance
        self.price = price
        self.add_info = add_info
        self.region = region
        self.cstm_cleared = cstm_cleared

def creating_base(html_text):
    soup = BeautifulSoup(html_text,'lxml')
    cards = soup.find_all('div',class_="card")
    car_list = []
    for card in cards:
        #getting name and year
        title_span = card.find("span", class_="card-title bold")
        if title_span:
            year_span = title_span.find("span", class_="grey-text")

            car_year = year_span.text.strip() if year_span else "N/A"
            car_name = title_span.contents[-1].strip()

        # getting price
        card_price = card.find("div","price bold blue-text").text.strip()
        card_desc = card.find("div", class_="card-desc").strong

        if card_price.split(" ")[0] == "֏":
            card_price = int(int(''.join(filter(str.isdigit, card_price))) * DRAM_TO_DOL)
            card_price = "${:,.0f}".format(card_price).replace(",", " ")
        elif card_price.split(" ")[0] == "€":
            card_price = int(int(''.join(filter(str.isdigit, card_price))) * EUR_TO_DOL)
            card_price = "${:,.0f}".format(card_price).replace(",", " ")
        else:
            pass

        #getting details
        if card_desc:
            card_details = [item.strip() for item in card_desc.next_sibling.split(',')]
            card_details = [detail for detail in card_details if detail]
        else:
            card_details = []
        #getting distance
        card_distance = card_desc.text
        if card_distance.split(" ")[2] != "կմ":
            card_distance = int(int(card_distance.split(" ")[0]) * MILE_TO_KM)
            card_distance = f"{card_distance} կմ "


        #location and custum part
        card_loc = card.find("div",class_='card-loc')
        if card_loc:
            card_location_span = card_loc.find("span", class_='flag-in-horizontal-azd')
            if card_location_span:
                card_location = card_location_span.text.strip()
                cstm_cleared_element = card_location_span.find_next_sibling()
                if cstm_cleared_element:
                    cstm_cleared = cstm_cleared_element.text.strip()
                else:
                    cstm_cleared = "N/A"
            else:
                card_location = "N/A"
                cstm_cleared = "N/A"
        else:
            card_location = "N/A"
            cstm_cleared = "N/A"

        car_list.append(Car(car_name,car_year,card_distance,card_price,card_details,card_location,cstm_cleared))
    return car_list

if __name__ == "__main__":
    Reqs = ListRequest()
    list_of_cars = []
    for num in range(1,200):
        response_by_page = Reqs.text_response(num)
        list_of_cars.extend(creating_base(response_by_page))
        print(num)
        time.sleep(3)

    car_data = [
        {
            'Name': car.name,
            'Year': car.year,
            'Distance': car.distance,
            'Price': car.price,
            'Additional Info': car.add_info,
            'Region': car.region,
            'Custom Cleared': car.cstm_cleared
        }
        for car in list_of_cars
    ]

    df = pd.DataFrame(car_data)
    excel_file_path = 'car_data.xlsx'
    df.to_excel(excel_file_path, index=False)

    print(f"Excel file saved at: {excel_file_path}")
