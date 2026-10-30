# `TUContinuityConversation`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _uuid;
@"NSString" _displayName;
Q _avMode;
q _letMeInRequestState;
@"NSNumber" _state;
q _remoteMemberCount;
@"NSArray" _remoteMemberContactIdentifiers;
@"NSData" _handlesHash;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TQ,R,N,V_avMode) avMode;
@property (Tq,R,N,V_letMeInRequestState) letMeInRequestState;
@property (T@"NSNumber",R,N,V_state) state;
@property (Tq,R,N,V_remoteMemberCount) remoteMemberCount;
@property (T@"NSArray",R,N,V_remoteMemberContactIdentifiers) remoteMemberContactIdentifiers;
@property (T@"NSData",R,N,V_handlesHash) handlesHash;
```

## Class methods

```
+[TUContinuityConversation supportsSecureCoding];
```

## Instance methods

```
-[TUContinuityConversation uuid];
-[TUContinuityConversation displayName];
-[TUContinuityConversation encodeWithCoder:];
-[TUContinuityConversation description];
-[TUContinuityConversation initWithCoder:];
-[TUContinuityConversation state];
-[TUContinuityConversation avMode];
-[TUContinuityConversation handlesHash];
-[TUContinuityConversation initWithUUID:displayName:state:avMode:remoteMemberCount:remoteMemberContactIdentifiers:letMeInRequestState:handlesHash:];
-[TUContinuityConversation letMeInRequestState];
-[TUContinuityConversation remoteMemberContactIdentifiers];
-[TUContinuityConversation remoteMemberCount];
```
