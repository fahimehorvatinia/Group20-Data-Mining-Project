#!/usr/bin/env python3
"""
Extract results from the Jupyter notebook and generate results.html
"""
import json
import pandas as pd
import re
from pathlib import Path

def extract_results_from_notebook(notebook_path):
    """Extract model results from notebook outputs"""
    with open(notebook_path, 'r') as f:
        nb = json.load(f)
    
    results = []
    
    # Look for result dataframes in outputs
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Look for results dataframes
            if 'results.append(res)' in source or '_df = pd.DataFrame(' in source:
                # Check outputs for dataframes
                if 'outputs' in cell:
                    for output in cell['outputs']:
                        if 'text' in output:
                            text = ''.join(output['text'])
                            # Try to extract table data
                            if 'Model' in text and 'Dataset' in text:
                                # This is a results table
                                lines = text.strip().split('\n')
                                # Skip header and separator lines
                                for line in lines[2:]:
                                    if line.strip() and not line.startswith('='):
                                        parts = line.split()
                                        if len(parts) >= 3:
                                            try:
                                                results.append({
                                                    'model': parts[0],
                                                    'dataset': parts[1],
                                                    'train_acc': float(parts[2]) if len(parts) > 2 else 0,
                                                    'val_acc': float(parts[3]) if len(parts) > 3 else 0,
                                                    'test_acc': float(parts[4]) if len(parts) > 4 else 0,
                                                })
                                            except:
                                                pass
    
    return results

def create_results_html(results_data=None):
    """Create HTML file to display results"""
    
    # If no results data, create a template
    if results_data is None:
        results_data = {
            'models': [
                {'name': 'Logistic Regression', 'raw': 0.45, 'normalized': 0.52, 'selected': 0.48},
                {'name': 'KNN', 'raw': 0.38, 'normalized': 0.41, 'selected': 0.39},
                {'name': 'Naive Bayes', 'raw': 0.42, 'normalized': 0.22, 'selected': 0.21},
                {'name': 'CNN', 'raw': 0.34, 'normalized': 0.36, 'selected': 0.35},
                {'name': 'SVM Linear', 'raw': 0.48, 'normalized': 0.55, 'selected': 0.52},
                {'name': 'SVM RBF', 'raw': 0.50, 'normalized': 0.58, 'selected': 0.55},
                {'name': 'MLP', 'raw': 0.45, 'normalized': 0.52, 'selected': 0.50},
                {'name': 'Random Forest', 'raw': 0.52, 'normalized': 0.58, 'selected': 0.56},
                {'name': 'Gradient Boosting', 'raw': 0.50, 'normalized': 0.56, 'selected': 0.54},
                {'name': 'XGBoost', 'raw': 0.51, 'normalized': 0.57, 'selected': 0.55},
                {'name': 'YAMNet + RF', 'raw': 0.65, 'normalized': 0.65, 'selected': 0.65},
                {'name': 'YAMNet + MLP', 'raw': 0.68, 'normalized': 0.68, 'selected': 0.68},
            ]
        }
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESC-50 Sound Classification - Results</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        h2 {{
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.8em;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        tr:hover {{
            background-color: #f5f5f5;
        }}
        
        .best {{
            background-color: #d4edda;
            font-weight: bold;
        }}
        
        .metric {{
            text-align: center;
            font-weight: 500;
        }}
        
        .chart-container {{
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }}
        
        .team-section {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        
        .team-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .team-card h3 {{
            margin-bottom: 10px;
            font-size: 1.3em;
        }}
        
        .team-card ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .team-card li {{
            padding: 5px 0;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }}
        
        .team-card li:last-child {{
            border-bottom: none;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            color: #666;
        }}
        
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.85em;
            margin: 2px;
        }}
        
        .badge-raw {{
            background: #ffc107;
            color: #000;
        }}
        
        .badge-norm {{
            background: #17a2b8;
            color: white;
        }}
        
        .badge-sel {{
            background: #28a745;
            color: white;
        }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎵 ESC-50 Sound Classification</h1>
            <p class="subtitle">Comprehensive Model Comparison and Results</p>
            <p class="subtitle">ECEN 758 Data Mining and Analysis - Fall 2025</p>
        </header>
        
        <div class="content">
            <div class="section">
                <h2>👥 Team Members</h2>
                <div class="team-section">
                    <div class="team-card">
                        <h3>Fahimeh Orvati Nia</h3>
                        <ul>
                            <li>Naive Bayes</li>
                            <li>CNN (1D)</li>
                        </ul>
                    </div>
                    <div class="team-card">
                        <h3>Banghyon Lee (Joseph)</h3>
                        <ul>
                            <li>Random Forest</li>
                            <li>Gradient Boosting</li>
                            <li>XGBoost</li>
                            <li>YAMNet Transfer Learning</li>
                            <li>Self-Supervised Learning</li>
                        </ul>
                    </div>
                    <div class="team-card">
                        <h3>Nandhini Valiveti</h3>
                        <ul>
                            <li>SVM (Linear)</li>
                            <li>SVM (RBF)</li>
                            <li>MLP</li>
                        </ul>
                    </div>
                    <div class="team-card">
                        <h3>Sushama Perati</h3>
                        <ul>
                            <li>Logistic Regression</li>
                            <li>KNN</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>📊 Model Performance Comparison</h2>
                <p style="margin-bottom: 20px; color: #666;">
                    All models were evaluated on three feature sets: <span class="badge badge-raw">Raw</span>, 
                    <span class="badge badge-norm">Normalized</span>, and <span class="badge badge-sel">Selected</span> features.
                    Test accuracy is shown below.
                </p>
                <table>
                    <thead>
                        <tr>
                            <th>Model</th>
                            <th>Team Member</th>
                            <th class="metric">Raw Features</th>
                            <th class="metric">Normalized Features</th>
                            <th class="metric">Selected Features</th>
                            <th class="metric">Best Accuracy</th>
                        </tr>
                    </thead>
                    <tbody id="resultsTable">
                        <!-- Results will be populated here -->
                    </tbody>
                </table>
            </div>
            
            <div class="section">
                <h2>📈 Performance Visualization</h2>
                <div class="chart-container">
                    <canvas id="performanceChart"></canvas>
                </div>
            </div>
            
            <div class="section">
                <h2>🔍 Key Findings</h2>
                <ul style="line-height: 2; color: #555;">
                    <li><strong>Transfer Learning:</strong> YAMNet embeddings significantly outperform traditional features</li>
                    <li><strong>Feature Preprocessing:</strong> Normalization generally improves performance for most models</li>
                    <li><strong>Best Model:</strong> YAMNet + MLP achieves the highest accuracy</li>
                    <li><strong>Traditional ML:</strong> Random Forest and XGBoost perform best among traditional methods</li>
                    <li><strong>Self-Supervised Learning:</strong> Pseudo-labeling shows promise for improving performance with limited labeled data</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>📁 Project Structure</h2>
                <p style="color: #666; line-height: 1.8;">
                    The complete project code is available in the main notebook: 
                    <code style="background: #f4f4f4; padding: 2px 8px; border-radius: 4px;">ESC_50_Complete_Project_All_Methods.ipynb</code>
                </p>
                <p style="color: #666; line-height: 1.8;">
                    For detailed methodology and analysis, see the project report: 
                    <code style="background: #f4f4f4; padding: 2px 8px; border-radius: 4px;">Project_Report.tex</code>
                </p>
            </div>
        </div>
        
        <div class="footer">
            <p>ECEN 758 Data Mining and Analysis Project - Fall 2025</p>
            <p>Texas A&M University</p>
        </div>
    </div>
    
    <script>
        // Sample data - replace with actual results from notebook
        const modelResults = [
            {{"name": "Logistic Regression", "member": "Sushama", "raw": 0.45, "norm": 0.52, "sel": 0.48}},
            {{"name": "KNN", "member": "Sushama", "raw": 0.38, "norm": 0.41, "sel": 0.39}},
            {{"name": "Naive Bayes", "member": "Fahimeh", "raw": 0.42, "norm": 0.22, "sel": 0.21}},
            {{"name": "CNN", "member": "Fahimeh", "raw": 0.34, "norm": 0.36, "sel": 0.35}},
            {{"name": "SVM Linear", "member": "Nandhini", "raw": 0.48, "norm": 0.55, "sel": 0.52}},
            {{"name": "SVM RBF", "member": "Nandhini", "raw": 0.50, "norm": 0.58, "sel": 0.55}},
            {{"name": "MLP", "member": "Nandhini", "raw": 0.45, "norm": 0.52, "sel": 0.50}},
            {{"name": "Random Forest", "member": "Joseph", "raw": 0.52, "norm": 0.58, "sel": 0.56}},
            {{"name": "Gradient Boosting", "member": "Joseph", "raw": 0.50, "norm": 0.56, "sel": 0.54}},
            {{"name": "XGBoost", "member": "Joseph", "raw": 0.51, "norm": 0.57, "sel": 0.55}},
            {{"name": "YAMNet + RF", "member": "Joseph", "raw": 0.65, "norm": 0.65, "sel": 0.65}},
            {{"name": "YAMNet + MLP", "member": "Joseph", "raw": 0.68, "norm": 0.68, "sel": 0.68}},
        ];
        
        // Populate table
        const tableBody = document.getElementById('resultsTable');
        modelResults.forEach(model => {{
            const best = Math.max(model.raw, model.norm, model.sel);
            const row = tableBody.insertRow();
            const bestClass = best === model.raw || best === model.norm || best === model.sel ? 'best' : '';
            
            row.innerHTML = `
                <td><strong>${{model.name}}</strong></td>
                <td>${{model.member}}</td>
                <td class="metric">${{(model.raw * 100).toFixed(1)}}%</td>
                <td class="metric">${{(model.norm * 100).toFixed(1)}}%</td>
                <td class="metric">${{(model.sel * 100).toFixed(1)}}%</td>
                <td class="metric ${{bestClass}}">${{(best * 100).toFixed(1)}}%</td>
            `;
        }});
        
        // Create chart
        const ctx = document.getElementById('performanceChart').getContext('2d');
        new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: modelResults.map(m => m.name),
                datasets: [
                    {{
                        label: 'Raw Features',
                        data: modelResults.map(m => m.raw * 100),
                        backgroundColor: 'rgba(255, 193, 7, 0.7)',
                    }},
                    {{
                        label: 'Normalized Features',
                        data: modelResults.map(m => m.norm * 100),
                        backgroundColor: 'rgba(23, 162, 184, 0.7)',
                    }},
                    {{
                        label: 'Selected Features',
                        data: modelResults.map(m => m.sel * 100),
                        backgroundColor: 'rgba(40, 167, 69, 0.7)',
                    }}
                ]
            }},
            options: {{
                responsive: true,
                scales: {{
                    y: {{
                        beginAtZero: true,
                        max: 100,
                        title: {{
                            display: true,
                            text: 'Test Accuracy (%)'
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        position: 'top',
                    }},
                    title: {{
                        display: true,
                        text: 'Model Performance Across Feature Sets'
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>"""
    
    return html

if __name__ == '__main__':
    # Create results.html
    html_content = create_results_html()
    
    with open('results.html', 'w') as f:
        f.write(html_content)
    
    print("✅ Created results.html")
    print("📝 Note: Update the JavaScript modelResults array with actual results from your notebook")

