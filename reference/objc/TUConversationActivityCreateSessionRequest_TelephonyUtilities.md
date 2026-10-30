# `TUConversationActivityCreateSessionRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
@"NSString" _activityIdentifier;
@"NSData" _applicationContext;
@"TUConversationActivityMetadata" _metadata;
@"CKShare" _share;
@"NSString" _staticIdentifier;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"NSString",C,N,V_activityIdentifier) activityIdentifier;
@property (T@"NSData",C,N,V_applicationContext) applicationContext;
@property (T@"TUConversationActivityMetadata",&,N,V_metadata) metadata;
@property (T@"CKShare",C,N,V_share) share;
@property (T@"NSString",C,N,V_staticIdentifier) staticIdentifier;
```

## Class methods

```
+[TUConversationActivityCreateSessionRequest supportsSecureCoding];
```

## Instance methods

```
-[TUConversationActivityCreateSessionRequest setShare:];
-[TUConversationActivityCreateSessionRequest activityIdentifier];
-[TUConversationActivityCreateSessionRequest setApplicationContext:];
-[TUConversationActivityCreateSessionRequest mutableCopyWithZone:];
-[TUConversationActivityCreateSessionRequest setUUID:];
-[TUConversationActivityCreateSessionRequest setActivityIdentifier:];
-[TUConversationActivityCreateSessionRequest UUID];
-[TUConversationActivityCreateSessionRequest share];
-[TUConversationActivityCreateSessionRequest metadata];
-[TUConversationActivityCreateSessionRequest applicationContext];
-[TUConversationActivityCreateSessionRequest encodeWithCoder:];
-[TUConversationActivityCreateSessionRequest setMetadata:];
-[TUConversationActivityCreateSessionRequest hash];
-[TUConversationActivityCreateSessionRequest description];
-[TUConversationActivityCreateSessionRequest initWithCoder:];
-[TUConversationActivityCreateSessionRequest copyWithZone:];
-[TUConversationActivityCreateSessionRequest isEqual:];
-[TUConversationActivityCreateSessionRequest initWithMetadata:applicationContext:activityIdentifier:uuid:];
-[TUConversationActivityCreateSessionRequest initWithMetadata:applicationContext:activityIdentifier:uuid:staticIdentifier:];
-[TUConversationActivityCreateSessionRequest isEqualToConversationActivitySessionCreationRequest:];
-[TUConversationActivityCreateSessionRequest setStaticIdentifier:];
-[TUConversationActivityCreateSessionRequest staticIdentifier];
```
