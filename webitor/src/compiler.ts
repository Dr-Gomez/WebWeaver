export default class Lexer {
  static TokenTypes = {
    FUNCTION: "FUNCTION",
    IDENTIFIER: "IDENTIFIER",
    NUMBER: "NUMBER",
    PLUS: "PLUS",
    MINUS: "MINUS",
    MULTIPLY: "MULTIPLY",
    DIVIDE: "DIVIDE",
    LPAREN: "LPAREN",
    RPAREN: "RPAREN",
    LBRACE: "LBRACE",
    RBRACE: "RBRACE",
    SEMICOLON: "SEMICOLON",
    RETURN: "RETURN",
    EOF: "EOF", // End of file/input
    WHITESPACE: "WHITESPACE",
  };

  constructor() {}
}
