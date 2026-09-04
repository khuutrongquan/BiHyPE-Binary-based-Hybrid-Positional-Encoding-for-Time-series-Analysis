# BiHyPE: Binary-based Hybrid Positional Encoding for Time-series Analysis

## Abstract

The potential of Transformer architectures for time-series modeling is commonly enhanced through positional representations that enable the model to distinguish tokens according to their temporal positions. Effective positional encoding should capture both absolute token identities and relative positional relationships while remaining adaptive to the underlying data. Motivated by this requirement, we propose **BiHyPE**, a plug-and-play positional encoding module designed to jointly incorporate these complementary forms of positional information. BiHyPE is directly injected into the input embeddings to encode temporal sequential order without requiring modifications to the underlying Transformer architecture. We conduct comprehensive quantitative and qualitative evaluations using eleven Transformer backbones across four primary time-series tasks. Across various backbones, BiHyPE consistently achieves superior performance on MSL, SMAP and SWaT datasets for anomaly detection; ETTm1, Traffic for forecasting; JapaneseVowels and Libras for classification; and Electricity, PM25 and Physio for imputation.

## Methodologies Highlight

- Propose a plug-and-play positional encoding module that uses data-adaptable binary hybrid positional representations to jointly encode absolute token identities and relative positional relationships.

- Evaluate the proposed PE (BiHyPE) using eleven Transformer-based architectures and 15 datasets spanning four fundamental time-series tasks: anomaly detection, forecasting, classification, and imputation. The results demonstrate improvements across most evaluated architectures and datasets.

- Conduct systematic comparisons with alternative positional encodings and provide extended quantitative and qualitative analyses of performance, robustness, and generalizability.

## Description

BiHyPE is a plug-and-play Positional Encoding module introduced to improve Transformer-based architectures in time-series modeling. This module can effectively encode both absolute token identities and relative-aware relationships, tending to distinguish input token while preserving data adaptability.

This repository aggregates detailed links to specific implementations on 11 Transformer-based backbones and some quantitative comparison evaluation. These backbones belong to four fundamental tasks of time-series:

- **Time-series Anomaly Detection (TSAD)**
- **Time-series Forecasting (TSF)**
- **Time-series Classification (TSC)**
- **Time-series Imputation (TSI)**.

For each task, BiHyPE is substituted into the original positional encoding module of the corresponding baseline model, and results are compared against the baseline's original positional encoding as well as other established positional encoding schemes. Notably, the underlying architectures of all Transformer-based baselines remain unchanged.

## Dataset Information (including third-party original source)

All benchmark datasets used in this project are pre-processed and organized by task domain. The detailed reference source of datasets will be provided recently.

| Task Domain                              | Included Datasets                      | Dataset Preprocessor / Origin Paper                                                             | Data Download Link                                                                                                      | Third-Party Link / Code                                                                                                                                                                                                    |
| :--------------------------------------- | :------------------------------------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time-series Anomaly Detection (TSAD)** | • MSL, PSM, SMAP, SMD<br><br>• SWaT    | • Xu et al. (_Anomaly Transformer_, NeurIPS 2021)<br><br>• Yang et al. (_DcDetector_, KDD 2023) | [Google Drive - TSAD Datasets](https://drive.google.com/drive/folders/1PKHJIi2--liygyXCXiGmgj_RBbDtz6DD?usp=drive_link) | • [Anomaly Transformer Drive](https://drive.google.com/drive/folders/1gisthCoE-RrKJ0j3KPV7xiibhHWT9qRm)<br><br>• [DcDetector Drive (SWaT)](https://drive.google.com/drive/folders/1xhcYqh6okRs98QJomFWBKNLw4d1T4Q0w?hl=vi) |
| **Time-series Forecasting (TSF)**        | Weather, ECL, ETTm1, Exchange, Traffic | Wu et al. (_Autoformer_, NeurIPS 2021)                                                          | [TSF Datasets](https://drive.google.com/drive/folders/19A8iSs74MszDLCXE7d9dDVp-Ih5PULj7?usp=drive_link)                 | [Autoformer Drive](https://drive.google.com/drive/folders/1ZOYpTUa82_jCcxIdTmyr0LXQfvaM9vIy)                                                                                                                               |
| **Time-series Classification (TSC)**     | JapaneseVowels, Libras                 | Foumani, Navid Mohammadi, et al. (_ConvTran_) / Liu, Minghao, et al. (_GTN_)                    | [TSC Datasets](https://drive.google.com/drive/folders/1kQXlX2C_Bp9Zy9r5UI1M37umWT4VIpLp?usp=sharing)                    | [ConvTran Drive](https://www.timeseriesclassification.com/aeon-toolkit/Archives/Multivariate2018_ts.zip)                                                                                                                   |
| **Time-series Imputation (TSI)**         | PhysioNet 2012, Electricity, PM25      | Tashiro, Yusuke, et al. (_CSDI_, NeurIPS 2021)                                                  | [TSI Datasets](https://drive.google.com/drive/folders/1fHAQ3iM61IFEkoW1b_aL82qmmN7oldhj?usp=drive_link)                 | [CSDI Github](https://github.com/ermongroup/csdi)                                                                                                                                                                          |

Detailed per-dataset specifications (number of channels, series length, train/test split, etc.) are provided as reference images:

- TSAD: `images/tsad_datasets_detail.jpg`
- TSF: `images/tsf_datasets_detail.jpg`
- TSC: `images/tsc_datasets_detail.jpg`
- TSI: `images/tsi_datasets_detail.jpg`

## Code information

- **BiHyPE Core Implementation:** The proposed positional encoding module is implemented in [`bihype.py`](./bihype.py).

- **Baseline Models:** BiHyPE is integrated into and evaluated against the following baseline architectures, each maintained in its own repository under the BiHyPE organization:

| Task Type         | Task Abbreviation | Baseline Model            | Official Source Code                                                                                      |
| :---------------- | :---------------- | :------------------------ | :-------------------------------------------------------------------------------------------------------- |
| Anomaly Detection | **TSAD**          | Anomaly Transformer       | [BiHyPE/AnomalyTransformer](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsad-anomaly-transformer) |
| Anomaly Detection | **TSAD**          | MEMTO                     | [BiHyPE/MEMTO](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsad-memto)                            |
| Anomaly Detection | **TSAD**          | AnomalyBERT               | [BiHyPE/AnomalyBERT](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsad-anomalybert)                |
| Anomaly Detection | **TSAD**          | RESTAD (R)                | [BiHyPE/RESTAD(R)](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsad-restad)                       |
| Anomaly Detection | **TSAD**          | RESTAD (K)                | [BiHyPE/RESTAD(K)](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsad-restad)                       |
| Forecasting       | **TSF**           | Autoformer                | [BiHyPE/Autoformer](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsf-autoformer-informer-reformer) |
| Forecasting       | **TSF**           | Informer                  | [BiHyPE/Informer](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsf-autoformer-informer-reformer)   |
| Forecasting       | **TSF**           | Reformer                  | [BiHyPE/Reformer](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsf-autoformer-informer-reformer)   |
| Classification    | **TSC**           | ConvTran                  | [BiHyPE/ConvTran](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsc-convtran)                       |
| Classification    | **TSC**           | Gated Transformer Network | [BiHyPE/GTN](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsc-gtn)                                 |
| Imputation        | **TSI**           | CSDI                      | [BiHyPE/CSDI](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsi-csdi)                               |

- Besides comparing against the baseline, we implemented further comparisons, including comparisons with existing positional encodings and non-Transformer-based approaches. These comparisons are implemented in two distinct repositories, as follows

| Task Type                                           | Task Abbreviation | Baseline codebase | Official Source Code                                                                                 |
| --------------------------------------------------- | ----------------- | ----------------- | ---------------------------------------------------------------------------------------------------- |
| Classification (PE Comparison)                      | **TSF**           | ConvTran          | [BiHyPE/PE_Comparison](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsc-convtran)             |
| Anomaly Detection (Transformer vs. Non-Transformer) | **TSAD**          | TranAD            | [BiHyPE/Trans_VS_Non-Trans](https://github.com/BiHyPE-TimeSeriesAnalysis/bihype-tsad-nonTransformer) |

---

## Usage Instructions

1. **Clone the chosen baseline repository** for task you want to run (see the table in [Code Information](#code-information)).
2. **Download the corresponding dataset** from the [Dataset Information](#dataset-information-including-third-party-original-source) links and place it in the designated folder, as specified in the implementation details of the baseline repository.
3. **Detailed implementation**: To ensure rigorous baseline comparison and experimental reproducibility, the code of proposed Positional encoding (BiHyPE) is utilized in the baseline implementation. For reproducing original version, please replace the proposed module by the original one. Otherwise, for reproducing the proposed version, please replace the original module by the proposed one (BiHyPE).
4. **Training/Evaluation**: Due to the extensive evaluations across four fundamental time-series tasks and multiple Transformer baselines, our experiments were conducted using codebase adapters spanning several repositories. Detailed instructions for reproducing the specific setups and configurations for each baseline are documented in the respective README files within their dedicated repositories, as summarized in the table of [Code Information](#code-information).

## Requirements

The specific requirements vary depending on the baseline codebase.

## Experimental Results

### 1. Time-series Anomaly Detection (TSAD)

#### MSL Dataset

<p align="center">
  <img src="images/tsad_msl_results.jpg" alt="TSAD MSL Results" width="90%"/>
</p>

#### PSM Dataset

<p align="center">
  <img src="images/tsad_psm_results.jpg" alt="TSAD PSM Results" width="90%"/>
</p>

#### SMAP Dataset

<p align="center">
  <img src="images/tsad_smap_results.jpg" alt="TSAD SMAP Results" width="90%"/>
</p>

#### SWaT Dataset

<p align="center">
  <img src="images/tsad_swat_results.jpg" alt="TSAD SWaT Results" width="90%"/>
</p>

#### SMD Dataset

<p align="center">
  <img src="images/tsad_smd_results.jpg" alt="TSAD SMD Results" width="90%"/>
</p>

#### Positional Encoding Comparison vs. Non-Transformer Models (MSL)

<p align="center">
  <img src="images/tsad_pe_comparison_non_transformer_msl.jpg" alt="TSAD Positional Encoding Comparison on MSL" width="90%"/>
</p>

#### Positional Encoding Comparison vs. Non-Transformer Models (SMAP)

<p align="center">
  <img src="images/tsad_pe_comparison_non_transformer_smap.jpg" alt="TSAD Positional Encoding Comparison on SMAP" width="90%"/>
</p>

---

### 2. Time-series Forecasting (TSF)

#### Weather Dataset

<p align="center">
  <img src="images/tsf_weather_results.jpg" alt="TSF Weather Results" width="90%"/>
</p>

#### ECL Dataset

<p align="center">
  <img src="images/tsf_ecl_results.jpg" alt="TSF ECL Results" width="90%"/>
</p>

#### ETTm1 Dataset

<p align="center">
  <img src="images/tsf_ettm1_results.jpg" alt="TSF ETT Results" width="90%"/>
</p>

#### Exchange Dataset

<p align="center">
  <img src="images/tsf_exchange_results.jpg" alt="TSF Exchange Rate Results" width="90%"/>
</p>

#### Traffic Dataset

<p align="center">
  <img src="images/tsf_traffic_results.jpg" alt="TSF Traffic Results" width="90%"/>
</p>

---

### 3. Time-series Classification (TSC)

#### 3.1. General Classification Benchmarks

Benchmark performance across 2 classification datasets (**JapaneseVowels** and **Libras**):

<p align="center">
  <img src="images/tsc_benchmark_results.jpg" alt="TSC Benchmark Results" width="90%"/>
</p>

#### 3.2. Comparison with Existing Positional Encoding Scenarios

##### Comparison with tAPE, eRPE, and ConvTran (tAPE + eRPE)

<p align="center">
  <img src="images/tsc_pe_comparison_tape_erpe_convtran.jpg" alt="TSC PE Comparison with tAPE, eRPE, and ConvTran" width="90%"/>
</p>

##### Comparison with LAPE, LRPE, and BiHyPE

<p align="center">
  <img src="images/tsc_pe_comparison_lape_lrpe_bihype.jpg" alt="TSC PE Comparison with LAPE, LRPE, and BiHyPE" width="90%"/>
</p>

### 4. Time-series Imputation (TSI)

Reconstruction performance across 3 imputation datasets (**PhysioNet 2012**, **Electricity**, and **PM25**):

<p align="center">
  <img src="images/tsi_benchmark_results.jpg" alt="TSI Benchmark Results" width="90%"/>
</p>
