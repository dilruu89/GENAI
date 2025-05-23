from sklearn.model_selection import train_test_split
from transformers import BertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset, RandomSampler, SequentialSampler
from transformers import AdamW
import torch


def eval_model(model, validation_dataloader):

    # Evaluation loop
    model.eval()
    eval_loss = 0
    eval_accuracy = 0
    nb_eval_steps = 0

    for batch in validation_dataloader:
        b_input_ids, b_attention_mask, b_labels = batch
        with torch.no_grad():
            outputs = model(b_input_ids, attention_mask=b_attention_mask, labels=b_labels)
            logits = outputs.logits
            loss = outputs.loss
            eval_loss += loss.item()
            preds = torch.argmax(logits, dim=1).flatten()
            eval_accuracy += (preds == b_labels).cpu().numpy().mean()
            nb_eval_steps += 1

    eval_loss = eval_loss / nb_eval_steps
    eval_accuracy = eval_accuracy / nb_eval_steps

    print(f"Validation Loss: {eval_loss}")
    print(f"Validation Accuracy: {eval_accuracy}")