# `FBSWorkspace`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionEndpointMonitorDelegate`, `BSDescriptionProviding`
- 10 instance variables, 9 properties, 37 instance methods, 2 class methods

## Instance variables

```
@"BSServiceDispatchQueue" _queue;
@"BSServiceQueue" _callOutQueue;
@"BSServiceCompoundQueue" _serviceQueue;
@"FBSPseudoSceneUpdater" _psuedoSceneUpdater;
@"<FBSWorkspaceDelegate>" _delegate;
@"NSMutableDictionary" _queue_identifierToScenesSource;
@"BSServiceConnectionEndpointMonitor" _connectionEndpointMonitor;
@"BSServiceConnectionEndpoint" _defaultShellEndpoint;
B _isSingleton;
B _queue_invalidated;
```

## Properties

```
@property (T@"BSServiceDispatchQueue",R,N) machQueue;
@property (T@"BSServiceQueue",R,N) callOutQueue;
@property (T@"<FBSWorkspaceDelegate>",R,N) delegate;
@property (T@"BSServiceConnectionEndpoint",R,N,V_defaultShellEndpoint) defaultShellEndpoint;
@property (T@"NSArray",R,C,N) scenes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSWorkspace startViewServiceDomain];
+[FBSWorkspace _findDomainSpecification];
```

## Instance methods

```
-[FBSWorkspace enumerateScenesWithBlock:];
-[FBSWorkspace initWithSerialQueue:];
-[FBSWorkspace requestSceneCreationWithInitialClientSettings:completion:];
-[FBSWorkspace defaultServiceForEndpoint:];
-[FBSWorkspace _queue_registerSource:];
-[FBSWorkspace callOutQueue];
-[FBSWorkspace debugDescription];
-[FBSWorkspace machQueue];
-[FBSWorkspace succinctDescriptionBuilder];
-[FBSWorkspace init];
-[FBSWorkspace dealloc];
-[FBSWorkspace defaultService];
-[FBSWorkspace monitor:willLoseEndpoint:];
-[FBSWorkspace sceneWithIdentifier:];
-[FBSWorkspace serviceQueue];
-[FBSWorkspace descriptionWithMultilinePrefix:];
-[FBSWorkspace monitor:didReceiveEndpoint:];
-[FBSWorkspace _registerSourcePeer:];
-[FBSWorkspace _callOutQueue];
-[FBSWorkspace _registerSourceEndpoint:];
-[FBSWorkspace succinctDescription];
-[FBSWorkspace requestDestructionOfScene:withCompletion:];
-[FBSWorkspace setDelegate:];
-[FBSWorkspace serviceForEndpoint:withIdentifier:];
-[FBSWorkspace requestSceneCreationWithIdentifier:initialClientSettings:completion:];
-[FBSWorkspace pseudoSceneWithIdentifier:specification:];
-[FBSWorkspace _registerSource:];
-[FBSWorkspace _initWithCoupler:options:];
-[FBSWorkspace _queue_unregisterSource:];
-[FBSWorkspace delegate];
-[FBSWorkspace defaultShellEndpoint];
-[FBSWorkspace description];
-[FBSWorkspace requestSceneFromEndpoint:withOptions:completion:];
-[FBSWorkspace _invalidateWithCompletion:];
-[FBSWorkspace _calloutQueue_executeCalloutFromSource:withBlock:];
-[FBSWorkspace scenes];
-[FBSWorkspace descriptionBuilderWithMultilinePrefix:];
```
