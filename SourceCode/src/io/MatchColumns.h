/*************************************************************************
 * \file MatchColumns.h
 * \brief Just keeps track of column names for match files.
 *************************************************************************/

#ifndef MATCHCOLUMNS_H
#define MATCHCOLUMNS_H

//#define NEW_COLUMNS 1

enum MATCH_COLUMNS_T {
  FILE_COL,
  FILE_IDX_COL,
  SCAN_COL,
  CHARGE_COL,
  SPECTRUM_PRECURSOR_MZ_COL,
  SPECTRUM_NEUTRAL_MASS_COL,
  PEPTIDE_MASS_COL,
  DELTA_CN_COL,
  DELTA_LCN_COL,
  SP_SCORE_COL,
  SP_RANK_COL,
  XCORR_SCORE_COL,
  XCORR_RANK_COL,
  EXACT_PVALUE_COL,
  REFACTORED_SCORE_COL,
  SIDAK_ADJUSTED_COL,  
  EVALUE_COL,
  PVALUE_COL,
  ELUTION_WINDOW_COL,
  DISTINCT_MATCHES_PEPTIDE_COL,
#ifdef NEW_COLUMNS
  WEIBULL_QVALUE_COL,
  WEIBULL_PEPTIDE_QVALUE_COL,      // NEW
  DECOY_XCORR_QVALUE_COL,
  DECOY_XCORR_PEPTIDE_QVALUE_COL,  // NEW
  PERCOLATOR_SCORE_COL,
  PERCOLATOR_RANK_COL,
  PERCOLATOR_QVALUE_COL,
  PERCOLATOR_PEPTIDE_QVALUE_COL,   // NEW
  QRANKER_SCORE_COL,
  QRANKER_QVALUE_COL,
  QRANKER_PEPTIDE_QVALUE_COL,      // NEW
#else
  WEIBULL_QVALUE_COL,
  WEIBULL_PEP_COL,
  DECOY_XCORR_QVALUE_COL,
  DECOY_XCORR_PEP_COL,
  DECOY_EVALUE_QVALUE_COL,
  DECOY_EVALUE_PEP_COL,
  PERCOLATOR_SCORE_COL,
  PERCOLATOR_RANK_COL,
  PERCOLATOR_QVALUE_COL,
  PERCOLATOR_PEP_COL,
  QRANKER_SCORE_COL,
  QRANKER_QVALUE_COL,
  QRANKER_PEP_COL,
  BARISTA_SCORE_COL,
  BARISTA_QVALUE_COL,
#endif
  QVALUE_TDC_COL,
  QVALUE_MIXMAX_COL,
  BY_IONS_MATCHED_COL,
  BY_IONS_TOTAL_COL,
  MATCHES_SPECTRUM_COL,
  DISTINCT_MATCHES_SPECTRUM_COL,
  SEQUENCE_COL,
  MODIFICATIONS_COL,
  CLEAVAGE_TYPE_COL,
  PROTEIN_ID_COL,
  PEPTIDES_COL,
  FLANKING_AA_COL,
  TARGET_DECOY_COL,
  ORIGINAL_TARGET_SEQUENCE_COL,
  ETA_COL,
  BETA_COL,
  SHIFT_COL,
  CORR_COL,
  RAW_SCORE_COL,
  SIN_SCORE_COL,
  NSAF_SCORE_COL,
  DNSAF_SCORE_COL,
  EMPAI_SCORE_COL,
  PARSIMONY_RANK_COL,
  DECOY_MATCHES_SPECTRUM_COL,
  SPEC_ID_COL, // for PinWriter
  LABEL_COL,
  SCAN_NR_COL,
  EXP_MASS_COL,
  CALC_MASS_COL,
  LNR_SP_COL,
  DELT_L_CN_COL,
  DELT_CN_COL,
  XCORR_COL,
  SP_COL,
  ION_FRAC_COL,
  MASS_COL,
  PEP_LEN_COL,
  ENZ_N_COL,
  ENZ_C_COL,
  ENZ_INT_COL,
  LN_NUM_SP_COL,
  DM_COL,
  ABS_DM_COL,
  PEPTIDE_COL,
  PROTEINS_COL,
  XLINK_PRODUCT_TYPE_COL,
  PPM_ERROR_COL,
  XCORR_FIRST_COL,
  XCORR_SECOND_COL,
  PROTEIN_ID_X_COL,
  INDEX_NAME_COL,
  XLINK_TYPE_COL,

  NUMBER_MATCH_COLUMNS,
  INVALID_COL
};

/**
 * Get the name of a given column, by index.
 */
const char* get_column_header(
  int columnIndex
);

int get_column_idx(
  const char* column_name
);

#endif // MATCHCOLUMNS_H
