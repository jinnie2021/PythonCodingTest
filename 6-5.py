# Quick sort python specific

array = [ 5 , 7 , 9 , 0 , 3 , 1 , 6 , 2 , 4 , 8 ]

def quick_sort(array):
	print("Start sorting: ", array)
	# Terminate if list is empty array  
	if len(array) <= 1:
		return array
	
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot]
	print("left", left_side)
	right_side = [x for x in tail if x > pivot]
	print("right", right_side)
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
