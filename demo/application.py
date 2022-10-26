"""
@auther Hyunwoong
@since 7/1/2020
@see https://github.com/gusdnd852
"""

import sys

sys.path.append('/home/pi/Desktop/kochat-master')
from flask import render_template

from kochat.app import KochatApi
from kochat.data import Dataset
from kochat.loss import CRFLoss, CosFace, CenterLoss, COCOLoss, CrossEntropyLoss
from kochat.model import intent, embed, entity
from kochat.proc import DistanceClassifier, GensimEmbedder, EntityRecognizer, SoftmaxClassifier

from demo.scenario import dust, weather, travel, restaurant, window , PDLC , LED
#from scenario import dust, weather, travel, restaurant
# 에러 나면 이걸로 실행해보세요!


dataset = Dataset(ood=True)
emb = GensimEmbedder(model=embed.FastText())

clf = DistanceClassifier( #의도 분류기 생성 
    model=intent.CNN(dataset.intent_dict),
    loss=CenterLoss(dataset.intent_dict),
)

rcn = EntityRecognizer( #개체명 인식기 생성
    model=entity.LSTM(dataset.entity_dict),
    loss=CRFLoss(dataset.entity_dict)
)

kochat = KochatApi( #딥러닝 챗봇 학습과 빌드 생성
    dataset=dataset,
    embed_processor=(emb, False),
    intent_classifier=(clf, False),
    entity_recognizer=(rcn, False),
    scenarios=[ #아마 특정 패턴을 두는곳같다
        weather, dust, travel, restaurant,window , LED, PDLC # API를 추가하고 여기다가 추가해야함
    ]
)

#ciew 소스 파일과 연결
@kochat.app.route('/')
def index():
    return render_template("index.html")

@kochat.app.route('/login')
def login():
    return render_template("login.html")

@kochat.app.route('/join')
def join():
    return render_template("join.html")

@kochat.app.route('/ppd')
def ppb():
    return render_template("ppd.html")

@kochat.app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")


if __name__ == '__main__':
    kochat.app.template_folder = kochat.root_dir + 'templates'
    kochat.app.static_folder = kochat.root_dir + 'static'
    kochat.app.run(port=8080, host='127.0.0.1')
