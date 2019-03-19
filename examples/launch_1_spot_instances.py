import scluster
import time


def main():
    scluster.set_backend('aws')

    start_time = time.time()
    job = scluster.make_job(num_tasks=1, spot=True)
    print(f"waited for startup for {time.time() - start_time} seconds")

    start_time = time.time()
    job.run('sleep 10')
    print(f"waited for exec for {time.time() - start_time} seconds")


if __name__ == '__main__':
    main()
