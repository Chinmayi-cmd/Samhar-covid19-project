from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
#open a file,where you stored the pickled data
file=open("model.pkl","rb")

clf=pickle.load(file)
file.close()
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        mydict=request.form 
        FEVER=int(mydict["FEVER"])
        AGE=int(mydict["AGE"])
        BODYPAIN=int(mydict["BODYPAIN"])
        NOSE=int(mydict["NOSE"])
        BREATH=int(mydict["BREATH"])
     #code for inference
        input=[FEVER,BODYPAIN,AGE,NOSE,BREATH]
        infprob=clf.predict_proba([input])[0][1]
        print(infprob)
        return render_template("show.html",inf=round(infprob*100))
    
    return render_template("index.html")
    return render_template("about.html")
    
        #return "Infection probability of getting coronavirus:" +str(infprob)
if __name__ == "__main__":
     app.run(debug=True)