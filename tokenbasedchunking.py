from typing import List

def chunk_text_tokens(text: str, chunk_size: int, overlap: int, tokenizer) -> List[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    tokens = tokenizer.encode(text)
    n = len(tokens)
    
    chunks = []
    step = chunk_size - overlap

    for start in range(0, n, step):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]

        if not chunk_tokens:
            break
       
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)

        if end >= n:
            break

    return chunks

import tiktoken
enc = tiktoken.get_encoding("cl100k_base")

print(chunk_text_tokens("I love USA and Canada", 2, 1, enc))
#print(chunk_text_tokens("The quick brown fox jumps over the lazy dog", 4, 2, enc))
#print(chunk_text("Hello World", 5, 2))



from typing import List
import tiktoken

def chunk_text_tokens(
    text: str,
    model: str = "text-embedding-3-small",
    max_tokens: int = 200,
    overlap: int = 50
) -> List[str]:
    """
    Splits text into overlapping chunks based on tokens.
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)

    chunks = []
    start = 0

    while start < len(tokens):
        end = start + max_tokens
        chunk_tokens = tokens[start:end]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)

        start += max_tokens - overlap

    return chunks


from openai import OpenAI
client = OpenAI()

def get_embeddings(chunks: List[str]) -> List[List[float]]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunks
    )
    return [item.embedding for item in response.data]


##Hugging face version## 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings_local(chunks: List[str]) -> List[List[float]]:
    return model.encode(chunks, convert_to_numpy=True).tolist()
######



from typing import Dict

def chunk_and_embed_tokens(
    document: str,
    model: str = "text-embedding-3-small",
    max_tokens: int = 200,
    overlap: int = 50
) -> List[Dict]:
    chunks = chunk_text_tokens(document, model, max_tokens, overlap)
    embeddings = get_embeddings(chunks)

    return [
        {"chunk": chunk, "embedding": emb}
        for chunk, emb in zip(chunks, embeddings)
    ]

##
##encoding = tiktoken.encoding_for_model("text-embedding-3-small")
#tiktoken is mapping the model name → a tokenizer behind the scenes.
#For most modern OpenAI models (including embeddings), that mapping resolves to:cl100k_base
###  encoding_for_model("text-embedding-3-small")  ->> resolves to ->>get_encoding("cl100k_base")

##I prefer using encoding_for_model(model) so that tokenization stays aligned with the embedding model. 
##While most current models use cl100k_base, this approach is safer and more maintainable.


