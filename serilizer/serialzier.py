def convertBlog(blog) -> dict:
    return {
        "id": str(blog['id']),
        'title': blog('title'),
        'description': blog['description'],
        'author': blog['author']
    }

def convertBlogs(blogs)->list:
    return [convertBlog(blog) for blog in blogs]