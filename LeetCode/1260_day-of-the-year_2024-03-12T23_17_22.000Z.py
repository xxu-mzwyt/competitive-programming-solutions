# https://leetcode.com/problems/day-of-the-year

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(i) for i in date.split('-')]
        leap = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
        monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap:
            monthDays[2] += 1
        dayNum = 0
        for i in range(1, month):
            dayNum += monthDays[i]
        dayNum += day
        return dayNum
