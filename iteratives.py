import constants
import dtilParser
def parse_for(self):
    store = "for" + " "
    self.advance()
    if self.current_token.type == constants.TT_IDENTIFIER:
        store += str(self.current_token.value) + " "
        self.advance()
        if self.current_token.value == "in":
            store += str(self.current_token.value) + " "
            self.advance()
            if self.current_token.type in [constants.TT_INT, constants.TT_STRING, constants.TT_IDENTIFIER]:
                store += str(self.current_token.value) + " "
                self.advance()
                if str(self.current_token.value) == "by":
                    store += self.current_token.value + " "
                    self.advance()
                    if self.current_token.type == constants.TT_INT:
                        store += str(self.current_token.value) + " "
                        self.advance()
                        if self.current_token.type == constants.TT_COLON:
                            store += str(self.current_token.value) + " "
                            self.advance()
                            if self.current_token.type == constants.TT_NEWLINE:
                                store += "\n"
                                self.advance()
                                if self.current_token.type == constants.TT_TAB:
                                    return dtilParser.ResParse(self.current_token.line, store,f'Line {str(self.current_token.line + 1)} executed successfuly')
                                else:
                                    self.idx = len(self.tokens)
                                    return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
                            else:
                                self.idx = len(self.tokens)
                                return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
                        else:
                            self.idx = len(self.tokens)
                            return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
                    else:
                        self.idx = len(self.tokens)
                        return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
                else:
                    self.idx = len(self.tokens)
                    return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
            else:
                self.idx = len(self.tokens)
                return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
        else:
            self.idx = len(self.tokens)
            return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')
    else:
        self.idx = len(self.tokens)
        return dtilParser.ResParse(str(self.current_token.line), store, f'Invalid syntax at line {str(self.current_token.line + 1)}')