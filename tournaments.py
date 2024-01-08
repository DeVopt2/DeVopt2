# Simulate a sports tournament

import csv
import sys
import random
import math
import time

# Number of simluations to run. The tournaments range (10*1, 10**10, 10*5)
N = 1000


def main():

    sys.argv[1] = [2018m.csv]     
    
    # Ensure correct usage
    if len(sys.argv) != 1:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = [0]
    
    # Read teams into memory from file
    filename = sys.argv[1]
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for team in reader:
            team["rating"] = int(team["rating"])
            teams.append(team)
            reader = csv.DictReader(f[team]_csv
    

def wrapped1(func):
    def inner_wrapped_tournament_wincounts(*args, **kwargs):                           
        counts = {}
        for k in range(j):
            won  = team.count(winners)
            won +1
            counts1 = won 
            counts.update(counts1)
                func(*args, **kwargs)           
            return inner_wrapped_tournament_wincounts
        
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

def wrapped(func):
    def inner_wrapped_game(*args, **kwargs):        
        if return = True:                  
            inner_wrapped_round():
            team1 = team1["rating"] 
            team2 = random.team2["rating"]):
            
        else:                          
            inner_wrapped_round():
            team1 = random.team1["rating"] 
            team2 = team2["rating"]):
            	
                    
        def inner_wrapped_round(*args, **kwargs):
           team1 == team1["rating"]
           team2 == team2["rating"]):
           	
    	def inner_wrapped_tournament(*args, **kwargs):
                # Record the start time
         start_time = time.monotonic_ns()  
        # Record the end time
        end_time = time.monotonic_ns()

        # Calculate the elapsed time in nanoseconds
        elapsed_time_ns = end_time - start_time

        # Convert the elapsed time to the "0m0.000s" format
        elapsed_time_seconds = elapsed_time_ns / 1e9  # Convert nanoseconds to seconds
        minutes = int(elapsed_time_seconds // 60)
        seconds = elapsed_time_seconds % 60
        
        # Append the elapsed time to answers.txt
        with open("answers.txt", "a") as f:
            f.write(f"{minutes}m{seconds:.3f}s\n")
            f.write(f"{"""Which predictions, if any, proved incorrect as you increased the number of simulations?: 
                    \n\nusually long term relative frequency moves closer to theoretical  probability as the repititons gets larger.
                    \n\nSuppose you're charged a fee for each second of compute time your program uses.
                    After how many simulations would you call the predictions "good enough"?: 
                    \n\n at calculated relative frequency"""\n")
                func(*args, **kwargs)
            
            return inner_wrapped_tournament
        
        return inner_wrapped_round
    
    return inner_wrapped_game

@wrapped
def simulate_game(team1, team2):
    
    if team1["rating"] > team2["rating"]):
        return True
    else: 
         return False
   

@wrapped
def simulate_round(team1, team2 ):
    """Simulate a round. Return a list of winning teams."""    
    # Simulate games for all pairs of teams
    for i in range(0, len(teams):
        if team1["rating"]  >  team2["rating"])
            winners.append(teams1[i])
        else:
            winners.append(teams2[i])

            return winners

winners = []
@wrapped1
@wrapped
def simulate_tournament():
    """Simulate a tournament. Return name of winning team."""
    # TODO
      # Perform 10 and 10**10 (5) simulations here
    for j in range(10, 10**10, 10**5): 
        if team1["rating"]  >  team2["rating"]):
        
            winners  == team1
            winners +1
            counts = team1["rating"]   
            counts +1    
            counts.append(team1)        
              return team1_winning

        break
    else:
            winners  == team2
            winners +1
            counts = team2["rating"]   
            counts +1       
            counts.append(team2)        
              return team2_winning
    
if __name__ == "__main__":
    main()






    
    

    
    

    
        

