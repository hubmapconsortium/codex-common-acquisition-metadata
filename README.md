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

#### Description of metadata fields and values

| Field                        | Example value                                                      | Data type                                                                                                                                                    | Description                                                                                                |
|------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Version                      | "1.0"                                                              | string                                                                                                                                                       | Version of this metadata                                                                                   |
| DatasetName                  | "Name"                                                             | string                                                                                                                                                       | Name recognizable by a provider                                                                            |
| AcquisitionDate              | "2020-02-19T13:51:35.857-05:00\[America/New_York\]"                | string                                                                                                                                                       | Date of sample acquisition                                                                                 |
| AssayType                    | "CODEX"                                                            | enum("CODEX", "ImmunoSABER")                                                                                                                                 | The type of assay, choose one                                                                              |
| AssaySpecificSoftware        | "Akoya CODEX Instrument Manager 1.29, Akoya CODEX Processor 1.7.6" | string                                                                                                                                                       | The comma separated list of company, name and version of the assay specific software used for this dataset |
| Microscope                   | "Sony, Nikon, Zeiss"                                               | string                                                                                                                                                       | Details about the microscope manufacturer and the model                                                    |
| AcquisitionMode              | "Confocal"                                                         | enum("Confocal", "WideField", "Lightsheet", "SingleMolecule", "MultiPhoton", "StructuredIllumination", "Spectral", "TotalInternalReflection", "BrightField") | Type of the microscopy method                                                                              |
| ImmersionMedium              | "Air"                                                              | enum("Air", "Water", "Oil", "Glycerin")                                                                                                                      | Type of the objective immersion medium                                                                     |
| NominalMagnification         | 40                                                                 | number > 0.0                                                                                                                                                 | The magnification of the objective as specified by the manufacturer                                        |
| NumericalAperture            | 1.0                                                                | number > 0.1                                                                                                                                                 | The numerical aperture of the objective                                                                    |
| ResolutionX                  | 300.0                                                              | number > 0.0                                                                                                                                                 | Physical size of a pixel                                                                                   |
| ResolutionXUnit              | "nm"                                                               | enum("m", "dm", "cm", "mm", "um", "nm", "pm", "fm")                                                                                                          | The units of the physical size of a pixel                                                                  |
| ResolutionY                  | 300.0                                                              | number > 0.0                                                                                                                                                 | Physical size of a pixel                                                                                   |
| ResolutionYUnit              | "nm"                                                               | enum("m", "dm", "cm", "mm", "um", "nm", "pm", "fm")                                                                                                          | The units of the physical size of a pixel                                                                  |
| ResolutionZ                  | 100.0                                                              | number > 0.0                                                                                                                                                 | Physical size of a pixel                                                                                   |
| ResolutionZUnit              | "nm"                                                               | enum("m", "dm", "cm", "mm", "um", "nm", "pm", "fm")                                                                                                          | The units of the physical size of a pixel                                                                  |
| BitDepth                     | 16                                                                 | integer > 2, multiple of 2                                                                                                                                   | Bits per pixel                                                                                             |
| NumRegions                   | 1                                                                  | integer >= 1                                                                                                                                                 | The number of regions in the dataset                                                                       |
| NumCycles                    | 4                                                                  | integer >= 1                                                                                                                                                 | The number of cycles in the dataset                                                                        |
| NumZPlanes                   | 5                                                                  | integer >= 1                                                                                                                                                 | The number of focal planes captured                                                                        |
| NumChannels                  | 6                                                                  | integer >= 1                                                                                                                                                 | The number of imaging channels captured                                                                    |
| RegionWidth                  | 10                                                                 | integer >= 1                                                                                                                                                 | The number of tiles per region in horizontal direction                                                     |
| RegionHeight                 | 10                                                                 | integer >= 1                                                                                                                                                 | The number of tiles per region in vertical direction                                                       |
| TileWidth                    | 2048                                                               | integer >= 1                                                                                                                                                 | The size of a tile horizontal direction in pixels                                                          |
| TileHeight                   | 2048                                                               | integer >= 1                                                                                                                                                 | The size of a tile vertical direction in pixels                                                            |
| TileOverlapX                 | 0.3                                                                | float >= 0.0                                                                                                                                                 | The horizontal overlap between neighbouring tiles in fractions of one                                      |
| TileOverlapY                 | 0.3                                                                | float >= 0.0                                                                                                                                                 | The vertical overlap between neighbouring tiles in fractions of one                                        |
| TileLayout                   | "Snake"                                                            | enum("Snake", "Grid")                                                                                                                                        | The way tiles are captured by the microscope                                                               |
| NuclearStain                 | \[{"CycleID": 1,"ChannelID": 1}, {"CycleID": 2,"ChannelID": 1}\]   | array\[object\{string: integer > 1\}]                                                                                                                        | A list of cycle and channel ids that capture stained nuclei                                                |
| MembraneStain                | \[{"CycleID": 3,"ChannelID": 4}, {"CycleID": 2,"ChannelID": 3}\]   | array\[object\{string: integer > 1\}]                                                                                                                        | A list of cycle and channel ids that capture stained cell membranes                                        |
| NuclearStainForSegmentation  | {"CycleID": 2,"ChannelID": 1}                                      | object\{string: integer > 1\}                                                                                                                                | The cycle and channel ids that will be used for nuclear segmentation                                       |
| MembraneStainForSegmentation | {"CycleID": 3,"ChannelID": 4}                                      | object\{string: integer > 1\}                                                                                                                                | The cycle and channel ids that will be used for cell segmentation                                          |

### ChannelDetails

| Field                  | Example value | Data type    | Description                                                       |
|------------------------|---------------|--------------|-------------------------------------------------------------------|
| Name                   | "CD31"        | string       | The name of the channel or its target                             |
| ChannelID              | 2             | integer >= 1 | The id of the imaging channel inside the cycle                    |
| CycleID                | 1             | integer >= 1 | The id of the imaging cycle                                       |
| Fluorophore            | "Cy5"         | string       | The name of the fluorophore for this channel                      |
| PassedQC               | true          | boolean      | Check if the channel passed qc                                    |
| QCDetails              | "None"        | string       | Additional details about qc                                       |
| ExposureTimeMS         | 100.0         | float > 0.0  | The length of the exposure in milliseconds                        |
| ExcitationWavelengthNM | 650           | integer >= 1 | The wavelength of light absorption by a fluorophore in nanometers |
| EmissionWavelengthNM   | 660           | integer >= 1 | The wavelength of light emission by a fluorophore in nanometers   |
| Binning                | 1             | integer >= 1 | The number of pixels that are combined during or after detection  |
| Gain                   | 1.0           | number >= 1  | Amplification applied to the detector signal                      |


For more information refer to the `experiment_schema.json`.
