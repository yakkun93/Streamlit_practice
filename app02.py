from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
import time
import streamlit as st


subscription_key = "b8d6d964989341a2bfe0893b4c769ecd"
endpoint = "https://20221127-yy.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def get_tags(filepath):
    local_image = open(filepath, "rb")
    tags_results = computervision_client.tag_image_in_stream(local_image)
    tags = tags_results.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)
    return tags_name
    
def detect_objects(filepath):
    local_image = open(filepath, "rb")
    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects


st.title("物体検出アプリ")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f"img_tmp/{uploaded_file.name}"
    img.save(img_path)
    objects = detect_objects(img_path)

    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFont.truetype(font="helvetica.ttf", size=50)

        # キャプションのサイズを取得
        text_w, text_h = draw.textsize(caption, font=font)

        draw.rectangle([(x, y), (x + w, y + h)], fill=None, outline="green", width=5)
        draw.rectangle([(x, y), (x + text_w, y + text_h)], fill="green", outline="green", width=5)
        draw.text((x, y), caption, fill="white", font=font)

    st.image(img) 

    st.markdown("**認識されたコンテンツタグ**")
    tags_name = get_tags(img_path)
    st.markdown(", ".join(tags_name))



