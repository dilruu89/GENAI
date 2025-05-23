from data_prep import create_train_test_split
from train_model import train_model
from eval_model import eval_model
import torch


def main():
    train_dataloader, validation_dataloader = create_train_test_split()
    model = train_model(train_dataloader)
    eval_model(model, validation_dataloader)

    

if __name__ == "__main__":
    main()