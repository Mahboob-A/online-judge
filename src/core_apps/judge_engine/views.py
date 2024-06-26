# views.py

import uuid

from django.http import JsonResponse
from django.core.exceptions import ImproperlyConfigured

from rest_framework.views import APIView


# object to execute code metaclass=SignletonMeta
from core_apps.judge_engine.exec_engine import code_execution_engine


class CodeSubmitRobustAPI(APIView):
    """An API to test the robust implementation of the Online Judge.

    and compare the time with simple implementation
    """

    def post(self, request):
        """Submit code to execute in secure docker container."""

        lang = request.data.get("lang")
        code = request.data.get("code")
        input_file = request.data.get("input")
        testcases = request.data.get("testcases")

        submission_id = uuid.uuid4()
        data = code_execution_engine.exec_code(
            user_codes=request.data, submission_id=submission_id
        )

        return JsonResponse({"submission_id": submission_id, "data": data}, status=200)
