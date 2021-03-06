import pytest


def test_todo_list(client):
    # View the home page and check to see the header and a to-do item
    response = client.get('/')
    assert b'<h1>A Simple To-do Application</h1>' in response.data
    assert b'clean room' in response.data

    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1


# Testing for the add task feature at /addATask
def test_todo_addtions_feature(client):
    response = client.get('/addATask')
    assert b'<h1>A Simple To-do Application</h1>' in response.data
    assert b'Add a Task' in response.data
    assert b'Ex: Feed Dog' in response.data


# Testing for the filter feature at /
def test_todo_filter(client):
    response = client.get('/')
    assert b'Filter Here' in response.data
    assert b'All Tasks' in response.data
    assert b'Completed' in response.data
    assert b'ToDo' in response.data

# Testing for the complete feature at /Done


def test_todo_make_completed():
    response = client.get('/Done')
    assert b'<h1>A Simple To-do Application</h1>' in response.data
    assert b'/Done' in response.data

# Testing the edit feature at /Edit


def test_edit_page(client):
    response = client.get('/Edit')
    assert b'Edit Page' in response.data
    assert b'for todo in todos' in response.data
    assert b'delete' in response.data
    assert b'Edit' in response.data

# Testing the delete feature at /Delete


def test_delete_feature(client):
    assert b'Delete' in response.data
