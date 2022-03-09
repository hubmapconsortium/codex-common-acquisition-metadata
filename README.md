## Internal standards for acquisition metadata

HuBMAP internal metadata standards that describe microscopy acquisition details 
for imaging spatial proteomics methods CODEX and ImmunoSABER.

### Hints
`ChannelID` must be specified per cycle (i.e. it resets in each cycle).
For example:
```
{"CycleID": 1, "ChannelID": 1}, 
{"CycleID": 1, "ChannelID": 2},
{"CycleID": 1, "ChannelID": 3},
{"CycleID": 2, "ChannelID": 1},
{"CycleID": 2, "ChannelID": 2},
{"CycleID": 2, "ChannelID": 3}
```

Almost all numerical values start from `1`, except for
`ExposureTimeMS, NominalMagnification, ResolutionX, ResolutionY, ResolutionZ, TileOverlapX, TileOverlapY`.

For more information refer to the `experiment_schema.json`.
