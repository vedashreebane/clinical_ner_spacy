import torch, spacy
print("Torch CUDA available?", torch.cuda.is_available())
print("spaCy prefers GPU?", spacy.prefer_gpu())

#Torch CUDA available? True
#spaCy prefers GPU? True