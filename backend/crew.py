import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import TavilySearchTool, ScrapeWebsiteTool
from config import TAVILY_API_KEY

def run_news_crew(topic: str) -> str:
    llm = LLM(
        model="ollama/llama3.2:3b",   # <-- prefix with "ollama/"
        base_url="http://localhost:11434"
    )

    search_tool = TavilySearchTool(max_results=2)

    scrape_tool = ScrapeWebsiteTool()

    news_researcher = Agent(
        role="Expert News Researcher",
        goal="Find and extract the full content of the top 2 most relevant news articles on a given topic.",
        backstory=(
            "You are a master news researcher, skilled in using search tools to find the most"
            "accurate and recent information. You are also an expert at extracting clean,"
            "readable text from websites, ignoring ads and other clutter."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[search_tool, scrape_tool] # The researcher has access to both tools
    )

    news_analyst = Agent(
        role="Professional News Analyst",
        goal="Analyze the provided news articles and write a concise, insightful summary for each.",
        backstory=(
            "As a professional news analyst, you have a keen eye for detail and a talent for"
            "distilling complex topics into clear, easy-to-understand summaries. You present"
            "the key findings of each article objectively, making sure to cite your sources."
        ),
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    research_task = Task(
        description=(
            f"1. Search for the most relevant and recent news articles on the topic: '{topic}'.\n"
            "2. For each of the top 2 articles found, use the scrape tool to get its full content.\n"
            "3. Compile all the scraped content and URLs into a final report.\n"
            "IMPORTANT: Make sure to scrape the ACTUAL articles found in the search results."
        ),
        expected_output=(
            "A structured report containing:\n"
            "- Article 1: Full URL and scraped text content\n"
            "- Article 2: Full URL and scraped text content\n"
            "Ensure both articles are relevant to the topic '{topic}' and contain the actual scraped content."
        ),
        agent=news_researcher
    )

    analyze_task = Task(
        description=(
            "Review the full content of each news article provided in the context. "
            "For each article, write a detailed, one-paragraph summary that captures the "
            "key points and main arguments. IMPORTANT: Use ONLY the articles that were actually "
            "scraped by the researcher, not any example URLs."
        ),
        expected_output=(
            "A clean, well-formatted markdown report with 2 numbered sections. "
            "Each section must contain:\n"
            "- A detailed summary paragraph of one article\n"
            "- The source URL on a new line starting with 'Source:'\n\n"
            "Format:\n"
            "1. [Your detailed summary here]...\n"
            "   Source: [actual URL from scraped content]\n\n"
            "2. [Your detailed summary here]...\n"
            "   Source: [actual URL from scraped content]"
        ),
        agent=news_analyst,
        context=[research_task]
    )

    news_crew = Crew(
        agents=[news_researcher, news_analyst],
        tasks=[research_task, analyze_task],
        process=Process.sequential,
        verbose=True 
    )

    try:
        result = news_crew.kickoff(inputs={'topic': topic})
        
        if hasattr(result,'raw'):
            return str(result.raw)
        elif hasattr(result,'output'):
            return str(result.output)
        else:
            return str(result)
        
    except Exception as e:
        return f"An error occurred while running the crew: {e}"