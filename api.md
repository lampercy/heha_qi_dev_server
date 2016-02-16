# Heha_qi backend API draft

## Index

* Find Users
* Get Friends
* Add Friend
* Invite Friend
* Create Chat
* Get Chats
* Get Chat

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
          "avatar_url": "http://example.com/avatars/1/thumb.jpg",
          "jid": "percy_bb@example.com"
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
          "avatar_url": "http://example.com/avatars/1/thumb.jpg",
          "jid": "percy_bb@example.com"
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
    "user": {
      "id": 1234,
      "name": "Percy BB",
      "avatar_url": "http://example.com/avatars/1/thumb.jpg",
      "jid": "percy_bb@example.com"
    }
  }
```

* fail
```
  {
    "success": false
  }
```

## Invite Friend

**Description:** invite a friend to join heha

**Route:** /invite

**Method:** GET

| Param  | Type                | Description  |
| ------ | ------------------- | ------------ |
| phone_number| <code>String</code> | optional |
| weibo_id | <code>String</code> | optional |
| weixin_id | <code>String</code> | optional |
| qq_id | <code>String</code> | optional|

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

## Create Chat

**Description:** create a chat (either direct message or group chat)

**Route:** /chats

**Method:** POST

| Param  | Type                | Description  |
| ------ | ------------------- | ------------ |
| participant_ids | <code>Array</code> | |
| is_direct_message | <code>Bool</code> | |
| name | <code>String</code> | only for group chat|
| jid | <code>String</code> | only for group chat|
| photo| <code>Base64</code> | only for group chat|


**Response:**

* success
```
  {
    "success": true
    "chat": {
      "id": 123,
      "is_direct_message": false,
      "name": "My Chat Group",
      "participants": [
        {
          "id": 1234,
          "name": "Percy BB",
          "avatar_url": "http://example.com/avatars/1/thumb.jpg",
          "jid": "percy_bb@example.com"
        },
        ...
      ],
      "jid": "my_chat_group-65ec9a385ee540c892527bca5ca3f936@example.com",
      "photo_url": "http://example.com/photos/1/thumb.jpg",
      "last_message_sent_at": null,
      "battles": []
    }
  }
```

* fail
```
  {
     "success": false
  }
```

## Get Chats

**Description:** get the chats in which the current user is participating

**Route:** /chats

**Method:** GET

**Response:**

```
  {
    "chats": [
      {
        "id": 1234,
        "is_direct_message": false,
        "name": "My Chat Group",
        "number_of_participants": 4
        "jid": "my_chat_group-65ec9a385ee540c892527bca5ca3f936@example.com",
        "photo_url": "http://example.com/photos/1/thumb.jpg",
        "last_message": "How are you?",
        "last_message_sent_by": {
            "id": 1234,
            "name": "Percy BB",
            "avatar_url": "http://example.com/avatars/1/thumb.jpg",
            "jid": "percy_bb@example.com"
        }
        "last_message_sent_at": 12569537329,
        "is_having_battle": true
        ]
      }, 
      ...
    ]
  }
```
**Note:** sorted in descending order of last_message_sent_at


## Get Chat

**Description:** get the details of a chat

**Route:** /chats/:id

**Method:** GET

**Response:**
```
  {
    "chat": {
      "id": 1234,
      "is_direct_message": false,
      "name": "My Chat Group",
      "participants": [
        {
          "id": 1234,
          "name": "Percy BB",
          "avatar_url": "http://example.com/avatars/1/thumb.jpg",
          "jid": "percy_bb@example.com"
        },
        ...
      ],
      "jid": "my_chat_group-65ec9a385ee540c892527bca5ca3f936@example.com",
      "photo_url": "http://example.com/photos/1/thumb.jpg",
      "is_having_battle": true,
      "battles": [
        {
          "id": 1234,
          "chat_id": 1234,
          "steps": {
            "1234": 8000,
            "2234": 3000,
            "3244": 4000
          },
          "current": true,
          "started_at": 12569537329,
          "finished_at": 12569637329
        },
        ...
      ]
    }
  }
```
