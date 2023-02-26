A, B = map(int, input().split())
outputs = {True: "<", False:">"}
if A == B:
    print("==")
else:
    print(outputs[A < B])
