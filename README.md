# Pandemic Outcome Predictor
## Overview
This Python program is designed to predict the progression of a pandemic caused by a communicable illness based on several key parameters. It can provide projections for the number of new cases, new hospital admissions, and new deaths over specific periods of time. This tool is meant to assist in understanding potential outcomes and resource planning during pandemics.

### Parameters
To use the model, you'll need to provide the following parameters:

*Basic Reproduction Number (R0):* The average number of secondary infections produced by one infected individual.

*Incubation Period (in days):* The time it takes for an infected individual to show symptoms.

*Mortality Rate (%):* The percentage of infected individuals who do not survive.

*Mortality Rate without Hospitalization (%):* The percentage of infected individuals who do not survive when unable to receive hospital care.

*Total Hospital Beds Available:* The total number of hospital beds available in the area of interest.

*Current Hospital Beds Occupied:* The number of hospital beds currently occupied in the area of interest.

*Positive Test Percentage (% of tests that come back positive):* The percentage of tests that result in a positive diagnosis.

### Usage
Clone this repository to your local machine.

Install the required dependencies:

```bash
pip install matplotlib
```

Modify the parameters in the predict_pandemic.py file according to your specific scenario.

Run the script:

```bash
python predict_pandemic.py
```

The program will provide projections for new cases, new hospital admissions, and new deaths over specific time periods.

### Extending for Other Diseases
To adapt this model for other communicable illnesses, you'll need to gather data on the disease's specific parameters (R0, incubation period, mortality rates, etc.) and modify the code accordingly. Ensure that the data you use is reliable and relevant to the disease you're modeling.

### Disclaimer
This model provides predictions based on the parameters you input. It is not a substitute for professional medical advice or official guidance from health authorities. Use the model responsibly and consult with experts and official sources for decision-making during a pandemic.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
