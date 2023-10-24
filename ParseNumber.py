class ParseNumbers:
    def __init__(self, tokens):
        self.tokens = tokens

    def solve(self):
        # Handle parentheses
        while '(' in self.tokens:
            open_paren_index = len(self.tokens) - 1 - self.tokens[::-1].index('(')
            close_paren_index = self.tokens.index(')', open_paren_index)
            sub_expr = self.tokens[open_paren_index + 1:close_paren_index]
            sub_result = self.evaluate(sub_expr)
            self.tokens = self.tokens[:open_paren_index] + [sub_result] + self.tokens[close_paren_index + 1:]

        # Evaluate the remaining expression
        return self.evaluate(self.tokens)

    def evaluate(self, tokens):
        # First handle multiplication and division
        while "*" in tokens or "/" in tokens:
            i = 1
            while i < len(tokens):
                if tokens[i] == "*" or tokens[i] == "/":
                    if tokens[i] == "*":
                        tokens[i-1] = float(tokens[i-1]) * float(tokens[i+1])
                    else:
                        tokens[i-1] = float(tokens[i-1]) / float(tokens[i+1])
                    del tokens[i:i+2]
                else:
                    i += 2

        # Then handle addition and subtraction
        result = float(tokens[0])
        i = 1
        while i < len(tokens):
            if tokens[i] == "+":
                result += float(tokens[i+1])
            elif tokens[i] == "-":
                result -= float(tokens[i+1])
            i += 2

        return result

