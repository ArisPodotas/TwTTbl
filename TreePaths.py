from bigtree import tree_to_pillow, print_tree, add_path_to_tree, list_to_tree
import os
import subprocess

def main(files: bool = False, video: bool = False, directory: str = f".\\"):
	path = f"C:\\Users\\aris\\Desktop\\Documents\\University\\Diplomatic exercise\\Post start materials\\"
	path1a = f"{path}GROUP 2 INTRONS\\ALIGNMENTS"
	path1b = f"{path}GROUP 2 INTRONS\\Organism Data Individually ODI"
	path1c = f"{path}GROUP 2 INTRONS\\Separate intron information"
	path1d = f"{path}GROUP 2 INTRONS\\Trees"
	path2 = f"{path}ORFS\\"
	path3 = f"{path}PLASMIDS\\"
	os.makedirs(directory, exist_ok = True)
	if files:
		fpar = "file"
	else:
		fpar = "folder"
	folder_tree(path2, name = f"{directory}{fpar} ORFS tree", files = files, video = video)
	folder_tree(path1a, name = f"{directory}{fpar} ALIGNMENTS tree", files = files, video = video)
	folder_tree(path1b, name = f"{directory}{fpar} Organism Data Individually ODI tree", files = files, video = video)
	folder_tree(path1c, name = f"{directory}{fpar} Separate intron information tree", files = files, video = video)
	folder_tree(path1d, name = f"{directory}{fpar} Trees tree", files = files, video = video)
	# folder_tree(f"C:\\Users\\aris\\Desktop\\Documents\\software\\python files\\cs50P\\", f"{directory}cs50p folder tree", files = True)

def folder_tree(path: str, name: str , files: bool = True, video: bool = False):
	dirlist = []
	if not video:
		if files:
			for (dirpath, dirnames, filenames) in os.walk(path):
				for file in filenames:
					dirlist.append(os.path.join(dirpath, file))
			filetree = list_to_tree(dirlist, sep = '\\')
			print_tree(filetree, style = "rounded")
			pillow = tree_to_pillow(filetree)
			pillow.save(f'{name}.png')
		else:
			for (dirpath, dirnames, filenames) in os.walk(path):
				dirlist.append(dirpath)
			filetree = list_to_tree(dirlist, sep = '\\')
			print_tree(filetree, style = "rounded")
			pillow = tree_to_pillow(filetree)
			pillow.save(f'{name}.png')
	else:
		loop_num = 0
		dirlist.append(path)
		filetree = list_to_tree(dirlist, sep = '\\')
		if files:
			for (dirpath, dirnames, filenames) in os.walk(path):
				for file in filenames:
					loop_num += 1
					add_path_to_tree(filetree, os.path.join(dirpath, file), sep = '\\')
					print_tree(filetree, style = "rounded")
					pillow = tree_to_pillow(filetree)
					pillow.save(f'{name} frame_{loop_num}.png')
		else:
			for (dirpath, dirnames, filenames) in os.walk(path):
				loop_num += 1
				add_path_to_tree(filetree, dirpath, sep = '\\')
				print_tree(filetree, style = "rounded")
				pillow = tree_to_pillow(filetree)
				pillow.save(f'{name} frame_{loop_num}.png')
		subprocess.run(f"ffmpeg -framerate 12 -y -f image2 -i \"C:\\Users\\aris\\Desktop\\Documents\\software\\python files\\Mine\\folder tree view results\\{name} frame_%d.png\" \"C:\\Users\\aris\\Desktop\\Documents\\software\\python files\\Mine\\folder tree view results\\{name}.mp4\"")

if __name__ == "__main__":
	main(files = True, video = False, directory = f"C:\\Users\\aris\\Desktop\\Documents\\software\\Python\\Mine\\folder tree view\\")

