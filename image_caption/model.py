import torch
import torch.nn as nn

class Encoder(nn.Module):
    def __init__(self, embed_size):
        super(Encoder, self).__init__()
        # Define your encoder architecture
        self.embed_size = embed_size
        # For simplicity, assume a basic CNN or something like ResNet
        self.model = torch.nn.Sequential(
            # Example layers
            nn.Conv2d(3, 64, kernel_size=3),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(64 * 224 * 224, embed_size)  # This depends on your image size
        )

    def forward(self, x):
        return self.model(x)

class Decoder(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size):
        super(Decoder, self).__init__()
        # Define your decoder architecture
        self.hidden_size = hidden_size
        self.embed_size = embed_size
        self.vocab_size = vocab_size

        self.lstm = nn.LSTM(embed_size, hidden_size)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        # LSTM and output layer
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out
