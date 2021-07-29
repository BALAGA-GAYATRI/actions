import os
os.system('pip install json2html')
# import json2html
from json2html import *

import json

f = open('./index.json', encoding='utf-8')
  
infoFromJson = json.load(f)
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style": "width:100%"}
# table = json2table.convert(infoFromJson, 
#                          build_direction=build_direction, 
#                          table_attributes=table_attributes)
table = json2html.convert(json = infoFromJson)
f = open( 'docs/validation-result.html', 'w' )
f.write( table )
f.close()
f = open('docs/validation-result.html', 'a')  
f.write("""<link rel="stylesheet" href="validation-result.css" type="text/css" media="all">
           <script>
            window.onload = function color() {
                console.log('test')
                var value = document.getElementsByTagName("td");
                for (var j = 0; j < value.length; j++) {
                    if (value[j].innerHTML == "No") { 
                    value[j].style.backgroundColor = "#ff8080";
                    }
                    if (value[j].innerHTML == "Access reqd") { 
                    value[j].style.backgroundColor = "#ffffcc";
                    }
                }
            }
            </script>
         """)
f.close()