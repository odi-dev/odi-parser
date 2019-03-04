import csv, enum, json

class Asset(enum.Enum):
	LAND = '토지(소계)'
	BUILDING = '건물(소계)'
	VEHICLE = '부동산에 관한 규정이 준용되는 권리와 자동차 건설기계 선박 및 항공기(소계)'
	DEPOSIT = '예금(소계)'
	DEBT = '채무(소계)'
	STOCK = '유가증권(소계)'
	MEMBERSHIP = '회원권(소계)'
	NONPROFIT_CORPORATION = '비영리법인에 출연한 재산'
	POLITICAL_FUND = '정치자금법에 따른 정치자금의 수입 및 지출을 위한 예금계좌의 예금(소계)'
	DENIAL_NOTICE = '고지거부 및 등록제외사항(소계)'

def hasName(line):
	for data in line:
		if data.find("성명") > -1:
			return True
	return False

def parseColumn(line):
	# 본인과의 관계		재산의 종류		소재지 면적 등 권리의 명세		종전가액		증가액		감소액		현재가액		변동사유 
	column = ['relation', 'type', 'description', 'last_price', 'price_increase', 'price_decrease', 'price', 'reason']
	result = {}
	for index, data in enumerate(line):
		result[column[index]] = data.strip()
	
	return result



f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

name = ''
assetName = ''
assets = {}

for line in rdr:
	if line[0] == '' or line[0].find("총계") > -1:
		continue

	if hasName(line):
		name = line[5].strip()
		assetName = ''
		print(name)
	elif line[0].find("▶") > -1:
		assetName = Asset(line[0].replace("▶", "").strip()).name
		assets[assetName] = []
		print(assetName)
	else:
		if assetName != '':
			assets[assetName].append(parseColumn(line))
			print(parseColumn(line))

with open( name + '.json', 'w', encoding='UTF-8') as file:
     json_val = json.dumps(assets, ensure_ascii=False)
     #print(json_val)
     file.write(json_val)

f.close()

