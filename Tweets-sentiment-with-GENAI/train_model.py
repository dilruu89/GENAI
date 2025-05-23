
from transformers import BertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset, RandomSampler, SequentialSampler
from transformers import AdamW



def train_model(train_dataloader):

    # Load pre-trained BERT model
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

    # Training loop
    optimizer = AdamW(model.parameters(), lr=2e-5)

    for epoch in range(4):  # Train for 4 epochs
        model.train()
        for batch in train_dataloader:
            b_input_ids, b_attention_mask, b_labels = batch
            model.zero_grad()
            outputs = model(b_input_ids, attention_mask=b_attention_mask, labels=b_labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()

    return model        