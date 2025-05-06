from sentence_transformers import SentenceTransformer
import json

# Загружаем модель один раз при импорте модуля
# sentence-transformers/LaBSE многоязычная модель (с русским языком) 

# sberbank-ai/sbert_large_nlu_ru - специально для русского языка.

model = None

def load_model():
    global model
    if model is None:
        model = SentenceTransformer('sentence-transformers/LaBSE')  

def get_embedding(text: str) -> str:
    load_model()
    if not text:
        return None
    embedding = model.encode(text)
    return json.dumps(embedding.tolist())

