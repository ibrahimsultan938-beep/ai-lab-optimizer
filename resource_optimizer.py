import csv

print("=== AI GPU Resource Analysis ===\n")

underutilized = []
overloaded = []

with open("lab_usage.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        pc = row["PC"]
        usage = int(row["GPU_Usage"])

        if usage > 80:
            print(f"{pc}: GPU Usage {usage}% -> Overloaded")
            overloaded.append(pc)

        elif usage < 30:
            print(f"{pc}: GPU Usage {usage}% -> Underutilized")
            underutilized.append(pc)

        else:
            print(f"{pc}: GPU Usage {usage}% -> Normal")

print("\n=== AI Resource Allocation Recommendation ===")

if underutilized:
    print("Recommended systems for new AI workloads:")
    print(", ".join(underutilized))

if overloaded:
    print("\nSystems requiring workload reduction:")
    print(", ".join(overloaded))

print("\n=== Summary ===")
print(f"Overloaded Systems: {len(overloaded)}")
print(f"Underutilized Systems: {len(underutilized)}")
