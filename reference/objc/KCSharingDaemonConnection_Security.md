# `KCSharingDaemonConnection`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `KCSharingXPCClientProtocol`, `KCSharingXPCServerProtocol`, `KCSharingInvitationNotificationProtocol`
- 3 instance variables, 7 properties, 36 instance methods, 2 class methods

## Instance variables

```
q _type;
@"NSXPCConnection" _connection;
@"NSHashTable" _connectionListeners;
```

## Properties

```
@property (Tq,V_type) type;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"NSHashTable",&,N,V_connectionListeners) connectionListeners;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[KCSharingDaemonConnection sharedInstance];
+[KCSharingDaemonConnection sharedInvitationNotifier];
```

## Instance methods

```
-[KCSharingDaemonConnection initWithType:];
-[KCSharingDaemonConnection dealloc];
-[KCSharingDaemonConnection setType:];
-[KCSharingDaemonConnection type];
-[KCSharingDaemonConnection connection];
-[KCSharingDaemonConnection setConnection:];
-[KCSharingDaemonConnection updateGroupWithRequest:completion:];
-[KCSharingDaemonConnection setChangeTrackingEnabled:reply:];
-[KCSharingDaemonConnection acceptInviteForGroupID:completion:];
-[KCSharingDaemonConnection accountChanged];
-[KCSharingDaemonConnection addConnectionListener:];
-[KCSharingDaemonConnection checkAvailabilityForHandles:completion:];
-[KCSharingDaemonConnection connectionListeners];
-[KCSharingDaemonConnection connectionWasInterrupted];
-[KCSharingDaemonConnection connectionWasInvalidated];
-[KCSharingDaemonConnection createGroupWithRequest:completion:];
-[KCSharingDaemonConnection declineInviteForGroupID:completion:];
-[KCSharingDaemonConnection deleteGroupWithRequest:completion:];
-[KCSharingDaemonConnection fetchCurrentUserIdentifierWithReply:];
-[KCSharingDaemonConnection fetchRemoteChangesWithReply:];
-[KCSharingDaemonConnection getGroupByGroupID:completion:];
-[KCSharingDaemonConnection getGroupsWithRequest:completion:];
-[KCSharingDaemonConnection groupInvitationWasCancelled];
-[KCSharingDaemonConnection groupsUpdated];
-[KCSharingDaemonConnection initWithConnection:queue:type:];
-[KCSharingDaemonConnection leaveGroupWithRequest:completion:];
-[KCSharingDaemonConnection performMaintenanceWithCompletion:];
-[KCSharingDaemonConnection provisionWithReply:];
-[KCSharingDaemonConnection receivedGroupInvitation:];
-[KCSharingDaemonConnection removeConnectionListener:];
-[KCSharingDaemonConnection resyncWithCompletion:];
-[KCSharingDaemonConnection saveLocalChangesWithReply:];
-[KCSharingDaemonConnection setConnectionListeners:];
-[KCSharingDaemonConnection verifyGroupsInSyncAndResyncMissingGroupsWithCompletion:];
-[KCSharingDaemonConnection verifyGroupsInSyncWithCompletion:];
-[KCSharingDaemonConnection wipe:reply:];
```
