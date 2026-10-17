# Step 1: Preloaded Feedbacks
feedback_data = { 
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'], 
'Feedback': [ 
'Very GOOD Service!!!', 
'poor support',
'GREAT experience! will come again.', 
'okay' 
'not BAD', 
'Excellent care, excellent staff!', 
'good food and good ambience!', 
'Poor response and poor handling of issue', 
'Satisfied. But could be better.', 
'Good support... quick service.' 
], 
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add More Feedbacks
n=int(input("How many more feedbacks do you want to add? : "))

for i in range(n):
    print(f"Enter details for feedback {i+1}")
    name = input("Enter Name : ")
    feedback = input("Enter written feedback : ")
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))

            if rating >= 1 and rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")

        except ValueError:
            print("Please enter a valid integer rating.")

   
    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print(feedback_data)


# Step 3: Text Cleaning
cleaned_feedbacks = []

for feedback in feedback_data['Feedback']:

    feedback = feedback.lower()

    feedback = feedback.replace('.', '')
    feedback = feedback.replace(',', '')
    feedback = feedback.replace('!', '')
    feedback = feedback.replace('?', '')

    feedback = ' '.join(feedback.split())

    cleaned_feedbacks.append(feedback)

feedback_data['Feedback'] = cleaned_feedbacks

print(feedback_data)


# Step 4: Word Count Insights
def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


print("\n--- Word Count Insights ---")
print("Feedbacks containing good:", count_word_in_feedbacks("good"))
print("Feedbacks containing poor:", count_word_in_feedbacks("poor"))
print("Feedbacks containing excellent:", count_word_in_feedbacks("excellent"))


# Step 5: Final Summary and Insights
print("\n--- Final Cleaned Feedback Data ---")
print(feedback_data)


# Average Rating

total_rating = sum(feedback_data['Rating'])
total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))


# Longest Feedback by Word Count

longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda feedback: len(feedback.split())
)

print("\n--- Longest Feedback ---")
print("Feedback:", longest_feedback)
print("Word Count:", len(longest_feedback.split()))


# Unique Words

unique_words = set()

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    unique_words.update(words)

print("\n--- Unique Words ---")
print(sorted(unique_words))

