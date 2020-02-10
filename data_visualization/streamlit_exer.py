import streamlit as st 
import numpy as np 
import pandas as pd 


st.title("My first app")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
		'first column': [1,2,3,4],
		'second column': [10, 20, 30, 40]
	}))

df = pd.DataFrame({
		'first column': [1,2,3,4],
		'second column': [10, 20, 30, 40]})
# df


# 画折线图
chart_data = pd.DataFrame(
		np.random.randn(20, 3),
		columns = ['a', 'b', 'c']
	)
st.line_chart(chart_data)


# 画地图
# map_data = pd.DataFrame(
# 		np.random.randn(10, 2) / [50, 50] + [37.76, -122.4],
# 		columns = ['lat', 'lon']
# 	)
# st.map(map_data)


# 增加交互  
if st.checkbox('Show dataframe'):
	chart_data = pd.DataFrame(
			np.random.randn(20, 3),
			columns = ['a', 'b', 'c']
		)
	st.line_chart(chart_data)


# 在一侧增加小工具
option = st.sidebar.selectbox(
		'Which number do you like best?',
		df['first column']
	)
'You selectbox', option


# 显示过程
import time 

'Starting a long comution...'
# add a placeholder 
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
	# update the progress bar with each iteration 
	latest_iteration.text(f"Iteration {i+1}")
	bar.progress(i+1)
	time.sleep(0.1)
'...and now we\'re done'