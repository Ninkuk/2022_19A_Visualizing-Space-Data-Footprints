from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def filter_image_paths(image_paths):
    filtered_paths = []
    for path in image_paths:
        index = path.find("/static")
        filtered_paths.append(path[index:])
    
    return filtered_paths

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_demo', methods=['GET', 'POST'])
def demo():
    # POST request
    if request.method == 'POST':
        image_paths = request.get_json()
        image_paths = filter_image_paths(image_paths) 
        print("image_paths", image_paths)

        #TODO YOUR CODE HERE Ninad
        '''
            image_paths is an array of the demo images selected. Since they're saved locally, it only contains
            the local path. The path should look something like "/static/img/X.jpg"
            
            What you need to do is iterate through these images and pass them through your algorithm that finds
            the interception points. Then create the CSV file from those interception points

            A problem is how do we save the CSV file generated on the frontend for the user. The solution
            I came up with is that this function returns the contents of the CSV file as a string to the frontend,
            of which I download the file there.
        '''
        CSV_file_content = "Lorem Ipsum"

        return CSV_file_content, 200

@app.route('/submit_uploads', methods=['GET', 'POST'])
def uploads():
    # POST request
    if request.method == 'POST':
        file_paths = request.get_json()
        
        # Use this function to remove everything before 
        print("file_paths", file_paths)

        #!
        #TODO READ Ninad
        '''
            So for now I'm just passing in the URL of the images uploaded.
            For whatever reason, the URL starts with "blob:", and if removed, the browser wouldn't find the file.

            I don't have .fits or .xml to test the output on, but you should have access to file paths at this stage

            Anyways, when you're done with passing data to the backend and then creating the CSV, just follow
            the instructions of the previous function's TODO comment. I explain there what to do
        '''
        CSV_file_content = "Lorem Ipsum"

        return CSV_file_content, 200

if __name__ == "__main__":
    app.run(debug=True)