from flask import Flask, render_template, request, url_for, redirect
from text_extractor import extract_text
from summarizer import generate_summary
from stats import compute_stats
from werkzeug.utils import secure_filename
import os
from datetime import datetime


os.makedirs('uploads', exist_ok=True)

app = Flask(__name__)

results_store = {}

@app.route("/")
def index():
    # Landing Page Requirements
        # Upload Form
        # Instructions
        # File Input
    return render_template("index.html")

@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")

@app.route("/upload", methods=["POST", "GET"])
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
    
    if request.method == "GET":
        return redirect(url_for('index'))
    
    file = request.files.get('file')

    if file and file.filename:
        if file.filename.endswith((".txt", ".docx", ".pdf")):

            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            file.save(filepath)

            return redirect(url_for('process_file', filename=filename))

    return redirect(url_for('index'))

@app.route("/process/<filename>")
def process_file(filename):

    filepath = os.path.join('uploads', filename)

    file_extension = filename.rsplit('.', 1)[1].lower()

    text = extract_text(filepath, file_extension)

    summary = generate_summary(text)

    stats = compute_stats(text)

    # Store results
    results_store[filename] = {
        "summary": summary,
        "stats": stats
    }

    return redirect(url_for('results', doc_id=filename))

@app.route("/report/<doc_id>")
def results(doc_id):

    data = results_store.get(doc_id)

    if not data:
        return "No results found"

    return render_template(
        "report.html",
        filename=doc_id,
        filetype=doc_id.rsplit('.', 1)[1].upper(),
        upload_date=datetime.now().strftime("%Y-%m-%d"),
        summary=data["summary"],
        word_count=data["stats"]["word_count"],
        sentence_count=data["stats"]["sentence_count"],
        char_count=data["stats"]["char_count"],
        reading_time=data["stats"]["reading_time"],
        keyword_count=len(data["stats"]["common_words"])
    )

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

# Delete route to remove the file that was saved in uploads and the stored results in the results_store dictionary
@app.route("/delete/<doc_id>")
def delete(doc_id):

    filepath = os.path.join('uploads', doc_id)

    # Remove file
    if os.path.exists(filepath):
        os.remove(filepath)

    # Remove stored results
    results_store.pop(doc_id, None)

    return redirect(url_for('index'))

if __name__ == "__main__": 
    app.run(debug=True)