import os

from regula.documentreader.webclient.ext.api import DocumentReaderApi
from regula.documentreader.webclient.ext.models import RecognitionImage, RecognitionRequest
from regula.documentreader.webclient.gen import ProcessParams, Scenario, Result, Light, TextFieldType, Source, \
    CheckResult

host = os.getenv("API_BASE_PATH", "http://localhost:8080")
license = os.getenv("TEST_LICENSE", None)

with open("australia_passport.jpg", "rb") as f:
    image_payload = f.read()

with DocumentReaderApi(host) as api:
    api.license = license

    process_params = ProcessParams(Scenario.FULL_PROCESS, [Result.STATUS, Result.TEXT, Result.IMAGES])
    process_images = [RecognitionImage(image_payload, Light.WHITE)]
    request = RecognitionRequest(process_params, process_images)

    response = api.process(request)
    response.result_by_type(Result.IMAGES)

    response_text = response.text

    doc_number_field = response_text.get_field(TextFieldType.DOCUMENT_NUMBER)

    doc_number_visual = doc_number_field.get_value(Source.VISUAL)
    doc_number_mrz = doc_number_field.get_value(Source.MRZ)

    doc_number_visual_validity = doc_number_field.get_validity(Source.VISUAL)
    doc_number_mrz_validity = doc_number_field.get_validity(Source.MRZ)

    doc_number_mrz_visual_matching = doc_number_field.get_comparison(Source.MRZ, Source.VISUAL)

    response_status = response.status
    doc_overall_status = "valid" if response_status.complete == CheckResult.OK else "not valid"

    response_images = response.images

    print(f"""
    ---------------------------------------------------------------------------
                   Document Overall Status: {doc_overall_status}
                    Document Number Visual: {doc_number_visual}
                       Document Number MRZ: {doc_number_mrz}
        Validity Of Document Number Visual: {doc_number_visual_validity}
           Validity Of Document Number MRZ: {doc_number_mrz_validity}
              MRZ-Visual values comparison: {doc_number_mrz_visual_matching}
    ---------------------------------------------------------------------------
    """)