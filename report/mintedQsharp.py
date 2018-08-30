# -*- coding: utf-8 -*-
"""
    Qsharp lexer
"""

pygments.lexers..

from pygments.lexers.dotnet import FSharpLexer
from pygments.token import Name, Keyword

class QSharpLexer(FSharpLexer):
    name = 'qsharp'
    aliases = ['Q#']
    filenames = ['*.qsharp'] # just to have one if you whant to use

    EXTRA_KEYWORDS = ['namespace','open','operation','body','Qubit','Pauli',
                      'Range','Int','Double','String','Result','Bool','let',
                      'set','mutable','true','false','One','Zero','PaulI',
                      'PauliX','PauliY','PauliZ','H','X','M','Y','Z','I',
                      'if','for','in','Controlled','Adjoint','return',
                      'adjoint','auto','controlled']

    def get_tokens_unprocessed(self, text):
        for index, token, value in RubyLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
               yield index, token, value