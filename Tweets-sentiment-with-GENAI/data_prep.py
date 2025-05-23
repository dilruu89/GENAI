import pandas as pd
import re
from transformers import BertTokenizer
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset, RandomSampler, SequentialSampler
import numpy as np


def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'#\w+', '', text)     # Remove hashtags
    text = re.sub(r'\s+', ' ', text)     # Remove extra whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text.strip()


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def tokenize_text(text):
    return tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors='pt'
    )


def preprocessed_df():
    # Load the CSV file
    df = pd.read_csv('./data/tweets.csv')
    df['cleaned_text'] = df['text'].apply(clean_text)
    df['tokens'] = df['cleaned_text'].apply(tokenize_text)

    print(df['cleaned_text'].head())
    return df


def create_train_test_split():

    df=preprocessed_df()

    # Prepare input tensors
    input_ids = torch.cat([item['input_ids'] for item in df['tokens']], dim=0)
    attention_masks = torch.cat([item['attention_mask'] for item in df['tokens']], dim=0)

    # Assuming 'sentiment' column contains the labels
    # For demonstration, let's create a dummy sentiment column
    df['sentiment'] = np.random.randint(0, 2, df.shape[0])
    labels = torch.tensor(df['sentiment'].values, dtype=torch.long)


    # Split the data into training and validation sets
    train_inputs, validation_inputs, train_labels, validation_labels = train_test_split(input_ids, labels, test_size=0.1)
    train_masks, validation_masks = train_test_split(attention_masks, test_size=0.1)

    # Create DataLoader for training
    train_dataset = TensorDataset(train_inputs, train_masks, train_labels)
    train_dataloader = DataLoader(train_dataset, sampler=RandomSampler(train_dataset), batch_size=32)

    # Create DataLoader for validation
    validation_dataset = TensorDataset(validation_inputs, validation_masks, validation_labels)
    validation_dataloader = DataLoader(validation_dataset, sampler=SequentialSampler(validation_dataset), batch_size=32)

    return train_dataloader, validation_dataloader

