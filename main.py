import json
import requests
def publish_image():
    #ENTER YOUR ACCESS TOKEN TO GRAPH API HERE
    access_token = "ENTER-ACCESS-TOKEN-HERE"
    ig_user_id = '17841453649235871'
    image_url = 'ENTER-LINK-TO-IMAGE'
    post_url = 'https://graph.facebook.com/v17.0/17841453649235871/media?image_url={}'.format(image_url)
    payload ={
        'image': image_url,
        'caption': "joo jeeeta voi sikandar",
        'access_token': access_token
    }
    r = requests.post(post_url, data=payload)
    y = json.loads(r.text)
    publish_url = 'https://graph.facebook.com/v17.0/17841453649235871/media_publish?creation_id={}'.format(y["id"])
    requests.post(publish_url,data=payload)
    print(y['id'])
    print("Media uploaded successfully")


if __name__ == '__main__':
    publish_image()



