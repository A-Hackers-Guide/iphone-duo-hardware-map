# `TUConversationReport`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timebase;
@"NSUUID" _conversationID;
@"NSUUID" _paddingForHashedValue;
```

## Properties

```
@property (T@"NSDate",R,N,V_timebase) timebase;
@property (T@"NSUUID",R,N,V_conversationID) conversationID;
@property (T@"NSUUID",R,N,V_paddingForHashedValue) paddingForHashedValue;
```

## Class methods

```
+[TUConversationReport supportsSecureCoding];
```

## Instance methods

```
-[TUConversationReport timebase];
-[TUConversationReport conversationID];
-[TUConversationReport init];
-[TUConversationReport hashForParticipantIdentifier:];
-[TUConversationReport paddingForHashedValue];
-[TUConversationReport isEqualToConversationReport:];
-[TUConversationReport encodeWithCoder:];
-[TUConversationReport hash];
-[TUConversationReport description];
-[TUConversationReport initWithCoder:];
-[TUConversationReport copyWithZone:];
-[TUConversationReport isEqual:];
-[TUConversationReport initWithConversationID:padding:timebase:];
```
