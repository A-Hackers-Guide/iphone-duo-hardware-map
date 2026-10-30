# `KCSharingGroupManager`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `KCSharingXPCClientProtocol`
- 2 instance variables, 6 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"KCSharingDaemonConnection" _daemonConnection;
@"NSString" _cachedCurrentUserIdentifier;
```

## Properties

```
@property (T@"KCSharingDaemonConnection",&,N,V_daemonConnection) daemonConnection;
@property (T@"NSString",&,V_cachedCurrentUserIdentifier) cachedCurrentUserIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[KCSharingGroupManager sharedInstance];
```

## Instance methods

```
-[KCSharingGroupManager setDaemonConnection:];
-[KCSharingGroupManager updateGroupWithRequest:completion:];
-[KCSharingGroupManager daemonConnection];
-[KCSharingGroupManager removeSubscriber:];
-[KCSharingGroupManager setCachedCurrentUserIdentifier:];
-[KCSharingGroupManager acceptInviteForGroupID:completion:];
-[KCSharingGroupManager accountChanged];
-[KCSharingGroupManager addSubscriber:];
-[KCSharingGroupManager cachedCurrentUserIdentifier];
-[KCSharingGroupManager checkAvailabilityForHandle:completion:];
-[KCSharingGroupManager checkAvailabilityForHandles:completion:];
-[KCSharingGroupManager createGroupWithRequest:completion:];
-[KCSharingGroupManager declineInviteForGroupID:completion:];
-[KCSharingGroupManager deleteGroupWithRequest:completion:];
-[KCSharingGroupManager fetchCurrentUserIdentifierWithReply:];
-[KCSharingGroupManager getGroupByGroupID:completion:];
-[KCSharingGroupManager getGroupsWithRequest:completion:];
-[KCSharingGroupManager initWithDaemonConnection:];
-[KCSharingGroupManager leaveGroupWithRequest:completion:];
-[KCSharingGroupManager performMaintenanceWithCompletion:];
-[KCSharingGroupManager provisionWithReply:];
-[KCSharingGroupManager resyncWithCompletion:];
-[KCSharingGroupManager verifyGroupsInSyncAndResyncMissingGroupsWithCompletion:];
-[KCSharingGroupManager verifyGroupsInSyncWithCompletion:];
```
