import sys
import json
import pickle

location = '/home/anon3/cite_reco_gather/'

look_for_file = 'found_paper_IDs.pkl'

out_dir = 'parse_out/'
parse_out_file = 'parses.jsonl'
limit = int(1e16)

parse_file_prefix = 'pdf_parses_'

def add_to_parses(paper_parse):
  global location, out_dir, parse_out_file
  with open(location + out_dir + parse_out_file, 'a+') as f:
    f.write(str(paper_parse) + '\n')
  return

if __name__ == '__main__':
    args = sys.argv
    dump_ID = str(args[1]).strip()

    paper_IDs = set()
    with open(location + look_for_file, 'rb') as f:
       paper_IDs = set(pickle.load(f))

    line_count = 0

    with open(location + 'temp/' + parse_file_prefix + dump_ID + '.jsonl', 'r+') as p:
        while line_count < limit:
            p_line = p.readline()
            if not p_line:
                break

            line_count += 1
            paper_parse = json.loads(p_line)

            if str(paper_parse['paper_id']).strip() in paper_IDs:
                add_to_parses(paper_parse)
    
