import csv

print("=== University Lab Resource Analysis ===\n")

underutilized = []
overloaded = []

with open("lab_usage.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        pc = row["PC"]
        usage = int(row["CPU_Usage"])

        if usage > 80:
            print(f"{pc}: {usage}% -> Overloaded")
            overloaded.append(pc)

        elif usage < 30:
            print(f"{pc}: {usage}% -> Underutilized")
            underutilized.append(pc)

        else:
            print(f"{pc}: {usage}% -> Normal")

print("\n=== Recommendation ===")

if underutilized:
    print("Assign new workloads to:", ", ".join(underutilized))

if overloaded:
    print("Reduce workload from:", ", ".join(overloaded))