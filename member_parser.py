import urllib.request
import xml.etree.ElementTree as ET


def getMemberDetailInfoList(deptCd, num):
	url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberDetailInfoList' + '?serviceKey=%2Fu2AU25IoxIFRV9%2FnJzYS%2FI7CyEQ8LR%2FPFSbvSSJjzIGD2OLDUmPfnTCvyy0t0wOAa7t7eaF8nVCD4u0QmkQWw%3D%3D' + '&numOfRows=10&pageNo=1' + '&dept_cd=' + deptCd + '&num=' + num 
	request = urllib.request.Request(url)


	response = urllib.request.urlopen(request)
	rescode = response.getcode()
	if(rescode==200):
	  response_body = response.read()
	  # print(response_body.decode('utf-8'))

	  root = ET.fromstring(response_body.decode('utf-8'))
	  item = root.find('body').find('item')

	  name = item.find('empNm').text if item.find('empNm') is not None else None
	  name_en = item.find('engNm').text if item.find('engNm') is not None else None
	  name_zh = item.find('hjNm').text if item.find('hjNm') is not None else None
	  birth_date = item.find('bthDate').text if item.find('bthDate') is not None else None
	  party = item.find('polyNm').text if item.find('polyNm') is not None else None
	  precinct = item.find('origNm').text if item.find('origNm') is not None else None
	  committee = item.find('shrtNm').text if item.find('shrtNm') is not None else None
	  elected_count = item.find('reeleGbnNm').text if item.find('reeleGbnNm') is not None else None
	  elected_number = item.find('electionNum').text if item.find('electionNum') is not None else None
	  office_phone = item.find('assemTel').text if item.find('assemTel') is not None else None
	  homepage = item.find('assemHomep').text if item.find('assemHomep') is not None else None
	  email = item.find('assemEmail').text if item.find('assemEmail') is not None else None
	  staff = item.find('staff').text if item.find('staff') is not None else None
	  secretary = item.find('secretary').text if item.find('secretary') is not None else None
	  assistant = item.find('secretary2').text if item.find('secretary2') is not None else None
	  hobby = item.find('hbbyCd').text if item.find('hbbyCd') is not None else None
	  speciality = item.find('examCd').text if item.find('examCd') is not None else None
	  profile = item.find('memTitle').text if item.find('memTitle') is not None else None
	  id_code = num

	  print(name)
	  print(name_en)
	  print(name_zh)
	  print(birth_date)
	  print(party)
	  print(precinct)
	  print(committee)
	  print(elected_count)
	  print(elected_number)
	  print(office_phone)
	  print(homepage)
	  print(email)
	  print(staff)
	  print(secretary)
	  print(assistant)
	  print(hobby)
	  print(speciality)
	  print(profile)
	  print(id_code)

	# else:
	#   print("Error Code:" + rescode)




url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberCurrStateList' + '?serviceKey=%2Fu2AU25IoxIFRV9%2FnJzYS%2FI7CyEQ8LR%2FPFSbvSSJjzIGD2OLDUmPfnTCvyy0t0wOAa7t7eaF8nVCD4u0QmkQWw%3D%3D' + '&numOfRows=999&pageNo=1' 
request = urllib.request.Request(url)


response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
  response_body = response.read()
  # print(response_body.decode('utf-8'))
  root = ET.fromstring(response_body.decode('utf-8'))
  items = root.find('body').find('items')
  for item in items:
  	deptCd = item.find('deptCd').text
  	num = item.find('num').text
  	getMemberDetailInfoList(deptCd, num)

# else:
#   print("Error Code:" + rescode)
