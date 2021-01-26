### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
     # javascript works is client side rendering, Python is a server side   rendering
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
      # self.assertTrue and self.assertEqual
- What is a unit test?
      # a way to test one function or method
- What is an integration test?
      # a way to test multiple functions 
- What is the role of web application framework, like Flask?
      # a way the server and the client can communicate
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
      # if you want privacy or the URL contains long strings of information
- How do you collect data from a URL placeholder parameter using Flask?
      # when defining app.route, pass an argument and save it to sessions
- How do you collect data from the query string using Flask?
      # request.args.get( )
- How do you collect data from the body of the request using Flask?
      # request.form[]
- What is a cookie and what kinds of things are they commonly used for?
      # is a dictionary object that store expiry time, path and domain
- What is the session object in Flask?
      # data stored in client
- What does Flask's `jsonify()` do?
      # it a function that converts data into a json type object