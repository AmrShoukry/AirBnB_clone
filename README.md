instructions for starting:
  you can start the command interpreter by moving to the root folder (/AirBnB_clone).
  after starting it you will see a prompt in the form of (hbnb), this means that the program is running  successfully

here is a list of the commands that you can use and an example -or more- for each of them:

1-quit: this command exits the command line interpreter.

2-create: this command takes one argument in the form of the class that you wish to create.
the possible arguments are as follow:
  a.BaseModel
  b.User
  c.State
  d.City
  e.Amenity
  f.Place
  g.Review
example of usage:
  create BaseModel
  output will be the id of the class instance that was just created

3-show: this command shows all the attributes of a certain instance that has been created, it needs two arguments, the name of the class that the instance belongs to and the id of the instance.
example of usage:
  show BaseModel 12353
  output will be all of the attributes of the class

4-destroy: this command destroys an instance of a class that has been created before, its usage is much similar to the usage of show, you specify the name of the class that the instance belongs to and the id of the instance.
example of usage:
  destroy BaseModel 12354
  there will be no output printed on the terminal.

5-all: this command shows the string representation of all the classes that are currently stored in storage, you can call it without any argument to show all string representations of all class instances or specify a specific class to show all its members, the possible arguments are the same as 2-create
example of usage:
  a.all
  output will be all of the instances stored
  b.all BaseModel
  output will be all of the BaseModel instances stored

6-update: this command will update a specfic instance of a class with the variable that you specify, you specify the name of the class, the id of the instance, specify the variable you want to change or add, specify the value of the variable you want to change.
example of usage:
  update BaseModel 12354 name "Ahmed Hamed"
  there will be no output
