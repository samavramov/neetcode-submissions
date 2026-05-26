class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, res = [], 0
        for o in operations: 
            if o == "C":
                res -= record.pop()
            elif o == "D":
                curr = (record[-1])*2
                record.append(curr)
                res += curr
            elif o == "+":
                curr = record[-1] + record[-2]
                record.append(curr)
                res += curr
            else:
                curr = int(o)
                record.append(curr)
                res += curr
        return res
  