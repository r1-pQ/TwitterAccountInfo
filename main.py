from webhook_edit import webHookEditor
from TwitterAccountInfo import TwitterAccountInfo

webhookUrl = "https://discord.com/api/webhooks/1156245529274097705/moT4XgkvuXq_GM6tIOLB5P07Im5x_htbuJ217D5oNdeXYjrKttdUqTsCu8WQ-Yx9xp2q"

try:
    print("実行中")
    account = TwitterAccountInfo().getAccountInfo("")

except:
    print("こっち実行中")
    try:
        x = input(">>")
        account = TwitterAccountInfo().getAccountInfo(TwitterAccountInfo.getScreenName("XXXX"))
    except:
        webHookEditor().HookEdit(webhook_url=webhookUrl, name="TwitterAccountInfo",
                                 message="時間をおいてもう一度お試しください。")
user_id = account["User Id"]
webHookEditor().HookEdit(webhook_url=webhookUrl, embed=True, name="TwitterAccountInfo",
                         avatar_url="https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png",
                         message=None, title=account["Screen Name"], description=account["Description"], url=f'https://x.com/i/user/{user_id}', footer_icon_url="https://pbs.twimg.com/profile_images/1702366056072052736/1Jm0PaJr_400x400.jpg", image_icon=None,
                         thumbnail=account["icon"], author=f'ID:{account["User Id"]}', author_url=f'https://x.com/i/user/{user_id}',
                         author_icon=account["icon"], fn1="フォロー", fn2="フォロワー", fv1=account["follow"], fv2=account["follower"])
