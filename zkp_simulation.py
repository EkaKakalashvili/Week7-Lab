import random

def simulate_zkp(trials=20, knows_password=True):
    success_count = 0

    for _ in range(trials):
        path_entered = random.choice(['A', 'B'])
        challenge = random.choice(['A', 'B'])

        if knows_password:
            success = True
        else:
            success = path_entered == challenge

        if success:
            success_count += 1

    probability = (success_count / trials) * 100
    print(f"Successful responses: {success_count}/{trials}")
    print(f"Probability of malicious success: {probability:.2f}%")

# Run honest prover (knows password)
simulate_zkp(knows_password=True)

# Run malicious prover (does NOT know password)
simulate_zkp(knows_password=False)
