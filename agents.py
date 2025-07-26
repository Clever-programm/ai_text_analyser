import os

from dotenv import load_dotenv
from langchain_gigachat.chat_models import GigaChat
from langchain.prompts import PromptTemplate

from logger import setup_logger
from exceptions import CredentialsException


logger = setup_logger("ai_agents")
load_dotenv()
CREDENTIALS = os.getenv('GIGACHAT_AUTH_KEY')

try:
    if CREDENTIALS is None:
        raise CredentialsException
    logger.info("API credentials successfully got")
except CredentialsException:
    logger.error("Gigachat API credentials is none")

try:
    llm = GigaChat(
        credentials=CREDENTIALS,
        verify_ssl_certs=False
    )

    theme_lang_agent_prompt = PromptTemplate.from_template(
        """ 
        Ты аналитик текстов. Твоя задача - определить тему следующего текста, а также язык, на котором он написан:
        
        "{query}"
        
        Твой ответ должен содержать исключительно тему этого текста и язык, на котором он написан в формате:
        
        <тема>|<язык>
        """
    )

    theme_lang_chain = theme_lang_agent_prompt | llm
    logger.info(f"theme_lang agent successfully setup")
except Exception as e:
    logger.error(f"Setup theme_lang agent error: {e}")


def analyse_text(query: str) -> (str | None, str | None):
    """
    Function asks AI for theme and language of text data
    :param query: text to find theme and language
    :return: founded theme and language of the text
    """
    try:
        result = theme_lang_chain.invoke({"query": query})
        decision = result.content.strip().lower()
        theme, language = decision.split("|")
        logger.info(f"Theme and language was found")
        return theme, language
    except Exception as e:
        logger.error(f"Unable to find theme and language: {e}")
    return None, None