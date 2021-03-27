import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', help="dictionary key", type=str)
parser.add_argument('-v', '--val', help="dictionary value", type=str)
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if args.key:
    with open(storage_path, 'r') as f_obj:
        try:
            dictionary = json.load(f_obj)
        except:
            dictionary = {}
    if args.val:
        with open(storage_path, 'w') as f_obj:
            values = dictionary.get(args.key, 'not found')
            if values == 'not found':
                dictionary[args.key] = [args.val]
            else:
                dictionary[args.key] = values + [args.val]
            json.dump(dictionary, f_obj)
            print('value stored')
    else:
        if args.key in dictionary:
            print(', '.join(dictionary[args.key]))
        else:
            print(None)
else:
    print(None)
