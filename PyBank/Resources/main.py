import os
import csv

csv_file = os.path.join("..", "Resources", "budget_data.csv")
output_file = os.path.join("..", "Resources", "budget_data_analysis.csv")
	
def total_months_func():
	with open('budget_data.csv', 'r') as budget_data_file:
	    bdr = csv.reader(budget_data_file)
	    total = 0
	        
	    for row in bdr:
	        if 'Jan' in row[0] or 'Feb' in row[0] or 'Mar' in row[0] or 'Apr' in row[0] or 'May' in row[0] or 'Jun' in row[0] or 'Jul' in row[0] or 'Aug' in row[0] or 'Sep' in row[0] or 'Oct' in row[0] or 'Nov' in row[0] or 'Dec' in row[0]:
	            total += 1
	    return total
	    
total_months_func()
total_months = total_months_func()
	

def net_amount_func():
	with open('budget_data.csv', 'r') as budget_data_file:
	    bdr = csv.DictReader(budget_data_file)
	    total = 0
	        
	    for row in bdr:
	        row_val = int(row['Profit/Losses'])
	        total += row_val
	    return total
	    
net_amount_func()
net_amount = net_amount_func()

	
def ave_change_func():
	with open('budget_data.csv', 'r') as budget_data_file:
	    bdr = csv.reader(budget_data_file)
	    total = 0
	        
	for row in bdr:
	    if '10' in row[1]:
	        total += row    
	return total

ave_change_func()  
ave_change = ave_change_func()
	

def great_prof_inc():
	with open('budget_data.csv', 'r') as budget_data_file:
	    bdr = csv.reader(budget_data_file)
	    y = 0
	    arr = []
	
	    for row in bdr:
	        if '10' in row[0] or '11' in row[0] or '12' in row[0] or '13' in row[0] or '14' in row[0] or '15' in row[0] or '16' in row[0] or '17' in row[0]:
	            y = int(row[1])
	            if y > 1:
	                arr.append(y)
	    max_val = max(arr)
	    str_val = str(max_val)
	        
	    return str_val
	            
great_prof_inc_func()
great_prof_inc = great_prof_inc_func()
	
def great_loss_dec():
	with open('budget_data.csv', 'r') as budget_data_file:
	    bdr = csv.reader(budget_data_file)
	    x = 0
	    z = 0
	    arr = []
	
	    for row in bdr:
	        if '10' in row[0] or '11' in row[0] or '12' in row[0] or '13' in row[0] or '14' in row[0] or '15' in row[0] or '16' in row[0] or '17' in row[0]:
	            x = int(row[1])
	            if x < 0:
	                arr.append(x)
	    max_val = max(arr)
	    str_max = str(max_val)
	      
	    return str_max
	
great_loss_dec_func()
great_loss_dec = great_loss_dec_func()


budget_summary = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: {net_amount}\n"
    f"Average Revenue Change: {ave_change}\n"
    f"Greatest Increase in Revenue: {great_prof_inc}\n"
    f"Greatest Decrease in Revenue: {great_loss_dec}"
)

print(budget_summary)

with open(output_file, "w") as txt_file:
    txt_file.write(budget_summary)
