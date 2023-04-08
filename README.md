# Car Data Analysis
This project looks into the various relationships, patterns, and relationships among common car feautures to answer research questions.

## About Dataset
This dataset contains the following categories:
- Make
- Model
- Year
- Engine Fuel Type
- Engine HP
- Engine Cylinders
- Transmission Type
- Driven_Wheels
- Number of Doors
- Market Category
- Vehicle Size
- Vehicle Style
- highway MPG
- city mpg
- Popularity
- MSRP

## Dataset Issues

- No indication of what currency MSRP is in, and some values are strangely extremely low
- Unequal quantity of samples by year
    - there are much more recent years models than older years models in the dataset. This will be important to account for when analyzing yearly trends

I am just now realizing that there is no indication of what the currencies are for MSRP. I had assumed USD but there are some strange values that might make it a hard category to work with (many models are listed as exactly 2,000 but most others indicate US or European currency) I guess we can just make research questions around this

I guess we could just look at aggregate power and efficiency developments throughout the years like HP and mpg

## Research Questions

1. 