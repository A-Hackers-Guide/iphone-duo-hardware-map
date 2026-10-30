# `KCSharingParticipant`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 10 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _isCurrentUser;
@"NSString" _participantID;
@"NSString" _handle;
q _permissionLevel;
q _inviteStatus;
@"KCSharingParticipant" _invitedBy;
@"NSData" _sharingInvitationData;
```

## Properties

```
@property (T@"NSString",R,C,N) longDescription;
@property (T@"NSDictionary",R,C,N) JSONObject;
@property (T@"NSString",R,C,N,V_participantID) participantID;
@property (T@"NSString",R,C,N,V_handle) handle;
@property (Tq,N,V_permissionLevel) permissionLevel;
@property (TB,R,N,V_isCurrentUser) isCurrentUser;
@property (TB,R,N) isOwner;
@property (Tq,R,N,V_inviteStatus) inviteStatus;
@property (T@"KCSharingParticipant",R,W,N,V_invitedBy) invitedBy;
@property (T@"NSData",R,N,V_sharingInvitationData) sharingInvitationData;
```

## Class methods

```
+[KCSharingParticipant supportsSecureCoding];
```

## Instance methods

```
-[KCSharingParticipant JSONObject];
-[KCSharingParticipant isOwner];
-[KCSharingParticipant participantID];
-[KCSharingParticipant handle];
-[KCSharingParticipant isCurrentUser];
-[KCSharingParticipant encodeWithCoder:];
-[KCSharingParticipant hash];
-[KCSharingParticipant description];
-[KCSharingParticipant initWithCoder:];
-[KCSharingParticipant copyWithZone:];
-[KCSharingParticipant isEqual:];
-[KCSharingParticipant longDescription];
-[KCSharingParticipant permissionLevel];
-[KCSharingParticipant initWithHandle:permissionLevel:];
-[KCSharingParticipant _setInvitedBy:];
-[KCSharingParticipant initWithParticipantID:handle:permissionLevel:isCurrentUser:inviteStatus:sharingInvitationData:];
-[KCSharingParticipant inviteStatus];
-[KCSharingParticipant invitedBy];
-[KCSharingParticipant setPermissionLevel:];
-[KCSharingParticipant sharingInvitationData];
```
