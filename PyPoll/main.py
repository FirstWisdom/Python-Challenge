import os
import csv

csv_file = os.path.join("..", "Resources", "election_data.csv")
output_file = os.path.join("..", "Resources", "election_data_summary.csv")


def total_votes_func():
	with open('election_data.csv', 'r') as election_data_file:
	    edr = csv.reader(election_data_file)
	    election_data_header = next(election_data_file)
	    total = 0
	        
	    for row in edr:
	        if row[0] is not None:
	            total += 1
	    return total
	
total_votes_func()
total_votes = total_votes_func()


candidates_list = ['Khan', 'Correy', 'Li', 'O\'Tooley']
	

def cand_num_votes_func():
	with open('election_data.csv', 'r') as election_data_file:
	    edr = csv.reader(election_data_file)
	    election_data_header = next(election_data_file)
	    candidates_list = ['Khan', 'Correy', 'Li', 'O\'Tooley']
	    dict_total = {}
	    total = 0
	    total2 = 0
	    total3 = 0
	    total4 = 0
	        
		for row in edr:
	        if row[2] == 'Khan':
	            total += 1
	        elif row[2] == 'Correy':
	            total2 += 1
	        elif row[2] == 'Li':
	            total3 += 1
	        elif row[2] == 'O\'Tooley':
	            total4 += 1
	    dict_total['Khan'] = total
	    dict_total['Correy'] = total2
	    dict_total['Li'] = total3
	    dict_total['O\'Tooley'] = total4
		return dict_total

cand_num_votes_func()
cand_num_votes = cand_num_votes_func()
	

def cand_percent_votes_func():
	dict_percent['Khan'] = str(round(dict_num_votes['Khan'] / total_votes * 100, 2)) + '%'
	dict_percent['Correy'] = str(round(dict_num_votes['Correy'] / total_votes * 100, 2)) + '%'
	dict_percent['Li'] = str(round(dict_num_votes['Li'] / total_votes * 100, 2)) + '%'
	dict_percent['O\'Tooley'] = str(round(dict_num_votes['O\'Tooley'] / total_votes * 100, 2)) + '%'
	return dict_percent
	    
cand_percent_votes_func()
cand_percent_votes = cand_num_votes_func()	


winner = max(dict_num_votes, key = dict_num_votes.get)


election_results = (
	f"Election Results"
	f"-------------------------"
	f"{candidates_list[0]}: {cand_percent_votes['Khan']} ({dict_total['Khan']})"
	f"{candidates_list[1]}: {cand_percent_votes['Correy']} ({dict_total['Correy']})"
	f"{candidates_list[2]}: {cand_percent_votes['Li']} ({dict_total['Li']})"
	f"{candidates_list[3]}: {cand_percent_votes['O\'Tooley']} ({dict_total['O\'Tooley']})"
	f"-------------------------"
	f"Winner: {winner}"
	f"-------------------------"
)


print(election_results)

with open(output_file, "w") as txt_file:
    txt_file.write(election_results)