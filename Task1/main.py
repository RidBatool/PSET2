def mountainpeAK(n):
    result=[]
    def dfs(value, path):
        if value == 0:
            result.append(path.copy())
            return
        elif value <0:
            return 
        path.append(1)
        dfs(value-1, path)
        path.pop()
        path.append(2)
        dfs(value-2, path)
        path.pop()
    dfs(n, [])
    return result
print("first run")
print(mountainpeAK(2))
print("second run")
print(mountainpeAK(3))
print("third run")
print(mountainpeAK(4))
