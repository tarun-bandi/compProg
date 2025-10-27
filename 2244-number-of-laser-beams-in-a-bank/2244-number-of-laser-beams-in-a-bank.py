class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        total_beams = 0
        prev_lasers = 0

        for floor in bank:
            curr_lasers = floor.count('1')
            if curr_lasers == 0:
                continue
            total_beams += curr_lasers * prev_lasers
            prev_lasers = curr_lasers
        
        return total_beams
