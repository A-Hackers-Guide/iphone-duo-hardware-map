# `TUConversationNotice`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationNoticeProtocol`
- 8 instance variables, 12 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
q _sessionEventType;
@"NSUUID" _sessionUUID;
@"NSURL" _actionURL;
@"NSString" _bundleIdentifier;
@"NSString" _item;
q _queueItemType;
@"TUConversationActivitySession" _session;
```

## Properties

```
@property (T@"NSUUID",&,N,V_sessionUUID) sessionUUID;
@property (T@"NSURL",&,N,V_actionURL) actionURL;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",C,N,V_item) item;
@property (Tq,N,V_queueItemType) queueItemType;
@property (T@"TUConversationActivitySession",&,N,V_session) session;
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (Tq,N,V_sessionEventType) sessionEventType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUConversationNotice supportsSecureCoding];
```

## Instance methods

```
-[TUConversationNotice sessionUUID];
-[TUConversationNotice setSessionUUID:];
-[TUConversationNotice initWithUUID:];
-[TUConversationNotice UUID];
-[TUConversationNotice setItem:];
-[TUConversationNotice bundleIdentifier];
-[TUConversationNotice item];
-[TUConversationNotice setSession:];
-[TUConversationNotice encodeWithCoder:];
-[TUConversationNotice hash];
-[TUConversationNotice description];
-[TUConversationNotice initWithCoder:];
-[TUConversationNotice actionURL];
-[TUConversationNotice setBundleIdentifier:];
-[TUConversationNotice session];
-[TUConversationNotice isEqual:];
-[TUConversationNotice setActionURL:];
-[TUConversationNotice isEqualToConversationNotice:];
-[TUConversationNotice queueItemType];
-[TUConversationNotice sessionEventType];
-[TUConversationNotice setQueueItemType:];
-[TUConversationNotice setSessionEventType:];
```
