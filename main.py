import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from bs4 import BeautifulSoup
import json
import time

amazon_url = "https://www.amazon.es/gp/product/B00MUSZCJ4/"
discord_webhook_url = ""
monitor_delay = 5400 #Seconds


def check_amazon():
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
    }
    r = s.get(amazon_url, headers=headers)

    if "No disponible." in r.text:
        return False
    else:
        return True


def send_webhook(item_title, item_img):
    webhook = DiscordWebhook(url=discord_webhook_url)
    embed = DiscordEmbed(title="Item Restocked on Amazon",description="["+item_title+"]("+amazon_url+")",color=3436348)
    embed.set_thumbnail(url=item_img)

    
    embed.set_footer(text='Amazon Monitor',icon_url='https://i.imgur.com/2MWqiOd.png')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()



if __name__ == "__main__":
    with requests.Session() as s:
        while True:
            if check_amazon():
                print("Item restocked, getting specifics...")
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
                }
                r = s.get(amazon_url, headers=headers)
                parsed_html = BeautifulSoup(r.text, "lxml")
                try:               
                    pre_item_img = parsed_html.body.find("div", attrs={"id":"imgTagWrapperId"}).find("img")["data-a-dynamic-image"]

                    json_images = json.loads(pre_item_img)

                    item_img = next(iter(json_images))
                except:
                    item_img = None
                    print("Could not find Image reference")
                
                item_title = parsed_html.body.find("span", attrs={"id":"productTitle"}).text
                
                send_webhook(item_title.strip(), item_img)
                break
            print("Sleeping...")
            time.sleep(monitor_delay)
            