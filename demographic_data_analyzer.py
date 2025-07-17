import pandas as pd
import os


def calculate_demographic_data(print_data=True):
    # Ruta absoluta al archivo CSV (relativa al archivo .py)
    csv_path = os.path.join(os.path.dirname(__file__), 'adultdata.csv')

    # Lee el CSV
    df = pd.read_csv(csv_path)

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # Advanced education
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Percentage with salary >50K
    higher_education_rich = round(
        len(df[higher_education & (df['salary'] == '>50K')]) /
        len(df[higher_education]) * 100, 1
    )
    lower_education_rich = round(
        len(df[lower_education & (df['salary'] == '>50K')]) /
        len(df[lower_education]) * 100, 1
    )

    # Min work hours per week
    min_work_hours = df['hours-per-week'].min()

    # % of people who work min hours and earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        len(num_min_workers[num_min_workers['salary']
            == '>50K']) / len(num_min_workers) * 100,
        1
    )

    # Country with highest % of rich
    country_rich_pct = (
        df[df['salary'] == '>50K']['native-country'].value_counts() /
        df['native-country'].value_counts() * 100
    ).dropna()
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)

    # Most common occupation for those who earn >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:",
              highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
