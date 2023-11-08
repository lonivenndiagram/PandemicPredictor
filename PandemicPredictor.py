import argparse
import json
import matplotlib.pyplot as plt

class PandemicSimulator:
    def __init__(self, r0, mortality_rate, mortality_rate_no_hospital, hospital_beds, occupied_beds):
        self.r0 = r0
        self.mortality_rate = mortality_rate
        self.mortality_rate_no_hospital = mortality_rate_no_hospital
        self.hospital_beds = hospital_beds
        self.occupied_beds = occupied_beds

    def calculate_new_infections(self, current_infections):
        new_infections = current_infections * self.r0
        return new_infections

    def calculate_hospitalizations(self, new_infections):
        unoccupied_beds = self.hospital_beds - self.occupied_beds
        hospitalizations = min(unoccupied_beds, new_infections)
        self.occupied_beds += hospitalizations
        return hospitalizations

    def calculate_deaths(self, new_infections, hospitalizations):
        deaths_hospitalized = hospitalizations * self.mortality_rate
        deaths_no_hospital = (new_infections - hospitalizations) * self.mortality_rate_no_hospital
        return deaths_hospitalized + deaths_no_hospital

    def run_simulation(self, days, initial_infections):
        infections = [initial_infections]
        hospitalizations = []
        deaths = []
        recoveries = []

        for day in range(days):
            new_infections = self.calculate_new_infections(infections[-1])
            new_hospitalizations = self.calculate_hospitalizations(new_infections)
            new_deaths = self.calculate_deaths(new_infections, new_hospitalizations)

            infections.append(new_infections)
            hospitalizations.append(new_hospitalizations)
            deaths.append(new_deaths)
            # Assuming a constant recovery rate of 10% of occupied beds per day
            recoveries.append(self.occupied_beds * 0.1)

            # Update occupied beds for next day
            self.occupied_beds = max(self.occupied_beds - recoveries[-1], 0)

        return infections, hospitalizations, deaths, recoveries

    def plot_simulation(self, days, initial_infections):
        infections, hospitalizations, deaths, recoveries = self.run_simulation(days, initial_infections)
        
        plt.figure(figsize=(12, 8))
        plt.plot(range(days + 1), infections, label="Infections")
        plt.plot(range(days + 1), hospitalizations, label="Hospitalizations")
        plt.plot(range(days + 1), deaths, label="Deaths")
        plt.plot(range(days + 1), recoveries, label="Recoveries")
        plt.xlabel("Days")
        plt.ylabel("Number of Cases")
        plt.title("Pandemic Simulation Over Time")
        plt.legend()
        plt.grid(True)
        plt.show()


def read_parameters_from_file(file_path):
    with open(file_path, 'r') as file:
        parameters = json.load(file)
    return parameters


def main():
    parser = argparse.ArgumentParser(description='Run a pandemic simulation model.')
    parser.add_argument('--r0', type=float, help='The basic reproduction number')
    parser.add_argument('--mortality_rate', type=float, help='Mortality rate for those in the hospital')
    parser.add_argument('--mortality_rate_no_hospital', type=float, help='Mortality rate for those not hospitalized')
    parser.add_argument('--hospital_beds', type=int, help='Total number of hospital beds available')
    parser.add_argument('--occupied_beds', type=int, help='Number of occupied hospital beds at start')
    parser.add_argument('--days', type=int, help='Number of days to simulate')
    parser.add_argument('--initial_infections', type=int, help='Initial number of infections at start of simulation')
    parser.add_argument('--param_file', type=str, help='Path to parameter file', default=None)
    
    args = parser.parse_args()
    
    if args.param_file:
        parameters = read_parameters_from_file(args.param_file)
        simulator = PandemicSimulator(**parameters)
    else:
        simulator = PandemicSimulator(
            r0=args.r0,
            mortality_rate=args.mortality_rate,
            mortality_rate_no_hospital=args.mortality_rate_no_hospital,
            hospital_beds=args.hospital_beds,
            occupied_beds=args.occupied_beds
        )

    simulator.plot_simulation(args.days, args.initial_infections)

if __name__ == '__main__':
    main()
