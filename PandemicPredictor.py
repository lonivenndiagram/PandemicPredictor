import matplotlib.pyplot as plt

class PandemicSimulator:
    def __init__(self, r0, incubation_rate, mortality_rate, mortality_rate_no_hospital):
        self.r0 = r0
        self.incubation_rate = incubation_rate
        self.mortality_rate = mortality_rate
        self.mortality_rate_no_hospital = mortality_rate_no_hospital
        self.hospital_beds = 0
        self.occupied_beds = 0

    def calculate_new_infections(self, current_infections):
        # Improved: Added parameter validation
        if current_infections < 0:
            raise ValueError("Current infections cannot be negative.")
        
        new_infections = current_infections * self.r0
        return new_infections

    def calculate_hospitalizations(self, new_infections):
        # Improved: Added scenario modeling for hospital bed capacity
        unoccupied_beds = self.hospital_beds - self.occupied_beds
        if unoccupied_beds >= new_infections:
            self.occupied_beds += new_infections
            return new_infections
        else:
            hospitalizations = unoccupied_beds
            self.occupied_beds = self.hospital_beds
            return hospitalizations

    def calculate_deaths(self, new_infections, hospitalizations):
        # Improved: Added scenario modeling for mortality rates
        deaths_hospitalized = hospitalizations * self.mortality_rate
        deaths_no_hospital = (new_infections - hospitalizations) * self.mortality_rate_no_hospital
        total_deaths = deaths_hospitalized + deaths_no_hospital
        return total_deaths

    def run_simulation(self, days, initial_infections):
        infections = [initial_infections]
        hospitalizations = [0]
        deaths = [0]

        for _ in range(1, days):
            new_infections = self.calculate_new_infections(infections[-1])
            hospitalization = self.calculate_hospitalizations(new_infections)
            death = self.calculate_deaths(new_infections, hospitalization)

            infections.append(new_infections + infections[-1])
            hospitalizations.append(hospitalizations[-1] + hospitalization)
            deaths.append(deaths[-1] + death)

        return infections, hospitalizations, deaths

    # Improved: Added data visualization
    def plot_simulation(self, days, initial_infections):
        infections, hospitalizations, deaths = self.run_simulation(days, initial_infections)
        
        plt.figure(figsize=(10, 6))
        plt.plot(range(days), infections, label="Infections")
        plt.plot(range(days), hospitalizations, label="Hospitalizations")
        plt.plot(range(days), deaths, label="Deaths")
        plt.xlabel("Days")
        plt.ylabel("Count")
        plt.legend()
        plt.title("Pandemic Simulation")
        plt.grid(True)
        plt.show()

# Example usage:
simulator = PandemicSimulator(r0=2.5, incubation_rate=0.1, mortality_rate=0.03, mortality_rate_no_hospital=0.1)
simulator.hospital_beds = 500
simulator.plot_simulation(days=120, initial_infections=10)
