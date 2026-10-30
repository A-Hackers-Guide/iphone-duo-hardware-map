# `TUConversationLink`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 22 properties, 52 instance methods, 14 class methods

## Instance variables

```
B _locallyCreated;
@"NSString" _pseudonym;
@"NSData" _publicKey;
@"NSDate" _creationDate;
@"NSDate" _deletionDate;
@"NSUUID" _groupUUID;
@"TUHandle" _originatorHandle;
q _linkLifetimeScope;
q _deleteReason;
q _deletionLayer;
@"NSUUID" _accessibilityReqUUID;
@"NSString" _URLFragment;
@"NSString" _linkName;
@"NSDate" _expirationDate;
@"NSSet" _invitedMemberHandles;
```

## Properties

```
@property (T@"NSDate",&,N,V_creationDate) creationDate;
@property (T@"NSDate",&,N,V_deletionDate) deletionDate;
@property (T@"NSUUID",&,N,V_groupUUID) groupUUID;
@property (TB,N,GisLocallyCreated,V_locallyCreated) locallyCreated;
@property (T@"TUHandle",&,N,V_originatorHandle) originatorHandle;
@property (T@"NSString",C,N,V_pseudonym) pseudonym;
@property (T@"NSData",C,N,V_publicKey) publicKey;
@property (Tq,N,V_linkLifetimeScope) linkLifetimeScope;
@property (Tq,N,V_deleteReason) deleteReason;
@property (Tq,N,V_deletionLayer) deletionLayer;
@property (T@"NSUUID",&,N,V_accessibilityReqUUID) accessibilityReqUUID;
@property (T@"NSString",&,N,V_URLFragment) URLFragment;
@property (T@"NSString",C,N,V_linkName) linkName;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSDate",&,N,V_expirationDate) expirationDate;
@property (T@"NSSet",C,N,V_invitedMemberHandles) invitedMemberHandles;
@property (T@"NSString",&,N) URLFragment;
@property (T@"NSString",C,N) linkName;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSDate",&,N) expirationDate;
@property (T@"NSSet",C,N) invitedMemberHandles;
@property (T@"NSURL",R,N) URL;
```

## Class methods

```
+[TUConversationLink supportsSecureCoding];
+[TUConversationLink baseURLs];
+[TUConversationLink featureFlags];
+[TUConversationLink baseURLComponentsForURL:];
+[TUConversationLink baseURLStrings];
+[TUConversationLink checkMatchingConversationLinkCriteriaForURL:];
+[TUConversationLink conversationLinkComponentsFromURL:];
+[TUConversationLink conversationLinkForURL:];
+[TUConversationLink conversationLinkVersion];
+[TUConversationLink preferredBaseURL];
+[TUConversationLink preferredBaseURLString];
+[TUConversationLink prefixedPseudonymFor:];
+[TUConversationLink publicKeyForBase64EncodedString:];
+[TUConversationLink userConfiguration];
```

## Instance methods

```
-[TUConversationLink setLinkName:];
-[TUConversationLink publicKey];
-[TUConversationLink setAccessibilityReqUUID:];
-[TUConversationLink setGroupUUID:];
-[TUConversationLink groupUUID];
-[TUConversationLink setDeleteReason:];
-[TUConversationLink setLinkLifetimeScope:];
-[TUConversationLink setLocallyCreated:];
-[TUConversationLink deleteReason];
-[TUConversationLink setPseudonym:];
-[TUConversationLink linkName];
-[TUConversationLink setPublicKey:];
-[TUConversationLink generateDisplayName];
-[TUConversationLink initWithPseudonym:publicKey:groupUUID:originatorHandle:creationDate:deletionDate:expirationDate:invitedMemberHandles:locallyCreated:linkName:linkLifetimeScope:deleteReason:deletionLayer:accessibilityReqUUID:];
-[TUConversationLink expirationDate];
-[TUConversationLink displayName];
-[TUConversationLink allInvitedMembersInContactsChecking:];
-[TUConversationLink isEquivalentToPseudonym:andPublicKey:];
-[TUConversationLink initWithPseudonym:publicKey:groupUUID:originatorHandle:];
-[TUConversationLink initWithDescriptor:];
-[TUConversationLink fetchedResults];
-[TUConversationLink pseudonym];
-[TUConversationLink creationDate];
-[TUConversationLink isLocallyCreated];
-[TUConversationLink deletionDate];
-[TUConversationLink valueForKey:];
-[TUConversationLink canCreateConversations];
-[TUConversationLink setDeletionLayer:];
-[TUConversationLink setCreationDate:];
-[TUConversationLink URLFragment];
-[TUConversationLink encodeWithCoder:];
-[TUConversationLink unprefixedPseudonym];
-[TUConversationLink isEqualToConversationLink:];
-[TUConversationLink base64PublicKey];
-[TUConversationLink deletionLayer];
-[TUConversationLink hash];
-[TUConversationLink invitedMemberHandles];
-[TUConversationLink setInvitedMemberHandles:];
-[TUConversationLink originatorHandle];
-[TUConversationLink description];
-[TUConversationLink isEquivalentToConversationLink:];
-[TUConversationLink isAccessibilityLink];
-[TUConversationLink initWithCoder:];
-[TUConversationLink setExpirationDate:];
-[TUConversationLink copyWithZone:];
-[TUConversationLink setOriginatorHandle:];
-[TUConversationLink setURLFragment:];
-[TUConversationLink isEqual:];
-[TUConversationLink linkLifetimeScope];
-[TUConversationLink setDeletionDate:];
-[TUConversationLink URL];
-[TUConversationLink accessibilityReqUUID];
```
