# Generated on 2020-01-27 09:43:07.850713

from darglint.parse.identifiers import (
    NoqaIdentifier,
)

from darglint.token import (
    TokenType,
)

from darglint.parse.grammar import (
    BaseGrammar,
    P,
)

from darglint.parse.identifiers import (
    ArgumentItemIdentifier,
    ArgumentTypeIdentifier,
    ExceptionIdentifier,
    ExceptionItemIdentifier,
    ShortDescriptionIdentifier,
)

class NumpyGrammar(BaseGrammar):
    productions = [
        P("docstring", ([], "short-description", "arguments-section", 100), ([], "short-description", "docstring1", 100), ([], "short-description", "long-description", 0), ([], "short-description", "docstring2", 0), ([], "short-description", "docstring3", 0), ([], "short-description", "raises-section", 0), ([], "short-description", "docstring5", 0), ([], "short-description", "docstring6", 0), ([], "short-description", "docstring7", 0), ([], "short-description", "returns-section", 0), ([], "short-description", "warns-section", 0), ([], "short-description", "yields-section", 0), ([ShortDescriptionIdentifier], "word", "line", 0), ([ShortDescriptionIdentifier], "word", "noqa-maybe", 0), ([NoqaIdentifier, ShortDescriptionIdentifier], "hash", "noqa", 0), ([NoqaIdentifier, ShortDescriptionIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0), ([ShortDescriptionIdentifier], "line", "newlines", 0)),
        P("long-description", ([], "line", "long-description0", 0), ([], "line", "newlines", 0), ([], "word", "line", 0), ([], "word", "noqa-maybe", 0), ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0)),
        P("short-description", ([ShortDescriptionIdentifier], "word", "line", 0), ([ShortDescriptionIdentifier], "word", "noqa-maybe", 0), ([NoqaIdentifier, ShortDescriptionIdentifier], "hash", "noqa", 0), ([NoqaIdentifier, ShortDescriptionIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0), ([ShortDescriptionIdentifier], "line", "newlines", 0), ([ShortDescriptionIdentifier], "word", "line", 0), ([ShortDescriptionIdentifier], "word", "noqa-maybe", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0)),
        P("arguments-section", ([], "arguments-header", "newlines", 0), ([], "arguments-header", "arguments-section0", 0), ([], "arguments", "arguments-header0", 0)),
        P("other-arguments-section", ([], "other", "other-arguments-section0", 0), ([], "other", "other-arguments-section1", 0)),
        P("arguments-header", ([], "arguments", "arguments-header0", 0)),
        P("arguments-body", ([], "argument-item", "arguments-body0", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item1", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item3", 0), ([ArgumentItemIdentifier, ArgumentTypeIdentifier], "ident-list", "argument-item6", 0)),
        P("argument-item", ([ArgumentItemIdentifier], "ident-list", "argument-item1", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item3", 0), ([ArgumentItemIdentifier, ArgumentTypeIdentifier], "ident-list", "argument-item6", 0)),
        P("ident-list", ([], "ident", "ident-list", 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0)),
        P("warns-section", ([], "warns-header", "newlines", 0), ([], "warns-header", "warns-section0", 0), ([], "warns", "warns-header0", 0)),
        P("warns-header", ([], "warns", "warns-header0", 0)),
        P("raises-section", ([], "raises-header", "newlines", 0), ([], "raises-header", "raises-section0", 0), ([], "raises", "raises-header0", 0)),
        P("raises-header", ([], "raises", "raises-header0", 0)),
        P("raises-body", ([], "raises-item", "raises-body", 0), ([ExceptionItemIdentifier], "ident", "raises-item1", 0)),
        P("raises-item", ([ExceptionItemIdentifier], "ident", "raises-item1", 0)),
        P("receives-section", ([], "receives-header", "newlines", 0), ([], "receives-header", "receives-section0", 0), ([], "receives", "receives-header0", 0)),
        P("receives-header", ([], "receives", "receives-header0", 0)),
        P("receives-body", ([], "receives-item", "receives-body", 0), ([], "ident", "receives-item0", 0), ([], "ident", "receives-item1", 0)),
        P("receives-item", ([], "ident", "receives-item0", 0), ([], "ident", "receives-item1", 0)),
        P("yields-section", ([], "yields-header", "newlines", 0), ([], "yields-header", "yields-section0", 0), ([], "yields", "yields-header0", 0)),
        P("yields-header", ([], "yields", "yields-header0", 0)),
        P("yields-body", ([], "line", "yields-body0", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0), ([], "yields-argument", "yields-body-typed0", 0), ([], "yields-argument", "yields-body-typed2", 0)),
        P("yields-body-typed", ([], "yields-argument", "yields-body-typed0", 0), ([], "yields-argument", "yields-body-typed2", 0)),
        P("yields-argument", ([], "ident", "yields-argument0", 0), ([], "ident", "newline", 0)),
        P("returns-section", ([], "returns-header", "newlines", 0), ([], "returns-header", "returns-section0", 0), ([], "returns", "returns-header0", 0)),
        P("returns-header", ([], "returns", "returns-header0", 0)),
        P("returns-body", ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0), ([], "returns-argument", "returns-body-typed0", 0), ([], "returns-argument", "returns-body-typed2", 0)),
        P("returns-body-typed", ([], "returns-argument", "returns-body-typed0", 0), ([], "returns-argument", "returns-body-typed2", 0)),
        P("returns-argument", ([], "ident", "returns-argument0", 0), ([], "ident", "newline", 0)),
        P("block-indented", ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("paragraph-indented", ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("indented", ([], "indent", "indents", 0), (TokenType.INDENT, 0)),
        P("indents", ([], "indent", "indents", 0), (TokenType.INDENT, 0)),
        P("split", ([], "newline", "split0", 0)),
        P("newlines", ([], "newline", "newlines", 0), (TokenType.NEWLINE, 0)),
        P("line", ([], "word", "line", 0), ([], "word", "noqa-maybe", 0), ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0)),
        P("word", (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0)),
        P("ident", (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0)),
        P("header", (TokenType.HEADER, 0)),
        P("arguments", (TokenType.ARGUMENTS, 0)),
        P("colon", (TokenType.COLON, 0)),
        P("hash", (TokenType.HASH, 0)),
        P("indent", (TokenType.INDENT, 0)),
        P("newline", (TokenType.NEWLINE, 0)),
        P("raises", (TokenType.RAISES, 0)),
        P("returns", (TokenType.RETURNS, 0)),
        P("yields", (TokenType.YIELDS, 0)),
        P("noqa", (TokenType.NOQA, 0)),
        P("other", (TokenType.OTHER, 0)),
        P("receives", (TokenType.RECEIVES, 0)),
        P("warns", (TokenType.WARNS, 0)),
        P("noqa-maybe", ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0)),
        P("noqa-head", ([], "hash", "noqa", 0)),
        P("words", ([], "word", "words", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0)),
        P("docstring1", ([], "arguments-section", "other-arguments-section", 0)),
        P("docstring2", ([], "long-description", "arguments-section", 0)),
        P("docstring3", ([], "long-description", "docstring4", 0)),
        P("docstring4", ([], "arguments-section", "other-arguments-section", 0)),
        P("docstring5", ([], "long-description", "raises-section", 0)),
        P("docstring6", ([], "arguments-section", "raises-section", 0)),
        P("docstring7", ([], "receives-section", "yields-section", 0)),
        P("long-description0", ([], "newlines", "long-description", 0), ([], "line", "long-description0", 0), ([], "line", "newlines", 0), ([], "word", "line", 0), ([], "word", "noqa-maybe", 0), ([NoqaIdentifier], "hash", "noqa", 0), ([NoqaIdentifier], "noqa-head", "noqa-statement1", 0), (TokenType.COLON, 0), (TokenType.HASH, 0), (TokenType.INDENT, 0), (TokenType.LPAREN, 0), (TokenType.RPAREN, 0), (TokenType.WORD, 0), (TokenType.RAISES, 0), (TokenType.ARGUMENTS, 0), (TokenType.ARGUMENT_TYPE, 0), (TokenType.RETURNS, 0), (TokenType.RETURN_TYPE, 0), (TokenType.YIELDS, 0), (TokenType.YIELD_TYPE, 0), (TokenType.VARIABLES, 0), (TokenType.VARIABLE_TYPE, 0), (TokenType.NOQA, 0), (TokenType.OTHER, 0), (TokenType.RECEIVES, 0), (TokenType.WARNS, 0), (TokenType.HEADER, 0)),
        P("arguments-section0", ([], "newline", "arguments-section1", 0)),
        P("arguments-section1", ([], "arguments-body", "newlines", 0), ([], "argument-item", "arguments-body0", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item1", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item3", 0), ([ArgumentItemIdentifier, ArgumentTypeIdentifier], "ident-list", "argument-item6", 0)),
        P("other-arguments-section0", ([], "arguments-header", "newlines", 0), ([], "arguments", "arguments-header0", 0)),
        P("other-arguments-section1", ([], "arguments-header", "other-arguments-section2", 0)),
        P("other-arguments-section2", ([], "newline", "other-arguments-section3", 0)),
        P("other-arguments-section3", ([], "arguments-body", "newlines", 0), ([], "argument-item", "arguments-body0", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item1", 0), ([ArgumentItemIdentifier], "ident-list", "argument-item3", 0), ([ArgumentItemIdentifier, ArgumentTypeIdentifier], "ident-list", "argument-item6", 0)),
        P("arguments-header0", ([], "newline", "header", 0)),
        P("arguments-body0", ([], "newline", "arguments-body", 0)),
        P("argument-item1", ([], "newline", "block-indented", 0)),
        P("argument-item3", ([], "colon", "argument-item4", 0)),
        P("argument-item4", ([], "newline", "block-indented", 0)),
        P("argument-item6", ([], "colon", "argument-item7", 0)),
        P("argument-item7", ([], "line", "argument-item8", 0)),
        P("argument-item8", ([], "newline", "block-indented", 0)),
        P("warns-section0", ([], "newline", "warns-section1", 0)),
        P("warns-section1", ([], "raises-body", "newlines", 0), ([], "raises-item", "raises-body", 0), ([ExceptionItemIdentifier], "ident", "raises-item1", 0)),
        P("warns-header0", ([], "newline", "header", 0)),
        P("raises-section0", ([], "newline", "raises-section1", 0)),
        P("raises-section1", ([], "raises-body", "newlines", 0), ([], "raises-item", "raises-body", 0), ([ExceptionItemIdentifier], "ident", "raises-item1", 0)),
        P("raises-header0", ([], "newline", "header", 0)),
        P("raises-item1", ([], "newline", "block-indented", 0)),
        P("receives-section0", ([], "newline", "receives-section1", 0)),
        P("receives-section1", ([], "receives-body", "newlines", 0), ([], "receives-item", "receives-body", 0), ([], "ident", "receives-item0", 0), ([], "ident", "receives-item1", 0)),
        P("receives-header0", ([], "newline", "header", 0)),
        P("receives-item0", ([], "newline", "block-indented", 0)),
        P("receives-item1", ([], "colon", "receives-item2", 0)),
        P("receives-item2", ([], "line", "receives-item3", 0)),
        P("receives-item3", ([], "newline", "block-indented", 0)),
        P("yields-section0", ([], "newline", "yields-section1", 0)),
        P("yields-section1", ([], "yields-body", "newlines", 0), ([], "line", "yields-body0", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0), ([], "yields-argument", "yields-body-typed0", 0), ([], "yields-argument", "yields-body-typed2", 0)),
        P("yields-header0", ([], "newline", "header", 0)),
        P("yields-body0", ([], "newline", "block-indented", 0)),
        P("yields-body-typed0", ([], "block-indented", "yields-body-typed1", 0)),
        P("yields-body-typed1", ([], "newline", "yields-body-typed", 0)),
        P("yields-body-typed2", ([], "block-indented", "newlines", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("yields-argument0", ([], "colon", "yields-argument1", 0)),
        P("yields-argument1", ([], "line", "newline", 0)),
        P("returns-section0", ([], "newline", "returns-section1", 0)),
        P("returns-section1", ([], "returns-body", "newlines", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0), ([], "returns-argument", "returns-body-typed0", 0), ([], "returns-argument", "returns-body-typed2", 0)),
        P("returns-header0", ([], "newline", "header", 0)),
        P("returns-body-typed0", ([], "block-indented", "returns-body-typed1", 0)),
        P("returns-body-typed1", ([], "newline", "returns-body-typed", 0)),
        P("returns-body-typed2", ([], "block-indented", "newlines", 0), ([], "paragraph-indented", "block-indented0", 0), ([], "indented", "paragraph-indented0", 0), ([], "indented", "line", 0)),
        P("returns-argument0", ([], "colon", "returns-argument1", 0)),
        P("returns-argument1", ([], "line", "newline", 0)),
        P("block-indented0", ([], "split", "block-indented", 0)),
        P("paragraph-indented0", ([], "line", "paragraph-indented1", 0)),
        P("paragraph-indented1", ([], "newline", "paragraph-indented", 0)),
        P("split0", ([], "newline", "newlines", 0), (TokenType.NEWLINE, 0)),
        P("noqa-statement1", ([], "colon", "words", 0)),
    ]
    start = "docstring"