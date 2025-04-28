from main import DFA, Node, parseDFA, minimizeDFA, ProductConstruction
import time

"""
Objectives:
Measure how DFA minimization affects the execution time for determining if a string is accepted or rejected.

Evaluate how DFA minimization impacts the number of states in the DFA after product construction.

Conditions:
Compare performance and state size:
After product construction (union, intersection)
    - before minimization
    - after minimization

To run: python test_minimization.py
"""

def main():
    dfa1 = parseDFA("dfa/dfa1.json")
    dfa2 = parseDFA("dfa/dfa2.json")
    dfa3 = parseDFA("dfa/dfa3.json")
    dfa4 = parseDFA("dfa/dfa4.json")
    dfa5 = parseDFA("dfa/dfa5.json")
    dfa6 = parseDFA("dfa/dfa6.json")
    dfa7 = parseDFA("dfa/dfa7.json")
    dfa8 = parseDFA("dfa/dfa8.json")

    DFA_list = [
        dfa1,
        dfa2,
        dfa3,
        dfa4,
        dfa5,
        dfa6,
        dfa7,
        dfa8
    ]


    # Union DFAs
    dfa1_union_dfa2 = ProductConstruction(dfa1, dfa2, 'union')
    dfa1_union_dfa3 = ProductConstruction(dfa1, dfa3, 'union')
    dfa2_union_dfa4 = ProductConstruction(dfa2, dfa4, 'union')
    dfa3_union_dfa5 = ProductConstruction(dfa3, dfa5, 'union')
    dfa4_union_dfa6 = ProductConstruction(dfa4, dfa6, 'union')
    dfa5_union_dfa6 = ProductConstruction(dfa5, dfa6, 'union')
    dfa6_union_dfa7 = ProductConstruction(dfa6, dfa7, 'union')
    dfa6_union_dfa8 = ProductConstruction(dfa6, dfa8, 'union')
    dfa7_union_dfa8 = ProductConstruction(dfa7, dfa8, 'union')
    dfa1_union_dfa8 = ProductConstruction(dfa1, dfa8, 'union')

    test_dfa1_union_dfa2 = ["0" + "1"*100, "1"*99 + "1", "0"*50 + "1"*50, "1"*200 + "0", "0"*300]
    test_dfa1_union_dfa3 = ["0" + "0"*100, "1"*99, "00001", "0"*999 + "2", "1"*100 + "0"*100]
    test_dfa2_union_dfa4 = ["1"*500 + "1", "010101", "000101000", "1001"*30 + "1", "0"*500 + "101"]
    test_dfa3_union_dfa5 = ["1"*100, "0002", "110", "0"*200 + "1", "100100100100"]
    test_dfa4_union_dfa6 = ["101" + "0"*100, "0"*4 + "1"*5, "101" * 10, "1"*50 + "0"*20, "0"*100 + "101"]
    test_dfa5_union_dfa6 = ["110110", "1"*10 + "0"*8, "0"*100, "1"*15 + "0"*4, "111000111000"]
    test_dfa6_union_dfa7 = ["1"*10 + "0"*4, "000001", "10101" * 5, "1"*500 + "01", "0000" + "1"*10]
    test_dfa6_union_dfa8 = ["1"*6, "0"*400 + "1"*5000, "1"*15 + "0"*4, "111000" * 10, "1"*9 + "0"*8]
    test_dfa7_union_dfa8 = ["111"*1000, "1"*4 + "01", "0"*100 + "01", "1"*9, "1101" * 50]
    test_dfa1_union_dfa8 = ["0" + "1"*1000, "111" * 50, "0" + "0"*200, "1"*6, "1"*8 + "0"]

    union_tests = [
        test_dfa1_union_dfa2,
        test_dfa1_union_dfa3,
        test_dfa2_union_dfa4,
        test_dfa3_union_dfa5,
        test_dfa4_union_dfa6,
        test_dfa5_union_dfa6,
        test_dfa6_union_dfa7,
        test_dfa6_union_dfa8,
        test_dfa7_union_dfa8,
        test_dfa1_union_dfa8
    ]

    union_list = [
        dfa1_union_dfa2,
        dfa1_union_dfa3,
        dfa2_union_dfa4,
        dfa3_union_dfa5,
        dfa4_union_dfa6,
        dfa5_union_dfa6,
        dfa6_union_dfa7,
        dfa6_union_dfa8,
        dfa7_union_dfa8,
        dfa1_union_dfa8
    ]

    # Intersection DFAs
    dfa1_intersection_dfa2 = ProductConstruction(dfa1, dfa2, 'intersection')
    dfa1_intersection_dfa3 = ProductConstruction(dfa1, dfa3, 'intersection')
    dfa2_intersection_dfa4 = ProductConstruction(dfa2, dfa4, 'intersection')
    dfa3_intersection_dfa5 = ProductConstruction(dfa3, dfa5, 'intersection')
    dfa4_intersection_dfa6 = ProductConstruction(dfa4, dfa6, 'intersection')
    dfa5_intersection_dfa6 = ProductConstruction(dfa5, dfa6, 'intersection')
    dfa6_intersection_dfa7 = ProductConstruction(dfa6, dfa7, 'intersection')
    dfa6_intersection_dfa8 = ProductConstruction(dfa6, dfa8, 'intersection')
    dfa7_intersection_dfa8 = ProductConstruction(dfa7, dfa8, 'intersection')
    dfa1_intersection_dfa8 = ProductConstruction(dfa1, dfa8, 'intersection')

    test_dfa1_intersection_dfa2 = ["0" + "1"*99 + "1", "0" + "0"*500 + "1", "0" + "1"*1000 + "1", "01", "0000000001"]
    test_dfa1_intersection_dfa3 = ["01", "0" + "1"*999, "0"*500 + "2", "000001", "0" + "0"*400 + "1"]
    test_dfa2_intersection_dfa4 = ["101", "000101", "101" + "1"*300, "0001010001", "01010101"]
    test_dfa3_intersection_dfa5 = ["110", "1001", "1" + "0"*5, "111000", "100100"]
    test_dfa4_intersection_dfa6 = ["0000101" + "1"*5, "101" + "0"*8 + "1"*10, "0000101", "1"*5 + "0"*4 + "101", "101" + "1"*10 + "0"*4]
    test_dfa5_intersection_dfa6 = ["1"*15 + "0"*8, "1100" * 3, "1001" * 2 + "0"*4, "0"*8 + "1111111110", "1"*30 + "0"*8]
    test_dfa6_intersection_dfa7 = ["0"*8 + "1"*10 + "01", "0"*4 + "1"*10 + "01", "0000" + "1"*10 + "01", "1"*10 + "01", "0"*4 + "1"*5 + "1"*5 + "01"]
    test_dfa6_intersection_dfa8 = ["1"*15 + "0"*4, "1"*30 + "0"*8, "111111" * 3 + "0"*4, "1"*45 + "0"*8, "1"*60 + "0"*12]
    test_dfa7_intersection_dfa8 = ["111111" + "01", "0"*100 + "11111101", "1"*6 + "01", "111111" * 2 + "01", "1"*12 + "01"]
    test_dfa1_intersection_dfa8 = ["0" + "111", "0" + "1"*6, "0" + "0"*100 + "111", "0" + "111111", "0" + "1"*9 + "0"*9]

    intersection_tests = [
    test_dfa1_intersection_dfa2,
    test_dfa1_intersection_dfa3,
    test_dfa2_intersection_dfa4,
    test_dfa3_intersection_dfa5,
    test_dfa4_intersection_dfa6,
    test_dfa5_intersection_dfa6,
    test_dfa6_intersection_dfa7,
    test_dfa6_intersection_dfa8,
    test_dfa7_intersection_dfa8,
    test_dfa1_intersection_dfa8
    ]

    intersection_list = [
    dfa1_intersection_dfa2,
    dfa1_intersection_dfa3,
    dfa2_intersection_dfa4,
    dfa3_intersection_dfa5,
    dfa4_intersection_dfa6,
    dfa5_intersection_dfa6,
    dfa6_intersection_dfa7,
    dfa6_intersection_dfa8,
    dfa7_intersection_dfa8,
    dfa1_intersection_dfa8
    ]

    minimized_intersection_list = [minimizeDFA(dfa) for dfa in intersection_list]
    minimized_union_list = [minimizeDFA(dfa) for dfa in union_list]


    #before minimization
    #time taken to recognize input (return average time)

    


    #after minimization
    print("====================EFFECT OF MINIMIZATION ON NUMBER OF STATES=======================\n")


    # print("\n====================UNION=======================\n")
    sum_before = 0
    sum_after = 0
    for dfa in union_list:
        number_of_states_before = len(dfa.stateList)
        sum_before += number_of_states_before
        min_dfa = minimizeDFA(dfa)
        number_of_states_after = len(min_dfa.stateList)
        sum_after += number_of_states_after
        # print(f"Number of states before minimizing: {number_of_states_before} Number of states after minimizing: {number_of_states_after}")
    
    reduction = round(((sum_after-sum_before)/sum_before) * 100,2)
    print(f"Number of states before minimization = {sum_before}\nNumber of states after minimization = {sum_after}\nOn average, applying minimization on union of two DFA's results in a average change of {reduction}% of states. \n")

    # print("\n====================INTERSECTION=======================\n")

    sum_before = 0
    sum_after = 0
    for dfa in intersection_list:
        number_of_states_before = len(dfa.stateList)
        sum_before += number_of_states_before
        min_dfa = minimizeDFA(dfa)
        number_of_states_after = len(min_dfa.stateList)
        sum_after += number_of_states_after
        # print(f"Number of states before minimizing: {number_of_states_before} Number of states after minimizing: {number_of_states_after}")
    
    reduction = round(((sum_after-sum_before)/sum_before) * 100,2)

    print(f"Number of states before minimization = {sum_before}\nNumber of states after minimization = {sum_after}\nOn average, applying minimization on intersection of two DFA's results in a average reduction of {reduction}% of states. \n")

    print("====================EFFECT OF MINIMIZATION ON EXECUTION TIME=======================\n")

    #before minimization
    total_time_before_minimization_union = 0
    for dfa in union_list:
        start_time = time.perf_counter()
        for test in union_tests:
            result = dfa.isAccepted(test)
        end_time = time.perf_counter()
        total_time_before_minimization_union += (end_time - start_time)

    total_time_before_minimization_intersection = 0
    for dfa in intersection_list:
        start_time = time.perf_counter()
        for test in intersection_tests:
            result = dfa.isAccepted(test)
        end_time = time.perf_counter()
        total_time_before_minimization_intersection += (end_time - start_time)

    #after minimization
    total_time_after_minimization_union = 0
    for dfa in minimized_union_list:
        start_time = time.perf_counter()
        for test in union_tests:
            result = dfa.isAccepted(test)
        end_time = time.perf_counter()
        total_time_after_minimization_union += (end_time - start_time)

    total_time_after_minimization_intersection = 0
    for dfa in minimized_intersection_list:
        start_time = time.perf_counter()
        for test in intersection_tests:
            result = dfa.isAccepted(test)
        end_time = time.perf_counter()
        total_time_after_minimization_intersection += (end_time - start_time)
    

    #percent change

    percent_change_union = round(((total_time_after_minimization_union-total_time_before_minimization_union)/total_time_before_minimization_union) * 100,2)
    percent_change_intersection = round(((total_time_after_minimization_intersection-total_time_before_minimization_intersection)/total_time_before_minimization_intersection) * 100,2)

    print(f"Total time before minimization on union: {total_time_before_minimization_union} \nTotal time after minimization on union: {total_time_after_minimization_union}\nPercent change = {percent_change_union}%. \n")
    print(f"Total time before minimization on intersection: {total_time_before_minimization_intersection} \nTotal time after minimization on intersection: {total_time_after_minimization_intersection}\nPercent change = {percent_change_intersection}%. \n")
    
    
            




    






if __name__ == "__main__":
    main()
        
