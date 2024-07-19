import pandas as pd

student_data={
    "Name":["Barun","Kumar","verma","mahto","kushwaha"],
    "Age":[23,43,44,23,13],
    "Marks":[490,433,390,245,245]
}
df=pd.DataFrame(student_data)
print(df)