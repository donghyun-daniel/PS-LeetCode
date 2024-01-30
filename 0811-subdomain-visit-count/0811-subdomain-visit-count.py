class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        visits = {}
        for cp in cpdomains:
            value, domain = cp.split(' ')
            subdomains = domain.split('.')
            
            for i in range(len(subdomains)):
                sub = '.'.join(subdomains[i:])
                if sub not in visits:
                    visits[sub] = value
                else:
                    visits[sub] = str(int(visits[sub]) + int(value))
        
        for k, v in visits.items():
            res.append(' '.join([v, k]))
        return res