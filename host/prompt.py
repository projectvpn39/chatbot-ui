prompt_for_classfication = """
I want you to classify prompts into one of 6 categories:

1.  Image-related
    Any prompt that involves generating, modifying, or describing an image, pictures, photos
    Examples:
    Generate an image of a cat
    Create a picture of a dog running through a field
    Can you make a photo editing to combine these two faces?
    
2.  Code-related
    Except for those asking the database, which should be classified as 4
    Any prompt that involves writing code or explaining code
    
    Examples:
    Write a function in Python to calculate the factorial of a number
    Can you explain what a for loop does in JavaScript?
    
3.  Email-sender
    Any prompt that involves writing an email, or sending an email
    Examples:
    Please draft an email to john@example.com asking about the status of the project
    Can you write an email to sales@company.com inquiring about pricing for a custom order?
    
4.  Document, database related
    Any prompt that involves updating / deleting documents in a database, listing files in a database, searching and answering questions about files in a database
    If start with something like "According to my database...", it should be this category
    Examples:
    What documents in the database relate to Project X?
    Please update the status for entry 12345 in the database to Completed
    According to the database, what is the status of Project Y?
    
5.  Selling product
    Any prompt that involves selling the product, or buying the product, or enquires about our company product
    Examples:
    I want to buy a blue model of the Acme Widget. Do you have this in stock?
    Can you tell me more about the features of the Deluxe Gizmo? I'm interested in purchasing one.
    
6.  Question-answering
    Any prompt that is asking a question that requires a factual answer
    Or any casual talk
    If you think it is not Image-related or Code-related, classify it as this one
    Examples:
    What is the capital of France?
    How are you doing today?
    Can you recommend a good restaurant in town for dinner?
    
I will provide a prompt. Your response should be the number corresponding to the category that best fits the prompt. Only respond with '1', '2' or '3', etc.

Do not provide any additional explanation or text besides the category number.

Now classify this prompt: {prompt}
"""


prompt_for_image_description = """
Given a prompt for generating an image, extract a descriptive summary of the main elements that the image should contain. 

The description should be reasonably concise while capturing the key details. Do not include any explanatory text. Just return the description as a string.

Prompt: Generate an image of a cute puppy playing with a ball in a field of flowers on a sunny day. The puppy is fluffy and brown with floppy ears. 
Description: a fluffy brown puppy with floppy ears playing with a ball in a field of flowers on a sunny day

Prompt: Make an image of a blue and red parrot perched on a branch of a rainforest tree. The parrot has bright feathers and looks down curiously. Lush green leaves surround it.
Description: a blue and red parrot with bright feathers perched on a rainforest tree branch surrounded by green leaves

Prompt: {prompt}
Description:
"""


prompt_for_image_modified = """
I will provide a prompt describing a request to modify generated images. Please parse the prompt and return a string in the format 'mode,index' based on the following:

I have 4 image indexes - 1, 2, 3, 4 (top left, top right, bottom left, bottom right)

Modes:

new: Generate a new image on a completely different topic. Return 'new,1'.
upscale: Enlarge or upscale an existing image. Return 'upscale,index'.
variation: Make changes to an existing image. Return 'variation,index'.
reset: Regenerate the existing images with the same prompts. Return 'reset,1'.
Do not return anything else besides the mode and index.

Examples:

Prompt: Can you draw a cat instead of a dog?
Ans: new,1

Prompt: Please zoom in on the top right image.
Ans: upscale,2

Prompt: Can you make some changes to the bottom left image?
Ans: variation,3

Prompt: Let's redo these with the same prompts.
Ans: reset,1

Prompt: {prompt}
Ans:
"""

prompt_for_email_content = """
Please draft the following email body in HTML format, with appropriate HTML tags for structure and formatting, on behalf of the user.

User request:
{request}

User background:
name: {user_name}
position: {user_position}   
boss_name: {boss_name}

"""
prompt_for_subject_line = """

Please review the email content, and give back the suitable subject line, 

here is the email content:
{content}
"""

prompt_file_uploader_routing = """
Please classify this user prompt into one of the following categories, and extract the relevant information from the prompt. Return the extracted information in JSON format:

Upload file - Return {"purpose": "upload", "file_path": "file path"}

Search file and answer question - Return {"purpose": "search", "query": "search query"}

Delete file - Return {"purpose": "delete", "file_id": "id"}

List files - Return {"purpose": "list"}

Upload file and search - Return {"purpose":"upload_and_search","file_path":"file path","query":"search query"}

Examples:

Prompt: I want to upload the file located at ./test.txt
Ans: {"purpose": "upload", "file_path": "./test.txt"}

Prompt: What is the best language for AI according to the database?
Ans: {"purpose": "search", "query": "What is the best language for AI?"}

Prompt: Delete file 12345
Ans: {"purpose": "delete", "file_id": "12345"}

Prompt: Show me all files
Ans: {"purpose": "list"}

Prompt: Based on the file I uploaded, what is the best language for AI?
Ans: {"purpose":"upload_and_search","file_path":"./test.txt","query":"What is the best language for AI?"}


"""
