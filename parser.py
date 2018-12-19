class TODOconf:
    titleFormat = "File name: {0}\n"
    lineFormat = 4*" " + "Line {0}: {1}\n"
    searchTerm = "TODO:"

    def __init__(self, fileObject, fileName):

        self.listoTODOS = {}
        self.name = fileName
        _lnum = 0

        for line in fileObject:
            _lnum += 1
            index = line.find(TODOconf.searchTerm)
            if index >= 0:
                self.listoTODOS[_lnum] = line[index : len(line) - 1]

    def __str__(self):
        to_return = ""
        for key in self.listoTODOS:
            to_return += TODOconf.lineFormat.format(key, self.listoTODOS[key])
        return TODOconf.titleFormat.format(self.name) + to_return


class CommentStyle:
    def __init__(self, fileTypeExtension, singleLineStart, singleLineEnd='\n', multilineStart="", multilineEnd=""):
        self.filetype = fileTypeExtension

        self.singleLineStart = singleLineStart
        self.singleLineEnd = singleLineEnd
        self.mstart = multilineStart
        self.mend = multilineEnd


fileTypeStyles = {
    'py' : CommentStyle('python', "#", '"""', '"""')
}

def get_comments(fileObject, commentStyle):
    """
    Returns a list of pairs whose first element is the line number that a comment was found on, and whose second element is the content of the comment.
    :param fileObject: The object corresponding to the file whose contents is being read from.
    :param commentStyle: An instance of the class
    :return: Of the form [(int, string), ...] where the first element of the pair is the line number and the string is the comment content.
    """
    lineNumber = 0
    for line in fileObject:
        lineNumber += 1
        inStringLiteral = False
        for char in line:
            if not inStringLiteral and char == commentStyle.singleLineStart: # Then we have entered the context of a single line comment.
                pass
