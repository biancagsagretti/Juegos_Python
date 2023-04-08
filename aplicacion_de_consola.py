import random

class  QA : 
  def  __init__ ( self ,  question ,  correctAnswer ,  otherAnswers ): 
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList  =  [ QA ( "Elige la opción escrita corrrectamente:",  "Where is the school?" ,  [ "Where are the school?" ,  "Who is school?" ]), 
QA ( "Elija la opción que tenga el orden correcto:" ,  "They are not sleeping now" ,  [ "They not are sleeping now" ,  "They now are not sleeping" ,  "They sleeping are not now" ])]

corrCount  =  0 
random.shuffle( qaList ) 
for  qaItem  in  qaList : 
  print ( qaItem.question ) 
  print ( "Las posibles respuestas son:" ) 
  possible  =  qaItem . otherAnsw  +  [ qaItem . corrAnsw ]  # los corchetes convierten la respuesta correcta en una lista para concatenarla con otra lista 
  random.shuffle ( possible ) 
  count  =  0  # listas de índices comienzan en 0 en Python 
  while  count  <  len ( possible ): 
    print ( str ( count + 1 )  +  ":"  +  possible [ count ]) 
    count  +=  1 
  print ( "Por favor ingrese el número de su respuesta: " ) 
  userAnsw  =  input () 
  while not  userAnsw . isdigit (): 
    print ( "Ese no era un número. Ingresa el número de tu respuesta:" ) 
    userAnsw  =  input () 
  userAnsw  =  int ( userAnsw ) 
  while not  userAnsw  >  0  and  userAnsw  <=  len ( possible):
    print ( "Ese número no corresponde a ninguna respuesta. Ingresa el número de tu respuesta:" ) 
    userAnsw  =  input () 
  if possible [ userAnsw - 1 ]  ==  qaItem . corrAnsw : 
    print ( "Tu respuesta fue correcta." ) 
    corrCount  +=  1 
  else : 
    print ( "Tu respuesta fue incorrecta." ) 
    print ( "La respuesta correcta fue:"  +  qaItem . corrAnsw ) 
  print ( "" )

print ( "Respondiste"  +  str ( corrCount )  +  "de"  +  str ( len ( qaList ))  +  "preguntas correctamente." )
