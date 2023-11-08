# PandemicPredictor

PandemicPredictor is an open-source tool designed to simulate and visualize pandemic outcomes over a specified period. It takes into account various initial conditions and parameters to model the trajectory of a disease outbreak. The tool now features a command-line interface (CLI) for easy customization and supports configuration through a JSON file.

## Features

- A robust simulation model for pandemic forecasting.
- A command-line interface for dynamic parameter input.
- Parameter input via a configuration file for ease of use.
- Visualization of infection, hospitalization, death, and recovery counts over time.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/PandemicPredictor.git
cd PandemicPredictor
```
### Usage
You can run the simulation in two ways: by passing parameters directly through the CLI or by specifying a parameter file.

Using the CLI
Run the simulation with the following command:

```bash
python predict_pandemic.py --r0 2.5 --mortality_rate 0.01 --mortality_rate_no_hospital 0.02 --hospital_beds 1000 --occupied_beds 500 --days 120 --initial_infections 100
```
Using a Parameter File
Alternatively, you can specify a JSON file with the required parameters:

```bash
python predict_pandemic.py --param_file 'parameters.json'
```
Here's an example of how to format parameters.json:

```json
{
  "r0": 2.5,
  "mortality_rate": 0.01,
  "mortality_rate_no_hospital": 0.02,
  "hospital_beds": 1000,
  "occupied_beds": 500,
  "days": 120,
  "initial_infections": 100
}
```
### Visualization
The tool automatically generates a graph at the end of the simulation, illustrating the progression of the pandemic over the specified period.

### Model Assumptions
The model assumes a constant reproduction number (R0), mortality rates, and hospital bed capacity. It does not account for demographic factors, behavior changes, or temporal variations in parameters.

### Contributions
We welcome contributions to the PandemicPredictor project. Please feel free to fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
All contributors who have helped in refining and enhancing this tool.
The open-source community for continuous support and inspiration.
