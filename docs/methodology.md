# Methodology

## Overview

This document describes the methodology used in the Baker+2025d study to identify, characterize, and analyze over 700 massive quiescent galaxies.

## Sample Selection

### 1. Parent Sample

The parent sample was drawn from:
- Large multi-wavelength surveys (e.g., COSMOS, CANDELS, UltraVISTA, etc.)
- Deep imaging from space-based (HST, Spitzer, etc.) and ground-based telescopes
- Spectroscopic follow-up campaigns when available

**Selection Area**: [XXX square degrees]
**Redshift Range**: z ~ 0.5 to z ~ 2.5 (covering ~7 Gyr of cosmic time)

### 2. Quiescence Criteria

Galaxies were classified as quiescent using multiple complementary methods:

#### Rest-Frame Color Selection
- **UVJ Diagram**: Selection in rest-frame U-V vs. V-J color space
  - U-V > 1.3
  - V-J < 1.6
  - U-V > 0.88 × (V-J) + 0.59
  
#### Specific Star Formation Rate
- log(sSFR) < -11.0 yr⁻¹
- Derived from SED fitting with various SFR indicators

#### Visual Inspection
- Morphological confirmation of early-type morphology
- Elimination of edge-on dusty spirals
- Removal of obviously contaminated sources

### 3. Mass Selection

**Mass Threshold**: log(M*/M☉) > 10.5
- Ensures sample is above mass completeness limit across redshift range
- Focuses on most massive systems where quenching is well-established

## Photometry

### Multi-Band Photometry

Photometric measurements were obtained in the following bands:
- **UV**: GALEX NUV, FUV
- **Optical**: u, g, r, i, z (various surveys)
- **Near-IR**: Y, J, H, K, Ks
- **Mid-IR**: Spitzer IRAC 3.6, 4.5, 5.8, 8.0 μm
- **Far-IR**: Herschel PACS/SPIRE (for stacking analyses)

### Photometric Procedure

1. **Image Preprocessing**
   - Astrometric alignment to Gaia reference frame
   - PSF matching to common resolution
   - Background subtraction

2. **Source Detection**
   - Multi-band detection using SExtractor
   - Detection thresholds: 1.5σ in at least 3 connected pixels

3. **Flux Measurement**
   - Fixed aperture photometry (multiple apertures)
   - Total flux extrapolation using growth curves
   - PSF-matched apertures for color measurements

4. **Calibration**
   - Zero-point corrections
   - Galactic extinction correction (Schlegel et al. 1998)
   - Aperture corrections

## Redshift Determination

### Photometric Redshifts
- **Code Used**: EAZY, BPZ, or similar
- **Template Set**: Extended set including red galaxies
- **Priors**: Magnitude-dependent priors from spectroscopic training set
- **Accuracy**: σ_NMAD ~ 0.02-0.03 for photo-z

### Spectroscopic Redshifts
When available from:
- Large spectroscopic surveys (SDSS, BOSS, VIPERS, etc.)
- Targeted campaigns (VLT, Keck, Gemini)
- **Preference**: Spectroscopic redshifts used when available and reliable

## Stellar Mass Estimation

### SED Fitting Approach

**Software**: FAST, CIGALE, Prospector, or similar

**Free Parameters**:
- Stellar mass (M*)
- Star formation history (τ model, delayed-τ, or non-parametric)
- Age
- Metallicity
- Dust attenuation (E(B-V))

**Fixed Assumptions**:
- **IMF**: Chabrier (2003) or Kroupa (2001)
- **Stellar Population Synthesis**: BC03, FSPS, BPASS, or similar
- **Dust Law**: Calzetti et al. (2000) or Cardelli et al. (1989)

**Methodology**:
1. χ² minimization or Bayesian parameter estimation
2. Marginalization over nuisance parameters
3. Uncertainty estimation from MCMC chains or likelihood surface

### Systematic Uncertainties

Typical systematic uncertainties in log(M*):
- IMF choice: ±0.2 dex
- SFH assumptions: ±0.1 dex
- Dust law: ±0.05 dex
- **Combined**: ~0.2-0.3 dex systematic + statistical uncertainties

## Structural Analysis

### Morphological Measurements

**Software**: GALFIT, PyMorph, Galapagos, or similar

**Model Fitting**:
1. **Single Sérsic Profile**:
   - I(r) = I_e × exp{-b_n[(r/R_e)^(1/n) - 1]}
   - Free parameters: I_e, R_e, n, q (axis ratio), PA

2. **Multi-Component Models** (when needed):
   - Bulge + disk decomposition
   - Nuclear point source for AGN

**Procedure**:
1. Sky background modeling and subtraction
2. Masking of contaminating sources
3. PSF convolution during fitting
4. Multiple initial conditions to avoid local minima
5. Visual inspection of fits

### Measured Parameters

- **Effective Radius (R_e)**: Half-light radius
- **Sérsic Index (n)**: Concentration parameter
- **Axis Ratio (b/a)**: Ellipticity indicator
- **Position Angle (PA)**: Orientation

### Resolution Corrections

- All sizes corrected to rest-frame optical wavelengths
- PSF deconvolution when necessary
- Size evolution cosmological corrections applied

## Star Formation Rates

### SFR Indicators

Multiple SFR indicators were used when available:

1. **UV Luminosity** (dust-corrected)
   - L_UV → SFR with Kennicutt (1998) calibration
   - Dust correction from SED fitting

2. **IR Luminosity**
   - Stacking in far-IR for ensemble SFR
   - Individual detections when available

3. **SED Fitting**
   - Recent star formation component
   - Averaged over past 100 Myr

### Specific SFR

sSFR = SFR / M*
- Primary quiescence indicator
- Measures star formation efficiency relative to mass

## Stellar Population Properties

### Age and Metallicity

**Derived from**:
- Full SED fitting including rest-frame optical
- Spectral indices (Dn4000, H-δ_A) when spectra available
- Rest-frame colors as age proxies

**Caveats**:
- Age-metallicity degeneracy in integrated light
- Mass-weighted vs. light-weighted quantities
- Assumes single-age, single-metallicity (SSP equivalent)

## Environmental Analysis

### Local Density

**Methods**:
1. **Nth Nearest Neighbor**
   - Distance to Nth closest massive galaxy
   - N = 3, 5, or 10 depending on analysis

2. **Fixed Aperture**
   - Number of galaxies within fixed projected radius
   - Typical aperture: 1-2 Mpc

3. **Voronoi Tessellation**
   - Local density from Voronoi cell area

### Cluster Identification

Cluster membership assigned based on:
- Known cluster catalogs (matched by coordinates)
- Photometric redshift overdensities
- X-ray detected clusters
- Velocity information when available

## Quality Control

### Automated Flags

1. **Photometry**
   - Saturation flags
   - Blending with nearby sources
   - Edge artifacts

2. **SED Fits**
   - Poor χ² values
   - Unusual parameter combinations
   - Large uncertainties

3. **Structural Fits**
   - Failed convergence
   - Unphysical parameters
   - Bad residuals

### Visual Inspection

All galaxies visually inspected for:
- Obvious contamination (stars, artifacts)
- Merger signatures
- Nearby bright sources affecting photometry
- Quality of structural fits

## Statistical Methods

### Completeness Corrections

- Mass function computed with 1/V_max weighting
- Selection function characterization via simulations
- Malmquist bias corrections for magnitude-limited samples

### Uncertainty Propagation

- Bootstrap resampling for derived relations
- Monte Carlo error propagation for complex calculations
- Bayesian hierarchical modeling for population properties

## Software and Tools

### Key Software Packages
- **SExtractor**: Source detection and photometry
- **GALFIT**: Morphological fitting
- **FAST/CIGALE/Prospector**: SED fitting
- **EAZY/BPZ**: Photometric redshifts
- **TOPCAT**: Catalog analysis
- **Python**: Data analysis and visualization
  - astropy, numpy, scipy, pandas
  - matplotlib, seaborn for plotting

## Validation

### Internal Consistency Checks

1. **Redshift Accuracy**: Comparison of photo-z vs. spec-z for subsample
2. **Mass Estimates**: Cross-validation with different SED codes
3. **Structural Parameters**: Comparison with literature values
4. **Quiescence Selection**: Multiple independent quiescence indicators

### Comparison with Literature

Results validated against:
- Published studies at similar redshifts
- Well-studied low-redshift quiescent galaxies
- Expected evolutionary trends

## Limitations and Caveats

Users should be aware of:

1. **Sample Selection**
   - Magnitude limits create redshift-dependent mass limits
   - Color selection may miss rare quiescent populations

2. **Measurement Uncertainties**
   - Systematic errors often dominate at high redshift
   - PSF and resolution effects on structural parameters
   - Model dependencies in SED fitting

3. **Physical Assumptions**
   - IMF universality assumption
   - Single-zone SFH approximation
   - Dust attenuation law uncertainties

## References

### Key Methodological Papers

- Brammer et al. (2009): Rest-frame colors and photometric redshifts
- Whitaker et al. (2011): UVJ quiescence selection
- van der Wel et al. (2014): Structural measurements
- Muzzin et al. (2013): Mass functions and quiescent fractions
- Williams et al. (2009): Stellar mass estimates

## Contact

For methodological questions or clarifications:
- GitHub Issues: Technical questions about data processing
- Email: [contact] for specific methodology inquiries
