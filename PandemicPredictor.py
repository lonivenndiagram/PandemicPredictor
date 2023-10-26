import matplotlib.pyplot as plt

class PandemicSimulator:
    def __init__(self, r0, mortality_rate, mortality_rate_no_hospital):
        # Validate input parameters
        if r0 < 0 or mortality_rate < 0 or mortality_rate_no_hospital < 0:
            raise ValueError("Input parameters cannot be negative.")

        self.r0 = r0
        self.mortality_rate = mortality_rate
        self.mortality_rate_no_hospital = mortality_rate_no_hospital

        # Initialize hospital bed and occupied bed counts
        self._hospital_beds = 0
        self._occupied_beds = 0

    @property
    def hospital_beds(self):
        return self._hospital_beds

    @hospital_beds.setter
    def hospital_beds(self, value):
        if value < 0:
            raise ValueError("Number of hospital beds cannot be negative.")
        self._hospital_beds = value

    @property
    def occupied_beds(self):
        return self._occupied_beds

    @occupied_beds.setter
    def occupied_beds(self, value):
        if value < 0 or value > self._hospital_beds:
            raise ValueError("Number of occupied beds cannot be negative or exceed total hospital beds.")
        self._occupied_beds = value

    def calculate_new_infections(self, current_infections):
        """Calculate the number of new infections for the day."""
        if current_infections < 0:
            raise ValueError("Current infections cannot be negative.")
        
        new_infections = current_infections * self.r0
        return new_infections

    def calculate_hospitalizations(self, new_infections):
        """Calculate the number of new hospitalizations for the day."""
        unoccupied_beds = self._hospital_beds - self._occupied_beds
        if unoccupied_beds >= new_infections:
            self._occupied_beds += new_infections
            return new_infections
        else:
            hospitalizations = unoccupied_beds
            self._occupied_beds = self._hospital_beds
            return hospitalizations

    def calculate_deaths(self, new_infections, hospitalizations):
        """Calculate the number of deaths for the day."""
        deaths_hospitalized = hospitalizations * self.mortality_rate
        deaths_no_hospital = (new_infections - hospitalizations) * self.mortality_rate_no_hospital
        total_deaths = deaths_hospitalized + deaths_no_hospital
        return total_deaths

    def run_simulation(self, days, initial_infections):
        """Run the simulation over a given number of days."""
        infections = [1000]
        hospitalizations = [50]
        deaths = [2000]
        recoveries = [300]  # Added to track recoveries

        for day in range(1, days):
            # Assuming a constant recovery rate of 10% of occupied beds per day
            recovered_today = int(0.1 * self._occupied_beds)
            self._occupied_beds = max(0, self._occupied_beds - recovered_today)

            new_infections = self.calculate_new_infections(infections[-1])
            hospitalization = self.calculate_hospitalizations(new_infections)
            death = self.calculate_deaths(new_infections, hospitalization)

            infections.append(new_infections + infections[-1])
            hospitalizations.append(hospitalizations[-1] + hospitalization)
            deaths.append(deaths[-1] + death)
            recoveries.append(recoveries[-1] + recovered_today)  # Update recoveries

        return infections, hospitalizations, deaths, recoveries

    def plot_simulation(self, days, initial_infections):
        """Visualize the simulation results."""
        infections, hospitalizations, deaths, recoveries = self.run_simulation(days, initial_infections)
        
        plt.figure(figsize=(12, 8))
        plt.plot(range(days), infections, label="Infections", linestyle='--', marker='o')
        plt.plot(range(days), hospitalizations, label="Hospitalizations", linestyle='--', marker='v')
        plt.plot(range(days), deaths, label="Deaths", linestyle='--', marker='s')
        plt.plot(range(days), recoveries, label="Recoveries", linestyle='--', marker='x')
        plt.xlabel("Days")
        plt.ylabel("Count")
        plt.legend()
        plt.title("Pandemic Simulation")
        plt.grid(True)
        plt.annotate('Initial Infections', xy=(0, initial_infections), xytext=(3, initial_infections + 50),
                     arrowprops=dict(facecolor='black', arrowstyle='->'),
                     fontsize=12)
        plt.show()

# Example usage:
try:
    simulator = PandemicSimulator(r0=3.28, mortality_rate=0.03, mortality_rate_no_hospital=0.1)
    simulator.hospital_beds = 500
    simulator.plot_simulation(days=120, initial_infections=1000)
except ValueError as e:
    print(f"An error occurred: {e}")
