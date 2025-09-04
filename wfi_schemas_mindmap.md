# Roman WFI Spectroscopy ASDF Schema Structure

## Overview
This mindmap represents the hierarchical structure of ASDF schemas for the Roman Space Telescope Wide Field Instrument (WFI) spectroscopy data products.

## WFI Spectroscopy Level 4 Data Products
### Level 4 Grism/Prism - 1D Derived Spectrum for each Source
- **Schema ID**: `wfi_spec_individual_1d_level_4`
- **Archive Type**: Placeholder SOC file type
- **Metadata Components**:
  - SSC Basic Schema
  - GDPS observation keywords
    - `ID_OBS`: Observation ID
    - `FILESET_ID`: Dataset ID
      - The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
    - `PROGNUM`: Program number
      - ID number assigned to the proposal
    - `SEGMENT`: Segment number
      - The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
    - `VISNUM`: Visit number
      - Visit number within a program
    - `PROGRAM_COMPLETE`: Program Complete
  - GDPS instrument keywords
    - `optical_element`: WFI Optical Element
      - Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - GDPS calibration keywords
    - `version_cdp_cal_file`: CDP calibration reference file
  - GDPS wavelength keywords
    - `wl_contamination_range`: Wl Contamination Range
    - `wl_reference`: Wl Reference
    - `wl_snr_global_range`: Wl Snr Global Range
    - `unit_flux`: Unit of flux
    - `unit_wl`: Unit of wavelength
    - `phot_filter_cut_off`: Phot Filter Cut Off
  - GDPS pointing keywords
    - `pos_wcs_field_center_ra`: Field Center RA
    - `pos_wcs_field_center_dec`: Field Center Dec
  - G2DP common keywords
    - `version_g2dp_software`: G2DP Software Version
    - `id_g2dp_run`: G2DP Run ID

### Level 4 Grism/Prism - Spectra Location Table
- **Schema ID**: `wfi_spec_location_table_level_4`
- **Archive Type**: Placeholder SOC file type
- **Metadata Components**:
  - SSC Basic Schema
  - GDPS observation keywords
    - `ID_OBS`: Observation ID
    - `FILESET_ID`: Dataset ID
      - The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
    - `PROGNUM`: Program number
      - ID number assigned to the proposal
    - `SEGMENT`: Segment number
      - The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
    - `VISNUM`: Visit number
      - Visit number within a program
    - `PROGRAM_COMPLETE`: Program Complete
  - GDPS instrument keywords
    - `optical_element`: WFI Optical Element
      - Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - GDPS location_table keywords
    - `dither`: Dither
    - `nsrc`: Nsrc
    - `optical_model`: Optical Model
    - `v3yangle`: V3Yangle

### Level 4 Grism/Prism - Catalog
- **Schema ID**: `wfi_spec_catalog_level_4`
- **Archive Type**: Placeholder SOC file type
- **Metadata Components**:
  - SSC Basic Schema
  - GDPS observation keywords
    - `ID_OBS`: Observation ID
    - `FILESET_ID`: Dataset ID
      - The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
    - `PROGNUM`: Program number
      - ID number assigned to the proposal
    - `SEGMENT`: Segment number
      - The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
    - `VISNUM`: Visit number
      - Visit number within a program
    - `PROGRAM_COMPLETE`: Program Complete
  - GDPS instrument keywords
    - `optical_element`: WFI Optical Element
      - Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - GDPS catalog keywords
    - `id_catalog`: Catalog ID

### Level 4 Grism/Prism - 2D Decontaminated Spectra
- **Schema ID**: `wfi_spec_decontaminated_2d_level_4`
- **Archive Type**: Placeholder SOC file type
- **Metadata Components**:
  - SSC Basic Schema
  - GDPS observation keywords
    - `ID_OBS`: Observation ID
    - `FILESET_ID`: Dataset ID
      - The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
    - `PROGNUM`: Program number
      - ID number assigned to the proposal
    - `SEGMENT`: Segment number
      - The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
    - `VISNUM`: Visit number
      - Visit number within a program
    - `PROGRAM_COMPLETE`: Program Complete
  - GDPS instrument keywords
    - `optical_element`: WFI Optical Element
      - Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - GDPS calibration keywords
    - `version_cdp_cal_file`: CDP calibration reference file
  - GDPS wavelength keywords
    - `wl_contamination_range`: Wl Contamination Range
    - `wl_reference`: Wl Reference
    - `wl_snr_global_range`: Wl Snr Global Range
    - `unit_flux`: Unit of flux
    - `unit_wl`: Unit of wavelength
    - `phot_filter_cut_off`: Phot Filter Cut Off
  - GDPS pointing keywords
    - `pos_wcs_field_center_ra`: Field Center RA
    - `pos_wcs_field_center_dec`: Field Center Dec
  - G2DP common keywords
    - `version_g2dp_software`: G2DP Software Version
    - `id_g2dp_run`: G2DP Run ID

### Level 4 Grism/Prism - Data Quality
- **Schema ID**: `wfi_spec_data_quality_level_4`
- **Archive Type**: Placeholder SOC file type
- **Metadata Components**:
  - SSC Basic Schema
  - GDPS observation keywords
    - `ID_OBS`: Observation ID
    - `FILESET_ID`: Dataset ID
      - The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
    - `PROGNUM`: Program number
      - ID number assigned to the proposal
    - `SEGMENT`: Segment number
      - The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
    - `VISNUM`: Visit number
      - Visit number within a program
    - `PROGRAM_COMPLETE`: Program Complete
  - GDPS instrument keywords
    - `optical_element`: WFI Optical Element
      - Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - GDPS catalog keywords
    - `id_catalog`: Catalog ID

### Level 4 Grism/Prism - 1D Combined Spectrum for each Source
- **Schema ID**: `wfi_spec_combined_1d_level_4`
- **Archive Type**: Placeholder SOC file type
- **Metadata Components**:
  - SSC Basic Schema
  - GDPS observation keywords
    - `ID_OBS`: Observation ID
    - `FILESET_ID`: Dataset ID
      - The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
    - `PROGNUM`: Program number
      - ID number assigned to the proposal
    - `SEGMENT`: Segment number
      - The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
    - `VISNUM`: Visit number
      - Visit number within a program
    - `PROGRAM_COMPLETE`: Program Complete
  - GDPS instrument keywords
    - `optical_element`: WFI Optical Element
      - Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - GDPS calibration keywords
    - `version_cdp_cal_file`: CDP calibration reference file
  - GDPS wavelength keywords
    - `wl_contamination_range`: Wl Contamination Range
    - `wl_reference`: Wl Reference
    - `wl_snr_global_range`: Wl Snr Global Range
    - `unit_flux`: Unit of flux
    - `unit_wl`: Unit of wavelength
    - `phot_filter_cut_off`: Phot Filter Cut Off
  - GDPS pointing keywords
    - `pos_wcs_field_center_ra`: Field Center RA
    - `pos_wcs_field_center_dec`: Field Center Dec
  - G2DP common keywords
    - `version_g2dp_software`: G2DP Software Version
    - `id_g2dp_run`: G2DP Run ID

## Keyword Schema Details
### GDPS wavelength keywords
#### Properties:
- **wl_contamination_range** (`string`): Wl Contamination Range
  - Archive: nvarchar(128) → Placeholder.wl_contamination_range
- **wl_reference** (`string`): Wl Reference
  - Archive: float → Placeholder.wl_reference
- **wl_snr_global_range** (`string`): Wl Snr Global Range
  - Archive: nvarchar(128) → Placeholder.wl_snr_global_range
- **unit_flux** (`string`): Unit of flux
  - Archive: nvarchar(16) → Placeholder.unit_flux
- **unit_wl** (`string`): Unit of wavelength
  - Archive: nvarchar(16) → Placeholder.unit_wl
- **phot_filter_cut_off** (`string`): Phot Filter Cut Off
  - Archive: nvarchar(128) → Placeholder.phot_filter_cut_off
#### Required Fields: wl_contamination_range, wl_reference, wl_snr_global_range, unit_flux, unit_wl, phot_filter_cut_off

### GDPS location_table keywords
#### Properties:
- **dither** (`number`): Dither
  - Archive: float → Placeholder.dither
- **nsrc** (`number`): Nsrc
  - Archive: float → Placeholder.nsrc
- **optical_model** (`string`): Optical Model
  - Archive: nvarchar(1024) → Placeholder.optical_model
- **v3yangle** (`number`): V3Yangle
  - Archive: float → Placeholder.v3yangle
#### Required Fields: dither, nsrc, optical_model, v3yangle

### GDPS pointing keywords
#### Properties:
- **pos_wcs_field_center_ra** (`number`): Field Center RA
  - Archive: float → Placeholder.pos_wcs_field_center_ra
- **pos_wcs_field_center_dec** (`number`): Field Center Dec
  - Archive: float → Placeholder.pos_wcs_field_center_dec
#### Required Fields: pos_wcs_field_center_ra, pos_wcs_field_center_dec

### GDPS calibration keywords
#### Properties:
- **version_cdp_cal_file** (`string`): CDP calibration reference file
  - Archive: nvarchar(1024) → Placeholder.version_cdp_cal_file
#### Required Fields: version_cdp_cal_file

### GDPS catalog keywords
#### Properties:
- **id_catalog** (`string`): Catalog ID
  - Archive: nvarchar(128) → Placeholder.id_catalog
#### Required Fields: id_catalog

### G2DP common keywords
#### Properties:
- **version_g2dp_software** (`string`): G2DP Software Version
  - Archive: nvarchar(128) → Placeholder.version_g2dp_software
- **id_g2dp_run** (`string`): G2DP Run ID
  - Archive: nvarchar(128) → Placeholder.id_g2dp_run
#### Required Fields: version_g2dp_software, id_g2dp_run

### GDPS observation keywords
#### Properties:
- **ID_OBS** (`string`): Observation ID
  - Archive: nvarchar(28) → Placeholder.observation_id
- **FILESET_ID** (`string`): Dataset ID
  - Description: The Level 2 WFI dataset ID, e.g., 'r0017001001001001006_0002_wfi16_f087'
  - Archive: nvarchar(28) → Placeholder.fileset_id
- **PROGNUM** (`string`): Program number
  - Description: ID number assigned to the proposal
  - Archive: nvarchar(16) → Placeholder.program
- **SEGMENT** (`string`): Segment number
  - Description: The sequence of activities produced by each iteration of a Segment Plan (Observation Sequence) in a Pass
  - Archive: nvarchar(16) → CGIExposure.segment
- **VISNUM** (`string`): Visit number
  - Description: Visit number within a program
  - Archive: nvarchar(16) → CGIExposure.visit
- **PROGRAM_COMPLETE** (`string`): Program Complete
  - Archive: nvarchar(8) → Placeholder.program_complete
#### Required Fields: ID_OBS, FILESET_ID, PROGNUM, SEGMENT, VISNUM, PROGRAM_COMPLETE

### GDPS instrument keywords
#### Properties:
- **optical_element** (`string`): WFI Optical Element
  - Description: Name of the optical element used to take the science
data ("GRISM" or "PRISM").

  - Archive: nvarchar(20) → Placeholder.optical_element
#### Required Fields: optical_element
