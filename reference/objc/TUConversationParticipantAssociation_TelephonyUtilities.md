# `TUConversationParticipantAssociation`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 15 instance methods, 5 class methods

## Instance variables

```
Q _identifier;
@"NSString" _avcIdentifier;
```

## Properties

```
@property (TQ,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_avcIdentifier) avcIdentifier;
```

## Class methods

```
+[TUConversationParticipantAssociation supportsSecureCoding];
+[TUConversationParticipantAssociation avcIdentifierFromURLComponents:namePrefix:];
+[TUConversationParticipantAssociation identifierFromURLComponents:namePrefix:];
+[TUConversationParticipantAssociation participantAssociationFromURLComponents:namePrefix:];
+[TUConversationParticipantAssociation queryItemName:prefix:];
```

## Instance methods

```
-[TUConversationParticipantAssociation identifier];
-[TUConversationParticipantAssociation avcIdentifier];
-[TUConversationParticipantAssociation setAvcIdentifier:];
-[TUConversationParticipantAssociation setIdentifier:];
-[TUConversationParticipantAssociation encodeWithCoder:];
-[TUConversationParticipantAssociation hash];
-[TUConversationParticipantAssociation description];
-[TUConversationParticipantAssociation initWithCoder:];
-[TUConversationParticipantAssociation copyWithZone:];
-[TUConversationParticipantAssociation isEqual:];
-[TUConversationParticipantAssociation initWithParticipantAssociation:];
-[TUConversationParticipantAssociation avcIdentifierQueryItemWithNamePrefix:];
-[TUConversationParticipantAssociation identifierQueryItemWithNamePrefix:];
-[TUConversationParticipantAssociation isEqualToParticipantAssociation:];
-[TUConversationParticipantAssociation queryItemsWithNamePrefix:];
```
