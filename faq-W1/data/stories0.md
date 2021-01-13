## happy path
* greet
  - utter_greet
* salary
  - faq
  - utter_did_that_help
* affirm
  - utter_happy

## sal q
* salary
  - faq

##pfcontact
* pfcontact
  - faq

## sa q
* specialallowance
  - faq

## hra q
* hra
  - faq

## pf q
* pf
  - faq

## sal q f     
* greet
  - utter_greet
* salary
  - faq
  - utter_did_that_help
* deny
  - utter_nohelp

## sp q f
* greet
  - utter_greet
* specialallowance
  - faq
  - utter_did_that_help
* affirm
  - utter_happy

## sqp q f
* greet
  - utter_greet
* specialallowance
  - faq
  - utter_did_that_help
* deny
  - utter_nohelp

## hra q f
* greet
  - utter_greet
* hra
  - faq
  - utter_did_that_help
* affirm
  - utter_happy

## hra q f n
* greet
  - utter_greet
* hra
  - faq
  - utter_did_that_help
* deny
  - utter_nohelp

## pf q f
* greet
  - utter_greet
* pf
  - faq
  - utter_did_that_help
* affirm
  - utter_happy

## pf q f n
* greet
  - utter_greet
* pf
  - faq
  - utter_did_that_help
* deny
  - utter_nohelp

## default fallback
* bot_challenge
  - action_default_fallback

* goodbye
  - utter_goodbye
