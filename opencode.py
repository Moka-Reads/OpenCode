from datetime import datetime, timedelta

def calculate_target_date(input_date):
    try:
        input_date = datetime.strptime(input_date, "%m-%d-%Y")
    except ValueError:
        return "Invalid date format. Please use mm-dd-yyyy."

    edition_date_start = input_date + timedelta(days=366)  # 1 year from input date
    edition_date_end = edition_date_start + timedelta(days=182)  # 0.5 year (181 days) after edition_date_start

    standalone_date_start = input_date + timedelta(days=548)  # 1.5 years from input date
    standalone_date_end = standalone_date_start + timedelta(days=182)  # 0.5 year (181 days) after standalone_date_start

    # Format the output
    output_str = f"From {input_date.strftime('%m-%d-%Y')}:\nEdition date: {edition_date_start.strftime('%m-%d-%Y')} - {edition_date_end.strftime('%m-%d-%Y')}\nStandalone date: {standalone_date_start.strftime('%m-%d-%Y')} - {standalone_date_end.strftime('%m-%d-%Y')}"
    
    return output_str

input_date = input("Enter a date in the format mm-dd-yyyy: ")
result = calculate_target_date(input_date)
print(result)
