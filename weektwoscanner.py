"""
Scans a csv file redirected into the script
"--header" indicates the first row is a header row
"""
import sys as sys
import argparse

# python weektwoscanner.py < data.csv
# python weektwoscanner.py --header < data_with_header.csv

def scan(has_header=False):
    result = []
    values = []
    do_header = has_header
    header_names = {}
    try:
        for aline in sys.stdin: # executes for each line in file being read
                this_line = aline.strip().split(',') # from current line, removes whitespace from ends and separates values into array, pointed to by this_line
                if do_header: # executes if file has headers
                    header_names = this_line # points header_names to current array
                    do_header = False # sets do_header to false for future iterations
                else:
                    a_dict = {} # points a_dict to empty dictionary item
                    for i in range(0,len(this_line)): # executes for each element in current array
                        if has_header : # executes if has_header is true
                            a_dict[header_names[i]]= this_line[i] # appends ith element to a_dict under key of ith header
                        else:
                            a_dict[i]= this_line[i] # appends ith element to a_dict under key i

                    result += [a_dict] # appends a_dict to results array
                    values += [this_line] # appends this_line to values array
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return result,values

    return result,values

# Exercise one
def sum_of(column_name, a_list_of_dictionary):
    """
    Return one value that is the sum of the column 
    column_name of each "row" (dictionary)
    """
    result = 0
    for eline in a_list_of_dictionary:
        result = result + int(eline[column_name])
    return result

#Exercise Two
def multiple_cols(column_names, a_list_of_dictionary):
    """
    Return a new list of "rows" (dictionary)
    That multiples the values of the named columns
    
    """
    result = []
    for eline in a_list_of_dictionary:
        edict = {}
        mult = int(eline[column_names[0]])
        for i in range(1,len(column_names)):
            mult *= int(eline[column_names[i]])
        edict['Mult'] = mult
        result += [edict]
    return result


#Exercise Three
# - fix display_table so that the columns all line up
def display_table(a_list_of_dictionary):
    lines = ""
    # Get a header line
    a_dictionary = a_list_of_dictionary[0]
    header_line = ""
    for key in a_dictionary:
        header_line += f'{key.strip()}' + '        '[0:8-len(f'{key.strip()}')]

    # Make up the table
    lines += header_line 

    for a_dictionary in a_list_of_dictionary:
        a_line = ''
        for key,value in a_dictionary.items():
            a_line += f'{value.strip()}' + '        '[0:8-len(f'{value.strip()}')]
        a_line = a_line.strip()
        lines += f'\n{a_line}'
    print(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan some rows into a list of one list per line.")
    parser.add_argument('--header',action='store_true',help='The first row is a header row.')
    args = vars(parser.parse_args())
    print(f'The args are {args}')
    #args = sys.argv
    #print(f'The args are {args}')
    dict_lst,values_lst = scan(args['header'])
    display_table(dict_lst)
    print(sum_of('Value', dict_lst))
    print(multiple_cols(['Length', 'Width'], dict_lst))
