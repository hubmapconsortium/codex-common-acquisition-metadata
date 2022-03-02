from pathlib import Path
import json
import jsonschema

cur_dir = Path().resolve()
meta_dir = Path("metadata_standard/1.0")
exp_schema_path = cur_dir / meta_dir / "experiment_schema.json"
with open(exp_schema_path, "r") as s:
    exp_schema = json.load(s)

exp_path = cur_dir / meta_dir / "experiment.json"
with open(exp_path, "r") as s:
    experiment = json.load(s)

# res = None if successful
jsonschema.validate(experiment, exp_schema)
