class Solution:
    import re
    def simplifyPath(self, path: str) -> str:
        result = []
        for name in path.split('/'):
            if name == '..':
                if result:
                    result.pop()
            elif name == '.' or name == '':
                continue
            else:
                result.append(name)
        print(result)
        return f"/{'/'.join(result)}"
            
        