# Detailed Data Description

## Overview

This document provides detailed descriptions of all data products available from the Baker+2025d study of massive quiescent galaxies.

## Main Catalog

### File Information
- **Filename**: `main_catalog_v1.0.fits`
- **Location**: `data/catalogs/`
- **Format**: FITS binary table
- **Rows**: 700+ galaxies
- **Columns**: ~30+ properties

### Column Descriptions

#### Identifiers and Coordinates

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `id` | int64 | - | Unique galaxy identifier in the catalog |
| `alt_id` | string | - | Alternative identifier from source survey |
| `ra` | float64 | degrees | Right Ascension (J2000.0) |
| `dec` | float64 | degrees | Declination (J2000.0) |
| `ra_err` | float32 | arcsec | Uncertainty in RA (including systematic errors) |
| `dec_err` | float32 | arcsec | Uncertainty in Dec |

#### Redshift Information

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `redshift` | float64 | - | Best available redshift (spec-z if available, else photo-z) |
| `redshift_err` | float64 | - | Uncertainty in redshift |
| `redshift_type` | string | - | Type: 'spec' (spectroscopic) or 'phot' (photometric) |
| `z_quality` | int16 | - | Quality flag: 4=excellent, 3=good, 2=uncertain, 1=poor |

#### Stellar Mass

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `log_stellar_mass` | float64 | log(M☉) | Logarithm of stellar mass |
| `log_stellar_mass_err_low` | float32 | dex | Lower 1σ uncertainty |
| `log_stellar_mass_err_high` | float32 | dex | Upper 1σ uncertainty |
| `mass_method` | string | - | Method used: 'SED_fit', 'stellar_pop', etc. |

#### Star Formation

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `log_SFR` | float64 | log(M☉/yr) | Logarithm of star formation rate |
| `log_SFR_err` | float32 | dex | Uncertainty in log(SFR) |
| `log_sSFR` | float64 | log(yr⁻¹) | Logarithm of specific SFR (SFR/M*) |
| `log_sSFR_err` | float32 | dex | Uncertainty in log(sSFR) |
| `SFR_indicator` | string | - | Primary SFR indicator used |

#### Structural Parameters

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `effective_radius` | float64 | kpc | Circularized half-light radius |
| `effective_radius_err` | float32 | kpc | Uncertainty in Re |
| `effective_radius_arcsec` | float32 | arcsec | Re in angular units |
| `sersic_n` | float64 | - | Sérsic index from profile fitting |
| `sersic_n_err` | float32 | - | Uncertainty in n |
| `axis_ratio` | float64 | - | Minor-to-major axis ratio (b/a) |
| `axis_ratio_err` | float32 | - | Uncertainty in b/a |
| `position_angle` | float32 | degrees | Position angle (N through E) |
| `PA_err` | float32 | degrees | Uncertainty in PA |

#### Photometry - Rest-Frame Colors

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `rest_U_V` | float64 | mag | Rest-frame U-V color |
| `rest_U_V_err` | float32 | mag | Uncertainty in U-V |
| `rest_V_J` | float64 | mag | Rest-frame V-J color |
| `rest_V_J_err` | float32 | mag | Uncertainty in V-J |
| `rest_NUV_r` | float64 | mag | Rest-frame NUV-r color |
| `rest_NUV_r_err` | float32 | mag | Uncertainty in NUV-r |

#### Stellar Populations

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `age_mass_weighted` | float64 | Gyr | Mass-weighted stellar age |
| `age_err` | float32 | Gyr | Uncertainty in age |
| `metallicity` | float64 | dex | Stellar metallicity [Z/H] |
| `metallicity_err` | float32 | dex | Uncertainty in [Z/H] |
| `dust_attenuation_V` | float32 | mag | V-band dust attenuation |

#### Environmental Properties

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `local_density` | float64 | Mpc⁻³ | Local galaxy density (3D or projected) |
| `distance_to_nearest` | float32 | Mpc | Distance to nearest massive neighbor |
| `cluster_member` | boolean | - | Flagged as cluster member (True/False) |
| `cluster_id` | string | - | Cluster identifier if member |

#### Quality Flags

| Column | Type | Unit | Description |
|--------|------|------|-------------|
| `quality_flag` | int16 | - | Overall quality: 0=good, 1=caution, 2=poor |
| `contamination_flag` | boolean | - | Possible contamination (e.g., star, artifact) |
| `notes` | string | - | Additional notes or warnings |

## Structural Parameters File

### File Information
- **Filename**: `structural_parameters_v1.0.fits`
- **Location**: `data/structural/`

Contains detailed morphological information including:
- Multi-band structural parameters
- Surface brightness profiles
- Concentration indices
- Asymmetry and clumpiness metrics

## Photometry Files

### Multi-band Catalogs
Individual files for different photometric surveys/instruments:
- `photometry_HST_v1.0.fits` - HST imaging
- `photometry_ground_v1.0.fits` - Ground-based imaging
- `photometry_JWST_v1.0.fits` - JWST imaging (if available)

Each contains:
- Aperture magnitudes (various radii)
- Total magnitudes
- PSF magnitudes for point sources
- Uncertainties and quality flags

## SED Fitting Results

### File Information
- **Filename**: `sed_fits_v1.0.fits`
- **Location**: `data/derived/`

Contains outputs from spectral energy distribution fitting:
- Best-fit stellar population models
- Derived physical parameters
- χ² values and fit quality metrics
- Template libraries used

## Data Quality Notes

### Systematic Uncertainties

Users should be aware of:

1. **Photometric Redshifts**: Typical accuracy Δz/(1+z) ~ 0.02-0.05, with catastrophic outlier rate < 5%

2. **Stellar Masses**: Systematic uncertainties ~0.1-0.2 dex due to:
   - IMF assumptions
   - Star formation history assumptions
   - Dust attenuation models

3. **Structural Parameters**: Uncertainties depend on:
   - Signal-to-noise ratio
   - Resolution/seeing effects
   - Sky subtraction quality

4. **Ages and Metallicities**: Subject to age-metallicity degeneracy, particularly for old populations

### Selection Function

The sample is subject to:
- **Mass completeness**: Complete above M* ~ 10^10.5 M☉ for z < [upper redshift limit]
- **Color selection**: May miss dusty star-forming galaxies misclassified as quiescent
- **Surface brightness**: Potentially missing very extended, low surface brightness galaxies

## Data Processing

### Photometry
1. Source detection and extraction with SExtractor
2. PSF matching across bands
3. Aperture photometry with local background subtraction
4. Galactic extinction correction using Schlegel et al. (1998) maps

### Structural Fitting
1. GALFIT/Galapagos/PyMorph fitting
2. Single Sérsic or multi-component models
3. PSF convolution for accurate measurements
4. Sigma clipping for robust fits

### SED Fitting
1. Template libraries: BC03, FSPS, or similar
2. Dust attenuation: Calzetti or Cardelli laws
3. Bayesian parameter estimation with MCMC
4. Metallicity and age as free parameters

## References

For methodology details, please refer to:
- Main paper: Baker+2025d
- Structural fitting: [reference]
- SED fitting code: [reference]
- Photometric calibrations: [reference]

## Updates and Versions

**Version 1.0** (2025-10):
- Initial release with 700+ galaxies
- All basic properties included
- Quality flags implemented

Future versions will include:
- Additional derived properties
- Improved measurements with new data
- Extended redshift coverage
