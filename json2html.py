# import os
# os.system('pip install json2table')
import json2table
import json

f = open('./index.json',)
  
data = json.load(f)
infoFromJson = json.loads(f)
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style": "width:100%"}
table = json2table.convert(infoFromJson, 
                         build_direction=build_direction, 
                         table_attributes=table_attributes)
f = open( 'docs/validation-result.html', 'w' )
f.write( table )
f.close()