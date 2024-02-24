import multiprocessing
from time import perf_counter


def process_ticket(ticket_number):  # unoptimized version: cant process any number of tickets
    first_part = ticket_number // 1000
    second_part = ticket_number % 1000

    first_sum = 0
    while first_part:
        first_sum += first_part % 10
        first_part //= 10

    second_sum = 0
    while second_part:
        second_sum += second_part % 10
        second_part //= 10

    return first_sum == second_sum


def check_tickets_parallel(tickets):
    with multiprocessing.Pool() as pool:
        results = pool.map(process_ticket, tickets)
    return results


if __name__ == "__main__":
    start = perf_counter()
    sum = 0
    tickets = []
    tickets.extend(range(1000000))  # building pool for multicore processing

    results = check_tickets_parallel(tickets)

    for i, result in enumerate(results):  # counter
        if result:
            sum = sum + 1

    print(sum)
    end = perf_counter()
    print(end - start)
