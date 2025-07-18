import re


import shutil
import os


# Process the markdown file
# Now open file “oot.md” as read
# 1. Set counter = 1
# 2. Start a while loop to quit after reached end of file of “oot.md”.     
# 
# - Only Read the block of text between two  occurrences of “![[“ and next “![[” in file “oot.md” or EOF whichever comes first and place into variable D. 
#     variable D should only contains the block of text starting at ![[ and stopping before the next ![[. Skips any content before the first ![[
# - Copy variable B to BT
# - If counter is even replace the string PICPOS in BT with “image-container-L”, if counter is odd replace the string PICPOS in BT with “image-container-R”
# - Replace the string FNAME in BT with the image file name found between “![[“ and “]]” in variable D. 
# - Remove “![[image file]]” from D
# - Replace the string CTR in BT with the value of  counter. 
# - Replace the string TITLE in BT with the text found inside the font tag  e.g <font color ….> text </font> tags in variable D
# - Remove the font tags and its text from variable D
# - Replace the string “story” in BT with the text remaining in variable D 
# - Set A = A + BT
# - Increment counter
# - Go to top of loop. 
# 
# 4. Once EOF is reached and the loop is exited then set A = A + C
# 5. Finally write the variable A into “oot.html”. Overwrite “oot..html” if file exists. 
# 

def copy_file(src, dst):
    """
    Copy a file from src to dst in Python
    
    Args:
        src (str): Source file path
        dst (str): Destination path (can be directory or full file path)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Expand user paths (~) and get absolute paths
        src = os.path.abspath(os.path.expanduser(src))
        dst = os.path.abspath(os.path.expanduser(dst))
        
        # If destination is a directory, use the same filename
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
            
        # Check if source exists
        if not os.path.exists(src):
            print(f"Error: Source file '{src}' does not exist")
            return False
            
        # Check if destination directory exists
        if not os.path.exists(os.path.dirname(dst)):
            print(f"Error: Destination directory '{os.path.dirname(dst)}' does not exist")
            return False
            
        # Perform the copy
        shutil.copy2(src, dst)  # copy2 preserves metadata
        print(f"Successfully copied '{src}' to '{dst}'")
        return True
        
    except Exception as e:
        print(f"Error copying file: {str(e)}")
        return False
    

# 1. HTML Template (Variable A)
A = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Observations of Thought</title>
    <meta name="description" content="Sri Rao - Thoughts from reading, listening and walking in Chicago">
    <meta name="keywords" content="Sri Rao - Thoughts from reading, listening and walking in Chicago">
    <style>
        body {
            background-image: url('Bkgrnd.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center center;
            color: #eae6ef;
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            text-align: center;
        }

        .heading-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .image-container-L {
            width: 90%;
            margin: 0 auto;
            overflow: hidden;
            position: relative;
        }
        .image-container-L img {
            float: left;
            margin: 0 20px 20px 20px;
            max-width: 33%;
            height: auto;
            shape-outside: ;
            shape-margin: 10px;
        }
        .image-container-R {
            width: 90%;
            margin: 0 auto;
            overflow: hidden;
            position: relative;
        }
        .image-container-R img {
            float: right;
            margin: 0 20px 20px 20px;
            max-width: 33%;
            height: auto;
            shape-outside: ;
            shape-margin: 10px;
        }
        p {
            margin-bottom: 1em;
            text-align: left;
        }
        .highlight-text {
            color: #f09e5a;
            font-weight: bold;
            font-size: 1.1em;
        }
    </style>
</head>
<body>
    <div class="heading-container">
        <h1 style="font-size: 2.5em; margin: 0;">Observations of Thought</h1>
        <h2 style="font-size: 1.2em; margin: 0;">Listen, Read, Walk</h2>
        <h3 style="font-size: 1.3em; margin: 0;">~***~</h3>
    </div>
"""

# 2. Image Block Template (Variable B)
B = """
    <div class="PICPOS">
        <img src="FNAME" alt="Sample Image">
        <p><span class="highlight-text">CTR. TITLE</span></p>
        <p>story</p>
    </div>
"""

# 3. HTML Footer (Variable C)
C = """
</body>
</html>
"""

# Process the markdown file
if __name__ == "__main__":
    # Copy to a directory (keeps original filename)
    # copy_file("~/Documents/test.txt", "~/Desktop/")
    
    # Copy with new filename
    copy_file("/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/MyBooks/Observations of Thoughts.md", "//Users/sri/Library/Mobile Documents/iCloud~md~obsidian/Documents/Libravault/AA_Journal/MyBooks/oot/oot.md")

counter = 1

try:
    with open('oot.md', 'r', encoding='utf-8') as md_file:
        content = md_file.read()
        
        # Find all image blocks and their following content
        pattern = re.compile(r'!\[\[(.*?)\]\](.*?)(?=!\[\[|\Z)', re.DOTALL)
        matches = pattern.finditer(content)
        
        for match in matches:
            image_filename = match.group(1).strip()  # Content between ![[ and ]]
            D = match.group(2).strip()              # Content between ]] and next ![[
            
            # Create a new block from template
            BT = B
            
            # Set image container class (alternating left/right)
            container_class = 'image-container-R' if counter % 2 else 'image-container-L'
            BT = BT.replace('PICPOS', container_class)
            
            # Insert image filename
            BT = BT.replace('FNAME', image_filename)
            
            # Insert counter
            BT = BT.replace('CTR', str(counter))
            
            # Extract title from font tags if they exist
            title_match = re.search(r'<font[^>]*>(.*?)</font>', D)
            title_text = title_match.group(1).strip() if title_match else ''
            BT = BT.replace('TITLE', title_text)
            
            # Remove font tags from content
            D = re.sub(r'<font[^>]*>.*?</font>', '', D, flags=re.DOTALL)
            
            # Clean and format remaining content
            story_content = D.strip()
            story_content = re.sub(r'<[^>]+>', '', story_content)  # Remove HTML tags
            story_content = re.sub(r'\[\[.*?\]\]', '', story_content)  # Remove markdown links
            
            # Preserve paragraphs and convert newlines
            story_content = story_content.replace('\n\n', '</p><p>')  # Double newlines become paragraphs
            story_content = story_content.replace('\n', '<br><br>')      # Single newlines become line breaks
            story_content = f"<p>{story_content}</p>"  # Wrap in paragraph tags
            
            # Insert formatted content
            BT = BT.replace('<p>story</p>', story_content)
            
            # Add to main HTML
            A += BT
            counter += 1
            
except FileNotFoundError:
    print("Error: oot.md file not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# Add footer and write to file
A += C

try:
    with open('oot.html', 'w', encoding='utf-8') as html_file:
        html_file.write(A)
    print(f"Successfully created oot.html with {counter-1} image blocks")
except Exception as e:
    print(f"Error writing to oot.html: {e}")