"""transform data from web to dictionary for ready to insert to database"""

from parsel import Selector
from model.model import Blog
from extract.extract_data import response

# Initialize selector with the response text
selector = Selector(response.text)


def get_cleaned_content(content):
    """Clean and organize the content by splitting it into sections."""
    clean_content = [content[0]]
    temp = ""

    for clean in content[2:]:
        clean = "".join(clean)
        if clean.startswith("by"):
            clean_content.append(temp)
            temp = ""
            continue
        temp += " " + clean

    if temp != "":
        clean_content.append(temp)

    return clean_content


def extract_blog_data():
    """Extract all the necessary blog data using the selector."""
    # Extract main data
    divs = selector.xpath('//div[contains(@class, "blog-posts hfeed")]')
    title = selector.xpath('//h3[@class="post-title entry-title"]/a/text()').extract()
    date = selector.xpath(
        '//div[@class="date-outer"]/h2[@class="date-header"]/span/text()'
    ).extract()

    # Extract authors and clean the list
    author = divs.xpath(
        '//div[contains(@class, "blog-posts hfeed")]/div/div/div/div/div[2]/div[1]/span/text()'
    ).extract()

    # Extract content and clean it
    content = selector.xpath('//span[@style="font-family: verdana;"]/text()').extract()[
        1:
    ]
    clean_content = get_cleaned_content(content)

    # Extract comments
    comment = selector.xpath('//a[contains(@class, "comment-link")]/text()').extract()

    # Extract labels
    span_elements = selector.xpath('//span[@class="post-labels"]')
    all_labels = [span.xpath("./a/text()").extract() for span in span_elements]

    data = []
    for i in range(len(title)):
        data.append(Blog(
            title=title[i],
            date=date[i],
            author=author[i],
            content=clean_content[i],
            comment=comment[i],
            label=all_labels[i]
            ).model_dump()
        )
    return data


# Extract blog data
blog_data = extract_blog_data()