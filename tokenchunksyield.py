def chunk_text_tokens_stream(text: str, chunk_size: int, overlap: int, tokenizer):
    tokens = tokenizer.encode(text)
    step = chunk_size - overlap

    for start in range(0, len(tokens), step):
        chunk_tokens = tokens[start:start + chunk_size]
        if not chunk_tokens:
            break
        yield tokenizer.decode(chunk_tokens)


import tiktoken
enc = tiktoken.get_encoding("cl100k_base")

chunk_text_tokens_stream("The quick brown fox jumps over the lazy dog. I love USA and Canada. Hello World!", 4, 2, enc)