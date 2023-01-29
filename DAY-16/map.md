

# Map for the scraping 

- create the soup object 
- *** create the function which loop the all possible anchor*[0-9], and get the all data availabel in the anchor    ***

- possible data in the anchor 
> aartical class review-*[0-9]


> div with class_ = 'reviewRating' > span itemprop='ratingvalue'
> div with class_ = 'body' 
> div.id = 'anchor*[0-9]'
> h2.content
> h3.span.span.content  1.itemprop='name'  2.h3.content    3. time.
> itemprop='datetime'
> div with class_ = 'text_content', itemprop='reviewBody'
> div with class_ = 'review-ratings'
> > table with class_ = 'review-ratings'
> > > td class_ = '' 'aircraft' .content
> > > td class_ = 'review-value' .content


---
> table 
> tr > td class='review-rating-header ___' > td class='review-value' 
>  > aircraft   > review-value
>  > type_of_traveller > review-vaule
>  > cabin_flown   > review-value
>  > route
>   > date_flown 
>   > seat_comfort > review-rating-stars 
>  >  cabin_staff_service > stars
>  >  food_and_beverages  > stars
>  >  inflight_entertainment > stars
>  >  ground_service
>  >  value_for_money
>  > recommended > rating-no


## things we need form the div 
- total rating(*/10)
- user name, location, date
- review text 
- aircraft name 
- type of traveller
- seat type
- route
- date flown
- seat comfort
- cabin staff service
- food and beverages
- inflight entertainment
- ground service
- value for money
- recommended