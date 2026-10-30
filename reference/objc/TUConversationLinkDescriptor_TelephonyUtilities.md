# `TUConversationLinkDescriptor`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 16 instance variables, 16 properties, 42 instance methods, 1 class methods

## Instance variables

```
B _activated;
i _version;
@"NSDate" _creationDate;
@"NSDate" _deletionDate;
@"NSDate" _expirationDate;
q _linkLifetimeScope;
q _deleteReason;
q _deletionLayer;
@"NSUUID" _groupUUID;
@"NSSet" _invitedHandles;
@"NSString" _name;
@"TUConversationLinkOriginator" _originator;
@"NSData" _privateKey;
@"NSString" _pseudonym;
@"NSData" _publicKey;
@"NSUUID" _accessibilityReqUUID;
```

## Properties

```
@property (TB,N,GisActivated,V_activated) activated;
@property (T@"NSDate",&,N,V_creationDate) creationDate;
@property (T@"NSDate",&,N,V_deletionDate) deletionDate;
@property (T@"NSDate",&,N,V_expirationDate) expirationDate;
@property (T@"NSUUID",&,N,V_groupUUID) groupUUID;
@property (T@"NSSet",C,N,V_invitedHandles) invitedHandles;
@property (T@"NSString",C,N,V_name) name;
@property (T@"TUConversationLinkOriginator",&,N,V_originator) originator;
@property (T@"NSData",C,N,V_privateKey) privateKey;
@property (T@"NSString",C,N,V_pseudonym) pseudonym;
@property (T@"NSData",C,N,V_publicKey) publicKey;
@property (T@"NSUUID",C,N,V_accessibilityReqUUID) accessibilityReqUUID;
@property (Ti,N,V_version) version;
@property (Tq,N,V_linkLifetimeScope) linkLifetimeScope;
@property (Tq,N,V_deleteReason) deleteReason;
@property (Tq,N,V_deletionLayer) deletionLayer;
```

## Class methods

```
+[TUConversationLinkDescriptor supportsSecureCoding];
```

## Instance methods

```
-[TUConversationLinkDescriptor isActivated];
-[TUConversationLinkDescriptor publicKey];
-[TUConversationLinkDescriptor setAccessibilityReqUUID:];
-[TUConversationLinkDescriptor setGroupUUID:];
-[TUConversationLinkDescriptor groupUUID];
-[TUConversationLinkDescriptor setDeleteReason:];
-[TUConversationLinkDescriptor setLinkLifetimeScope:];
-[TUConversationLinkDescriptor mutableCopyWithZone:];
-[TUConversationLinkDescriptor deleteReason];
-[TUConversationLinkDescriptor setActivated:];
-[TUConversationLinkDescriptor setPseudonym:];
-[TUConversationLinkDescriptor setPublicKey:];
-[TUConversationLinkDescriptor expirationDate];
-[TUConversationLinkDescriptor pseudonym];
-[TUConversationLinkDescriptor setOriginator:];
-[TUConversationLinkDescriptor creationDate];
-[TUConversationLinkDescriptor version];
-[TUConversationLinkDescriptor deletionDate];
-[TUConversationLinkDescriptor setDeletionLayer:];
-[TUConversationLinkDescriptor setCreationDate:];
-[TUConversationLinkDescriptor encodeWithCoder:];
-[TUConversationLinkDescriptor deletionLayer];
-[TUConversationLinkDescriptor hash];
-[TUConversationLinkDescriptor description];
-[TUConversationLinkDescriptor setName:];
-[TUConversationLinkDescriptor initWithCoder:];
-[TUConversationLinkDescriptor setExpirationDate:];
-[TUConversationLinkDescriptor setVersion:];
-[TUConversationLinkDescriptor copyWithZone:];
-[TUConversationLinkDescriptor isEqual:];
-[TUConversationLinkDescriptor linkLifetimeScope];
-[TUConversationLinkDescriptor originator];
-[TUConversationLinkDescriptor name];
-[TUConversationLinkDescriptor setDeletionDate:];
-[TUConversationLinkDescriptor accessibilityReqUUID];
-[TUConversationLinkDescriptor privateKey];
-[TUConversationLinkDescriptor setPrivateKey:];
-[TUConversationLinkDescriptor invitedHandles];
-[TUConversationLinkDescriptor setInvitedHandles:];
-[TUConversationLinkDescriptor initWithConversationLinkDescriptor:];
-[TUConversationLinkDescriptor initWithGroupUUID:originator:pseudonym:publicKey:];
-[TUConversationLinkDescriptor isEqualToConversationLinkDescriptor:];
```
