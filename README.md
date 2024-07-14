# Overview

TwTTbl Stand for Tree with a Taxonomic Table, this program uses a already made phylogenetic tree to add symbolism to the names automatically so that one does not need to parse the treefile on their own

## Preview

Tree before interpretations

![image](https://github.com/user-attachments/assets/355e0a3f-da30-40be-a4af-8e586a93983b)

Tree after interpretation

![image](https://github.com/user-attachments/assets/1e1a75f0-614e-4944-830f-dde3d7d6da9f)

# Bootstrapping

This program parses the tree in a Nexus format and changes all the bootstrap values (assumes that the bootstrap has one NJ-bootstrap and one Bayesian/Likelyhood ratio value) to a format where all values less than 70 turn to "*". 

## Example

Value: 24.5/77 -> "\*/ "
Value: 88/77 -> ""
Value: 24.5/18.8-> "\*/\*"
Value: 100/48.8-> " /\*"

## Formatting

The text is changed to a monospaced font and needs align labels enabled to represent the table in a readable way so that the collumns in the names are aligned

The data.txt file is for a preview of the format that the taxonomic groups have to be outside of your phylogenetic tree for the program to work properly
