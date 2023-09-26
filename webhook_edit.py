import json
from urllib.request import Request, urlopen
import datetime


class webHookEditor:
    def HookEdit(self, webhook_url, embed=False, name="TwitterAccountInfo",
                 avatar_url="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6cc3c481a15a141738_icon_clyde_white_RGB.png",
                 message=None, title=None, description=None, url=None, footer_icon_url=None, image_icon=None,
                 thumbnail=None, author=None, author_url=None,
                 author_icon=None, fn1=None, fn2=None, fv1=None, fv2=None):
        dt_now = datetime.datetime.now()
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
        }
        if not embed:
            data = {"username": name,
                    "avatar_url": avatar_url,
                    "content": message}
            request = Request(
                webhook_url,
                data=json.dumps(data).encode(),
                headers=headers,
            )
            with urlopen(request) as res:
                assert res.getcode() == 204
        elif embed:
            data = {"username": name,
                    "avatar_url": avatar_url,
                    # "content": message,

                    "embeds": [
                        {
                            "title": title,
                            "description": description,
                            "url": url,
                            "footer": {
                                "text": dt_now.strftime('%Y年%m月%d日 %H:%M'),
                                "icon_url": footer_icon_url
                            },
                            # "image": {
                            #     "url": image_icon
                            # },
                            "thumbnail": {
                                "url": thumbnail
                            },
                            "author": {
                                "name": author,
                                "url": author_url,
                                "icon_url": author_icon
                            },
                            "fields": [
                                {
                                    "name": fn1,
                                    "value": fv1,
                                    "inline": True
                                },
                                {
                                    "name": fn2,
                                    "value": fv2,
                                    "inline": True
                                }
                            ]
                        }
                    ]
                    }

            request = Request(
                webhook_url,
                data=json.dumps(data).encode(),
                headers=headers,
            )

            with urlopen(request) as res:
                assert res.getcode() == 204

        else:
            print("正しい値を設定してください。[False, True]")

if __name__ == "__main__":
    print("a")