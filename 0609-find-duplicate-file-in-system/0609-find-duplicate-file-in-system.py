class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        groups = collections.defaultdict(list)
        for path in paths:
            path_strings = path.split(" ")

            folder = path_strings[0]

            for f in path_strings[1:]:
                filename, file_body = f.split("(")
                file_body = file_body[:-1] # remove )

                groups[file_body].append(folder + "/" + filename)
        
        result = []

        for body, path in groups.items():
            if len(path) > 1:
                result.append(path)
        
        return result
