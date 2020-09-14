from sys import argv
import csv

def main():

	# check user input
	if len(argv) != 3:
		print("Input should be: python primer_disigner.py sequences.txt n-clusters")
		exit(1)

	file = open(argv[1], "r")
	sequences = []
	for line in file:
		sequences.append(line.rstrip("\r\n"))
	
	nclusters = int(argv[2])
	
	max_clusters = []
	number = 0
	#find all clusters
	while number < nclusters and len(sequences) > 0:
		clusters = clusterprogram(sequences)
		max_clusters.append(max(clusters, key= len))
		sequences = [e for e in sequences if e not in max(clusters, key= len)]
		number = number + 1
	
	print(max_clusters)
	
	with open("clusters.csv",'wb') as resultFile:
		wr = csv.writer(resultFile)
		for cluster in max_clusters:
			print(cluster)
			wr.writerow(cluster)
	
def clusterprogram(sequences):
	clusters = []
	for sequence in sequences:
		cluster = []
		cluster.append(sequence)

		# iterate over all sequences INCLUDING the sequence itself
		for compare in sequences:

			# store the overlap as 0 and not as 1
			overlap = []

			#compare sequences
			for substring in range(40):
				if sequence[substring] == compare[substring]:
					overlap.append(0)
				else:
					overlap.append(1)

			step = 0
			error = 0

			while error == 0:
				if sum(overlap[step:(step+10)]) > 2:
					error = 1
				step = step + 10

				# if there is enough overlap than the compared sequence is added to the cluster
				if step == 40 and error == 0:
					cluster.append(compare)
					error = 1

		clusters.append(cluster)
	return clusters


if __name__ == "__main__":
    main() 
