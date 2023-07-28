def test_fibonacci_endpoint_when_no_input(client):
    response = client.get("/fibonacci")
    assert response.status_code == 400
    assert (b'{"error":"Please specify the number till which you want a fibonacci series"}'
            b'\n') in response.data


def test_fibonacci_endpoint_when_wrong_input_param(client):
    response = client.get("/fibonacci?inpuut=1")
    assert response.status_code == 400
    assert (b'{"error":"Please specify the number till which you want a fibonacci series"}'
            b'\n') in response.data


def test_fibonacci_endpoint_when_negative_input(client):
    response = client.get("/fibonacci?input=-1")
    assert response.status_code == 400
    assert b'{"error":"Negative numbers are not supported"}\n' in response.data


def test_endpoint_not_found(client):
    response = client.get("/fibonaci?input=1")
    assert response.status_code == 404
    assert (b'{"error":"The requested URL was not found on the server. If you entered the '
            b'URL manually please check your spelling and try again."}\n') in response.data


def test_fibonacci_endpoint_when_valid_input(client):
    response = client.get("/fibonacci?input=1")
    assert response.status_code == 200
    assert b'[0]' in response.data

