our_dict = {
    "float":[],
    "bool":[],
    "none":[],
    "int":[],
    "str":[]
}


class FilterList:

    def __init__(self, our_list: list):
        self.our_list = our_list

    def filter_list(self):
        for output in self.our_list:
            if float == type(output):
                our_dict["float"].append(output)
            elif bool == type(output):
                our_dict["bool"].append(output)
            elif None == type(output):
                our_dict["none"].append(output)
            elif int == type(output):
                our_dict["int"].append(output)
            elif str == type(output):
                our_dict["str"].append(output)

Result = FilterList([1, 4.7, "hi", False, None])
Result.filter_list()
print(our_dict)
