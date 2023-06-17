from transformers import pipeline

def summerize(leng = 56):

    model_name = 't5-base'
    model_revision = 'main'

    summarizer = pipeline('summarization', model=model_name, revision=model_revision)


    text = """
    The history of natural language processing (NLP) generally started in the 1950s, although work can be found from earlier periods. In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence. The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English. The authors claimed that within three or five years, machine translation would be a solved problem. However, real progress was much slower, and after the ALPAC report in 1966, which found that ten-year-long research had failed to fulfill the expectations, funding for machine translation was dramatically reduced. Little further research in machine translation was conducted until the late 1980s when the first statistical machine translation systems were developed.
    """

    summary = summarizer(text, max_length=leng, min_length = 10)[0]['summary_text']

    print(summary)


summerize()