# import os
# os.system('pip install json2table')
import json2html
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