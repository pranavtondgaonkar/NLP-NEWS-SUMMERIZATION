from src.pipeline.prediction_pipeline import SinglePrediction

pred = SinglePrediction()

text ="""Actor Sushant Singh Rajput has said that he doesn't mind men flirting with him and takes it as a compliment. 
        However, he added that he doesn't usually expect attention from men. 
        Meanwhile, it has been rumoured that Sushant has been dating actress Kriti Sanon since they started filming for their upcoming film 'Raabta'. """

result = pred.predict(text)
print(result)