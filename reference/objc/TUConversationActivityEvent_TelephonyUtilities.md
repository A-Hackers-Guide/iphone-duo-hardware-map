# `TUConversationActivityEvent`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _sessionUUID;
@"TUConversationParticipant" _originator;
q _type;
q _queueItemType;
@"NSString" _item;
@"NSString" _localizedDescription;
@"TUConversationActivitySession" _session;
@"NSURL" _url;
```

## Properties

```
@property (T@"NSUUID",&,N,V_sessionUUID) sessionUUID;
@property (T@"TUConversationParticipant",&,N,V_originator) originator;
@property (Tq,N,V_type) type;
@property (Tq,N,V_queueItemType) queueItemType;
@property (T@"NSString",&,N,V_item) item;
@property (T@"NSString",R,N,V_localizedDescription) localizedDescription;
@property (T@"TUConversationActivitySession",&,N,V_session) session;
@property (T@"NSURL",&,N,V_url) url;
```

## Class methods

```
+[TUConversationActivityEvent supportsSecureCoding];
```

## Instance methods

```
-[TUConversationActivityEvent localizedDescription];
-[TUConversationActivityEvent sessionUUID];
-[TUConversationActivityEvent setSessionUUID:];
-[TUConversationActivityEvent setItem:];
-[TUConversationActivityEvent setOriginator:];
-[TUConversationActivityEvent item];
-[TUConversationActivityEvent setSession:];
-[TUConversationActivityEvent setType:];
-[TUConversationActivityEvent type];
-[TUConversationActivityEvent encodeWithCoder:];
-[TUConversationActivityEvent hash];
-[TUConversationActivityEvent description];
-[TUConversationActivityEvent initWithCoder:];
-[TUConversationActivityEvent setUrl:];
-[TUConversationActivityEvent session];
-[TUConversationActivityEvent copyWithZone:];
-[TUConversationActivityEvent isEqual:];
-[TUConversationActivityEvent originator];
-[TUConversationActivityEvent url];
-[TUConversationActivityEvent initWithSessionUUID:originator:type:];
-[TUConversationActivityEvent isEqualToConversationActivityEvent:];
-[TUConversationActivityEvent queueItemType];
-[TUConversationActivityEvent setQueueItemType:];
```
