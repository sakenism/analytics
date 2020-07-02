import os
import plotly.graph_objects as go

from app import database

class JsPiscine:
	children_of_js_Query = """
	{
	  object_child(where: {parentId: {_in: [%s]}}, order_by: {index: asc}) {
		child {
		  id
		  name
		}
	  }
	}
	"""
	count_status = """
	{
	  obj1: progress_aggregate(where: {objectId: {_eq: %s},
			bestResult: {grade: {_gte: 1}}}) {
		aggregate {
		  count
		}
	  }
	  
	  obj0: progress_aggregate(where: {objectId: {_eq: %s},
			bestResult: {grade: {_lt: 1}}}) {
		aggregate {
		  count
		}
	  }
	}
	"""
	z01 = database.Hasura(os.getenv("HASURA_ADDR"), os.getenv("HASURA_SCRT"))
	
	def __init__(self):
		pass

	def get_children_array(self, query):
		children_of_js = self.z01.query(query)
		children_of_js = children_of_js['data']['object_child']
		tmp = []
		for child in children_of_js:
			tmp.append(child['child'])
		return tmp

	def get_children_str(self, arr):
		str_children_of_js = ""
		for child in arr:
			str_children_of_js = str_children_of_js + str(child['id']) + ','
		if len(str_children_of_js) > 0:
			str_children_of_js = str_children_of_js[:-1]
		return str_children_of_js

	def steps(self):
		js_id = "3402"
		children_of_js = self.get_children_array(self.children_of_js_Query % js_id)
		children_of_child = {}
		str_children_of_js = self.get_children_str(children_of_js)
		grandchildren_of_js = self.get_children_array(self.children_of_js_Query % str_children_of_js)
		str_grandchildren_of_js = self.get_children_str(grandchildren_of_js)
		map_ans = {}

		for grandchild in grandchildren_of_js:
			map_ans[grandchild['id']] = []
			res = self.z01.query(self.count_status % (grandchild['id'], grandchild['id']))
			positive = res['data']['obj1']['aggregate']['count']
			negative = res['data']['obj0']['aggregate']['count']
			map_ans[grandchild['id']].append({
				"name": grandchild['name'],
				"success": positive,
				"fail": negative
			})

		for child in children_of_js:
			map_ans[child['id']] = []
			res = self.z01.query(self.children_of_js_Query % str(child['id']))
			res = res['data']['object_child']
			children_of_child[child['id']] = res
			positive = 0
			negative = 0
			for tmp in res:
				positive = positive + map_ans[tmp['child']['id']][0]['success']
				negative = negative + map_ans[tmp['child']['id']][0]['fail']
			map_ans[child['id']].append({
				"name": child['name'],
				"success": positive,
				"fail": negative	
			})	

		bin_grandchildren_name = []
		bin_grandchildren_success = []
		bin_grandchildren_fail = []
		final_map = {}
		cnt = 0
		for child in children_of_js:
			for grand in children_of_child[child['id']]:
				final_map[cnt] = []
				final_map[cnt].append({
					"id": grand['child']['id'],
					"name": map_ans[grand['child']['id']][0]['name'],
					'success': map_ans[grand['child']['id']][0]['success'],
					"fail": map_ans[grand['child']['id']][0]['fail']
				})
				cnt = cnt + 1
				bin_grandchildren_name.append(map_ans[grand['child']['id']][0]['name'])
				bin_grandchildren_success.append(map_ans[grand['child']['id']][0]['success'])
				bin_grandchildren_fail.append(map_ans[grand['child']['id']][0]['fail'])
		data = [
			bin_grandchildren_name,
			bin_grandchildren_success,
			bin_grandchildren_fail
		]
		return data

js_piscine_model = JsPiscine()
