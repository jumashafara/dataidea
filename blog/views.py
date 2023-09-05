import requests
import markdown
from . models import Blog
from . models import BlogComment
from . models import Hashnode
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

# Create your views here.
# def blogs(request):
#     context = {}
#     return render(request, 'blog/blogs.html')


def blogs(request):
    username = 'jumashafara'
    page = 1
    all_blogs = []

    while True:
        query = """
        query GetAllBlogsByUser($username: String!, $page: Int) {
            user(username: $username) {
                publication {
                    posts (page:  $page){
                        popularity
                        slug
                        cuid
                        title
                        brief
                        dateFeatured
                        contentMarkdown
                        coverImage
                    }
                }
            }
        }
        """
        variables = {
            "username": username,
            "page": page
        }

        response = requests.post(
            "https://api.hashnode.com",
            json={"query": query, "variables": variables},
        )

        data = response.json()['data']['user']['publication']['posts']
        all_blogs.extend(data)

        if len(data) == 0:
            break
        else:
            page += 1

    sorted_blogs = sorted(all_blogs, key=lambda k: k['popularity'], reverse=True)

    # pagination
    paginator = Paginator(sorted_blogs, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'blogs': page_obj}
    template_name = 'blog/blogs.html'
    return render(request=request, template_name=template_name, context=context)



def blogDetails(request):
    # Fetch Blog Details
    slug = request.GET.get('slug')

    query = """
    query GetAllBlogsByUser($slug: String!) {
        post(slug:  $slug, hostname: "") {
            title
            cuid
            slug
            brief
            coverImage
            contentMarkdown
            author {
                    username
                    name
                }
        }
    }
    """
    variables = {
        "slug": slug,
        
    }

    response = requests.post(
        "https://api.hashnode.com",
        json={"query": query, "variables": variables},
    )

    data = response.json()['data']['post']

    # Fetch Blog Comments
    comments = BlogComment.objects.filter(blog_slug=slug)
    
    context = {
        'blog': data, 
        'details': markdown.markdown(data['contentMarkdown']), 
        'comments': comments
        }
    return render(request, 'blog/blog_details.html', context=context)


# Comments
def comment(request):
    try:
        comment = BlogComment(
            comment = request.POST.get(key='comment'),
            blog_slug = request.POST.get(key='slug'),
            user = request.user
        )

        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        context = {'message': 'An error occured while trying to add your comment', 'state':  'danger'}
        template_name = 'components/message.html'
        return render(request=request, template_name=template_name, context=context)