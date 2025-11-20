# Fixed Feature Selection Code
# Copy this into your notebook cell to replace the broken code

# Feature Selection using Mutual Information
import re

if not os.path.exists("data_out/esc50_features_selected.csv"):
    print("Creating selected features...")
    df_raw = pd.read_csv("data_out/esc50_features_raw.csv")
    # Use regex to match only numeric feature columns (f0, f1, f2, etc.), not "filename"
    feature_cols = [c for c in df_raw.columns if re.fullmatch(r'f\d+', c)]
    feature_cols = sorted(feature_cols, key=lambda x: int(x[1:]))  # Sort by number
    
    X = df_raw[feature_cols].values.astype(np.float32)  # Convert to numpy array and ensure float
    y = df_raw['target'].values.astype(int)
    
    print(f"Computing mutual information for {len(feature_cols)} features...")
    mi = mutual_info_classif(X, y, random_state=42)
    mi_series = pd.Series(mi, index=feature_cols).sort_values(ascending=False)
    top_features = mi_series.head(100).index.tolist()

    df_selected = df_raw[['filename', 'target', 'label', 'fold'] + top_features]
    df_selected.to_csv("data_out/esc50_features_selected.csv", index=False)
    print(f"Saved selected feature file: {df_selected.shape}")
    print(f"Top 10 features by MI: {top_features[:10]}")
else:
    print("Selected features already exist.")

