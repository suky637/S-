import sys

# "//" -> "#"; "COMMENT"
# "\"" -> "\""; "STRING"
# ";" -> "\n" loop(s): "\t"; "semi-colon"
#
#
#

class Parser:
    def __init__(self, text):
        self.text = text
        self.tokens = []

    def parse(self):
        code = ''
        is_s = False
        ct = ''

        divisions = 0
        
        current_tabs = 0
        
        self.text = self.text.replace("include", "import")
        self.text = self.text.replace("toString", "str")
        self.text = self.text.replace("parseInt", "int")
        self.text = self.text.replace("parseIntChr", "ord")

        for c in self.text:


            ct += c
            if c in ' \t':
                for i in range(current_tabs):
                    if not is_s and not c == '\t':
                        code += '\t'

                ct = ''


            if divisions == 2:
                divisions = 0
                code += '#'
                ct = ''
            elif c == '/' and not is_s:
                divisions += 1

            elif not c == '/' and divisions == 1:
                code += '/'
                divisions = 0
            elif c == '"':
                is_s = not is_s
                ct = ''
                code += '"'
            elif ct == ';':
                code += '\n'
            elif c == '{' and not is_s:
                code += ':'
                current_tabs += 1
            elif c == '}' and not is_s:
                current_tabs -= 1
            else:
                code += c
        return code

def main():
    try:
        
        parser = Parser(open(sys.argv[1], 'r').read())
        t = parser.parse()
        name = 'out.py'
        
        ind = 0
        for arg in sys.argv:
            if arg == '-o':
                name = sys.argv[ind+1] + '.py'
            ind += 1

        f_out = open(name, 'w')
        f_out.write(t)
        f_out.close()

    except IndexError:
        print("No Input File")
if __name__ == '__main__':
    main()
