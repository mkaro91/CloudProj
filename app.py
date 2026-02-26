from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    # Landing Page Requirements
        # Upload Form
        # Instructions
        # File Input
    return "Placeholder Document App Index Page"

@app.route("/upload", methods=["POST"])
def upload_file():
    # Accept File Upload - main purpose
    # Validate File Type - Step 1
        # Check allowed extentions
            # .txt, .pdf, .docx, ???
            # Suggest using endswith() - Matt
    # Save temporarily - Step 2
        # Send file to uploads
    # Trigger processing - Step 3
        # Redirect to /processing
            # Eventually - return redirect("/process/filename")
    pass

@app.route("/process/<filename>")
def process_file(filename):
    # Read Document
    # Extract Text (text_extractor.py)
    # Generate Summary (summarizer.py)
    # Compute Stats (stats.py)
    pass

@app.route("/results/<doc_id>")
def results(doc_id):
    # Displays
        # Original Filename
        # Summary
        # Stats
            # Word Count
            # Sentence Count
            # Character count
            # Reading time estimate ?
            # Most common words ?
    pass

@app.route("/api/summarize", methods=["POST"])
def api_summarize():
    """
    Returns Example
    {
        "summary": ...,
        "word_count: 542,
        "sentence_count": 38,
        "top_words": ["Networking", "Cloud", "Chuck"]
    }
    """
    pass

@app.route("/delete/<doc_id>")
def delete(doc_id):
    # Remove file and any stored metadata
    pass

if __name__ == "__main__": app.run()