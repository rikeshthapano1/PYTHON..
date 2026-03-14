import random  # to make the computer pick random choices

candidate_words = [
    "food",
    "snacks",
    "leftovers",
    "her",
    "for",
    "water",
    "photosynthesis",
    "pyramid",
]

#list of words computer le choose garna sakne words haru, jasma "food" sab bhanda thulo probability sanga choose garna sakinchha, ani "snacks" second highest probability sanga choose garna sakinchha, etc.

your_mental_model = [0.50,0.30,0.15,0.05,0,0,0,0] # the mental model is a list of probabilities that sum up to 1, where each probability corresponds to the likelihood of choosing the respective word from the candidate_words list. In this case, "food" has the highest probability of being chosen (0.50), followed by "snacks" (0.30), "leftovers" (0.15), and "her" (0.05). The other words have a probability of 0, meaning they will not be chosen.

chosen_word = random.choices(candidate_words, weights=your_mental_model , k=1)[0] #[0] to get the words or say string without array from the list

#k=1 bhaneko chai yeuta matra word choose garne ho ani multiple words choose garna chaheko bhaye k=2, k=3, etc. garna sakinchha.

print(f"Sudesh is hungry so he went for {chosen_word}...")