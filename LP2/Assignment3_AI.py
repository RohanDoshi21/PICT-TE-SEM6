def job_sequence(jobs):
    """
    Greedy algorithm for job sequencing with profits and deadlines.

    Args:
        jobs (list): List of tuples containing job ID, profit, and deadline.

    Returns:
        List of job IDs in the order they should be scheduled to maximize profit.
    """
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x[1], reverse=True)
    print("Sorted Jobs ", jobs)

    # Create a list of available time slots
    slots = [False] * (max(jobs, key=lambda x: x[2])[2])

    # Create a list to store the scheduled jobs
    schedule = []

    # Iterate over the jobs and schedule them in the latest available time slot before the deadline
    for job in jobs:
        # Find the latest available time slot before the deadline
        # print(str(job[0]) + " " + str(job[2]-1))
        for i in range(0, job[2], 1):
            if not slots[i]:
                slots[i] = True
                schedule.append(job[0])
                break

    return schedule

# Example input
jobs = [("J1", 70, 3), ("J2", 80, 2), ("J3", 50, 4), ("J4", 40, 1), ("J5", 80, 3), ("J6", 100, 1)]

# Expected output
expected_output = ['J6', 'J2', 'J5', 'J3']

# Test the function
output = job_sequence(jobs)
print(output)
# assert output == expected_output, f"Expected {expected_output}, but got {output}"
