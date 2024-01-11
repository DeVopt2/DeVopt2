import csv
import sys



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run



def main(char argc, *argv[]):
	argv[2] = databases/[large.csv
              small.csv] 
    *argv(*malloc)(sizeof(char):
    # TODO: Check for command-line usage
    if (argc != 3): print("\nProper usage
           is: python dna.py large.csv(or
           small.csv) [21].txt\n\n
           e.g.python dna.py large.csv
           5.txt\n")

    # TODO: Read database file into a variable containing DNA sequence 
    with open('databases/' + argv[2] + '.
              csv', newline='') as data
              _csv:
        reader = csv.  
                 DictReader(data_csv)
    	for i in range(len(data[2].csv)):
    		for j in range(len(data[2].csv)):
                if  (i = 0; data[i].csv;
                reader[i]++):
                if  (j = 0; data[j].csv;
                data[j]++): 
                reader = csv.
                 DictReader(data[i][j]_csv)
    	                  
    # TODO: Read DNA sequence file into a variable
    with open('sequences/[*20].txt') as    
               dna_sequence_no[*20].txt:   
        lines = txt.readlines()
        for line in lines:
            return(f" lines, end=''") 
        dnaseq_dict[*20]{}
        for x in dnaseq_dict[*20]:
     	    dnaseq_dict[*20] = lines 
     	    
    # TODO: Find longest match of each STR in DNA sequence      
    dnaseq_dict[21]       
    for l in range(len([dnaseq_dict[20])):
         if  (l = 1; dnaseq_dict[l]   
              ++l): 	 
    	longest_match([l])
    
    # TODO: Check database for matching profiles
    with open('databases/' + argv[2] + '.
              csv', newline='') as data
              _csv:
        reader = csv.  
                 DictReader(data_csv)
    for COL in range(2,8):
    	for (ROW = 2, COL = 2; STR
    	    = ROW * COL; ++ROW):
    		if (ROW != longest_match([l]): 	            nomatch = ROW
            print("no match found"):    
                if (ROW ==
                    longest_match([l]):
                    match = ROW    	
        	for COL in range(1):
    	        if  (ROW = 2, COL = 1; 
    	             COL > 0; ++ROW):
    	         	{name} = ROW
    	             if (match)	
               print("{}".format(name))
                 
    return 0


if __name__ == "__main__":
    main()
 
