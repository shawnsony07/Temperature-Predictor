
# Temperature Prediction Using Linear Regression 📈

## Project Overview

This project implements a linear regression model to predict monthly temperatures based on historical weather station data. The model can forecast temperatures for any given year and month using gradient descent optimization.
## Features


•	Data preprocessing and cleaning

•	Linear regression implementation with gradient descent.

•	Temperature prediction for specific year and month.

•	Visualization of temperature trends over time.

•	Handling of missing values (999.9) by replacing with mean temperature.

•	Logarithmic transformation for better linear fit.





## Prerequisites

•	Python 3.x 

•	Required Python packages (see requirements.txt) 

•	Input data file: station.csv with columns: 

    •	YEAR
    
    •	Monthly temperature columns (JAN through DEC)

## Installation

1.	Clone the repository
2.	Install required packages:

```bash
pip install -r requirements.txt
```




## Usage

1.	Ensure your station.csv file is in the same directory as the script

2.	Run the script:

```bash
python temperature_prediction.py
```

3.	When prompted:

    •	Enter the year for prediction

    •	Enter the month number (1-12)

4.	The script will display:

    •	A plot showing the temperature trends

    •	The predicted temperature for the specified year and month



## Model Details

•	Uses simple linear regression 

•	Applies logarithmic transformation to both features and target variables 

•	Implements gradient descent optimization 

•	Learning rate (alpha) = 0.01 

•	Number of iterations = 2000





## Output

•	Visualization of temperature trends

•	Predicted temperature for specified year and month in °C




## Error Handling

•	Missing values (999.9) are replaced with the mean temperature.

•	Data is transformed using log10 for better linear fit.

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## License

[MIT](https://choosealicense.com/licenses/mit/)

