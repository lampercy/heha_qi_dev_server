# Heha_qi backend API draft

## Index

* Find Users
* Get Friends
* Add Friend

## Find Users

**Description:** Find users by phone numbers, weibo ids, weixin ids or qq ids

**Route:** /users

**Method:** GET

| Param  | Type                | Description  |
| ------ | ------------------- | ------------ |
| phone_numbers| <code>Array</code> | optional |
| weibo_ids | <code>Array</code> | optional |
| weixin_ids | <code>Array</code> | optional |
| qq_ids | <code>Array</code> | optional|

**Response:**

```
   {
      "users": [
        {
          "id": 1234,
          "name": "Percy BB",
          "avatar_url": "http://example.com/avatars/1/thumb.jpg"
        },
        ...
      ]
  }
```

## Get Friends

**Description:** Get friends of the current user

**Route:** /friends

**Method:** GET

**Response:**

```
   {
      "friends": [
        {
          "id": 1234,
          "name": "Percy BB",
          "avatar_url": "http://example.com/avatars/1/thumb.jpg"
        },
        ...
      ]
  }
```

## Add Friend

**Description:** add user as a friend of the current user

**Route:** /friends

**Method:** POST

| Param  | Type                | Description  |
| ------ | ------------------- | ------------ |
| user_id| <code>id</code> | |

**Response:**

* success
```
  {
     "success": true
  }
```

* fail
```
  {
     "success": false
  }
```
