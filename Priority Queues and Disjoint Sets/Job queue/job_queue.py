# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    data=list()
    for i in range(n_workers):
        data.append(i)
    data=build_heap(data)
    for i in range(len(jobs)):
        data,Max=ExtractMax(data)
        next_worker=Max%n_workers
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker]=next_free_time[next_worker]+jobs[i]
        data=Insert(data,next_worker+(next_free_time[next_worker]*n_workers))
    return result

def build_heap(data):
    for i in reversed(range(len(data))):
        swift_down(data,i+1)
    return data

def left(data,i):
    if len(data)<(2*i):
        return None
    return data[(2*i)-1]

def right(data,i):
    if len(data)<(2*i)+1:
        return None
    return data[(2*i)]

def parent(data,i):
    if i==1:
        return None
    return(data[int(i/2)-1])

def swift_up(data,i):
    if parent(data,i) is not None:
        if data[i-1]<parent(data,i):
            data[int(i/2)-1],data[i-1]=data[i-1],data[int(i/2)-1]
            data = swift_up(data,int(i/2))
    return data

def swift_down(data,i):
    if left(data,i) is not None and right(data,i) is not None:
        if data[i-1]>left(data,i) and data[i-1]>right(data,i):
            if left(data,i)>right(data,i):
                data[(2*i)],data[i-1]=data[i-1],data[(2*i)]
                data = swift_down(data,(2*i)+1)
            else:
                data[(2*i)-1],data[i-1]=data[i-1],data[(2*i)-1]
                data = swift_down(data,2*i)
        elif data[i-1]>left(data,i):
            data[(2*i)-1],data[i-1]=data[i-1],data[(2*i)-1]
            data = swift_down(data,2*i)
        elif data[i-1]>right(data,i):
            data[(2*i)],data[i-1]=data[i-1],data[(2*i)]
            data = swift_down(data,(2*i)+1)
    elif left(data,i) is not None:
        if data[i-1]>left(data,i):
            data[(2*i)-1],data[i-1]=data[i-1],data[(2*i)-1]
            data = swift_down(data,2*i)
    elif right(data,i) is not None:
        if data[i-1]>right(data,i):
            data[(2*i)],data[i-1]=data[i-1],data[(2*i)]
            data = swift_down(data,(2*i)+1)
    return data

def ExtractMax(data):
    Max=data[0]
    data[0]=data[len(data)-1]
    data.pop()
    data=swift_down(data,1)
    return (data, Max)

def Remove(data,i):
    data[i-1]=0
    data=swift_up(data,i)
    data, max=ExtractMax(data)
    return data

def Insert(data,element):
    data.append(element)
    data=swift_up(data,len(data))
    return data

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
