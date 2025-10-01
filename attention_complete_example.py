import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ================================
# COMPLETE ATTENTION IMPLEMENTATION
# ================================

class SelfAttention(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed_dim = embed_dim
        
        # Linear transformations for Q, K, V
        self.W_q = nn.Linear(embed_dim, embed_dim, bias=False)
        self.W_k = nn.Linear(embed_dim, embed_dim, bias=False)  
        self.W_v = nn.Linear(embed_dim, embed_dim, bias=False)
        
    def forward(self, x):
        # x shape: [batch_size, seq_len, embed_dim]
        batch_size, seq_len, embed_dim = x.shape
        
        # Transform input to Q, K, V
        Q = self.W_q(x)  # [batch_size, seq_len, embed_dim]
        K = self.W_k(x)  # [batch_size, seq_len, embed_dim]  
        V = self.W_v(x)  # [batch_size, seq_len, embed_dim]
        
        # Calculate attention scores: Q @ K^T
        scores = torch.matmul(Q, K.transpose(-2, -1))  # [batch_size, seq_len, seq_len]
        
        # Scale by sqrt(embed_dim)
        scores = scores / math.sqrt(embed_dim)
        
        # Apply softmax to get attention weights
        attention_weights = F.softmax(scores, dim=-1)  # [batch_size, seq_len, seq_len]
        
        # Apply attention to values
        output = torch.matmul(attention_weights, V)  # [batch_size, seq_len, embed_dim]
        
        return output, attention_weights

# ================================
# COMPLETE EXAMPLE WITH REAL DATA
# ================================

def main():
    print("=== COMPLETE ATTENTION EXAMPLE ===\n")
    
    # Step 1: Create sample sentence
    sentence = "Tarbo is an AI guru"
    tokens = sentence.lower().split()
    print(f"Sentence: '{sentence}'")
    print(f"Tokens: {tokens}")
    print(f"Number of tokens: {len(tokens)}\n")
    
    # Step 2: Build vocabulary
    unique_tokens = list(set(tokens))
    token_to_idx = {token: idx for idx, token in enumerate(unique_tokens)}
    vocab_size = len(token_to_idx)
    
    print("Vocabulary mapping:")
    for token, idx in token_to_idx.items():
        print(f"  '{token}' -> {idx}")
    print(f"Vocab size: {vocab_size}\n")
    
    # Step 3: Convert tokens to indices
    token_indices = torch.tensor([token_to_idx[token] for token in tokens])
    print(f"Token indices: {token_indices}\n")
    
    # Step 4: Create embeddings
    embed_dim = 8  # Small for easy visualization
    embedding_layer = nn.Embedding(vocab_size, embed_dim)
    
    # Get embeddings for our tokens
    word_embeddings = embedding_layer(token_indices)  # [seq_len, embed_dim]
    word_embeddings = word_embeddings.unsqueeze(0)    # Add batch dim: [1, seq_len, embed_dim]
    
    print(f"Word embeddings shape: {word_embeddings.shape}")
    print("Word embeddings (first 3 dimensions for each word):")
    for i, token in enumerate(tokens):
        print(f"  '{token}': {word_embeddings[0, i, :3].detach().numpy()}")
    print()
    
    # Step 5: Apply self-attention
    attention_layer = SelfAttention(embed_dim)
    
    print("=== BEFORE ATTENTION ===")
    print("All words have independent embeddings (no context)")
    print()
    
    # Apply attention
    contextualized_embeddings, attention_weights = attention_layer(word_embeddings)
    
    print("=== AFTER ATTENTION ===")
    print(f"Contextualized embeddings shape: {contextualized_embeddings.shape}")
    print("Contextualized embeddings (first 3 dimensions for each word):")
    for i, token in enumerate(tokens):
        print(f"  '{token}': {contextualized_embeddings[0, i, :3].detach().numpy()}")
    print()
    
    # Step 6: Show attention weights (who pays attention to whom)
    print("=== ATTENTION WEIGHTS MATRIX ===")
    print("Rows = words asking 'what should I pay attention to?'")
    print("Cols = words being attended to")
    print("Values = attention weights (higher = more attention)")
    print()
    
    weights = attention_weights[0].detach().numpy()  # Remove batch dim
    
    # Print header
    print("        ", end="")
    for token in tokens:
        print(f"{token:>8}", end="")
    print()
    
    # Print attention matrix
    for i, token_from in enumerate(tokens):
        print(f"{token_from:>8}", end="")
        for j, token_to in enumerate(tokens):
            print(f"{weights[i,j]:8.3f}", end="")
        print()
    print()
    
    # Step 7: Interpret results
    print("=== INTERPRETATION ===")
    for i, token in enumerate(tokens):
        max_attention_idx = weights[i].argmax()
        max_attention_token = tokens[max_attention_idx]
        max_attention_value = weights[i, max_attention_idx]
        
        print(f"'{token}' pays most attention to '{max_attention_token}' ({max_attention_value:.3f})")
    
    print("\n=== KEY INSIGHTS ===")
    print("1. Each word's output is a weighted combination of ALL words")
    print("2. Attention weights show which words influence each other")
    print("3. Same input embeddings → different contextualized outputs")
    print("4. This is how words get context-aware representations!")

if __name__ == "__main__":
    main()
