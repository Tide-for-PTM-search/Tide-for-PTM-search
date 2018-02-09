# Tide-for-PTM-search

Accelerating a Cross-correlation Algorithm in Tide using a single GPU

Our method requires GNU C++ compiler (gcc version 4.8.5), and NVIDIA’s CUDA (Compute Unified Device Architecture) version 8.0. 

Our method recommands CentOS 7.
<br>
<br>
<br>
<br>
# SpectrumData
> cat Sample.mzML.bz2aa Sample.mzML.bz2ab > Sample.mzML.bz2 

> bzip2 -d Sample.mzML.bz2

# Database indexing
> ./OurMethod tide-index --missed-cleavages 2 Human_swissProt_v2016.07.fasta index

# Search
> ./OurMethod tide-search --precursor-window 50 -- precursor-window-type ppm --mz-bin-width 0.02 Sample.mzML index


# option
> --precursor-window <float> – Tolerance used for matching peptides to spectra. Peptides must be within +/- 'precursor-window' of the spectrum value. The precursor window units depend upon precursor-window-type. Default = 3.
  
> --precursor-window-type mass|mz|ppm – Specify the units for the window that is used to select peptides around the precursor mass location (mass, mz, ppm). The magnitude of the window is defined by the precursor-window option, and candidate peptides must fall within this window. For the mass window-type, the spectrum precursor m+h value is converted to mass, and the window is defined as that mass +/- precursor-window. If the m+h value is not available, then the mass is calculated from the precursor m/z and provided charge. The peptide mass is computed as the sum of the average amino acid masses plus 18 Da for the terminal OH group. The mz window-type calculates the window as spectrum precursor m/z +/- precursor-window and then converts the resulting m/z range to the peptide mass range using the precursor charge. For the parts-per-million (ppm) window-type, the spectrum mass is calculated as in the mass type. The lower bound of the mass window is then defined as the spectrum mass / (1.0 + (precursor-window / 1000000)) and the upper bound is defined as spectrum mass / (1.0 - (precursor-window / 1000000)). Default = mass.

> --mz-bin-width <float> – Before calculation of the XCorr score, the m/z axes of the observed and theoretical spectra are discretized. This parameter specifies the size of each bin. The exact formula for computing the discretized m/z value is floor((x/mz-bin-width) + 1.0 - mz-bin-offset), where x is the observed m/z value. For low resolution ion trap ms/ms data 1.0005079 and for high resolution ms/ms 0.02 is recommended. Default = 1.0005079.
  
> --num-threads <integer> – 0=poll CPU to set num threads; else specify num threads directly. Default = 0.

<br>
tide-search option detail in http://crux.ms/commands/tide-search.html

tide-index option detail in http://crux.ms/commands/tide-index.html
