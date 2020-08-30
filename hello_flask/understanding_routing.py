from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')        # New "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'         # Return the string 'Dojo!' as a response


#      @app.route('/say/flask')        # New "@"                                             now want this all in one function
#      def say_flask1():
#          return 'Hi Flask!'         # Return the string 'Hi Flask!' as a response          now want this all in one function   
#      
#      @app.route('/say/michael')        # New "@"                                           now want this all in one function    
#      def say_flask2():
#          return 'Hi Michael!'         # Return the string 'Hi Michael!' as a response      now want this all in one function          
#      
#      
#      @app.route('/say/john')        # New "@"                                              now want this all in one function
#      def say_flask3():
#          return 'Hi John!'         # Return the string 'Hi John!' as a response            now want this all in one function


@app.route('/say/<name>')        # New "@"   # for a route '/say/____' anything after '/say/' gets passed as a variable 'name'
def say(name):
    return ('hi ' + name + '!')*3 # Return the string 'Shut yo mouth ' + [input name] as a response


@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    for x in range(1, int(num)):
       # print("<word> ")
        return word * int(num)


# ninja bonus gets error type error  @app.route('/repeat1/<num1>/<num2>')
# ninja bonus gets error type error  def repeat1(num1, num2):
# ninja bonus gets error type error      #for x in range(1, int(num)):
# ninja bonus gets error type error         # print("<word> ")
# ninja bonus gets error type error      num3 = int(num1) + int(num2)
# ninja bonus gets error type error      print (int(num3))
# ninja bonus gets error type error      return num1 + num2


@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "You Suck, " + name



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.