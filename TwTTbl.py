# Project made for the purpose of the paper Group II introns
# Project name TwTTbl
# Collaborators Aris Podotas
# Country: Greece
# City: Athens
# National and Kapodistrian University of Athens
# Date: 4-7/7/2024

# This file used the data.txt file in the same directory
import re
import random

def main():
	repr(path = "./Thesis materials/Trees/MIXTURES/Clustal/Iqtree/", tree = "STRIPPED_ORFLESS_CLUSTAL_RAW-alignment.nex.treefile", out = "C:/Users/aPodo/Documents/University/Research/ORFLESS AP B+S.nex.treefile")
	repr(path = "./Thesis materials/Trees/MIXTURES/Muscle/Iqtree/", tree = "RRRL CDS MUSCLE-alignment.nex.treefile", out = "C:/Users/aPodo/Documents/University/Research/RRRL AP B+S.nex.treefile")

def repr(path: str, tree: str, out: str, *args, **kwargs):
	# Input in a format that's mutable
	query = open(path + tree, "r")
	tree_file = query.readlines()
	query.close()
	# Output
	replacer = open(out, "w")
	longest = 50
	padding = 2
	transfer = 100
	# This variable is for the tree and all the regex substitutions that happen one by one below
	var = [line for line in tree_file if line.__contains__("tree tree_1")]
	def bootstrapper(input):
		# Bootstrap changes where anything uder 70 is changed to * and everything over is left blank
		first = re.sub(r'"(?:[0-6]?\d(?:\.\d{1,2})?)/(?:[0-6]?\d(?:\.\d{1,2})?)"', '"*/*"', input)
		second = re.sub(r'"(?:[7-9][0-9](?:\.\d{1,2})?|100)/(?:[7-9][0-9](?:\.\d{1,2})?|100)"', '""', first)
		third= re.sub(r'"[1-6]?[0-9]\.?(\d{0,2})?/(?:[7-9][0-9](?:\.\d{1,2})?|100)"', '"*/"', second)
		fo = re.sub(r'"(?:[7-9][0-9](?:\.\d{1,2})?|100)/[1-6]?[0-9]{1}\.?[0-9]{0,2}"', '"/*"', third)
		return fo
	def lookup(taxon: str, condition: dict = {r"Ascomycota": r"          " + r"+| | '", r"Basidiomycota": r"          " + r" |+| '", r"Nothing": r"          " + r" | |+'"}, data: str = "./data.txt"):
		"""Data should be a file with each line the taxonomic group you want and the organism name
		Retrun the symbolism based on the taxonomic group found."""
		draw = open(data, "r") 
		table = draw.readlines()
		draw.close()
		for line in table:
			if re.search(f"{taxon}", line, flags = re.IGNORECASE):
				for thing in condition:
					if re.search(thing, line):
						return condition[thing]
				return condition[r"Nothing"]
			continue
		return r"None"
	# For quick and easy replacement definitions
	def nested(pattern: str, grouping: str, symbol: str, spacing: int, iterator: list, subst: str, condition: str, query: str, num: int, *capture_groups, output = replacer, ids = {r"Ascomycota": r"          " + r"+| | '", r"Basidiomycota": r"          " + r" |+| '", r"Nothing": r"          " + r" | |+'"}, data: str = "./data.txt", **any):
		"""Please name your groups."""
		if re.search(grouping, query, flags = re.IGNORECASE):
			parameter = r""
			if subst:
				for parenthesis in re.search(subst, query).groups():
					parameter += parenthesis
			parameter += f"_{num}"
			num += 1
			parameter += (spacing - len(parameter)) * r" "
			if symbol:
				parameter += symbol
			if data:
				parameter += lookup(taxon = pattern.group('genus'), condition = ids, data = data)
			output.write(re.sub(subst, parameter, query, flags = re.IGNORECASE))
			for sh, sl in enumerate(tree_file):
				if re.search(condition, sl):
					iterator.append(re.sub(pattern.group('whole'), parameter, iterator[len(iterator) - 1], flags = re.IGNORECASE))
		return num
	for holder, line in enumerate(tree_file):
		# print(f"{holder}", end = " ")	# Matches only the begin taxa black names
		if match := re.search(r"^\t(?P<whole>'(?P<genus>(?:[a-zA-Z0-9-_\.]*?)* )(?P<species>(?:[a-zA-Z0-9-_\.]*?\s)*)(?P<Gene>(?:[a-zA-Z0-9-_\.]*?\s)+)(?P<intron>I\d{0,2} )(?P<orf>[a-zA-Z0-9-_\s\.]*?)')", line, flags = re.IGNORECASE):
			# print(match.group(2))
			mangrep = r"(?P<genus>^\t'(?:[a-zA-Z0-9-_\.]*?)* )(?P<species>(?:[a-zA-Z0-9-_\.]*?\s)*)(?:(?:[a-zA-Z0-9-_\.]*?\s)+)(?:I\d{0,2} )(?:[a-zA-Z0-9-_\s\.]*?)'"
			transfer = nested(num = transfer, pattern = match, query = line, spacing = longest + padding, symbol = r" |+| | | ", grouping = r"RTM'", iterator = var, condition = r"tree tree_1", subst = mangrep)
			transfer = nested(num = transfer, pattern = match, query = line, spacing = longest + padding, symbol = r"+| | | | ", grouping = r"RTME'", iterator = var, condition = r"tree tree_1", subst = mangrep)
			transfer = nested(num = transfer, pattern = match, query = line, spacing = longest + padding, symbol = r" | |+| | ", grouping = r"RTE'", iterator = var, condition = r"tree tree_1", subst = mangrep)
			transfer = nested(num = transfer, pattern = match, query = line, spacing = longest + padding, symbol = r" | | |+| ", grouping = r"LAGLIDADG'", iterator = var, condition = r"tree tree_1", subst = mangrep)
			transfer = nested(num = transfer, pattern = match, query = line, spacing = longest + padding, symbol = r" | | | |+", grouping = r"ORFLESS'", iterator = var, condition = r"tree tree_1", subst = mangrep)
			# print(line, end = "")
		elif re.search(r"tree tree_1", line):
			replacer.write(bootstrapper(var[len(var) - 1]))
		# Won't work if these arent added
		elif re.search(r'\tset.*"Arial"', line):
			replacer.write(re.sub(r'Arial', r"Monospaced", line))
		elif thing := re.search(r'\tset \w+\.fontSize=(\d\d?)', line):
			replacer.write(re.sub(thing.group(1), r"16", line))
		else:
			replacer.write(line)
	replacer.close()

if __name__ == "__main__":
	main()


