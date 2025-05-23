import json
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

def init():
    global model, tokenizer
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

def run(raw_data):
    data = json.loads(raw_data)
    inputs = tokenizer(data["text"], return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
    return {"positive": scores[0][1].item(), "negative": scores[0][0].item()}