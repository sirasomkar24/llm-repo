from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(model='gpt-5')

# schema

class Review(BaseModel):

    key_themes: list[str] = Field(description="write down all the key themes discussed in the review in a list")

    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal['pos','neg'] = Field( description="return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]]= Field(description="write down all the pros inside a list.",default=None)
    cons: Optional[list[str]] = Field(description="write down all the cons inside a list.",default=None)

    name: Optional[str] = Field(description= "write the name of the reviewer", default="Omkar")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung galaxy S24 Ultra, and I must say, its an absolute powerhouse! The snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 500mAh battery easily lasts a full day even with heavy use, and 45W fast charging is a lifesaver.

The S-Pen intergration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200 MP camera-the night modeis stunning, capturing crisp, vibrant images even in low light. zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weigth and size makes it a bit uncomfortable for one-handed use. Also, Samsung One UI  still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to compititors
""")

print(result)