import os
import csv
from course_planning_crew.crew import CollegePlanningCrew

def run():
    print("\n--- Academic Assistant Interactive Mode ---")
    user_q = input("Enter your course planning question: ")

    if user_q.strip():
        inputs = {'user_input': user_q}
        # Initialize and kickoff the crew
        result = CollegePlanningCrew().crew().kickoff(inputs=inputs)

        print("\n" + "="*50)
        print("AGENTIC RESPONSE")
        print("="*50)
        print(result)
    else:
        print("Query cannot be empty.")
    # print("\n--- Starting Mandatory 25-Query Evaluation Set ---")
    # run_evaluation_set()

def run_single_query(query):
    """Runs a single interaction for demonstration purposes."""
    print(f"\n--- Processing Query: {query} ---\n")
    inputs = {
        'user_input': query
    }
    # Initialize and kickoff the crew
    result = CollegePlanningCrew().crew().kickoff(inputs=inputs)
    return result


def run_evaluation_set():
    """
    Executes the mandatory 25-query test set and saves to CSV.
    Categories: Prereq checks (10), Prereq chains (5), Program reqs (5), Trick questions (5).
    """
    test_queries = [
        # 1. 10 Prerequisite Checks (Eligible/Not Eligible)
        "I have completed Maths-1 / I. Can I enroll in Maths-2 / II next semester?",
        "Can I take OOPS if I only have a grade of B+ in Programming Fundamentals?",
        "I am currently taking Machine Learning. Can I register for Deep Learning if it requires Machine Learning as a prerequisite?",
        "Is it possible to take MC205  and MC210 at the same time if they are co-requisites?",
        "Can I enroll in CH317 as an undergraduate student?",
        "Does EP306 require 'instructor consent' before I can register?" ,
        "I have a 'Pass' grade in CS208. Does this satisfy the prerequisite for CS319?" ,
        "Can I take BT206 if I am a Software Engineering student?",
        "If I failed CS318 once but am retaking it, can I sign up for the follow-up course CS427 now?",

        # 2. 5 Prerequisite Chains (Multi-hop)
        "What is the full sequence of courses I must complete, starting from the beginning, to eventually take Minor in Machine Learning?",
        # "I want to take [Advanced AI]. Can you list every prerequisite I need to finish first, including their own prerequisites?",
        # "If I've only taken [Course A], how many more semesters of prerequisites do I need before I can take [Final Year Course]?",
        "Trace the requirement path for Sustainable Inftastructure. What are the three foundation courses that start this chain?",
        # "I want to reach [Specialized Elective]. Does this path require me to take [Math Course] before I start the [Major] sequence?",


        # 3. 5 Program Requirement Questions
        "How many total elective credits do I need to complete a Major in Software Engineering?",
        "What are the minimum residency requirements (credits taken on campus) to graduate from this program?",
        "Can I count Data Structures toward both my Major and my Minor requirements?",
        "What courses I need to take to do Minor in Machine Learning ?",
        "List the three different categories of General Education requirements I must fulfill for this degree.",

        # 4. 5 'Not in docs' / Trick Questions
        "Which professor is considered the 'easiest' grader for Maths?",
        "What time and building is the Machine Design final exam held in this semester?",
        "I missed the registration deadline. Can you give me the home phone number of the Department Head to ask for an exception?",
        "Which of these two electives is more useful for getting a high-paying job in Silicon Valley?",
        "How many students are currently on the waitlist for Mechanics of Solids?"
    ]

    results_log = []
    print(f"Starting Evaluation of {len(test_queries)} queries...")

    for i, query in enumerate(test_queries, 1):
        print(f"Evaluating {i}/{len(test_queries)}...")
        try:
            output = run_single_query(query)
            results_log.append({
                "query": query,
                "output": output,
                "has_citation": "Citations:" in str(output) and "http" in str(output)
            })
        except Exception as e:
            results_log.append({"query": query, "output": f"Error: {str(e)}", "has_citation": False})

    keys = results_log[0].keys()
    with open('evaluation_results.csv', 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(results_log)

    print("\nEvaluation complete. Results saved to 'evaluation_results.csv'.")

# if __name__ == "__main__":
#     # sample_query = "I'm a CS major and I've finished MATH120. What do I need before enrolling in Database Systems?"
#     # final_output = run_single_query(sample_query)

#     # print("\n" + "="*50)
#     # print("FINAL AGENTIC RESPONSE")
#     # print("="*50)
#     # print(final_output)

    # run_evaluation_set()