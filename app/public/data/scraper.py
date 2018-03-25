#!/usr/bin/python

import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess


def parse_question_answer(texts):
    question = None
    answer_list = []
    for text in texts:
        if text == '':
            pass
        if question is None:
            question = text
        else:
            answer_list.append(text)
    return {
        'question': question,
        'answer_list': answer_list
    }
    pass


def parse_centers(texts):
    # partiendo de un substring html.question

    # primero parsear centerspregunta

    # para extrar el tipo de quiz

    # segundo extrar la pregunta, el id de la pregunta

    # tercero extrear url de imagen si exitst

    # quarto extraer las respuestas y la buena


    """

    :param texts:
    :return:

    @json
    {
        question: "str",
        image: "url",
        type: "", // boolean or multiple choice
        answers: []
        correct: [] // sometimes there might be
    }
    """

    pass


class QuizSpider(scrapy.Spider):
    name = 'quiz'
    start_urls = ['http://www.chinesedrivingtest.com/test/']

    def parse(self, response):
        questions = Selector(response=response).xpath('//*[@id="questioncontainer"]/form').extract()[0].split('<hr>')
        for question in questions:
            striped_str = ' '.join(question.split())
            pass
            # texts = Selector(text=striped_str).xpath('//text()').extract()
            # print parse_question_answer(texts)

            texts = Selector(text=striped_str).xpath('//center').extract()
            parse_centers(texts=texts)

            # questioncontainer > form > center:nth-child(10) > img
        pass


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(QuizSpider)
process.start()  # the script will block here until the crawling is finished
# //*[@id="questioncontainer"]/form/text()[1]
