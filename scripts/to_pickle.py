import pickle

IDs = []

with open('found_paper_IDs.txt', 'r+') as f:
    texts = f.read().split('\n')
    for text in texts:
        id = text.strip()
        if id and id != '':
            IDs.append(id)

with open('found_paper_IDs.pkl', 'wb') as f:
    pickle.dump(IDs, f)
