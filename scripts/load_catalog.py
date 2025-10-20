"""
Load and explore the Baker+2025d quiescent galaxy catalog

This script demonstrates how to load the main catalog and perform
basic exploration of the data.

Requirements:
    - astropy
    - numpy
    - pandas (optional)
"""

from astropy.table import Table
import numpy as np
import os


def load_catalog(catalog_path='data/catalogs/main_catalog_v1.0.fits'):
    """
    Load the main galaxy catalog
    
    Parameters
    ----------
    catalog_path : str
        Path to the catalog FITS file
        
    Returns
    -------
    catalog : astropy.table.Table
        The galaxy catalog
    """
    if not os.path.exists(catalog_path):
        raise FileNotFoundError(
            f"Catalog not found at {catalog_path}. "
            "Please check the file path or download the data."
        )
    
    catalog = Table.read(catalog_path)
    print(f"Loaded {len(catalog)} galaxies")
    print(f"Available columns: {catalog.colnames}")
    
    return catalog


def catalog_summary(catalog):
    """
    Print summary statistics for the catalog
    
    Parameters
    ----------
    catalog : astropy.table.Table
        The galaxy catalog
    """
    print("\n" + "="*60)
    print("CATALOG SUMMARY")
    print("="*60)
    
    print(f"\nTotal number of galaxies: {len(catalog)}")
    
    # Redshift information
    if 'redshift' in catalog.colnames:
        z = catalog['redshift']
        print(f"\nRedshift range: {np.min(z):.3f} - {np.max(z):.3f}")
        print(f"Median redshift: {np.median(z):.3f}")
    
    # Mass information
    if 'log_stellar_mass' in catalog.colnames:
        log_mass = catalog['log_stellar_mass']
        print(f"\nlog(M*/M☉) range: {np.min(log_mass):.2f} - {np.max(log_mass):.2f}")
        print(f"Median log(M*/M☉): {np.median(log_mass):.2f}")
    
    # Size information
    if 'effective_radius' in catalog.colnames:
        sizes = catalog['effective_radius']
        sizes_clean = sizes[~np.isnan(sizes)]
        print(f"\nEffective radius range: {np.min(sizes_clean):.2f} - {np.max(sizes_clean):.2f} kpc")
        print(f"Median effective radius: {np.median(sizes_clean):.2f} kpc")
    
    # Redshift type breakdown
    if 'redshift_type' in catalog.colnames:
        spec_z = np.sum(catalog['redshift_type'] == 'spec')
        phot_z = np.sum(catalog['redshift_type'] == 'phot')
        print(f"\nSpectroscopic redshifts: {spec_z} ({100*spec_z/len(catalog):.1f}%)")
        print(f"Photometric redshifts: {phot_z} ({100*phot_z/len(catalog):.1f}%)")
    
    print("="*60)


def select_subsample(catalog, z_min=None, z_max=None, 
                     mass_min=None, mass_max=None):
    """
    Select a subsample based on redshift and/or mass cuts
    
    Parameters
    ----------
    catalog : astropy.table.Table
        The galaxy catalog
    z_min, z_max : float, optional
        Redshift range
    mass_min, mass_max : float, optional
        log(M*/M☉) range
        
    Returns
    -------
    subsample : astropy.table.Table
        The selected subsample
    """
    mask = np.ones(len(catalog), dtype=bool)
    
    if z_min is not None and 'redshift' in catalog.colnames:
        mask &= catalog['redshift'] >= z_min
    if z_max is not None and 'redshift' in catalog.colnames:
        mask &= catalog['redshift'] <= z_max
        
    if mass_min is not None and 'log_stellar_mass' in catalog.colnames:
        mask &= catalog['log_stellar_mass'] >= mass_min
    if mass_max is not None and 'log_stellar_mass' in catalog.colnames:
        mask &= catalog['log_stellar_mass'] <= mass_max
    
    subsample = catalog[mask]
    print(f"Selected {len(subsample)} galaxies")
    
    return subsample


def save_to_csv(catalog, output_path):
    """
    Save catalog to CSV format
    
    Parameters
    ----------
    catalog : astropy.table.Table
        The galaxy catalog
    output_path : str
        Path for output CSV file
    """
    catalog.write(output_path, format='csv', overwrite=True)
    print(f"Saved catalog to {output_path}")


def main():
    """
    Example usage of the catalog loading functions
    """
    # Load the catalog
    print("Loading Baker+2025d catalog...")
    catalog = load_catalog()
    
    # Print summary
    catalog_summary(catalog)
    
    # Example: Select low-redshift subsample
    print("\n\nSelecting low-redshift subsample (z < 1.0)...")
    low_z = select_subsample(catalog, z_max=1.0)
    
    # Example: Select massive galaxies
    print("\nSelecting very massive galaxies (log M*/M☉ > 11.0)...")
    massive = select_subsample(catalog, mass_min=11.0)
    
    # Example: Save subsample
    # save_to_csv(low_z, 'low_redshift_subsample.csv')


if __name__ == '__main__':
    main()
