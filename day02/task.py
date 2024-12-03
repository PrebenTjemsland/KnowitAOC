import time

#https://stackoverflow.com/a/568618
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def list_first_n_primes(limit):
    prime_generator = gen_primes()
    count = 0
    index = 1
    cross_prime_sum = 0

    while count < limit:
        prime = next(prime_generator)
        cross_sum = sum(int(digit) for digit in str(prime))
        cross_sum_index = sum(int(digit) for digit in str(index))
        if cross_sum == cross_sum_index:
            count += 1
            cross_prime_sum += prime
        index += 1
    return cross_prime_sum


limit = 10000
start_time = time.time()

prime_sum = list_first_n_primes(limit)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Primes sum: {prime_sum}")
print(f"Time Elapsed: {elapsed_time:.4f} seconds")