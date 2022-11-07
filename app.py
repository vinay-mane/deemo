from flask import Flask,request,app,render_template

app = Flask(__name__)

# def getText(image):
#   return(pytesseract.image_to_string(image))

@app.route('/',methods=['POST','GET'])
def wetImage():
    return "helo"
    


if __name__=="__main__":
    app.run(debug=True)