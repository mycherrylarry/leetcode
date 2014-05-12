#!/usr/bin/env ruby

class Util
    def quickSort(li)
        if li.count == 0 or li.count == 1
            return li
        end
        pivot = li.pop()
        lesser = quickSort(li.select {|item| item <= pivot})
        bigger = quickSort(li.select {|item| item >  pivot})
        return lesser << pivot << bigger
    end

    def binarySearch(li, target)
        i, j = 0, li.count
        while i <j do
            mid = (i+j)/2
            case li[mid] <=> target
            when 0
                return mid
            when -1
                i = mid + 1
            else
                j = mid
            end
        end
        return -1
    end
end

util = Util.new()
li = [4,3,2,1]
puts util.quickSort(li)
li = [0, 1,2,3,4,5]
puts util.binarySearch(li, -1)
puts util.binarySearch(li, 0)
puts util.binarySearch(li, 5)
puts util.binarySearch(li, 6)
puts util.binarySearch(li, 7)
