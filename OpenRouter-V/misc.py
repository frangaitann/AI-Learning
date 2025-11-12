import json, faiss
from sentence_transformers import SentenceTransformer

def token_loader(token: str = "GPT"):
    with open("tokens.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                if data.get("model") == token:
                    main_token = data.get("token")
                    return main_token
            except json.JSONDecodeError:
                continue
            



# Our own history reading & embedding cache system (vectorial DDBB)

def chat_cache(user_input):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    try:
        with open("history.txt", "r", encoding="utf-8") as f:   # Made with .txt for being simplier to understand but preferable to use .csv / NoSQL / SQL (Depends if you want to be attached to a timestamp, message-id, etc.)
            data = f.read().splitlines()
    except FileNotFoundError:
        data = []

    if not data:
        return 

    vectors = model.encode(data, convert_to_numpy=True)

    if vectors.ndim == 1:
        vectors = vectors.reshape(1, -1)

    vec_dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(vec_dimension)
    index.add(vectors.astype('float32'))

    prompt_vector = model.encode([user_input]).astype('float32')
    D, I = index.search(prompt_vector, k=min(10, len(data)))

    return [data[idx] for idx in I[0]]