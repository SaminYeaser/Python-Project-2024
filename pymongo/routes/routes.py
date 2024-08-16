
# username: saminyeaser1
# password : rJajvlRXXl0G964z

# mongodb+srv://saminyeaser1:<password>@cluster0.dgdc3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

from fastapi import APIRouter
from model.model import Blog
from serilizer.serialzier import convertBlog, convertBlogs

endPoint = APIRouter()

@endPoint.get('/')
def home():
    return {
        'name':'samin'
    }
@endPoint.post('/new/blog')
def newBlogAdd(blog:Blog):
    blogsCollection
