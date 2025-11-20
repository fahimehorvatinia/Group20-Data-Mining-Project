# Report Figures and Tables Guide

This document lists all the figures and tables you need to add to your LaTeX report from your code outputs.

## Required Figures to Add

### 1. Exploratory Data Analysis (Section: Method - EDA)
- **Figure 1**: PCA 2D visualization showing class separability
  - File: From your PCA visualization code (Cell 16 in notebook)
  - Caption: "PCA projection of ESC-50 features showing class distribution (first 2 principal components explain 31.2% and 22.0% variance)"
  - Add to report: After EDA subsection

- **Figure 2**: Top 30 Features by Mutual Information
  - File: From Cell 13 (bar chart of top features)
  - Caption: "Top 30 features selected by Mutual Information for feature selection"
  - Add to report: In Feature Extraction section

### 2. Model Performance Visualizations (Section: Experimental Results)

- **Figure 3**: Model Comparison by Dataset
  - File: `data_out/model_comparison_by_dataset.png` (from your visualization code)
  - Caption: "Test accuracy comparison across all models for Raw, Normalized, and Selected feature sets"
  - Add to report: After Table 1 (traditional results)

- **Figure 4**: Performance Heatmap
  - File: `data_out/performance_heatmap.png`
  - Caption: "Heatmap showing model performance (test accuracy) across different datasets"
  - Add to report: After Figure 3

- **Figure 5**: Learning Curve for Random Forest
  - File: `data_out/plots_yamnet/rf_learning_curve.png` or `data_out/learning_curve_rf.png`
  - Caption: "Learning curve showing training and cross-validation accuracy vs. training set size for Random Forest"
  - Add to report: In Model Interpretability section

- **Figure 6**: OOB Curve for Random Forest
  - File: `data_out/plots_yamnet/rf_oob_curve.png`
  - Caption: "Out-of-bag accuracy vs. number of estimators for Random Forest"
  - Add to report: In Model Interpretability section

- **Figure 7**: Feature Importance Plot
  - File: `data_out/plots_yamnet/rf_feature_importances_top30.png` or `data_out/rf_feature_importance.png`
  - Caption: "Top 30 most important features for Random Forest classifier"
  - Add to report: In Model Interpretability section

- **Figure 8**: Confusion Matrix (Best Model)
  - File: `data_out/plots_yamnet/rf_confmat_test.png` (YAMNet+RF)
  - Caption: "Confusion matrix for YAMNet + Random Forest on test set (best performing model)"
  - Add to report: In Model Interpretability section

- **Figure 9**: MLP Training Curves
  - File: `data_out/plots_yamnet/mlp_training_curves.png`
  - Caption: "Training curves for MLP on YAMNet embeddings showing accuracy and loss over epochs"
  - Add to report: In Transfer Learning Results section

## Tables Already Included

The following tables are already in the LaTeX file - you just need to verify the numbers match your actual results:

1. **Table 1**: Traditional Classifiers Results (Table~\ref{tab:traditional_results})
   - Update with your actual test accuracies from `all_model_results.csv`

2. **Table 2**: Self-Supervised Learning Results (Table~\ref{tab:ssl_results})
   - Update with your actual SSL results

3. **Table 3**: Transfer Learning Comparison (Table~\ref{tab:transfer_results})
   - Already included, verify numbers

## How to Add Figures to LaTeX

For each figure, add this code before the section where you discuss it:

```latex
\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{path/to/figure.png}
\caption{Your caption here}
\label{fig:figure_label}
\end{figure}
```

Then reference it in text: "As shown in Figure~\ref{fig:figure_label}..."

## Additional Recommendations

1. **Class Distribution Bar Chart**: Create a bar chart showing the 50 classes and their sample counts (should be 40 each)
   - Add to EDA section

2. **Confusion Matrix Comparison**: Side-by-side comparison of confusion matrices for:
   - Best traditional model (Random Forest)
   - YAMNet + Random Forest
   - This shows the improvement visually

3. **Feature Importance Comparison**: Compare feature importance between:
   - Traditional features (MFCC, Chroma, etc.)
   - YAMNet embeddings
   - Shows what each approach focuses on

## Code References

Make sure to reference specific code cells or functions in your report where appropriate. For example:
- "Feature extraction is performed using librosa (see extract_features() function, Cell 5)"
- "Hyperparameter tuning results are shown in Table X (tuning code in Cell Y)"

## Final Checklist

Before submitting:
- [ ] All figures are high resolution (300 DPI minimum)
- [ ] All tables have accurate numbers from your results
- [ ] All figures are referenced in the text
- [ ] Figure captions are descriptive
- [ ] Code link is added at the end (GitHub/Colab)
- [ ] Report is exactly 5 pages (including references)
- [ ] All team members' names are correct
- [ ] All citations are in IEEE format

