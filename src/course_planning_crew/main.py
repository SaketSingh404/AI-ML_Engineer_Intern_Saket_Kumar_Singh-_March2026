import os
import csv
from course_planning_crew.crew import CollegePlanningCrew

def run():
    """
    The entry point required by 'crewai run'.
    This will run the sample interaction for your demo. [cite: 119, 131]
    """
    sample_query = "I'm a CS major and I've finished MATH120. What do I need before enrolling in Database Systems?"

    print(f"\n--- Processing Sample Query: {sample_query} ---\n")
    inputs = {'user_input': sample_query}

    # Initialize and kickoff the crew [cite: 119]
    result = CollegePlanningCrew().crew().kickoff(inputs=inputs)

    print("\n" + "="*50)
    print("FINAL AGENTIC RESPONSE")
    print("="*50)
    print(result)

def run_single_query(query):
    """Runs a single interaction for demonstration purposes."""
    print(f"\n--- Processing Query: {query} ---\n")
    inputs = {
        'user_input': query
    }
    # Initialize and kickoff the crew [cite: 119]
    result = CollegePlanningCrew().crew().kickoff(inputs=inputs)
    return result


def run_evaluation_set():
    """
    Executes the mandatory 25-query test set and saves to CSV. [cite: 103-106, 120]
    Categories: Prereq checks (10), Prereq chains (5), Program reqs (5), Trick questions (5).
    """
    test_queries = [
        # 1. 10 Prerequisite Checks (Eligible/Not Eligible) [cite: 104]
        "Can I take CS301 if I've taken CS101 and MATH120?",
        "I've completed Introduction to Biology. Can I enroll in Genetics next term?",
        # ... add 8 more similar queries based on your chosen catalog ...

        # 2. 5 Prerequisite Chains (Multi-hop) [cite: 105]
        "What is the full sequence of courses I need to take before Advanced AI?",
        "If I want to take the Senior Capstone, what 3-course chain must I complete first?",
        # ... add 3 more ...

        # 3. 5 Program Requirement Questions [cite: 106]
        "How many elective credits do I need for a Minor in Data Science?",
        "What are the residency requirements for graduation in this program?",
        # ... add 3 more ...

        # 4. 5 'Not in docs' / Trick Questions [cite: 106]
        "Who is the easiest professor for Organic Chemistry?",
        "What time is the CS101 final exam scheduled for this semester?",
        # ... add 3 more ...
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

    # Save results for your Report [cite: 107, 120]
    keys = results_log[0].keys()
    with open('evaluation_results.csv', 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(results_log)

    print("\nEvaluation complete. Results saved to 'evaluation_results.csv'.")

if __name__ == "__main__":
    # 1. Run a sample interaction for the demo [cite: 119, 131]
    sample_query = "I'm a CS major and I've finished MATH120. What do I need before enrolling in Database Systems?"
    final_output = run_single_query(sample_query)

    print("\n" + "="*50)
    print("FINAL AGENTIC RESPONSE")
    print("="*50)
    print(final_output)

    # 2. Uncomment the line below to run the full 25-query evaluation for your report [cite: 120]
    # run_evaluation_set()