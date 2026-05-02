from typing import List

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    if chunk_size <= 0:
        raise ValueError("Invalid chunk size. Has to be > 0")
    elif overlap < 0:
        raise ValueError("Overlap has to be > 0")
    elif overlap >= chunk_size:
        raise ValueError("Invalid overlap. Has to be less than chunk size")
    else:
        pass

    words = text.split(" ")
    n = len(words)
    chunks = []
    step = chunk_size - overlap

    for start in range(0, n, step):
        end = start + chunk_size
        chunk_words = words[start:end]

        if not chunk_words:
            break

        #chunks.append(chunk_words)
        chunks.append(" ".join(chunk_words))
        
        if end > n:
            break

    return chunks        

#print(chunk_text("I love USA and Canada", 2, 1))
print(chunk_text("The quick brown fox jumps over the lazy dog", 4, 0))
#print(chunk_text("Hello World", 5, 2))

"""
    def main():
        chunk_text("I love USA", 0, 0)



    if __name__ == "__main__":
        main()
"""