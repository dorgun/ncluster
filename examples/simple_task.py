#!/usr/bin/env python
import scluster

# allocate default machine type and default image
task = scluster.make_task()
output = task.run('ifconfig')
print(f"Task ifconfig returned {output}")
