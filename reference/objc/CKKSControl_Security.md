# `CKKSControl`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 34 instance methods, 2 class methods

## Instance variables

```
B _synchronous;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (TB,V_synchronous) synchronous;
@property (T@"NSXPCConnection",&,V_connection) connection;
```

## Class methods

```
+[CKKSControl CKKSControlObject:error:];
+[CKKSControl controlObject:];
```

## Instance methods

```
-[CKKSControl setSynchronous:];
-[CKKSControl dealloc];
-[CKKSControl initWithConnection:];
-[CKKSControl connection];
-[CKKSControl setConnection:];
-[CKKSControl synchronous];
-[CKKSControl rpcKnownBadStateForViews:reply:];
-[CKKSControl pcsMirrorKeysForServices:reply:];
-[CKKSControl deleteSEView:reply:];
-[CKKSControl fetchSEViewKeyHierarchy:forceFetch:reply:];
-[CKKSControl fetchSEViewKeyHierarchy:reply:];
-[CKKSControl initialSyncStatus:reply:];
-[CKKSControl isOctagonExcluded:];
-[CKKSControl modifyTLKSharesForSEView:adding:deleting:reply:];
-[CKKSControl objectProxyWithErrorHandler:];
-[CKKSControl proposeTLKForSEView:proposedTLK:wrappedOldTLK:tlkShares:reply:];
-[CKKSControl rpcCKMetric:attributes:reply:];
-[CKKSControl rpcFastStatus:reply:];
-[CKKSControl rpcFetchAndProcessChanges:classA:onlyIfNoRecentFetch:reply:];
-[CKKSControl rpcFetchAndProcessChanges:reply:];
-[CKKSControl rpcFetchAndProcessChangesIfNoRecentFetch:reply:];
-[CKKSControl rpcFetchAndProcessClassAChanges:reply:];
-[CKKSControl rpcGetCKDeviceIDWithReply:];
-[CKKSControl rpcKnownBadState:reply:];
-[CKKSControl rpcPerformanceCounters:];
-[CKKSControl rpcPushOutgoingChanges:reply:];
-[CKKSControl rpcResetCloudKit:reason:reply:];
-[CKKSControl rpcResetLocal:reply:];
-[CKKSControl rpcResync:reply:];
-[CKKSControl rpcResyncLocal:reply:];
-[CKKSControl rpcStatus:fast:waitForNonTransientState:reply:];
-[CKKSControl rpcStatus:reply:];
-[CKKSControl rpcTLKMissing:reply:];
-[CKKSControl toggleHavoc:];
```
