# `TUConversationParticipantCluster`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 13 instance methods, 5 class methods

## Instance variables

```
@"NSUUID" _UUID;
q _type;
```

## Properties

```
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[TUConversationParticipantCluster supportsSecureCoding];
+[TUConversationParticipantCluster UUIDFromURLComponents:namePrefix:];
+[TUConversationParticipantCluster participantClusterFromURLComponents:namePrefix:];
+[TUConversationParticipantCluster queryItemName:prefix:];
+[TUConversationParticipantCluster typeFromURLComponents:namePrefix:];
```

## Instance methods

```
-[TUConversationParticipantCluster UUID];
-[TUConversationParticipantCluster type];
-[TUConversationParticipantCluster encodeWithCoder:];
-[TUConversationParticipantCluster hash];
-[TUConversationParticipantCluster description];
-[TUConversationParticipantCluster initWithCoder:];
-[TUConversationParticipantCluster copyWithZone:];
-[TUConversationParticipantCluster isEqual:];
-[TUConversationParticipantCluster initWithUUID:type:];
-[TUConversationParticipantCluster isEqualToParticipantCluster:];
-[TUConversationParticipantCluster queryItemsWithNamePrefix:];
-[TUConversationParticipantCluster typeQueryItemWithNamePrefix:];
-[TUConversationParticipantCluster uuidQueryItemWithNamePrefix:];
```
