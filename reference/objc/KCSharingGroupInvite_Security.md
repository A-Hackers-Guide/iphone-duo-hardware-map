# `KCSharingGroupInvite`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _groupID;
@"NSURL" _shareURL;
@"NSData" _inviteToken;
@"NSString" _senderHandle;
@"NSString" _inviteeHandle;
@"NSDate" _sentTime;
@"NSString" _displayName;
```

## Properties

```
@property (T@"NSString",R,C,N,V_groupID) groupID;
@property (T@"NSURL",R,C,N,V_shareURL) shareURL;
@property (T@"NSData",R,C,N,V_inviteToken) inviteToken;
@property (T@"NSString",R,C,N,V_senderHandle) senderHandle;
@property (T@"NSString",R,C,N,V_inviteeHandle) inviteeHandle;
@property (T@"NSDate",R,C,N,V_sentTime) sentTime;
@property (T@"NSString",C,N,V_displayName) displayName;
```

## Class methods

```
+[KCSharingGroupInvite supportsSecureCoding];
```

## Instance methods

```
-[KCSharingGroupInvite shareURL];
-[KCSharingGroupInvite groupID];
-[KCSharingGroupInvite displayName];
-[KCSharingGroupInvite setDisplayName:];
-[KCSharingGroupInvite senderHandle];
-[KCSharingGroupInvite encodeWithCoder:];
-[KCSharingGroupInvite initWithCoder:];
-[KCSharingGroupInvite initWithGroupID:shareURL:senderHandle:inviteeHandle:inviteToken:sentTime:displayName:];
-[KCSharingGroupInvite inviteToken];
-[KCSharingGroupInvite inviteeHandle];
-[KCSharingGroupInvite sentTime];
```
