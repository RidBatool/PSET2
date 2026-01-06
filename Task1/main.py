def mountainpeAK(n):
    result=[]
    def dfs(value, path):
        if value == 0:
            result.append(path.copy())
            return
        elif value <0:
            return 
        path.append(1)
        print("from first iteration", path)
        dfs(value-1, path)
        path.pop()
        path.append(2)
        print("from second iteration", path)
        dfs(value-2, path)
        path.pop()
    dfs(n, [])
    return result

print(mountainpeAK(3))