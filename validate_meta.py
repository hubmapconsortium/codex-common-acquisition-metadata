import argparse
from pathlib import Path
import json
import jsonschema


def read_json(path: Path):
    with open(path, "r") as s:
        obj = json.load(s)
    return obj


def main(schema_path, meta_path):
    schema = read_json(schema_path)
    meta = read_json(meta_path)
    try:
        jsonschema.validate(meta, schema)
        print("Validated successfully")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", type=Path, help="Path to the metadata schema")
    parser.add_argument("--meta", type=Path, help="Path to the metadata for validation")
    args = parser.parse_args()

    main(args.schema, args.meta)
