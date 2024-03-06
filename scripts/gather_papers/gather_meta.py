import sys
import json
import nltk

location = '/home/anon3/cite_reco_gather/'
out_dir = 'out/'
limit = 100000

topic_names = ['summarization', 'machine translation', 'named entity recognition', 'sentiment analysis']
topic_abbs = ['summ', 'mt', 'ner', 'sa']
look_for_file = 'found_paper_IDs.txt'

metadata_file_prefix = 'metadata_'

def add_to_look_for_file(paper_ID):
  global location, look_for_file
  with open(location + out_dir + look_for_file, 'a+') as f:
    f.write(str(paper_ID) + '\n')
  return

def add_to_topic_metas(meta_record, topic_id):
  global topic_abbs
  with open(location + out_dir + topic_abbs[topic_id] + '.jsonl', 'a+') as f:
    f.write(str(meta_record) + '\n')
  return

def normalize_text(text):
  tokens = nltk.word_tokenize(text.lower())
  return ' '.join(tokens).strip()

def merge_dicts(a, b):
    merged = {**a, **b}
    return merged

def process_paper(paper_meta):
  global topic_names, topic_papers, look_for_list
  display = False
  if not paper_meta['has_pdf_parse']:
    return False

  if not paper_meta['abstract']:
    return False

  abstract_text = normalize_text(paper_meta['abstract'])
  outcome = False

  for index, topic in enumerate(topic_names):
    if topic in abstract_text:
      if display:
        print('Topic:', topic)
        print('Title:', paper_meta['title'])
        print('Normalized Abstract:', abstract_text)
        print()

      add_to_topic_metas(paper_meta, index)

      add_to_look_for_file(paper_meta['paper_id'])

      outcome = True
  return outcome

def is_CS_paper(paper_meta):
  if not paper_meta['mag_field_of_study']:
    return False
  if 'Computer Science' not in paper_meta['mag_field_of_study']:
    return False
  return True

if __name__ == '__main__':
  # Gather papers from the metadata parses
  # Match papers in the PDF parses using their 'paper_id'
  args = sys.argv
  dump_ID = str(args[1]).strip()

  line_count = 0
  successes = 0
  cs_papers = 0

  with open(location + 'temp/' + metadata_file_prefix + dump_ID + '.jsonl') as m:
    while line_count < limit:
      m_line = m.readline()
      if not m_line:
        break

      line_count += 1
      paper_meta = json.loads(m_line)

      if not is_CS_paper(paper_meta):
        continue

      cs_papers += 1

      if process_paper(paper_meta):
        successes += 1

  print('Number of fetches:', successes)
  print('Number of CS papers: ' + str(cs_papers) + '/' + str(line_count))
