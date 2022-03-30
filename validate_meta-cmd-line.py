if __name__ == "__main__":
    import sys
    from pathlib import Path
    import json
    import jsonschema

    path_to_test_schema = Path(sys.argv[1])

    cur_dir = Path().resolve()
    meta_dir = Path("metadata_standard/1.0")
    exp_schema_path = cur_dir / meta_dir / "dataset_schema.json"
    with open(exp_schema_path, "r") as s:
        exp_schema = json.load(s)

    # check if provided path is a directory, if so
    # assume it is the "raw_data" directory of a submission
    if path_to_test_schema.is_dir():
        exp_path = path_to_test_schema / "experiment.json"
    elif path_to_test_schema.suffix.lower() == ".json":
        exp_path = path_to_test_schema
    else:
        ValueError(
            "Could not find a .json file to validate. Please provide"
            " a raw data directory with an experiment.json file"
            " or a file path to the .json file to validate"
        )

    with open(exp_path, "r") as s:
        experiment = json.load(s)

    # res = None if successful
    res = jsonschema.validate(experiment, exp_schema)
    if not res:
        print(
            f'Experimental schema found in file "{str(exp_path)}" validated successfully'
        )
