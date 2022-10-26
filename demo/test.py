from kochat.data import Dataset
from kochat.proc import GensimEmbedder
from kochat.model import embed


dataset = Dataset(ood=True)

# 프로세서 생성
emb = GensimEmbedder(
    model=embed.FastText()
)

# 모델 학습
emb.fit(dataset.load_embed())

# 모델 추론 (임베딩)
user_input = emb.predict("서울 홍대 맛집 알려줘")
