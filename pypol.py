import os
import csv

csvpath=os.path.join('Resources','election_data.csv')

txtpath=os.path.join('Resources','result.txt')


totalvotes=0
candidates=[]
candi_votes={}
winner_count=0 
winner=""

with open(csvpath) as csvfile:
    csvredaer=csv.DictReader(csvfile)

    for row in csvredaer:
        totalvotes +=1
        candidate=row["Candidate"]
         
        if candidate not in candidates:
            candidates.append(candidate)
            candi_votes[candidate] = 1

        candi_votes[candidate]=candi_votes[candidate] + 1
        
with open(txtpath, 'w') as text_file:
    #Headerrrrrr
    elect_header=(
        f"Election Result \n"
        f"-------------------------\n"
        f"-------------------------\n"
        f"-------------------------\n"
        f'Total Vote : {totalvotes}\n  '
        f'""""""'""""""""""""'""""""\n'
    )

    print( f'Total Vote : {totalvotes}  ')
    text_file.write(elect_header)

    for candidate in candi_votes:
        votes=candi_votes[candidate]
        vote_percentage =float(votes)/float(totalvotes)*100
        if(votes >winner_count):
            winner_count= votes
            winner=candidate
        voter_output=f"{candidate}:{vote_percentage:.3f} % ({votes})\n"
        print(voter_output)
        
        text_file.write(voter_output)

    winning_sum= (
        f"Winner: {winner}"
     )
    
    print(winning_sum) 
    text_file.write(winning_sum)
