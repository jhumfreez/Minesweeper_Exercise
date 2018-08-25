# Minesweeper Exercise

## Goal: This repo is an exercise to create a minesweeper-like game in various languages (Python3, C, C++, C#, Java), and algorithms (sorting and possibly tile traversal). It is largely just for fun.

###### The pseudocode is as follows:
*Determine area i x j; store i x j array of tiles with fields to store adjacency to mines, whether they contain mines, whether flagged, and whether they are revealed to the player.

*Plot mines; randomly choose a fair subset of the tiles to store mines

*Draw the play area: show X's for hidden tiles, F's for flagged tiles (set a maximum), or [number of adjacent mines].

*Player chooses whether to [D]etonate or [F]lag a tile with the coordinate <k><l>
	*Validate input
	*Mine: Gameover
	*Reveal tile adjacency field
		*>=1: Return
		*0: Recursive traversal and reveal of adjacent tiles, return on adjacency field >=1

*Win: All mines flagged

*On win: Append name of player and score (time bonus * area size) to a sorted highscore log (multiple sorting algorithms will be tested for experimentation) for printing
