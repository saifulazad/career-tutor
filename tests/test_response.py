from cvService.response import Response


def test_response():
    response = Response(status_code=200, payload={"key": "val"})
    rendered_response = response.render()
    assert isinstance(rendered_response["body"], str)


def test_none_response():
    response = Response(status_code=200, payload=None)
    rendered_response = response.render()
    assert isinstance(rendered_response["body"], str)
