# views.py
import tempfile
import uuid
import os, json, time, random

from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from rest_framework.views import APIView

# from core_apps.judge_engine.file_data_processor import file_processor
# from core_apps.judge_engine.containers import code_container
# from core_apps.judge_engine.exec_engine import code_exec_engine
from exec_engine import code_exec_engine

from dummy_questions import hello_world_with_num_data_problem


def test_inside_cont_exe():
    submission_id = uuid.uuid4()
    data = code_exec_engine(
        user_codes=hello_world_with_num_data_problem, submission_id=submission_id
    )

    print("data: \n", data)


# This is the entrypoint function to check the Judge locally. No request is needed.
test_inside_cont_exe()
