import sys
sys.set_int_max_str_digits(1000000000)

class Lexer:
    def __init__(self, line, ListOfTokens):
        self.line = line
        self.ListOfTokens = ListOfTokens
        
    def ToTokens(self):
        chars = list(self.line)
        tokens = []
        tmp_string = ""
        qutes_count = 0
        for char in chars:
            if char == '"' or char == "`":
                qutes_count+=1
            if qutes_count % 2 == 0:
                in_qutes = False
            else:
                in_qutes = True
            if char in self.ListOfTokens and not in_qutes:
                if tmp_string:
                    tokens.append(tmp_string)
                    tmp_string = ""
                tokens.append(char)
            elif char == " " and not in_qutes:
                if tmp_string:
                    tokens.append(tmp_string)
                    tmp_string = ""
            else:
                tmp_string += char
        if tmp_string:
            tokens.append(tmp_string)

        nums = []
        new_tokens = []
        for token in tokens:
            if token.replace(".", "", 1).isdigit() or token in ['+', '-', '*', '/', '(', ')']:
                nums.append(token)
            else:
                if nums:  # process the previous sequence of numbers and operators
                    seq = ""
                    for i, v in enumerate(nums):
                        seq = f"{seq}{v}"
                    
                    c = compile(seq, '<string>', 'eval')
                    result = eval(c)
                    new_tokens.append("'"+str(result)+"'")
                    nums = []  # reset the list of numbers and operators
                new_tokens.append(token)
        if nums:  # process the last sequence of numbers and operators
            seq = ""
            for i, v in enumerate(nums):
                seq = f"{seq}{v}"
            
            c = compile(seq, '<string>', 'eval')
            result = eval(c)
            new_tokens.append("'"+str(result)+"'")
        return new_tokens  
                

