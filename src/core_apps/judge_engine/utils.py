
# Just some testing code to test different python module. 
# file werite and delete test

import os
import shutil


def test_path_create():
    path = "./new-util-2/hi/ok/bye/"
    os.makedirs(path)

    #     create a file
    os.mknod(f"{path}/kul.txt")

    print(os.listdir(os.getcwd()))


def delete_dirs_files():
    file_path = "./new-util-2/hi/ok/bye/kul.txt"

    # using os
    #     first delete the file
    os.remove(file_path)

    #     now delete the dirs
    head, tail = os.path.split(file_path)
    print("head: ", head)
    print("tail: ", tail)
    os.removedirs(head)


def test_os_path_join():
    curr = os.getcwd()
    print("curr: ", curr)
    print()
    new_path = os.path.join(curr, "new", "demo.txt")
    print(new_path)
    print("base name: ", os.path.basename(new_path))
    print()


def test_head_teil_path():
    print()
    curr = os.getcwd()
    new_path = os.path.join(curr, "hi", "kul", "demo.txt")
    print("new_path: ", new_path)
    head, tail = os.path.split(new_path)
    print("head: ", head)
    print("tail: ", tail)

    if os.path.isfile(head):
        print("head is file")
    else:
        print("head is not file")

    if os.path.isfile(tail):
        print("tail is file")
    else:
        print("tail is not file")

    # is new path exists.
    path = "./new-util-2/hi/ok/bye"
    if os.path.exists(path):
        print("new path exists")
    else:
        print("new path does not exist")

    print()


# test_path_create()
# test_head_teil_path()
# delete_dirs_files()

######################################################


import json
import os


def extract_and_save_cpp_code(json_data, output_dir):
    """Extracts C++ code from JSON and saves it to a file.

    Args:
        json_data (dict): The parsed JSON data.
        output_dir (str): The directory to save the extracted code file.
    """
    if "lang" in json_data and "code" in json_data and json_data["lang"] == "cpp":
        cpp_code = json_data["code"]

        # Sanitize the code (ideally implement more robust sanitization)
        # This is a simplified example for demonstration purposes only!
        # cpp_code = cpp_code.replace("<", "&lt;").replace(
        #     ">", "&gt;"
        # )  # Basic HTML escaping

        # Create unique filename (replace with proper ID handling)
        filename = f"user_code_{len(os.listdir(output_dir))}.cpp"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            f.write(cpp_code)
        print(f"C++ code saved to: {filepath}")
    else:
        print("Invalid JSON format or language not supported")


# Example usage (assuming you have received JSON data)
json_data = {
    "lang": "cpp",
    "code": '#include <iostream>\nusing namespace std;\n\nint main()\n{\ncout << "Hello World" << endl;\nreturn 0;\n}',
}

# Replace with your actual output directory (potentially shared with container)
# output_dir = os.getcwd()
# extract_and_save_cpp_code(json_data, output_dir)

#################################################################3

# check if already parent dir is passed, what is the output if again parent dir is extracted from the path.
user_code_parent_dir = "/home/mehboob/module-codes/algocode/online-judge/src/user_codes/cpp/1af556c5-f034-44a4-a742-ebfdb65f410d/////////"

parent_dir = os.path.dirname(user_code_parent_dir)


if os.path.isfile(user_code_parent_dir):
    print("user_code_parent_dir: is a file", user_code_parent_dir)
else:
    print("user_code_parent_dir: is not a file: ", user_code_parent_dir)

if os.path.isfile(parent_dir):
    print("parent_dir: is a file", parent_dir)
else:
    print("parent_dir: is not a file: ", parent_dir)


print("parent dir: ", parent_dir)


# #Use the above API for full implementation.
# class CodeSubmitSimpleImplementation(APIView):
#     """A simple approach to test the code submission without creating the files beforehand.
#     In this use case, the host volume creation also handled by docker.
#     The volume created in host by docker has permission only of docker, hence the files can not be deleted by host user.

#     The time is also same as the robust implementation of creating files beforehand. Infact, this method takes one second more
#     one average than the robust implementation.

#     """

# def post(self, request):
#     start = time.time()

#     lang = request.data.get("lang")
#     code = request.data.get("code")
#     input_data = request.data.get("input")

#     print("Code: ", code)

#     client = from_env()

#     file_path = f"user-files/{random.randint(10, 100000)}"
#     curr_path = os.getcwd()
#     print("curr path: ", os.getcwd())
#     new_file_path = os.path.join(curr_path, file_path)

#         # About image: simple_cpp
#         # Image name, just the g++ compiler.
#         # create a Dockerfile with this only: FROM gcc:12.3.0
#         # and create an image using it and name it as "simple_cpp"
#         try:
#             # Create and start a container
#             container = client.containers.run(
#                 "simple_cpp",
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

# Wait for the container to finish
# result = container.wait()
# print("result: ", result)

# # Get the logs (output)
# output = container.logs().decode("utf-8")

# with open(f"{new_file_path}/output.txt", "r") as f:
#     data = f.read()
#     print("data: ", data)

# # Remove the container
# container.remove()

# end = time.time()

# print("total time taken: ", end - start)
# # Return output to the user
# return JsonResponse({"output": output})

#         except docker.errors.ContainerError as e:
#             print(f"Error: {e}")
#             return JsonResponse({"error": str(e)}, status=500)
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#             return JsonResponse({"error": "An unexpected error occurred"}, status=500)

#         # return JsonResponse({"error": "Method not allowed"}, status=405)
