# Data Directory

This directory contains the publicly available data from the Baker+2025d paper on massive quiescent galaxies.

## Directory Structure

### `catalogs/`
Main galaxy catalogs containing fundamental properties:
- Galaxy identifiers and coordinates
- Redshifts and stellar masses
- Basic photometric properties

### `photometry/`
Multi-band photometric measurements:
- Observed magnitudes in various filters
- Photometric uncertainties
- Aperture corrections

### `spectroscopy/`
Spectroscopic data (when available):
- Emission/absorption line measurements
- Spectroscopic redshifts
- Velocity dispersions

### `structural/`
Morphological and structural parameters:
- Effective radii (half-light radii)
- Sérsic indices
- Axis ratios and position angles
- Surface brightness profiles

### `derived/`
Derived physical properties:
- Star formation rates and specific SFRs
- Stellar population ages and metallicities
- Rest-frame colors and magnitudes
- Environmental measurements

## Data Formats

Data files are provided in multiple formats for convenience:

1. **FITS Tables** (`.fits`)
   - Binary format with full numerical precision
   - Recommended for scientific analysis
   - Compatible with astropy, TOPCAT, DS9

2. **CSV Files** (`.csv`)
   - Comma-separated values
   - Human-readable and spreadsheet-compatible
   - Easy import into Python pandas, R

3. **ASCII Tables** (`.dat`, `.txt`)
   - Plain text with column descriptions
   - Universal compatibility

## Data Access Examples

### Python (Astropy)
```python
from astropy.table import Table

# Read FITS table
catalog = Table.read('catalogs/main_catalog.fits')

# Read CSV
import pandas as pd
df = pd.read_csv('catalogs/main_catalog.csv')
```

### TOPCAT
1. Open TOPCAT
2. File → Load Table
3. Select FITS or CSV file
4. Explore interactively with plots and filters

### IDL
```idl
; Read FITS table
catalog = mrdfits('catalogs/main_catalog.fits', 1)
```

## File Naming Convention

Files follow the pattern: `[category]_[description]_[version].ext`

Examples:
- `main_catalog_v1.0.fits` - Main galaxy catalog
- `structural_params_v1.0.csv` - Structural parameters
- `sed_fits_v1.0.dat` - SED fitting results

## Data Quality

- All measurements include uncertainty estimates where applicable
- Quality flags indicate potential issues or contamination
- See individual file headers for detailed column descriptions

## Updates

Data files will be versioned (v1.0, v1.1, etc.) as updates become available.
Check the main README.md for the latest version information.

## Note

If you download data from this repository, please:
1. Cite the Baker+2025d paper
2. Check for the latest version
3. Report any issues via GitHub Issues
