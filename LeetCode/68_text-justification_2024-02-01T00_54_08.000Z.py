# https://leetcode.com/problems/text-justification

class Solution:

    def printJustify(self, lines) -> List[str]:
        strLines = []
        for line, spaceWidth in lines:
            # print(line, spaceWidth)
            strLine = ""
            if spaceWidth <= 0:
                for word in line:
                    strLine += word + " "
                strLines.append(strLine[:-1] + " " * (-spaceWidth))
            elif len(line) == 1:
                strLines.append(line[0] + " " * spaceWidth)
            else:
                narrowSpace = spaceWidth // (len(line) - 1)
                wideSpace = narrowSpace + 1
                wideCount = spaceWidth - narrowSpace * (len(line) - 1)
                narrowCount = len(line) - 1 - wideCount
                spaces = [wideSpace] * wideCount + [narrowSpace] * narrowCount + [-1]
                # print(spaces)
                for word in line:
                    strLine += word + " " * (spaces.pop(0) + 1)
                strLines.append(strLine) 
        return strLines

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        currLine = []
        currWidth = 0
        for w in words:
            if len(w) + currWidth <= maxWidth:
                currLine.append(w)
                currWidth += len(w) + 1
            else:
                lines.append((currLine, maxWidth - currWidth + 1))
                currLine = [w]
                currWidth = len(w) + 1
        lines.append((currLine, currWidth - maxWidth - 1))
        return self.printJustify(lines)

        