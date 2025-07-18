
import re
import shutil
import os

# Process the markdown file
# Now open file "oot.md" as read
# 1. Set counter = 1
# 2. Start a while loop to quit after reached end of file of "oot.md".     
# 
# - Only Read the block of text between two occurrences of "![[" and next "![[" in file "oot.md" or EOF whichever comes first and place into variable D. 
#     variable D should only contains the block of text starting at ![[ and stopping before the next ![[. Skips any content before the first ![[
# - Copy variable B to BT
# - If counter is even replace the string PICPOS in BT with "image-container-L", if counter is odd replace the string PICPOS in BT with "image-container-R"
# - Replace the string FNAME in BT with the image file name found between "![[" and "]]" in variable D. 
# - Remove "![[image file]]" from D
# - Replace the string CTR in BT with the value of counter. 
# - Replace the string TITLE in BT with the text found inside the font tag e.g <font color ….> text </font> tags in variable D
# - Remove the font tags and its text from variable D
# - Replace the string "story" in BT with the text remaining in variable D 
# - Set A = A + BT
# - Increment counter
# - Go to top of loop. 
# 
# 4. Once EOF is reached and the loop is exited then set A = A + C
# 5. Finally write the variable A into "oot.html". Overwrite "oot.html" if file exists. 

# CHanges:
# Title Page as First Page: Added a dedicated page-0 with your title content
# Pagination System:
#     - Each image/text block now lives in its own full-screen .page div
#     - Only one page visible at a time with smooth transitions
#     - Navigation Arrows:
#     - Appear when hovering over left/right 20% of screen
#     - Clicking arrows navigates between pages
#     - Visual arrow indicators using CSS triangles
#     - Swipe Gestures:
#     - Touchstart/touchend event listeners
#     - Left swipe = next page, Right swipe = previous page
#    -  50px threshold for swipe detection
# Dynamic Slider:
#     - Appears when mouse enters bottom 1/8 of screen
#     - Black background with opacity
#     - Shows current page/total pages
#     - Can drag to specific pages
#     - Auto-updates during navigation
#     - Responsive Design:
#     - Works on both mobile (touch) and desktop (mouse)
#     - Prevents accidental zooming with viewport meta tag
#     - Visual Improvements:
# Consistent 1.5em spacing between paragraphs
# Better floating image handling
# Smooth opacity transitions between pages
# The code maintains all your original content processing while adding the new navigation features. 
# The slider and page count are automatically calculated based on the number of entries found in your markdown file.
# 
# CHANGES:
#     - add Down key, right key and page down key for next page. 
#     - add up key, left key and page up key for prev page.
#     - Changed slider background to rgba(0,0,0,0.5)
#     - Added backdrop-filter: blur(5px) for frosted glass effect


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

# 1. HTML Template (Variable A) - Now with pagination
A = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
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
            overflow: hidden;
            touch-action: pan-y;
        }

        .page {
            width: 100vw;
            height: 100vh;
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            transition: opacity 0.5s ease;
            overflow-y: auto;
            padding: 20px;
            box-sizing: border-box;
        }

        .page.active {
            opacity: 1;
            z-index: 1;
        }

        .heading-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            gap: 0.5rem;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }

        .nav-arrow {
            position: fixed;
            top: 0;
            height: 100vh;
            width: 10vw;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
            cursor: pointer;
            backdrop-filter: blur(5px); /* Frosted glass effect */
            background: rgba(0,0,0,0.1); /* More transparent background */
        }

        .nav-arrow.left {
            left: 0;
        }

        .nav-arrow.right {
            right: 0;
        }

        .nav-arrow:hover {
            opacity: 1;
            background: rgba(0,0,0,0.2);
        }

        .nav-arrow::after {
            content: "";
            border: solid rgba(255,255,255,0.9);
            border-width: 0 4px 4px 0;
            display: inline-block;
            padding: 15px;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .left::after {
            transform: rotate(135deg) scale(1.2);
            margin-left: 10px;
        }

        .right::after {
            transform: rotate(-45deg) scale(1.2);
            margin-right: 10px;
        }

        .nav-arrow:hover::after {
            border-color: #f09e5a;
        }

        .slider-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 12.5vh;
            background: rgba(0,0,0,0.3); /* Doubled transparency */
            z-index: 20;
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-top: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 -5px 15px rgba(0,0,0,0.3);
            backdrop-filter: blur(5px); /* Frosted glass effect */
        }

        .slider {
            width: 80%;
            margin: 10px auto;
            -webkit-appearance: none;
            height: 6px;
            background: rgba(255,255,255,0.2);
            border-radius: 3px;
            outline: none;
            opacity: 0.8;
            transition: opacity 0.2s;
        }

        .slider:hover {
            opacity: 1;
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: #f09e5a;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .slider::-webkit-slider-thumb:hover {
            transform: scale(1.2);
            background: #ffb366;
        }

        .slider-info {
            color: white;
            font-size: 1.1em;
            font-family: Arial, sans-serif;
            margin-top: 5px;
            text-shadow: 0 1px 2px rgba(0,0,0,0.5);
        }

        .slider-info span {
            color: #f09e5a;
            font-weight: bold;
        }

        .image-container {
            width: 90%;
            margin: 0 auto;
            overflow: hidden;
            position: relative;
        }

        .image-container img {
            float: left;
            margin: 0 20px 20px 20px;
            max-width: 50%;
            height: auto;
            shape-outside: margin-box;
            shape-margin: 10px;
            border-radius: 3px;
        }

        .image-container.right img {
            float: right;
        }

        .highlight-text {
            color: #f09e5a;
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 1.5em;
        }

        /* Paragraph spacing */
        p {
            margin-bottom: 1.5em; /* 1.5 line spacing */
            text-align: left;
            line-height: 1.6; /* Increased line height */
        }

        /* Additional spacing for paragraphs within story content */
        .page p {
            margin-bottom: 1.5em;
        }

        /* Spacing after line breaks */
        br {
            display: block;
            content: "";
            margin-top: 0.75em; /* Half of paragraph spacing */
        }
    </style>
</head>
<body>
    <!-- Title Page -->
    <div class="page active" id="page-0">
        <div class="heading-container">
            <h1 style="font-size: 2.5em; margin: 0;">Observations of Thought</h1>
            <h2 style="font-size: 1.2em; margin: 0;">Listen, Read, Walk</h2>
            <h3 style="font-size: 1.3em; margin: 0;">~***~</h3>
        </div>
    </div>
"""

# 2. Image Block Template (Variable B) - Updated for pagination
B = """
    <div class="image-container PICPOS">
        <img src="FNAME" alt="Sample Image">
        <p><span class="highlight-text">CTR. TITLE</span></p>
        <p>story</p>
    </div>
"""

# 3. HTML Footer (Variable C) - Now with navigation controls
C = """
    <!-- Navigation Arrows -->
    <div class="nav-arrow left" id="prev-arrow"></div>
    <div class="nav-arrow right" id="next-arrow"></div>

    <!-- Slider Container -->
    <div class="slider-container" id="slider-container">
        <input type="range" min="0" max="TOTALPAGES" value="0" class="slider" id="page-slider">
        <div class="slider-info">Page <span id="current-page">1</span> of <span id="total-pages">TOTALPAGES</span></div>
    </div>

    <script>
        let currentPage = 0;
        const totalPages = TOTALPAGES;
        const pages = document.querySelectorAll('.page');
        const slider = document.getElementById('page-slider');
        const currentPageDisplay = document.getElementById('current-page');
        const totalPagesDisplay = document.getElementById('total-pages');

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            totalPagesDisplay.textContent = totalPages;
            updateSlider();
            
            // Touch events for swipe
            let touchStartX = 0;
            let touchEndX = 0;
            
            document.body.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
            }, false);
            
            document.body.addEventListener('touchend', (e) => {
                touchEndX = e.changedTouches[0].screenX;
                handleSwipe();
            }, false);
            
            // Mouse hover for slider
            document.body.addEventListener('mousemove', (e) => {
                const bottomArea = window.innerHeight - (window.innerHeight / 8);
                if (e.clientY > bottomArea) {
                    document.getElementById('slider-container').style.display = 'flex';
                }
            });
            
            document.getElementById('slider-container').addEventListener('mouseleave', () => {
                document.getElementById('slider-container').style.display = 'none';
            });

            // Keyboard navigation
            document.addEventListener('keydown', (e) => {
                switch(e.key) {
                    case 'ArrowRight':
                    case 'ArrowDown':
                    case 'PageDown':
                        nextPage();
                        break;
                    case 'ArrowLeft':
                    case 'ArrowUp':
                    case 'PageUp':
                        prevPage();
                        break;
                }
            });
        });

        // Navigation functions
        function goToPage(pageNum) {
            if (pageNum < 0 || pageNum > totalPages) return;
            
            pages[currentPage].classList.remove('active');
            currentPage = pageNum;
            pages[currentPage].classList.add('active');
            updateSlider();
        }

        function nextPage() {
            if (currentPage < totalPages) goToPage(currentPage + 1);
        }

        function prevPage() {
            if (currentPage > 0) goToPage(currentPage - 1);
        }

        function handleSwipe() {
            if (touchStartX - touchEndX > 50) {
                nextPage(); // Left swipe
            } else if (touchEndX - touchStartX > 50) {
                prevPage(); // Right swipe
            }
        }

        function updateSlider() {
            slider.value = currentPage;
            currentPageDisplay.textContent = currentPage + 1;
        }

        // Event listeners
        document.getElementById('next-arrow').addEventListener('click', nextPage);
        document.getElementById('prev-arrow').addEventListener('click', prevPage);
        
        slider.addEventListener('input', (e) => {
            goToPage(parseInt(e.target.value));
        });

        // Hide slider after 3 seconds if not hovering
        let sliderTimeout;
        document.getElementById('slider-container').addEventListener('mouseenter', () => {
            clearTimeout(sliderTimeout);
        });

        document.getElementById('slider-container').addEventListener('mouseleave', () => {
            sliderTimeout = setTimeout(() => {
                document.getElementById('slider-container').style.display = 'none';
            }, 3000);
        });
    </script>
</body>
</html>
"""

# Process the markdown file
if __name__ == "__main__":
    # Copy to a directory (keeps original filename)
    # copy_file("~/Documents/test.txt", "~/Desktop/")
    
    # Copy with new filename
    copy_file("/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/Observations of Thoughts.md", 
              "/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/WalkingNotes/Img_wn/oot.md")

    counter = 1
    pages = []

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
                container_class = 'right' if counter % 2 else 'left'
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
                
                # Preserve paragraphs with proper 1.5 line spacing
                story_content = story_content.replace('\n\n', '</p><p style="margin-bottom:1.5em;">')  # Double newlines become paragraphs
                story_content = story_content.replace('\n', '<br><br style="display:block; margin-bottom:0.75em;">')  # Single newlines with half spacing
                story_content = f"<p style=\"margin-bottom:1.5em;\">{story_content}</p>"  # Wrap in paragraph tags
                
                # Insert formatted content
                BT = BT.replace('<p>story</p>', story_content)
                
                # Create a new page for this entry
                page_html = f'<div class="page" id="page-{counter}">{BT}</div>'
                pages.append(page_html)
                counter += 1
                
    except FileNotFoundError:
        print("Error: oot.md file not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

    # Add all pages to the HTML
    for page in pages:
        A += page

    # Update total pages count in footer
    total_pages = counter - 1  # Subtract 1 because counter starts at 1
    A = A.replace('TOTALPAGES', str(total_pages))
    C = C.replace('TOTALPAGES', str(total_pages))

    # Add footer and write to file
    A += C

    try:
        with open('oot.html', 'w', encoding='utf-8') as html_file:
            html_file.write(A)
        print(f"Successfully created oot.html with {total_pages} content pages")
    except Exception as e:
        print(f"Error writing to oot.html: {e}")