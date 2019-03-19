import scluster
import time

def main():
  scluster.set_backend('local')

  job = scluster.make_job(num_tasks=2)

  start_time = time.time()
  job.run('sleep 1')
  print(f"waited for {time.time()-start_time} seconds")

if __name__ == '__main__':
  main()
