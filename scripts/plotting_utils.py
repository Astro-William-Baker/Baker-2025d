"""
Plotting utilities for the Baker+2025d quiescent galaxy catalog

This module provides functions for creating common plots used in
galaxy evolution studies.

Requirements:
    - matplotlib
    - numpy
    - astropy
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


def setup_plot_style():
    """
    Set up a clean, publication-ready plotting style
    """
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['xtick.major.width'] = 1.5
    plt.rcParams['ytick.major.width'] = 1.5
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.top'] = True
    plt.rcParams['ytick.right'] = True


def plot_mass_size_relation(catalog, z_bins=None, show_errors=False, 
                            output=None):
    """
    Plot the mass-size relation for quiescent galaxies
    
    Parameters
    ----------
    catalog : astropy.table.Table
        Galaxy catalog with log_stellar_mass and effective_radius columns
    z_bins : list of tuples, optional
        Redshift bins for color-coding [(z_min, z_max), ...]
    show_errors : bool
        Whether to show error bars
    output : str, optional
        If provided, save figure to this path
    """
    setup_plot_style()
    
    # Extract data
    mass = catalog['log_stellar_mass']
    size = catalog['effective_radius']
    
    # Remove NaN values
    good = ~(np.isnan(mass) | np.isnan(size))
    mass = mass[good]
    size = size[good]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    if z_bins is None:
        # Single sample
        ax.scatter(mass, np.log10(size), alpha=0.5, s=20, color='darkred')
    else:
        # Color-code by redshift
        z = catalog['redshift'][good]
        colors = plt.cm.viridis(np.linspace(0, 1, len(z_bins)))
        
        for i, (z_min, z_max) in enumerate(z_bins):
            in_bin = (z >= z_min) & (z < z_max)
            ax.scatter(mass[in_bin], np.log10(size[in_bin]), 
                      alpha=0.6, s=20, color=colors[i],
                      label=f'{z_min:.1f} < z < {z_max:.1f}')
        
        ax.legend(loc='upper left', frameon=True, fontsize=10)
    
    # Add reference lines (literature relations)
    mass_ref = np.linspace(10.5, 12.0, 100)
    # Example: van der Wel et al. 2014 relation at z~1
    size_ref = 10**(0.75 * (mass_ref - 11.0) - 0.19)
    ax.plot(mass_ref, np.log10(size_ref), 'k--', alpha=0.5, 
            label='van der Wel+14 (z~1)', linewidth=2)
    
    ax.set_xlabel(r'log(M$_*$/M$_\odot$)', fontsize=14)
    ax.set_ylabel(r'log(R$_e$/kpc)', fontsize=14)
    ax.set_title('Mass-Size Relation', fontsize=16)
    ax.grid(True, alpha=0.3)
    
    if output:
        plt.savefig(output, dpi=300, bbox_inches='tight')
        print(f"Saved figure to {output}")
    else:
        plt.show()
    
    return fig, ax


def plot_UVJ_diagram(catalog, highlight_quiescent=True, output=None):
    """
    Plot the rest-frame UVJ color-color diagram
    
    Parameters
    ----------
    catalog : astropy.table.Table
        Galaxy catalog with rest_U_V and rest_V_J columns
    highlight_quiescent : bool
        Whether to highlight the quiescent region
    output : str, optional
        If provided, save figure to this path
    """
    setup_plot_style()
    
    U_V = catalog['rest_U_V']
    V_J = catalog['rest_V_J']
    
    # Remove NaN values
    good = ~(np.isnan(U_V) | np.isnan(V_J))
    U_V = U_V[good]
    V_J = V_J[good]
    
    fig, ax = plt.subplots(figsize=(8, 7))
    
    # 2D histogram for density
    hist = ax.hist2d(V_J, U_V, bins=50, cmap='Blues', 
                     norm=LogNorm(), cmin=1)
    plt.colorbar(hist[3], ax=ax, label='Number of galaxies')
    
    if highlight_quiescent:
        # Draw quiescent selection box
        VJ = np.array([0.6, 1.6, 1.6, 0.6, 0.6])
        UV = np.array([1.3, 1.3, 2.1, 2.01, 1.3])
        ax.plot(VJ, UV, 'r-', linewidth=2, label='Quiescent region')
        
        # Diagonal line
        VJ_diag = np.linspace(0.6, 1.5, 100)
        UV_diag = 0.88 * VJ_diag + 0.59
        ax.plot(VJ_diag, UV_diag, 'r-', linewidth=2)
    
    ax.set_xlabel('Rest-frame V-J [mag]', fontsize=14)
    ax.set_ylabel('Rest-frame U-V [mag]', fontsize=14)
    ax.set_title('UVJ Color-Color Diagram', fontsize=16)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 2.5)
    ax.legend(loc='upper left', fontsize=12)
    
    if output:
        plt.savefig(output, dpi=300, bbox_inches='tight')
        print(f"Saved figure to {output}")
    else:
        plt.show()
    
    return fig, ax


def plot_redshift_distribution(catalog, bins=30, output=None):
    """
    Plot the redshift distribution of the sample
    
    Parameters
    ----------
    catalog : astropy.table.Table
        Galaxy catalog with redshift column
    bins : int
        Number of histogram bins
    output : str, optional
        If provided, save figure to this path
    """
    setup_plot_style()
    
    z = catalog['redshift']
    z = z[~np.isnan(z)]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.hist(z, bins=bins, color='darkblue', alpha=0.7, edgecolor='black')
    
    ax.set_xlabel('Redshift', fontsize=14)
    ax.set_ylabel('Number of galaxies', fontsize=14)
    ax.set_title('Redshift Distribution', fontsize=16)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add statistics
    ax.text(0.95, 0.95, f'N = {len(z)}\n' +
                        f'Median z = {np.median(z):.2f}\n' +
                        f'Range: {np.min(z):.2f} - {np.max(z):.2f}',
            transform=ax.transAxes, fontsize=12,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    if output:
        plt.savefig(output, dpi=300, bbox_inches='tight')
        print(f"Saved figure to {output}")
    else:
        plt.show()
    
    return fig, ax


def plot_mass_function(catalog, z_min, z_max, bins=15, output=None):
    """
    Plot the stellar mass function
    
    Parameters
    ----------
    catalog : astropy.table.Table
        Galaxy catalog
    z_min, z_max : float
        Redshift range for the mass function
    bins : int or array
        Mass bins
    output : str, optional
        If provided, save figure to this path
    """
    setup_plot_style()
    
    # Select redshift range
    in_z_range = (catalog['redshift'] >= z_min) & (catalog['redshift'] < z_max)
    mass = catalog['log_stellar_mass'][in_z_range]
    mass = mass[~np.isnan(mass)]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Histogram
    counts, bin_edges, _ = ax.hist(mass, bins=bins, color='darkred', 
                                   alpha=0.7, edgecolor='black')
    
    ax.set_xlabel(r'log(M$_*$/M$_\odot$)', fontsize=14)
    ax.set_ylabel('Number of galaxies', fontsize=14)
    ax.set_title(f'Stellar Mass Function ({z_min:.1f} < z < {z_max:.1f})', 
                fontsize=16)
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)
    
    if output:
        plt.savefig(output, dpi=300, bbox_inches='tight')
        print(f"Saved figure to {output}")
    else:
        plt.show()
    
    return fig, ax


def plot_size_evolution(catalog, mass_range=(11.0, 11.5), z_bins=None, 
                        output=None):
    """
    Plot size evolution with redshift at fixed mass
    
    Parameters
    ----------
    catalog : astropy.table.Table
        Galaxy catalog
    mass_range : tuple
        (log_mass_min, log_mass_max) to select
    z_bins : array, optional
        Redshift bin edges for calculating median sizes
    output : str, optional
        If provided, save figure to this path
    """
    setup_plot_style()
    
    # Select mass range
    in_mass = ((catalog['log_stellar_mass'] >= mass_range[0]) & 
               (catalog['log_stellar_mass'] < mass_range[1]))
    
    z = catalog['redshift'][in_mass]
    size = catalog['effective_radius'][in_mass]
    
    good = ~(np.isnan(z) | np.isnan(size))
    z = z[good]
    size = size[good]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Scatter plot
    ax.scatter(z, size, alpha=0.3, s=20, color='darkblue')
    
    # Running median
    if z_bins is not None:
        z_centers = []
        size_medians = []
        size_errs = []
        
        for i in range(len(z_bins)-1):
            in_bin = (z >= z_bins[i]) & (z < z_bins[i+1])
            if np.sum(in_bin) > 3:
                z_centers.append((z_bins[i] + z_bins[i+1]) / 2)
                size_medians.append(np.median(size[in_bin]))
                # 16th-84th percentile range
                size_errs.append(np.std(size[in_bin]) / np.sqrt(np.sum(in_bin)))
        
        ax.errorbar(z_centers, size_medians, yerr=size_errs, 
                   color='red', marker='o', markersize=10, 
                   linewidth=2, capsize=5, label='Median')
    
    ax.set_xlabel('Redshift', fontsize=14)
    ax.set_ylabel(r'R$_e$ [kpc]', fontsize=14)
    ax.set_title(f'Size Evolution ' +
                f'({mass_range[0]:.1f} < log M$_*$/M$_\odot$ < {mass_range[1]:.1f})',
                fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    
    if output:
        plt.savefig(output, dpi=300, bbox_inches='tight')
        print(f"Saved figure to {output}")
    else:
        plt.show()
    
    return fig, ax
