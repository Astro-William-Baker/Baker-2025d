# Baker+2025d: Exploring Over 700 Massive Quiescent Galaxies

## Overview

This repository contains the explanation and publicly available data from the Baker+2025d paper investigating massive quiescent galaxies. The study explores structural and physical properties of over 700 massive quiescent galaxies, providing insights into galaxy evolution and the quenching mechanisms that shut down star formation in massive systems.

## Paper Summary

### Scientific Context

Quiescent galaxies are galaxies that have ceased forming new stars, having exhausted or expelled their gas reservoirs. Understanding these "dead" galaxies is crucial for comprehending galaxy evolution, as the mechanisms that quench star formation remain one of the key open questions in modern astrophysics.

### Key Research Questions

1. **What are the structural properties of massive quiescent galaxies?**
   - Size-mass relations
   - Morphological characteristics
   - Density profiles

2. **How do quiescent galaxies evolve over cosmic time?**
   - Redshift evolution
   - Mass assembly histories
   - Environmental dependencies

3. **What mechanisms drive star formation quenching?**
   - Internal processes (AGN feedback, stellar feedback)
   - External processes (environmental quenching, gas stripping)

### Sample Characteristics

The study includes:
- **Sample Size**: Over 700 massive quiescent galaxies
- **Mass Range**: Typically M* > 10^10.5 M☉ (massive galaxies)
- **Selection Criteria**: Quiescent based on rest-frame colors, specific star formation rates, and spectral features
- **Data Sources**: Multi-wavelength photometry and spectroscopy from major surveys

### Main Findings

The paper presents comprehensive analysis of:
- **Structural Parameters**: Effective radii, Sérsic indices, axis ratios
- **Stellar Population Properties**: Ages, metallicities, star formation histories
- **Environmental Context**: Density measurements, cluster membership
- **Evolutionary Trends**: How properties change with redshift and mass

## Data Description

### Data Structure

The publicly available data includes:

#### 1. Galaxy Catalog
- **Galaxy identifiers** (IDs, coordinates)
- **Photometric properties** (magnitudes, colors)
- **Structural parameters** (sizes, morphologies)
- **Stellar masses** and associated uncertainties
- **Redshifts** (photometric and/or spectroscopic)

#### 2. Derived Properties
- **Star formation rates** (SFR) and specific SFRs
- **Stellar population ages** and metallicities
- **Rest-frame colors** and spectral indices
- **Environmental measurements** (local densities, nearest neighbor distances)

### Data Format

Data files are provided in standard astronomical formats:
- **FITS tables** (`.fits`) - Binary tables with full precision
- **CSV files** (`.csv`) - Human-readable comma-separated values
- **ASCII tables** (`.dat`, `.txt`) - Space/tab-delimited text files

### Data Access

The data directory structure:
```
data/
├── catalogs/          # Main galaxy catalogs
├── photometry/        # Multi-band photometric measurements
├── spectroscopy/      # Spectroscopic data (if available)
├── structural/        # Morphological and structural parameters
└── derived/          # Derived physical properties
```

## Usage

### Prerequisites

For working with the data, we recommend:
- **Python 3.7+** with astropy, numpy, pandas, matplotlib
- **TOPCAT** or **DS9** for interactive data exploration
- Basic knowledge of astronomical data formats (FITS, magnitude systems)

### Quick Start

```python
# Example: Reading the main catalog
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt

# Load the catalog
catalog = Table.read('data/catalogs/main_catalog.fits')

# Display basic information
print(f"Number of galaxies: {len(catalog)}")
print(f"Available columns: {catalog.colnames}")

# Example analysis: mass-size relation
masses = catalog['log_stellar_mass']
sizes = catalog['effective_radius']

plt.figure(figsize=(8, 6))
plt.scatter(masses, np.log10(sizes), alpha=0.5, s=10)
plt.xlabel('log(M*/M☉)')
plt.ylabel('log(Re/kpc)')
plt.title('Mass-Size Relation for Quiescent Galaxies')
plt.grid(True, alpha=0.3)
plt.show()
```

## Citation

If you use this data in your research, please cite:

```bibtex
@article{Baker2025d,
    author = {Baker, William and collaborators},
    title = {Exploring Over 700 Massive Quiescent Galaxies},
    journal = {Journal Name},
    year = {2025},
    volume = {XXX},
    pages = {XXX},
    doi = {XXX/XXX}
}
```

## Data Products

### Main Catalog Columns

| Column Name | Unit | Description |
|------------|------|-------------|
| `id` | - | Unique galaxy identifier |
| `ra` | deg | Right Ascension (J2000) |
| `dec` | deg | Declination (J2000) |
| `redshift` | - | Spectroscopic or photometric redshift |
| `log_stellar_mass` | log(M☉) | Logarithmic stellar mass |
| `effective_radius` | kpc | Half-light radius |
| `sersic_n` | - | Sérsic index |
| `axis_ratio` | - | Minor-to-major axis ratio (b/a) |
| `log_sSFR` | log(yr⁻¹) | Logarithmic specific star formation rate |
| `rest_U_V` | mag | Rest-frame U-V color |
| `age` | Gyr | Mass-weighted stellar age |
| `metallicity` | dex | Stellar metallicity [Z/H] |

## Repository Structure

```
Baker-2025d/
├── README.md              # This file
├── data/                  # Data directory (to be populated)
│   ├── catalogs/         # Galaxy catalogs
│   ├── photometry/       # Photometric data
│   ├── structural/       # Structural parameters
│   └── derived/          # Derived properties
├── notebooks/            # Example Jupyter notebooks
│   ├── 01_data_overview.ipynb
│   ├── 02_mass_size_relation.ipynb
│   └── 03_environmental_analysis.ipynb
├── scripts/              # Analysis scripts
│   ├── load_catalog.py
│   └── plotting_utils.py
└── docs/                 # Additional documentation
    ├── data_description.md
    ├── methodology.md
    └── FAQ.md
```

## Contact

For questions about the data or paper:
- **Lead Author**: William Baker
- **Email**: [contact information]
- **GitHub Issues**: Please use the issue tracker for bug reports or data questions

## License

This data is released under [specify license, e.g., Creative Commons Attribution 4.0 International License (CC BY 4.0)].

When using this data, please:
1. Cite the original paper
2. Acknowledge the data source
3. Report any issues or errors you find

## Acknowledgments

This research was based on observations from [surveys/telescopes used], and we acknowledge:
- Funding sources
- Survey teams and data providers
- Computing resources used

## Related Resources

- **Paper Preprint**: [arXiv link]
- **Journal Article**: [DOI link]
- **Related Data Releases**: [Links to complementary datasets]
- **Analysis Code**: [GitHub repository with analysis pipeline]

## Version History

- **v1.0.0** (2025): Initial data release with 700+ quiescent galaxies
- Future updates will include additional derived products and value-added catalogs

## FAQ

### What makes a galaxy "quiescent"?
Quiescent galaxies have low or negligible star formation rates, typically defined as log(sSFR) < -11 yr⁻¹ or by rest-frame color cuts (e.g., U-V > 1.3).

### What redshift range does this sample cover?
The sample spans [specify redshift range, e.g., 0.5 < z < 2.5], covering a significant portion of cosmic time.

### How were stellar masses calculated?
Stellar masses were derived using spectral energy distribution (SED) fitting to multi-band photometry, accounting for different star formation histories and dust attenuation.

### Are there known caveats or selection effects?
Users should be aware of:
- Selection function effects at the boundaries of the mass-redshift plane
- Potential biases from magnitude-limited surveys
- Systematic uncertainties in photometric redshifts (if applicable)

---

**Last Updated**: October 2025