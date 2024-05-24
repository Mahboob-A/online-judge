# views.py

from django.core.exceptions import ImproperlyConfigured

try:
    from docker import from_env
    from docker.errors import ContainerError
except ImportError:
    raise ImproperlyConfigured("Docker library not installed. Please install 'docker'")


# from django.http import JsonResponse


# from rest_framework.views import APIView

# from .models import CodeSubmission
import tempfile
import uuid
import os, json, time, random


# from core_apps.judge_engine.file_data_processor import file_processor
# from core_apps.judge_engine.containers import code_container
# from core_apps.judge_engine.exec_engine import code_exec_engine
from  exec_engine import code_exec_engine

hello_world_with_num_data_problem = {
    "lang": "cpp",
    "code": '#include <bits/stdc++.h>\nusing namespace std;\n\nvoid sol(int num)\n{\n    cout<<"Hello World: "<<num<<endl;\n}\n\nint main()\n{\n    int t, num; \n    cin>>t;\n\n    while(t--)\n    {\n        cin>>num; \n        sol(num);\n    }\n\n    return 0;\n}',
    "input": ["10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "testcases": [
        "Hello World: 1",
        "Hello World: 2",
        "Hello World: 3",
        "Hello World: 4",
        "Hello World: 5",
        "Hello World: 6",
        "Hello World: 7",
        "Hello World: 8",
        "Hello World: 9",
        "Hello World: 0",
    ],
}


# class CodeSubmitSimpleImplementation(APIView):
#     """A simple approach to test the code submission without creating the files beforehand.
#     In this use case, the host volume creation also handled by docker.
#     The volume created in host by docker has permission only of docker, hence the files can not be deleted by host user.

#     The time is also same as the robust implementation of creating files beforehand. Infact, this method takes one second more
#     one average than the robust implementation.

#     """

#     def post(self, request):
#         start = time.time()

#         lang = request.data.get("lang")
#         code = request.data.get("code")
#         input_data = request.data.get("input")

#         print("Code: ", code)

#         client = from_env()

#         file_path = f"user-files/{random.randint(10, 100000)}"
#         curr_path = os.getcwd()
#         print("curr path: ", os.getcwd())
#         new_file_path = os.path.join(curr_path, file_path)

#         try:
#             # Create and start a container
#             container = client.containers.run(
#                 "simple_cpp",  # Image name
#                 volumes={
#                     f"{new_file_path}/": {
#                         "bind": "/user-files",
#                         "mode": "rw",
#                     }
#                 },
#                 command=[
#                     "sh",
#                     "-c",
#                     f'echo "{code}" > /user-files/code.cpp && echo "{input_data}" > /user-files/input.txt && g++ /user-files/code.cpp -o /user-files/code && /user-files/code < /user-files/input.txt > /user-files/output.txt',
#                 ],
#                 detach=True,
#             )

#             # Wait for the container to finish
#             result = container.wait()
#             print("result: ", result)

#             # Get the logs (output)
#             output = container.logs().decode("utf-8")

#             with open(f"{new_file_path}/output.txt", "r") as f:
#                 data = f.read()
#                 print("data: ", data)

#             # Remove the container
#             container.remove()

#             end = time.time()

#             print("total time taken: ", end - start)
#             # Return output to the user
#             return JsonResponse({"output": output})

#         except ContainerError as e:
#             print(f"Error: {e}")
#             return JsonResponse({"error": str(e)}, status=500)
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#             return JsonResponse({"error": "An unexpected error occurred"}, status=500)

#         # return JsonResponse({"error": "Method not allowed"}, status=405)


# class CodeSubmitRobustAPI(APIView):
#     """An API to test the robust implementation of the Online Judge.

#     and compare the time with simple implementation
#     """

#     def post(self, request):
#         """Submit code to execute in secure docker container."""

#         lang = request.data.get("lang")
#         code = request.data.get("code")
#         input_file = request.data.get("input")
#         testcases = request.data.get("testcases")

#         # print('lang: ', lang)
#         # print("code: ", code)
#         # print("input file ", input_file)
#         # print("testcases: ", testcases)

#         # print('request.data: ', request.data)
#         # print('\ntype of requst.data: ', type(request.data))

#         # print('\ntype of code: ', type(code))
#         # print('\ntype of input: ', type(input_file))

#         submission_id = uuid.uuid4()
#         data = code_exec_engine(user_codes=request.data, submission_id=submission_id)

#         return JsonResponse({"submission_id": submission_id, "data": data}, status=200)


############################

def test_inside_cont_exe():
    submission_id = uuid.uuid4()
    data = code_exec_engine(
        user_codes=hello_world_with_num_data_problem, submission_id=submission_id
    )

    print("data: \n", data)


# This is the entrypoint function to check the Judge locally. No request is needed. 
test_inside_cont_exe()


    
