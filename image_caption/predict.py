import torch
from torchvision import transforms
from PIL import Image
from .model import Encoder, Decoder

def generate_caption(image_path, encoder_path='encoder.pth', decoder_path='decoder.pth'):
    # Initialize models
    encoder = Encoder(embed_size=256)
    decoder = Decoder(embed_size=256, hidden_size=512, vocab_size=10000)

    # Load pre-trained weights
    encoder.load_state_dict(torch.load(encoder_path))
    decoder.load_state_dict(torch.load(decoder_path))

    # Process the image
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Get features and make prediction
    with torch.no_grad():
        features = encoder(image)  # Extract features using the encoder
        caption_tokens = decoder.greedy_decode(features)  # Get caption tokens from the decoder

    # If tokenizer is available, decode tokens (if needed)
    caption = ' '.join([str(token) for token in caption_tokens])
    return caption
