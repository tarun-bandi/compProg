class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count, website = cpdomain.split(" ")
            count = int(count)
            subdomains = website.split(".")
            current_domain = ""
            subdomains.reverse()
            for subdomain in subdomains:
                if current_domain:
                    current_domain = f"{subdomain}.{current_domain}"
                else:
                    current_domain = subdomain
                counts[current_domain] += count
        
        visit_counts = []
        for website, count in counts.items():
            visit_counts.append(f"{count} {website}")

        return visit_counts


                 

