from kochat.data import Dataset
from kochat.proc import SoftmaxClassifier
from kochat.model import intent
from kochat.loss import CrossEntropyLoss
from kochat.data import Dataset
from kochat.proc import GensimEmbedder
from kochat.model import embed
from kochat.data import Dataset
from kochat.proc import DistanceClassifier
from kochat.model import intent
from kochat.loss import CenterLoss



from kochat.data import Dataset
from kochat.proc import GensimEmbedder
from kochat.model import embed
from kochat.data import Dataset
from kochat.proc import EntityRecognizer
from kochat.model import entity
from kochat.loss import CRFLoss


dataset = Dataset(ood=True)

# 프로세서 생성
emb = GensimEmbedder(
    model=embed.FastText()
)

# 모델 학습
emb.fit(dataset.load_embed())

# 모델 추론 (임베딩)
#user_input = emb.predict("서울 홍대 맛집 알려줘")


# 프로세서 생성
clf = DistanceClassifier(
    model=intent.CNN(dataset.intent_dict),
    loss=CenterLoss(dataset.intent_dict)
)

# 되도록이면 DistanceClassifier는 Margin 기반의 Loss 함수를 이용해주세요
# 현재는 CenterLoss, COCOLo+ss, Cosface, GausianMixture 등의
# 거리기반 Metric Learning 전용 Loss함수를 지원합니다.


# 모델 학습
clf.fit(dataset.load_intent(emb))
clf.predict(dataset.load_predict("환기좀 시켜", emb))
#    model=entity.LSTM(dataset.intent_dict),
 #   loss=CRFLoss(dataset.intent_dict)
# Conditional Random Field를 Loss함수로 지원합니다.
#)

# 모델 학습
#rcn.fit(dataset.load_entity(emb))

# 모델 추론 (엔티티 검출)
#rcn.predict(dataset.load_predict("창문 좀 열어줄래", emb))