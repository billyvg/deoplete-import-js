import sys
import os
import neovim
sys.path.insert(1, os.path.dirname(__file__))

@neovim.plugin
class ImportJsHost(object):

    def __init__(self, vim):
        self.vim = vim

    def relative_file(self):
        """
            Return the current file
        """
        return self.vim.current.buffer.name

    @neovim.autocmd('CompleteDone', pattern='*.js,*.jsx', eval='expand("<amatch>")', sync=False)
    def importWord(self, afile):
        completed_item = self.vim.eval('v:completed_item')
        if completed_item:
            self.vim.call("importjs#ExecCommand", "word", completed_item["word"])

    def printError(self, message):
        self.vim.err_write(message + '\n')
        # self.vim.command(
        #     'echohl WarningMsg | echo "' + message + '" | echohl None')

    def log(self, message):
        """
        Log message to vim echo
        """
        val = "{}".format(message)
        # self.vim.command('redraws!')
        self.vim.out_write(val + '\n')
