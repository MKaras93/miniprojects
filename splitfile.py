# coding=utf-8
class FileSeparator:

    def __init__(self, separated_file_path):
        self.src_file = open(separated_file_path, 'r')
        self.lines_iter = iter(self.src_file)

    def next_text_block(self):
        line = ''
        while not line.strip():
            try:
                line = next(self.lines_iter)
            except StopIteration:
                return
            
        text_block = ''
        while line.strip():
            text_block += line
            try:
                line = next(self.lines_iter)
            except StopIteration:
                return text_block
        
        return text_block

