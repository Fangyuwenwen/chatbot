"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1',                             # 選單名稱
    'chatBarText': '測試設備',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 34.4, 'y': 31, 'width': 566, 'height': 787.6},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu2','data':'richmenu=menu2'} 
        },
        {
            'bounds': {'x': 652.6, 'y': 31, 'width':566, 'height': 787.6},     # 選單位置與大小
            'action': {'type': 'message', 'text':'B/S動力站濾油車'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 1270.6, 'y': 31, 'width':566, 'height': 787.6},     # 選單位置與大小
            'action': {'type': 'message', 'text':'吊掛油壓缸'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 794, 'y': 0, 'width': 905, 'height': 255},           # 選單位置與大小
            'action': {'type': 'message', 'text':'伸縮油壓缸'}  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
            'bounds': {'x': 794, 'y': 255, 'width': 905, 'height': 279},           # 選單位置與大小
            'action': {'type': 'message', 'text':'迴旋油壓缸'} 
        },
        {
            'bounds': {'x': 794, 'y': 535, 'width': 905, 'height': 307},           # 選單位置與大小
            'action': {'type': 'message', 'text':'B/E動力站濾油車'}  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
            'bounds': {'x': 1699, 'y': 9, 'width': 801, 'height': 252},           # 選單位置與大小
            'action': {'type': 'message', 'text':'B/E動力站儲水機'}  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
            'bounds': {'x': 1699, 'y': 261, 'width': 801, 'height': 274},           # 選單位置與大小
            'action': {'type': 'message', 'text':'監視系統'}  # 點擊後開啟地圖定位，傳送位置資訊
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu1.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-68a9f2ebf37bf71dedd1b1875058c51d", "image/jpeg", f)"""
"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-68a9f2ebf37bf71dedd1b1875058c51d', 
                        headers=headers)

print(req.text)"""

"""import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu1",
    "richMenuId":"richmenu-68a9f2ebf37bf71dedd1b1875058c51d"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)"""

"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1_1',                             # 選單名稱
    'chatBarText': '測試點',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 25.8, 'y': 25.8, 'width': 791.2, 'height': 791.4},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu3','data':'richmenu=menu3'} 
        },
        {
            'bounds': {'x': 854.4, 'y': 25.8, 'width':791.2, 'height': 791.4},     # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu4','data':'richmenu=menu4'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 1686.6, 'y': 25.8, 'width':791.2, 'height': 791.4},     # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu5','data':'richmenu=menu5'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 25.8, 'y':868.8, 'width': 791.2, 'height': 781.1},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu6','data':'richmenu=menu6'}  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
            'bounds': {'x': 854.4, 'y': 868.8, 'width': 791.2, 'height': 787.1},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu7','data':'richmenu=menu7'} 
        },
        {
            'bounds': {'x': 1682.6, 'y': 868.8, 'width': 791.2, 'height': 787.1},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu1','data':'richmenu=menu1'} 
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu2.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-762649377738e444ac83a2620432e83e", "image/jpeg", f)"""
"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-762649377738e444ac83a2620432e83e', 
                        headers=headers)

print(req.text)"""

"""import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu2",
    "richMenuId":"richmenu-762649377738e444ac83a2620432e83e"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)"""

"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1_2',                             # 選單名稱
    'chatBarText': '工作項目',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 25.8, 'y': 25.8, 'width':1198.4, 'height': 520.4},           # 選單位置與大小
            'action': {'type': 'message', 'text':'含水度'} 
        },
        {
            'bounds': {'x': 1275.8, 'y': 25.8, 'width':1198.4, 'height': 508.7},     # 選單位置與大小
            'action': {'type': 'message', 'text':'油質老化度'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 25.8, 'y': 580.6, 'width':1198.4, 'height': 550.9},     # 選單位置與大小
            'action': {'type': 'message', 'text':'油質檢測'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 1271.5, 'y':580.3, 'width': 1198.4, 'height': 550.9},           # 選單位置與大小
            'action': {'type': 'message', 'text':'油溫檢查'}  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
            'bounds': {'x': 25.8, 'y': 1182.5, 'width': 2444.1, 'height': 488.8},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu2','data':'richmenu=menu2'} 
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu3.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-baabd8c9ae001e1aa1f4b800caad734b", "image/jpeg", f)"""

"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-baabd8c9ae001e1aa1f4b800caad734b', 
                        headers=headers)

print(req.text)"""

"""import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu3",
    "richMenuId":"richmenu-baabd8c9ae001e1aa1f4b800caad734b"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)"""

"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1_3',                             # 選單名稱
    'chatBarText': '工作項目',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 29.4, 'y': 31, 'width':578.9, 'height': 1628.4},           # 選單位置與大小
            'action': {'type': 'message', 'text':'出口壓力'} 
        },
        {
            'bounds': {'x': 650.9, 'y': 28.8, 'width':570.3, 'height': 1628.4},     # 選單位置與大小
            'action': {'type': 'message', 'text':'出口流量'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 1273.2, 'y': 28.8, 'width':574.6, 'height': 1628.4},     # 選單位置與大小
            'action': {'type': 'message', 'text':'目視檢查'}               # 點擊後傳送文字
        },
        {
            'bounds': {'x': 1899.8, 'y': 28.8, 'width': 574.6, 'height':1628.4},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu2','data':'richmenu=menu2'} 
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu4.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-204eb0b6c9ba174b2d7b180a7ee5c131", "image/jpeg", f)"""
"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-204eb0b6c9ba174b2d7b180a7ee5c131', 
                        headers=headers)

print(req.text)"""

"""import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu4",
    "richMenuId":"richmenu-204eb0b6c9ba174b2d7b180a7ee5c131"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)"""

"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1_4',                             # 選單名稱
    'chatBarText': '工作項目',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 38.7, 'y': 34.4, 'width':1185.8, 'height': 1621.5},           # 選單位置與大小
            'action': {'type': 'message', 'text':'目視檢查'} 
        },
        {
            'bounds': {'x': 1288.7, 'y': 34.4, 'width': 1179.6, 'height': 1621.5},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu2','data':'richmenu=menu2'} 
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu5.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-daacfa9077285e655f58182a7ba1b9c2", "image/jpeg", f)"""
"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-daacfa9077285e655f58182a7ba1b9c2', 
                        headers=headers)

print(req.text)"""

"""import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu5",
    "richMenuId":"richmenu-daacfa9077285e655f58182a7ba1b9c2"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)"""

"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1_5',                             # 選單名稱
    'chatBarText': '工作項目',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 38.7, 'y': 34.4, 'width':1185.8, 'height': 1621.5},           # 選單位置與大小
            'action': {'type': 'message', 'text':'目視檢查'} 
        },
        {
            'bounds': {'x': 1288.7, 'y': 34.4, 'width': 1179.6, 'height': 1621.5},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu2','data':'richmenu=menu2'} 
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu5.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-94b32b1771dde148b10a5075745ed414", "image/jpeg", f)"""
"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-94b32b1771dde148b10a5075745ed414', 
                        headers=headers)

print(req.text)"""

"""import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu6",
    "richMenuId":"richmenu-94b32b1771dde148b10a5075745ed414"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)"""

"""import requests
import json

# 設定 headers，輸入你的 Access Token，記得前方要加上「Bearer 」( 有一個空白 )
headers = {'Authorization':'Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1686},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'menu1_6',                             # 選單名稱
    'chatBarText': '工作項目',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
            'bounds': {'x': 38.7, 'y': 34.4, 'width':1185.8, 'height': 1621.5},           # 選單位置與大小
            'action': {'type': 'message', 'text':'目視檢查'} 
        },
        {
            'bounds': {'x': 1288.7, 'y': 34.4, 'width': 1179.6, 'height': 1621.5},           # 選單位置與大小
            'action': {'type': 'richmenuswitch', 'richMenuAliasId':'menu2','data':'richmenu=menu2'} 
        }
    ]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)"""

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=')

with open("menu5.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-5e8e386cecf30f138ea452fceedd3b29", "image/jpeg", f)"""
"""import requests

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-5e8e386cecf30f138ea452fceedd3b29', 
                        headers=headers)

print(req.text)"""

import requests,json

headers = {"Authorization":"Bearer Qq8YVQLr/e7ZOeW6wF7U/ULd070P47a1YmFRVJE4KBjr+e+Xwkv1FkfC0FeZDP+gDlFoZJ2RiiyQXQstjiu7xtT4ckcNFvpg/ZVvQXnzldRJaMsBSAjiuETZ2lBx6AhjJHMDR/eTmVNmRmsaxQI8uQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "richMenuAliasId":"menu7",
    "richMenuId":"richmenu-5e8e386cecf30f138ea452fceedd3b29"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)

"""from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('4kW19F7L5Yt+DKSvppThCuirviV8iyqGcEYrg8aM2NjaDNl4zyA5fsFebqJusjAEb5CLVAD/dC7eDl3m7E64ByD6qOoUB0h+jyFRZkfq5tZ+gBxdd/adTJri+vdiikYKn9J58RLux6L14oElp7BBRwdB04t89/1O/w1cDnyilFU=')

rich_menu_list = line_bot_api.get_rich_menu_list()

for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)
    
line_bot_api.delete_rich_menu('richmenu-9e38a19e8b18429071b22e758501402f')"""