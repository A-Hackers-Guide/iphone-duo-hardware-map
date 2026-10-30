# `TUConversationMemberAssociation`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 20 instance methods, 3 class methods

## Instance variables

```
B _primary;
q _type;
@"TUHandle" _handle;
Q _identifier;
@"NSString" _avcIdentifier;
@"NSData" _messagingData;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"TUHandle",&,N,V_handle) handle;
@property (TB,N,GisPrimary,V_primary) primary;
@property (TQ,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_avcIdentifier) avcIdentifier;
@property (T@"NSData",R,C,N,V_messagingData) messagingData;
```

## Class methods

```
+[TUConversationMemberAssociation supportsSecureCoding];
+[TUConversationMemberAssociation associationForHandle:from:];
+[TUConversationMemberAssociation messagingDataWithType:primaryHandle:primaryIdentifier:primaryAvcIdentifier:associatedPseudonym:conversationGroupUUIDString:];
```

## Instance methods

```
-[TUConversationMemberAssociation identifier];
-[TUConversationMemberAssociation isPrimary];
-[TUConversationMemberAssociation messagingData];
-[TUConversationMemberAssociation setPrimary:];
-[TUConversationMemberAssociation avcIdentifier];
-[TUConversationMemberAssociation setAvcIdentifier:];
-[TUConversationMemberAssociation setIdentifier:];
-[TUConversationMemberAssociation handle];
-[TUConversationMemberAssociation setType:];
-[TUConversationMemberAssociation type];
-[TUConversationMemberAssociation encodeWithCoder:];
-[TUConversationMemberAssociation hash];
-[TUConversationMemberAssociation description];
-[TUConversationMemberAssociation initWithCoder:];
-[TUConversationMemberAssociation setHandle:];
-[TUConversationMemberAssociation copyWithZone:];
-[TUConversationMemberAssociation isEqual:];
-[TUConversationMemberAssociation initWithHandle:type:primary:];
-[TUConversationMemberAssociation initWithMemberAssociation:];
-[TUConversationMemberAssociation isEqualToAssociation:];
```
