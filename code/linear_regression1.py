import numpy as np
import csv
def inverse(A):
	return np.linalg.inv(A)
def transpose(A):
	return np.transpose(A)
def main():
	#initializing the date list
	date=[[0 for i in range(4)] for j in range(165)]
	#opening the  dates2 file
	with open('../dates/dates2.csv','r') as f:
		reader=csv.reader(f,delimiter=',',quotechar='"',skipinitialspace=True)
		# read rows, append values to lists
		j=0
		#putting the value in date list
		for row in reader:
			i=0
			date[j][i]=1
			for i in range(3):
				try:
					date[j][i+1]=float(row[i])
				except ValueError:
					print (" Value Error on line",i)
			j+=1
	#initializing the opening price list
	price=[0 for i in range(165)]
	#opening the  opening price1 file
	with open('../feeding/opening_price1.csv','r') as f:
		reader=csv.reader(f,delimiter=',',quotechar='"',skipinitialspace=True)
		# read rows, append values to lists
		j=0
		#putting the value in price list
		for row in reader:
			for i in range(1):
				try:
					price[j]=float(row[i])
				except ValueError:
					print (" Value Error on line",i)
			j+=1
	#Performing formula operation on data to get the parameter dependencies
	A=transpose(date)
	B=np.matmul(A,date)
	C=inverse(B)
	D=np.matmul(A,price)
	E=np.matmul(C,D)
	#initializing the predicting date list
	date1=[[0 for i in range(4)] for j in range(104)]
	#opening the  dates_prediction1 file
	with open('../dates/date_prediction1.csv','r') as f:
		reader=csv.reader(f,delimiter=',',quotechar='"',skipinitialspace=True)
		# read rows, append values to lists
		j=0
		#putting the value in date1 list
		for row in reader:
			i=0
			date1[j][i]=1
			for i in range(3):
				try:
					date1[j][i+1]=float(row[i])
				except ValueError:
					print (" Value Error on line",i)
			j+=1
	#initializing the actual price list
	price1=[0 for i in range(104)]
	#opening the  actual_Price file
	with open('../actual/actual_Price.csv','r') as f:
		reader=csv.reader(f,delimiter=',',quotechar='"',skipinitialspace=True)
		# read rows, append values to lists
		j=0
		#putting the value in price1 list
		for row in reader:
			for i in range(1):
				try:
					price1[j]=float(row[i])
				except ValueError:
					print (" Value Error on line",i)
			j+=1
	#calculating predicted price for those dates
	price2=np.matmul(date1,E)
	avgError=0
	#printing actual and predicted price with the error percentage
	for i in range(104):
		error=((abs(price2[i]-price1[i]))/price1[i])*100
		avgError+=error
		print("Actual price",price1[i])
		print("Predicted price",price2[i])
		print("Error",error)
		print()
	#calculating and printing average error
	avgError/=104
	print("Average Error",avgError)
	print()
	#Taking input date for prediction
	date3=[0 for i in range(4)]
	date3[0]=1
	print("Enter the date for which price is to be predicted")
	date3[1]=int(input('Year:'))
	date3[2]=int(input('Month:'))
	date3[3]=int(input('Day:'))
	#calculating predicted price for the date
	price3=np.matmul(date3,E)
	#printing the predicted price
	print("Predicted Price:",price3)
if __name__ == "__main__":
	main()
