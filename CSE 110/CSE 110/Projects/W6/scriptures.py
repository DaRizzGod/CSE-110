# largest_chapter = 0
# largest_book = ""
# largest_scripture = ""

# with open ('books_and_chapters.txt') as file:
#   for line in file:
#     stripped_line = line.strip()
#     split_line = sstripped_line.split(":")
    
#     scripture = split_line[0]
#     chapters = float(split_line[1])
#     book = split_line[2]
    
#     if largest_chapter < chapters:
#       largest_chapter = chapters
#       largest_book = book
#       largest_scripture = scripture
      
# print(f'The largest book is {largest_book} with {largest_chapter} chapters and is {largest_scripture}')


largest_chapter = 0
largest_book = ''
largest_scripture = ''

with open ("books_and_chapter.txt") as file:
  for line in file:
    stripped_line = line.strip()
    split_line = stripped_line.split(":")
    
    scripture = split_line[0]
    chapters = float(split_line[1])
    book = split_line[2]
    
    if largest_chapter < chapters:
      largest_chapter = chapters
      largest_book = book
      largest_scripture = scripture
      
print(f'The largest book is {largest_book} with {largest_chapter} chapters and is {largest_scripture}')

selected_scripture = input("Which volume of scripture are you interested in? ")
for line in file:
        stripped = line.strip()
        split = stripped.split(":")

        book = split[0]
        chapters = int(split[1])
        scripture = split[2]
        if scripture.lower() == selected_scripture.lower():
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

        if largest_chapter < chapters and scripture.lower() == selected_scripture.lower():
            largest_chapter = chapters
            largest_book = book
            largest_scripture = scripture
print(f"The largest book of scripture, with {largest_chapter} chapters, is {largest_book} in the {largest_scripture}.")
