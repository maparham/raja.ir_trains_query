import requests, json
import urllib3
import time
from plyer import notification
from dateutil import parser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import os

blockedTrains = []

urls = [
    "Tehran-Mashhad",
    # "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=XIhEPqlFGRWXg6CFzUV8nlzxjFhSAX/VW5Dg+jDJenofk8EOcbEnaYAA04d4NEYkI5DHI7deROYqaSJU91VjPPMLp7QhgxpP/Up4LLzXr8c="
    # ,"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=n20LbDe5MSaiSJn/tDYGe0h/S+4vhAK3UZ0si1qWbMTiSMXoGtDMVgOygW+iw0+BgAsRtoL+sBA1c5oLOP1rNeDERBewmIUTYzZVvvCV2/0="
    # ,"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=ZJKzBlOf7+c47rvjblaLGT/mWeM82n7SWTg7x2notUoLyYSlXngtGTHT6I0X2DyAlC0yxwkbUiAxlyMcwlREUn1jvLyO0Fi0BNDUMiivgRs="
    # ,"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=SdUe2tGSW0i3A3aPpiXodkClRDepiUKrURcL4EFm527+8X4v6N0pqsFFHEcbznpPqC0wYFzm8nrdEXsw/tI7SwbiGyq02BY7nw8qW5T4XpM="
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=l/GCerurXfinLwhZWveQ3sTSY3hC++S4qoeKCWu3vtNHQ4gQXPuP5onmnh+DgBIVJbbRXQEE+Wmwjtt6bhCeUgWNjN44NjJ8RcCTWLZE2ow="
    ,
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=l7TK+L8IF1bUlWLPYBrPz5XheTZkdGDHRDWbd5BJfegt4ZChd2UPbya//5rbA6QIrZ3J6fccqZNm6M74gOZCxxfAFe8wIhBoGX6OsQeZqv8="
    ,
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=zTRP6kKo2efORmxQr0MVVs0ivcNDvwK/oLWjiGdKSfiSvV4Jovq/TpRLOdJqhLaRqnknqGg/RSpaEZNegHR7DOtTMXoTso84Rtq8Wp5o4RU="
    ,
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=UGYASyuSzO1UQUD2QYgt9LtBfjtZGLV/ld4AGpQTw6kkweJhaOieEEw5IRW6RztF71SbgyfLP78mrkp27hCzup1MqRRT5pHduoABeL2Ba3w="
    # ,"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=zRDJJmHnuYY4q6coS245KkP81C5W790lMHDUkcSCbah4K/fClSpRRgHliEkabdF311tRzU527GrKL2DTeGFTHtyfdvkkZvFnudtjM5HmnK4="
    ,
    "Tehran-Shahrood",
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=OeSrjrusxlJgTYZbaO+sc7r6YjepL3g/z02g1mxTgs37zPXhRrfnJ+C5miOyevEFtHG8YCxXUvPVxlkqlAHVIOCIgQ1kMaj0JR7zP+kjYSk="
    ,
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=Pu4PpL2uDdNvi0O4wPo5N6prZNjBndbeqSn7GJIgGZHYay/Rlc7vM7K6le+D++6OHcoWzPUO2woxIrLUJu+HVHZ7ERp9wv5HfCx/n/u42DU="
    ,
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=Xj+5z6F+KSa7He5UwLmP17+gN49cioGQN6zalLY2j+xrxeXim+iVUcLM7gh+M0NstLmbwzEXTZlM1jsZD9pmSfgZXlTCDAAeAX7boioOtJ0="
    ,
    "https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=0ymMuG7IhWlNJbzRPKAo+KsO3ihZcvpqN4+hcDBntfls1Tsa7ISMvwZq/mBi2nnwsyy48kV1LPsb4co9ULSf9qL4OKsbFO3NIaM40ZroYiQ="
    # ,"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=byAIb7W0g16XBo+dRwlgcMliQp2sTJAvU77TCZbsUGC0CY92bBzMhfV2ksxGBrT3ghfyjEIacHSJStduNIFQG5Vkq0/+jyPL4H9rzK22zpE=",
    # ,"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q=RcLsUo8Xu+OqeyvGOOF26kGAdavM5YbqVTSq3XBs7SGLV9s9VccadiEQNmJ6GX9rAePkHwMHCDHTQ+eOgSrQzBl+fn3wJ+02wGCMKH2Ij8c="
]

while True:
    for url in urls:
        if not url.startswith("http"):
            print(url)
            continue
        try:
            r = requests.get(url, auth=('usrname', 'password'), verify=False, stream=True)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
            break
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
            break
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
            break
        if r.status_code == 400:
            print(r.content.decode())
            break

        data = json.loads(r.content)

        for train in data['GoTrains']:  # list of all trains
            departure = parser.parse(train['ExitDate'])  # Tarikhe Harkat be miladi
            if train['TrainNumber'] not in blockedTrains and 3 <= train['Counting'] and departure.day <= 18:
                print(train['ShamsiMoveDate'], train['TrainNumber'], "CompartmentCapicity=",
                      train['CompartmentCapicity'], "Free=", int(train['Counting']))
                notification.notify(
                    title="Raja Checker",
                    message=train['ShamsiMoveDate'] + " " + train['ExitTime'] + ", " + str(train['TrainNumber']),
                    timeout=100
                )
                os.system('say "Qataar payda shud."')
    time.sleep(30)
