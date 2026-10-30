# `TUMomentsMessageSendRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _sessionUUID;
@"NSUUID" _conversationID;
@"TUHandle" _senderHandle;
@"NSSet" _destinationHandles;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_sessionUUID) sessionUUID;
@property (T@"NSUUID",R,C,N,V_conversationID) conversationID;
@property (T@"TUHandle",R,C,N,V_senderHandle) senderHandle;
@property (T@"NSSet",R,C,N,V_destinationHandles) destinationHandles;
```

## Class methods

```
+[TUMomentsMessageSendRequest supportsSecureCoding];
```

## Instance methods

```
-[TUMomentsMessageSendRequest conversationID];
-[TUMomentsMessageSendRequest sessionUUID];
-[TUMomentsMessageSendRequest senderHandle];
-[TUMomentsMessageSendRequest encodeWithCoder:];
-[TUMomentsMessageSendRequest initWithCoder:];
-[TUMomentsMessageSendRequest destinationHandles];
-[TUMomentsMessageSendRequest initWithSessionUUID:conversationID:senderHandle:destinationHandles:];
```
