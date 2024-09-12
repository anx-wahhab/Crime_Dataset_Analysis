# Crime Dataset Analysis: Convictions and Unsuccessful Attempts

This repository contains the analysis of the Crown Prosecution Service (CPS) Case Outcomes dataset, focusing on convictions and unsuccessful attempts. The dataset used for this analysis spans a 24-month period and was sourced from the UK government’s data portal.

## Dataset
The dataset comprises various criminal incidents categorized by principal offense. It includes:
- **Convictions_Total**: Total number of convictions.
- **Unsuccessful_Total**: Total number of unsuccessful attempts.
- Additional crime-related variables for each incident.

**Source**: [Crown Prosecution Service Case Outcomes by Principal Offence Category Data](https://data.gov.uk/dataset/89d0aef9-e2f9-4d1a-b779-5a33707c5f2c/crown-prosecution-service-case-outcomes-by-principal-offence-category-data)

## Project Structure
- **Data Exploration**: Initial data import, handling of missing values, and data transformation.
- **Descriptive Analytics**: Visualization of data distribution, outlier detection, and correlation analysis.
- **Hypothesis Testing**: Two key hypotheses explored:
  - Correlation between convictions and unsuccessful attempts.
  - Pattern differences among distinct clusters of data.
- **Model Training**: Development of predictive models, including:
  - **Linear Regression**: Predicting unsuccessful attempts.
  - **Clustering (k-means)**: Identifying distinct criminal behavior patterns.
  - **Support Vector Machine (SVM)**: Classification of data points based on crime-related variables.
  
## Key Results
1. **Significant Correlation**: A strong correlation was found between convictions and unsuccessful attempts.
2. **Cluster Identification**: K-means clustering revealed four distinct clusters, highlighting variations in criminal behavior.
3. **Predictive Modeling**: A linear regression model showed significant results for predicting the number of administratively finalized unsuccessful attempts.

## Tools & Libraries
- **R Programming**: Analysis was performed using R, with key libraries including `ggplot2`, `dplyr`, `e1071`, and `factoextra` for data visualization and modeling.
  
## Report
A detailed PDF report of the analysis can be found [here](./Report.pdf). This report contains comprehensive explanations of the methods, visualizations, and conclusions drawn from the analysis.

## How to Use
1. Clone the repository.
2. Ensure R and required libraries are installed.
3. Use the scripts provided for replicating the analysis on the dataset.
