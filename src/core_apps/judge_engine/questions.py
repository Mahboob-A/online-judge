sum_of_a_b_problem = {
    "lang": "cpp",
    "code": "#include <bits/stdc++.h>\nusing namespace std; \n\nvoid sum_of_a(int a, int b)\n{\n    cout << a + b << endl; \n}\n\n\nint main()\n{\n    int t, a, b; \n    cin >> t; \n    \n    while(t--)\n    {\n        cin >> a >> b; \n        sum_of_a_b(a, b); \n    }\n\n    return 0;\n}",
    "input": [
        "10",
        "1 2",
        "5 7",
        "4 6",
        "10 5",
        "15 15",
        "25 30",
        "150 50",
        "100 200",
        "110 90",
        "1000 2000",
    ],
    "testcases": ["3", "12", "10", "15", "30", "55", "200", "300", "200", "300"],
}
