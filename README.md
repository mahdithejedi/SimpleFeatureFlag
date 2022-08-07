# Feature Flag Platform
By this platform you can Set Rules for your Features and do A/B test for your users

# Architecture 
A brief explanation of the architecture

As the code shows, I don't use complicated architecture. I use a simple microkernel architecture in which you have a core that manages CRUD and Rules [manager.py](FeatureFlag/Core/Rules/manager.py) and a file to which you add rules. This way, you can easily add, remove and manage your rules without facing unnecessary complexities.
We have Four Rules:

  * Global: It's just a simple query in which you just inquiry for rules that their type is `Global`

  * Minimum: You have a version that can be split into Major, Minor, and Patch. You have to split the string format of the version into Three separate columns in the DB and use indexing to optimize your queries. (Although there are different other possible ways to tackle this problem, this way is the most simple and memory-efficient way)
  
  * Partial Rule: For this rule, I've used an algorithm to active/directive a feature for the user instead of saving which feature is active for which user in DB.
You can make a hash of user_id and then count the remainder of 100.
For example consider a user_id = 12. You get sha256 of 12, which is 48542053925442562206970678378617219313498267117402160926478466274825158240536, then get the remainder of it of 100 which is 36. Now you make a DB query asking for active features for 36 percent of users or more. But this method has a problem. What if user_id of users is like this -> 12, 24, 36, etc. Consider you have a Feature that should be active for 30 percent of users. Users with user_id -> 12, 24, 36,4 are requested for a feature. Users with user_id -> 12, 24, 36 are more likely to be in 30 percent who see the features, and user_id=4 is more probable to be in 70 percent who can't see the feature. So for adding more randomness, we save the first time the user_id is requested and get the hash of (user_id#unix time of the first time the user requested). **This way will also ensure that if a feature is active for a user, it will be active for the user in all requests.**

  * MinimumeRule: As our architecture is a microkernel and each rule is independent, we can combine two Minimum and Partial rules without extra time for choosing a new algorithm or new logic. We combine their queries and make a new rule =).

# Set Rule for Feature

## Create New Feature

Add Rule for Feature

**URL** : `/V1/feature/`

**Method** : `POST`

**Auth required** : No


**Data constraints**

```json
{
  "rule": "AllowedRules:Global,Minimum,Partial,MinimumPartial",
  "name": "A Unique Name",
  "version": "Integer.Integer.Integer for Minimum or MinimumPartial",
  "percent": "Integer for Partial or MinimumPartial"
}
```
fields:

  * Rule : Can be on of _Global,Minimum,Partial,MinimumPartial_ \*
  * Name: A Unique for your Rule \*
  * version: Your Feature version \**
  * percent: specifies the percentage of users this feature should be enabled for \***

*: This field is necessary

**: This field is necessary if you specify Minimum or Minimum Partial Rule

***:This field is necessary if you specify Partial or Minimum Partial Rule


### Success Responses

**Code** : `200 OK`


```json
{
  "pk": 25,
  "rule": "MinimumPartial",
  "name": "MP2",
  "version": "3.2.1",
  "percent": 90
}
```

### Error Response

**Condition** : If provided data is invalid, e.g. rule with duplicated name.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
  "name": [
    "feature with this name already exists."
  ]
}
```

## Get Current Features

get list of features

**URL** : `/V1/feature/`

**Method** : `GET`

**Auth required** : No


### Success Responses

**Code** : `200 OK`

```json
[
  {
    "pk": 14,
    "rule": "Partial",
    "name": "PartialTest",
    "version": "..",
    "percent": 20
  },
  {
    "pk": 15,
    "rule": "Minimum",
    "name": "Version1.0.2",
    "version": "1..2",
    "percent": null
  }
]
```
## Get Specific Features

Get specific feature

**URL** : `/V1/feature/<PK>`

**Method** : `GET`

**Auth required** : No


### Success Responses

**Code** : `200 OK`

```json
{
  "pk": 14,
  "rule": "Partial",
  "name": "PartialTest",
  "version": "..",
  "percent": 20
}
```


## Get Current Features

get list of features

**URL** : `/V1/feature/<PK>`

**Method** : `GET`

**Auth required** : No


### Success Responses

**Code** : `200 OK`

```json
[
  {
    "pk": 14,
    "rule": "Partial",
    "name": "PartialTest",
    "version": "..",
    "percent": 20
  },
  {
    "pk": 15,
    "rule": "Minimum",
    "name": "Version1.0.2",
    "version": "1..2",
    "percent": null
  }
]
```

[//]: # (## update Specific Features)

[//]: # ()
[//]: # (Get specific feature)

[//]: # ()
[//]: # (**URL** : `/V1/feature/<PK>`)

[//]: # ()
[//]: # (**Method** : `PATCH`)

[//]: # ()
[//]: # (**Auth required** : No)

[//]: # ()
[//]: # ()
[//]: # (### Success Responses)

[//]: # ()
[//]: # (**Code** : `200 OK`)

[//]: # ()
[//]: # (```json)

[//]: # ({)

[//]: # (  "pk": 14,)

[//]: # (  "rule": "Partial",)

[//]: # (  "name": "PartialTest",)

[//]: # (  "version": "..",)

[//]: # (  "percent": 20)

[//]: # (})

[//]: # (```)



## Get Current Features

get list of features

**URL** : `/V1/feature/<PK>`

**Method** : `DELETE`

**Auth required** : No


### Success Responses

**Code** : `204 No Content`

### Error Response
**Code** : `404 Not Found`


# Add Rule
Add rule is so easy, 
  * First: thing you should do is override a class from `_BaseRule`  and implement `get_features` function
, you should return a Django `Q` instance
  * Second: add your class with a name inside `Feature` model `_rules_classes` attribute
  * Third: add your rule name into `RuleChoices` class

:smiley:

**_Done =)_**
