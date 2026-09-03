# map(function, iterable, ...)
# it allows for a certain function to be used in every element of an iterable
import math

# measurement of diameter of a metal sphere using any of the below instruments
true_value = 5.00 # in (cm)


# instruments along with their least counts in (cm)
instruments = {"Ruler": 0.1, "Vernier Calipers": 0.01, "Micrometer Screw Gauge": 0.001}
di = {"A": "Ruler", "B": "Vernier Calipers", "C": "Micrometer Screw Gauge"}


choice = input("Which instrument would you like?" \
              "\nA: RULER" \
              "\nB: VERNIER CALIPER" \
              "\nC: MICROMETER SCREW GAUGE\n")

least_count = instruments[di[choice]]

def error_calc(value: float):

    min = true_value - least_count
    max = true_value + least_count

    if value >= min and value <= max:
        return 0
    else:
        abs_error = abs(true_value - value)
        relative_error = abs_error / true_value
        percent_error = relative_error * 100
        return percent_error


# input values obtained from experiments
exp_values = list(map(float, input("Enter the obtained values: ").split()))

errors = list(map(error_calc, exp_values))

result = {}

for i in range(len(exp_values)):
    result[F"Measured Value: {exp_values[i]} cm"] = F"{errors[i]:.2f}% error"

print(result)




