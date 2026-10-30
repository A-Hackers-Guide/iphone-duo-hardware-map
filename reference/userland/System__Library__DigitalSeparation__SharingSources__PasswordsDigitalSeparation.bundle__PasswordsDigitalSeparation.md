# `/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`

iOS 27.2 dyld shared cache image. Version `7625.2.8.21.6`. **[DSC]**

## Linked libraries (9)

- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/Contacts.framework/Contacts`
- `/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`
- `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 4 classes, 5 protocols, 82 methods, 50 properties

### Class pages

Every class and protocol, with its methods: [`DSIdentifiable`](../objc/DSIdentifiable_PasswordsDigitalSeparation.protocol.md), [`DSParticipation`](../objc/DSParticipation_PasswordsDigitalSeparation.protocol.md), [`DSSharedResource`](../objc/DSSharedResource_PasswordsDigitalSeparation.protocol.md), [`DSSource`](../objc/DSSource_PasswordsDigitalSeparation.protocol.md), [`NSObject`](../objc/NSObject_PasswordsDigitalSeparation.protocol.md), [`PMSeparationGroup`](../objc/PMSeparationGroup_PasswordsDigitalSeparation.md), [`PMSeparationParticipant`](../objc/PMSeparationParticipant_PasswordsDigitalSeparation.md), [`PMSeparationParticipantIdentity`](../objc/PMSeparationParticipantIdentity_PasswordsDigitalSeparation.md), [`PMSeparationSource`](../objc/PMSeparationSource_PasswordsDigitalSeparation.md)

### Classes

`PMSeparationGroup`, `PMSeparationParticipant`, `PMSeparationParticipantIdentity`, `PMSeparationSource`

### Protocols

`DSIdentifiable`, `DSParticipation`, `DSSharedResource`, `DSSource`, `NSObject`

### Properties

```
@property (T@"NSString",R,C,N) unifiedContactIdentifier;
@property (T@"NSPersonNameComponents",R,C,N) nameComponents;
@property (T@"NSString",R,C,N) emailAddress;
@property (T@"NSString",R,C,N) phoneNumber;
@property (Tq,R,N) role;
@property (Tq,R,N) permission;
@property (T@"<DSIdentifiable>",R,N) identity;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) displayDetail;
@property (T@"NSArray",R,C,N) participants;
@property (Tq,R,N) visibility;
@property (TQ,?,R,N) participationAccess;
@property (T@"NSString",R,C,N) name;
@property (T@"NSArray",?,R,C,N) resourceNames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"KCSharingGroup",R,N,V_group) group;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) displayDetail;
@property (T@"NSArray",R,C,N,V_participants) participants;
@property (Tq,R,N) visibility;
@property (TQ,?,R,N) participationAccess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"KCSharingParticipant",R,N,V_participant) participant;
@property (Tq,R,N) role;
@property (Tq,R,N) permission;
@property (T@"<DSIdentifiable>",R,N,V_identity) identity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_contactIdentifier) unifiedContactIdentifier;
@property (T@"NSPersonNameComponents",R,C,N) nameComponents;
@property (T@"NSString",R,C,N,V_emailAddress) emailAddress;
@property (T@"NSString",R,C,N,V_phoneNumber) phoneNumber;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) name;
@property (T@"NSArray",?,R,C,N) resourceNames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (45)

```
<%@: %p; groupID: %@>
v16@?0@\"NSError\"8
Safari
%s
com.apple.SafariShared.PasswordsDigitalSepration.PMSeparationErrorDomain
v32@?0@\"KCSharingGroup\"8Q16^B24
B16@?0@\"KCSharingParticipant\"8
Failed to copy contributed items back to My Passwords from group.
ocs
Invalid participant: %@
/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation
/AppleInternal/Library/Frameworks/DigitalSeparation.framework/DigitalSeparation
void *DigitalSeparationLibrary(void)
DSSourceNamePassKeys
@\"PMSeparationParticipant\"16@?0@\"KCSharingParticipant\"8
v32@?0@\"WBSPair\"8Q16^B24
B16@?0@\"KCSharingGroup\"8
v8@?0
DigitalSeparationSoftLink.m
<%@: %p; handle: %@>
v24@?0@\"KCSharingGroup\"8@\"NSError\"16
v24@?0@\"NSArray\"8@\"NSError\"16
@\"PMSeparationGroup\"16@?0@\"KCSharingGroup\"8
Invalid resource: %@
/System/Library/Frameworks/DigitalSeparation.framework/DigitalSeparation
/System/AppleInternal/Library/Frameworks/DigitalSeparation.framework/DigitalSeparation
typeof (((typeof (DSSourceNamePassKeys) (*)(void))0)()) getDSSourceNamePassKeys(void)
Stop sharing with participant: %@
Falling back to email address for unknown participant handle: %@
Failed to fetch groups: %@
Ignoring fetch groups request: ongoing sharing feature is disabled
Failed to fetch group (%@): %@
Failed to remove participant (%@) from group (%@): %@
Failed to leave group (%@): %@
Failed to stop all sharing: %@
Failed to remove participants from group (%@): %@
Failed to copy contributed items back to My Passwords from group: %@
Invalid resource: %@
Failed to stop sharing with group (%@): %@
Invalid participant: %@
Failed to stop sharing with participant (%@): %@
Fetch shared groups
Stop sharing with group: %@
Ignoring stop sharing request: ongoing sharing feature is disabled
Stop all sharing
```
