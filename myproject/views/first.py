from django.http import Http404, HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from myproject.db import query

def users123(request):
	id = request.REQUEST.get('id','')
	age = request.REQUEST.get('age','')
	
	if id != '':
		sql = "SELECT * from users WHERE id= %s"
		param_for_user_details=[id]        
   
	elif age != '':
		sql = "SELECT * from users WHERE age= %s"
		param_for_user_details=[age]
	else:
		sql = "SELECT * from users"
		param_for_user_details=[]
	results = query(sql,*param_for_user_details)     
	final_test_map = []  
	metadata_totalcount=0 
    #result is constructed in the expected format
	for result in results:
		metadata_totalcount=metadata_totalcount+1
		response_map = {}
		response_map['id']=result['id']
		response_map['age']=result['age']                                                                                       
		final_test_map.append(response_map)       
	metadata = {"total_count":metadata_totalcount}
	response = {"metadata":metadata,'data_test':final_test_map} 
	data = json.dumps(response, encoding="ISO-8859-1")    
	http_response = HttpResponse(data,content_type="application/json")
	return http_response
	
def users999(request):
	id = request.REQUEST.get('id','')
	name = request.REQUEST.get('name','')
	address = request.REQUEST.get('address','')
	number = request.REQUEST.get('number','')
	
	if id != '':
		sql = "SELECT * from details WHERE id= %s"
		param_for_user_details=[id]        
   
	elif name != '':
		sql = "SELECT * from details WHERE name= %s"
		param_for_user_details=[name]
	elif address != '':
		sql = "SELECT * from details WHERE address=%s"
		param_for_user_details=[address]
	elif number !='':
		sql = "SELECT * from details WHERE number=%s"
		param_for_user_details=[number]
	else:
		sql = "SELECT * from details"
		param_for_user_details=[]
	results = query(sql,*param_for_user_details)     
	final_test_map = []  
	metadata_totalcount=0 
    #result is constructed in the expected format
	for result in results:
		metadata_totalcount=metadata_totalcount+1
		response_map = {}
		response_map['id']=result['id']
		response_map['name']=result['name']
		response_map['address']=result['address']
		response_map['number']=result['number']
		final_test_map.append(response_map)       
	metadata = {"total_count":metadata_totalcount}
	response = {"metadata":metadata,'data_test':final_test_map} 
	data = json.dumps(response, encoding="ISO-8859-1")    
	http_response = HttpResponse(data,content_type="application/json")
	return http_response
	
