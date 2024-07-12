def hexa():
    part1 = " " + "--- " + "   "
    part2a = "/   \\"
    part2b = "___"
    part3 = "\\   /   "
    return part1, part2a, part2b, part3

def combine_hexagons(height,width ):
    lines = []
    for row in range(height):
        line1 = ""
        line2 = ""
        line3 = ""
        for col in range(width - height + 1):
            part1, part2a, part2b, part3 = hexa()
            line1 += part1
            if col == width - height:
                line2 += part2a
            else:
                line2 += part2a + part2b
            line3 += part3
        lines.append(line1)
        lines.append(line2.strip())
        lines.append(line3.strip())
    
    final_line1 = ""
    for col in range(width - height + 1):
        final_line1 += hexa()[0]
    lines.append(final_line1)
    
    return "\n".join(lines)


#when the input is 4 rows and 7 columns
hexagon_grid = combine_hexagons( 4,7)
print(hexagon_grid)
print()

#when the input is 3 rows and 5 columns
hexagon_grid = combine_hexagons( 3,5)
print(hexagon_grid)
