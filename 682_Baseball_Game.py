class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        new_ls = []
        operator_ls = []
        count = 0
        for operator in ops:
            if operator == "C":
                new_ls.pop()
            else:
                new_ls.append(operator)
        for i in range(len(new_ls)):
            if new_ls[i][0] == "-":
                count += int(new_ls[i])
                operator_ls.append(int(new_ls[i]))
            if new_ls[i].isdigit():
                count += int(new_ls[i])
                operator_ls.append(int(new_ls[i]))
            elif new_ls[i] == "D":
                count += 2*operator_ls[i-1]
                operator_ls.append(2*operator_ls[i-1])
            elif new_ls[i] == "+":
                count +=operator_ls[i-1]+operator_ls[i-2]
                operator_ls.append(operator_ls[i-1]+operator_ls[i-2])
        return count
