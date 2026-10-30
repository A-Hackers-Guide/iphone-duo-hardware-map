# `KCSharingMessagingdConnection`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `KCSharingMessagingdXPCServerProtocol`
- 1 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[KCSharingMessagingdConnection sharedInstance];
```

## Instance methods

```
-[KCSharingMessagingdConnection init];
-[KCSharingMessagingdConnection dealloc];
-[KCSharingMessagingdConnection connection];
-[KCSharingMessagingdConnection setConnection:];
-[KCSharingMessagingdConnection cancelPendingInvitesForGroup:participantHandles:completion:];
-[KCSharingMessagingdConnection connectionWasInterrupted];
-[KCSharingMessagingdConnection connectionWasInvalidated];
-[KCSharingMessagingdConnection didAcceptInviteForGroupID:completion:];
-[KCSharingMessagingdConnection didDeclineInviteForGroupID:completion:];
-[KCSharingMessagingdConnection fetchReceivedInviteWithGroupID:completion:];
-[KCSharingMessagingdConnection fetchReceivedInvitesWithCompletion:];
-[KCSharingMessagingdConnection initWithConnection:interface:queue:];
-[KCSharingMessagingdConnection sendNewInvitesForGroup:completion:];
```
