#!/usr/bin/env python
# coding: utf-8

from .base import Base
from logging import getLogger
from subprocess import Popen, PIPE
import json

logger = getLogger('deoplete')

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'importjs'
        self.mark = '[importjs]'
        self.filetypes = ['javascript', 'javascript.jsx']
        self.min_pattern_length = 2
        self.rank = 10000
        self.input_pattern = '((?:\.|(?:,|:|->)\s+)\w*|\()'
        self.__completer = Completer(vim)

    def get_complete_position(self, context):
        return self.__completer.determine_completion_position(context)

    def gather_candidates(self, context):
        return self.__completer.find_candidates(
            context
        )

class Completer(object):
    def __init__(self, vim):
        import re
        self.__vim = vim
        self.__completion_pattern = re.compile('\w*$')

    def get_bin(self):
        try:
            return self.__vim.vars.get('deoplete_import_js#bin')
        except:
            return 'importjs'

    def determine_completion_position(self, context):
        result = self.__completion_pattern.search(context['input'])

        if result is None:
            return self.__vim.current.window.cursor.col

        return result.start()

    def abbreviate_if_needed(self, text):
        return (text[:47] + '...') if len(text) > 50 else text

    def find_candidates(self, context):
        line = str(self.__vim.current.window.cursor[0])
        column = str(self.__vim.current.window.cursor[1] + 1)
        word = context["input"]
        command = [self.get_bin(), 'search', word + '*', context["bufpath"]]

        buf = '\n'.join(self.__vim.current.buffer[:])

        try:
            process = Popen(command, stdout=PIPE, stdin=PIPE)
            command_results = process.communicate()[0]

            logger.debug(command_results)
            if process.returncode != 0:
                return []

            results = json.loads(command_results.decode('utf-8'))

            return [{
                'word': x["variableName"],
                'abbr': self.abbreviate_if_needed(x["variableName"]),
                'kind': '' if x["hasNamedExports"] else 'd',
                'menu': x["filePath"] if "filePath" in x else x["importPath"] if "importPath" in x else ""
                } for x in results]
        except FileNotFoundError:
            pass

