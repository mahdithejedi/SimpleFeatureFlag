# Feature Flag Platform
By this platform you can Set Rules for your Features and do A/B test for your users


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