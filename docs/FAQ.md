# Frequently Asked Questions (FAQ)

## General Questions

### What is the Baker+2025d paper about?

The Baker+2025d paper presents a comprehensive study of over 700 massive quiescent galaxies. These are galaxies that have stopped forming stars and represent a key phase in galaxy evolution. The study examines their structural properties, stellar populations, and environmental contexts to understand how and why massive galaxies become "dead."

### What does "quiescent" mean?

Quiescent galaxies are galaxies that have very low or negligible star formation rates. They have exhausted, expelled, or somehow prevented their gas supply from forming new stars. They are also called "red and dead" galaxies due to their red colors (lack of young blue stars) and absence of ongoing star formation.

### How many galaxies are in the sample?

The sample contains over 700 massive quiescent galaxies spanning a range of redshifts and environments.

## Sample Selection

### What redshift range does the sample cover?

The sample typically spans z ~ 0.5 to z ~ 2.5, covering approximately 7 billion years of cosmic time when many massive galaxies were transitioning from star-forming to quiescent states.

### What is the mass range of galaxies in the sample?

All galaxies have stellar masses above log(M*/M☉) > 10.5, meaning they are at least 3 × 10^10 solar masses. These are considered "massive" galaxies.

### How were quiescent galaxies selected?

Galaxies were selected as quiescent using multiple criteria:
1. **Rest-frame colors**: Position in the UVJ color-color diagram
2. **Specific star formation rates**: log(sSFR) < -11 yr⁻¹
3. **Spectral features**: When spectroscopy is available
4. **Visual inspection**: To remove contaminating sources

### Why focus on massive galaxies?

Massive galaxies are particularly interesting because:
- They were among the first to quench star formation
- They dominate the stellar mass budget in galaxy clusters
- Understanding their formation informs galaxy evolution models
- They are bright enough to study in detail at high redshifts

## Data Products

### What data is publicly available?

The repository provides:
- Main galaxy catalog with positions, redshifts, masses
- Structural parameters (sizes, morphologies)
- Photometric measurements across multiple bands
- Derived properties (ages, metallicities, star formation rates)
- Environmental measurements

### What format is the data in?

Data is provided in multiple formats:
- **FITS tables** (`.fits`) - Best for scientific analysis
- **CSV files** (`.csv`) - Compatible with spreadsheets and pandas
- **ASCII tables** (`.dat`) - Plain text format

### How do I download the data?

You can clone the entire repository:
```bash
git clone https://github.com/Astro-William-Baker/Baker-2025d.git
```

Or download specific files directly from the `data/` directory.

### Is there example code for using the data?

Yes! Check the `notebooks/` directory for Jupyter notebooks demonstrating:
- Loading and exploring the catalog
- Making mass-size plots
- Analyzing environmental trends
- And more...

## Physical Properties

### How were stellar masses calculated?

Stellar masses were derived from spectral energy distribution (SED) fitting to multi-wavelength photometry. This involves:
1. Fitting stellar population models to observed photometry
2. Marginalizing over star formation history, age, metallicity, and dust
3. Assuming a standard IMF (Chabrier 2003 or similar)

Typical uncertainties are ~0.1-0.2 dex statistical, plus ~0.2 dex systematic.

### What is the uncertainty in stellar masses?

- **Statistical**: ~0.1-0.2 dex from SED fitting
- **Systematic**: ~0.2-0.3 dex from IMF, SFH, and dust assumptions
- **Total**: Typically 0.3-0.4 dex when combined

### How were sizes measured?

Effective radii (half-light radii) were measured by fitting Sérsic profiles to high-resolution imaging (typically HST). The process includes:
1. PSF convolution for accurate modeling
2. Masking of contaminating sources
3. Multi-component fitting when necessary
4. Correction to rest-frame optical wavelengths

### What is a Sérsic index?

The Sérsic index (n) describes how centrally concentrated a galaxy's light is:
- n = 0.5-2: Disk-like, exponential profiles
- n = 4: De Vaucouleurs profile, typical of ellipticals
- n > 4: Very concentrated, often in cluster centers
- Higher n = more centrally concentrated

### How accurate are the ages and metallicities?

Ages and metallicities suffer from degeneracies in integrated light spectroscopy:
- **Age-metallicity degeneracy**: Older, metal-poor populations can look similar to younger, metal-rich ones
- Typical uncertainties: ~0.3-0.5 Gyr for ages, ~0.2 dex for metallicities
- More reliable when spectroscopy is available
- Mass-weighted quantities reported

## Redshifts

### Are redshifts spectroscopic or photometric?

Both! The catalog includes:
- **Spectroscopic redshifts** when available (highest quality)
- **Photometric redshifts** for galaxies without spectroscopy
- A flag indicating which type is used

### How accurate are photometric redshifts?

For quiescent galaxies, photometric redshifts are quite reliable:
- Typical accuracy: σ_NMAD ~ 0.02-0.03
- Catastrophic outlier rate: < 5%
- Better accuracy due to strong 4000Å break feature

The `z_quality` flag indicates confidence level.

## Environmental Information

### What environmental measurements are included?

The catalog includes:
- **Local density**: Number of neighbors within fixed radius
- **Distance to nearest neighbor**: To closest massive galaxy
- **Cluster membership**: Boolean flag and cluster ID
- Some galaxies have additional environmental data

### How is local density calculated?

Multiple methods are used:
1. Nth nearest neighbor distances (typically N=3, 5, or 10)
2. Fixed aperture counts (within 1-2 Mpc projected radius)
3. 3D densities when spectroscopy is available

## Using the Data

### What software do I need?

Recommended tools:
- **Python**: astropy, pandas, numpy, matplotlib
- **TOPCAT**: For interactive table exploration
- **DS9/SAOImage**: For viewing FITS images
- Any language that can read FITS or CSV files

### How do I cite this data?

Please cite the main paper:
```
Baker, W. et al. 2025, "Exploring Over 700 Massive Quiescent Galaxies", 
[Journal], [Volume], [Pages]
```

And acknowledge the data release in your methods section.

### Can I use this data for my research?

Yes! The data is publicly released for scientific use. Please:
1. Cite the original paper
2. Acknowledge the data source
3. Report any issues you find
4. Consider reaching out for potential collaboration

### I found an error or problem with the data. What should I do?

Please report it via:
- GitHub Issues (preferred for technical problems)
- Email to the lead author for scientific concerns

Include:
- Galaxy ID(s) affected
- Description of the issue
- Your version of the data

## Scientific Questions

### What causes galaxies to become quiescent?

This is an active area of research! Proposed mechanisms include:
- **AGN feedback**: Supermassive black hole winds heat/expel gas
- **Stellar feedback**: Supernovae and stellar winds
- **Environmental quenching**: Ram pressure stripping in clusters
- **Starvation**: Cutting off fresh gas supply
- **Mergers**: Consumption of gas in starbursts

The relative importance varies with mass, redshift, and environment.

### Do all massive galaxies become quiescent?

At low redshift (z ~ 0), most massive galaxies (M* > 10^11 M☉) are quiescent. However, at higher redshifts, massive star-forming galaxies still exist. Understanding this transition is a key science goal.

### Why are quiescent galaxies red?

Quiescent galaxies are red because:
1. They lack young, hot blue stars (no recent star formation)
2. Their stellar populations are dominated by old, cool red stars
3. This gives them the characteristic red colors in rest-frame optical

### How do quiescent galaxies evolve?

Quiescent galaxies continue to evolve through:
- **Dry mergers**: Mergers without gas, growing in size
- **Minor mergers**: Accretion of smaller satellites
- **Adiabatic expansion**: Puffing up due to mass loss
- **Passive evolution**: Stellar populations aging

This leads to size growth and evolving mass-size relations.

## Technical Questions

### What coordinate system is used?

- **Equatorial**: J2000.0 (ICRS frame)
- **RA/Dec** in decimal degrees
- Astrometry referenced to Gaia when possible

### What magnitude system?

- **AB magnitudes** throughout
- Galactic extinction corrected
- Various apertures available (see documentation)

### What is the angular resolution?

Depends on the imaging source:
- **HST**: ~0.03-0.1" (excellent for morphology)
- **Ground-based**: ~0.5-1.0" (seeing-limited)
- **JWST**: ~0.03-0.1" (excellent in near/mid-IR)

### Are there known issues or caveats?

Yes, users should be aware of:
1. **Selection function**: Sample is not complete at all masses and redshifts
2. **Blending**: Some galaxies may be blended at low resolution
3. **Photo-z uncertainties**: Some catastrophic outliers exist
4. **Systematic uncertainties**: Especially in masses and ages

See the methodology document for details.

## Data Access and Updates

### How often is the data updated?

- **Version 1.0**: Initial release (2025)
- Future updates will include additional measurements, improved calibrations, and potentially expanded samples
- Check the repository for version information

### Can I contribute to this dataset?

If you have complementary data or improved measurements:
1. Open a GitHub Issue describing your contribution
2. Contact the lead author
3. We welcome community contributions with proper attribution

### Is there a data paper?

The main science paper includes data descriptions. Detailed methodology is provided in the `docs/` directory of this repository.

## Getting Help

### Where can I get help?

1. **GitHub Issues**: For data problems, technical questions
2. **Documentation**: Check `docs/` directory
3. **Example notebooks**: See `notebooks/` directory
4. **Email**: Contact information in README

### I have a science question not answered here

Feel free to:
- Open a GitHub Issue for general questions
- Email the authors for specific scientific inquiries
- Cite the paper and proceed with your analysis

## Additional Resources

### Related Papers

Key papers on massive quiescent galaxies:
- van Dokkum et al. (2008): Quiescent galaxies at z~2
- Bezanson et al. (2009): Compact massive galaxies
- Newman et al. (2012): Velocity dispersions
- van der Wel et al. (2014): Structural evolution

### Useful Catalogs and Surveys

- **COSMOS**: Large multi-wavelength survey
- **CANDELS**: Deep HST imaging
- **3D-HST**: Grism spectroscopy
- **UltraVISTA**: Deep near-IR imaging

### Educational Resources

For those new to galaxy evolution:
- Textbook: "Galaxy Formation and Evolution" by Mo, van den Bosch, and White
- Review: Madau & Dickinson (2014) on cosmic star formation history
- Review: Peng et al. (2010) on galaxy bimodality

---

**Last Updated**: October 2025

**Have a question not listed here?** Open a GitHub Issue and we'll add it to the FAQ!
