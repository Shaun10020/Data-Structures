# python3


def build_heap(data):
    swaps = []
    for i in reversed(range(len(data))):
        data = swift_down_swaps(data,i+1,swaps)
    return swaps

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

def swift_up_swaps(data,i,swaps):
    if parent(data,i) is not None:
        if data[i-1]<parent(data,i):
            data[int(i/2)-1],data[i-1]=data[i-1],data[int(i/2)-1]
            swaps.append((int(i/2)-1,i-1))
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

def swift_down_swaps(data,i,swaps):
    if left(data,i) is not None and right(data,i) is not None:
        if data[i-1]>left(data,i) and data[i-1]>right(data,i):
            if left(data,i)>right(data,i):
                data[(2*i)],data[i-1]=data[i-1],data[(2*i)]
                swaps.append((i-1,2*i))
                data = swift_down_swaps(data,(2*i)+1,swaps)
            else:
                data[(2*i)-1],data[i-1]=data[i-1],data[(2*i)-1]
                swaps.append((i-1,(2*i)-1))
                data = swift_down_swaps(data,2*i,swaps)
        elif data[i-1]>left(data,i):
            data[(2*i)-1],data[i-1]=data[i-1],data[(2*i)-1]
            swaps.append((i-1,(2*i)-1))
            data = swift_down_swaps(data,2*i,swaps)
        elif data[i-1]>right(data,i):
            data[(2*i)],data[i-1]=data[i-1],data[(2*i)]
            swaps.append((i-1,2*i))
            data = swift_down_swaps(data,(2*i)+1,swaps)
    elif left(data,i) is not None:
        if data[i-1]>left(data,i):
            data[(2*i)-1],data[i-1]=data[i-1],data[(2*i)-1]
            swaps.append((i-1,(2*i)-1))
            data = swift_down_swaps(data,2*i,swaps)
    elif right(data,i) is not None:
        if data[i-1]>right(data,i):
            data[(2*i)],data[i-1]=data[i-1],data[(2*i)]
            swaps.append((i-1,2*i))
            data = swift_down_swaps(data,(2*i)+1,swaps)
    return data

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
