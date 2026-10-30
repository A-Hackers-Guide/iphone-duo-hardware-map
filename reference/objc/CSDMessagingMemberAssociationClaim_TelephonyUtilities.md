# `CSDMessagingMemberAssociationClaim`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 34 instance methods, 0 class methods

## Instance variables

```
Q _primaryIdentifier;
@"CSDMessagingHandle" _associatedPseudonym;
@"NSString" _conversationGroupUUIDString;
@"NSString" _primaryAvcIdentifier;
@"CSDMessagingHandle" _primaryHandle;
i _type;
I _version;
{?="primaryIdentifier"b1"type"b1"version"b1} _has;
```

## Properties

```
@property (TB,N) hasVersion;
@property (TI,N,V_version) version;
@property (TB,R,N) hasPrimaryHandle;
@property (T@"CSDMessagingHandle",&,N,V_primaryHandle) primaryHandle;
@property (TB,N) hasPrimaryIdentifier;
@property (TQ,N,V_primaryIdentifier) primaryIdentifier;
@property (TB,R,N) hasPrimaryAvcIdentifier;
@property (T@"NSString",&,N,V_primaryAvcIdentifier) primaryAvcIdentifier;
@property (TB,R,N) hasAssociatedPseudonym;
@property (T@"CSDMessagingHandle",&,N,V_associatedPseudonym) associatedPseudonym;
@property (TB,R,N) hasConversationGroupUUIDString;
@property (T@"NSString",&,N,V_conversationGroupUUIDString) conversationGroupUUIDString;
@property (TB,N) hasType;
@property (Ti,N,V_type) type;
```

## Instance methods

```
-[CSDMessagingMemberAssociationClaim primaryIdentifier];
-[CSDMessagingMemberAssociationClaim hasVersion];
-[CSDMessagingMemberAssociationClaim writeTo:];
-[CSDMessagingMemberAssociationClaim setHasType:];
-[CSDMessagingMemberAssociationClaim mergeFrom:];
-[CSDMessagingMemberAssociationClaim hasType];
-[CSDMessagingMemberAssociationClaim setHasVersion:];
-[CSDMessagingMemberAssociationClaim version];
-[CSDMessagingMemberAssociationClaim setType:];
-[CSDMessagingMemberAssociationClaim type];
-[CSDMessagingMemberAssociationClaim hash];
-[CSDMessagingMemberAssociationClaim copyTo:];
-[CSDMessagingMemberAssociationClaim description];
-[CSDMessagingMemberAssociationClaim setVersion:];
-[CSDMessagingMemberAssociationClaim readFrom:];
-[CSDMessagingMemberAssociationClaim copyWithZone:];
-[CSDMessagingMemberAssociationClaim isEqual:];
-[CSDMessagingMemberAssociationClaim dictionaryRepresentation];
-[CSDMessagingMemberAssociationClaim setConversationGroupUUIDString:];
-[CSDMessagingMemberAssociationClaim associatedPseudonym];
-[CSDMessagingMemberAssociationClaim conversationGroupUUIDString];
-[CSDMessagingMemberAssociationClaim hasAssociatedPseudonym];
-[CSDMessagingMemberAssociationClaim hasConversationGroupUUIDString];
-[CSDMessagingMemberAssociationClaim hasPrimaryAvcIdentifier];
-[CSDMessagingMemberAssociationClaim hasPrimaryHandle];
-[CSDMessagingMemberAssociationClaim hasPrimaryIdentifier];
-[CSDMessagingMemberAssociationClaim primaryAvcIdentifier];
-[CSDMessagingMemberAssociationClaim primaryHandle];
-[CSDMessagingMemberAssociationClaim setAssociatedPseudonym:];
-[CSDMessagingMemberAssociationClaim setHasPrimaryIdentifier:];
-[CSDMessagingMemberAssociationClaim setPrimaryAvcIdentifier:];
-[CSDMessagingMemberAssociationClaim setPrimaryHandle:];
-[CSDMessagingMemberAssociationClaim setPrimaryIdentifier:];
-[CSDMessagingMemberAssociationClaim tuAssociationForHandle:];
```
