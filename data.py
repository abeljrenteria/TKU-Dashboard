import pandas as pd

def unique_students(df):
    total = df['Student'].nunique()
    return total

def total_students(df):
    total = df['Student'].count()
    return total

def return_rates(df):
    returning_students_df = pd.DataFrame(df.groupby('Student').date.count()).reset_index().sort_values('date', ascending=False)
    returning_students_df.columns = ['STUDENT','VISITS']
    unique_students = df['Student'].nunique()
    return_students = (returning_students_df['VISITS'] > 1).sum()
    return_rate = ((return_students / unique_students).round(2)) * 100
    return return_rate

def total_revenue(df):
    total = df['Amount Paid'].sum()
    return total

def total_scholarship(df):
    total = df['Scholarship Amount'].count()
    return total

def amount_scholarship(df):
    total = df['Scholarship Amount'].sum()
    return total

def student_attendance(df):
    df = pd.merge(((df.groupby('date').first().reset_index())[['date', 'Workshop Name']]), (pd.DataFrame(df.groupby(['date'])['Student'].agg('nunique')).reset_index()), on='date', how='outer')
    x = df.date
    y = df['Student']
    labels = df['Workshop Name']
    
    return x, y, labels

def revenue_line_data(df):
    df = pd.merge(((df.groupby('date').first().reset_index())[['date', 'Workshop Name']]), (pd.DataFrame(df.groupby(['date'])['Amount Paid'].agg('sum')).reset_index()), on='date', how='outer')
    x = df.date
    y = df['Amount Paid']
    labels = df['Workshop Name']
    
    return x, y, labels

def scholarship_line_data(df):
    df = pd.merge(((df.groupby('date').first().reset_index())[['date', 'Workshop Name']]), (pd.DataFrame(df.groupby(['date'])['Scholarship Amount'].agg('sum')).reset_index()), on='date', how='outer')
    x = df.date
    y = df['Scholarship Amount']
    labels = df['Workshop Name']
    
    return x, y, labels
