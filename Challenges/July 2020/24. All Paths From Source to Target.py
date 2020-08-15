class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        noOfNodes = len(graph)
        ans = []
        
        def recurse(source, dest, path):
            if(len(graph)==0):
                return
            elif(source == dest):
                ans.append(path)
                return
            for num in graph[source]:
                recurse(num, dest, path+[num])
        recurse(0, noOfNodes-1, [0])
        return ans