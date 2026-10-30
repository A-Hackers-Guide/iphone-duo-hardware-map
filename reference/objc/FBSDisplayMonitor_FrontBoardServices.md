# `FBSDisplayMonitor`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 11 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _callOutQueue;
@"CADisplay" _mainDisplay;
@"FBSDisplaySource" _mainDisplaySource;
@"<FBSDisplayTransformer>" _transformer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<FBSDisplayObserving>" _lock_bookendObserver;
@"NSHashTable" _lock_observers;
@"NSMapTable" _lock_sourcesByDisplay;
@"NSMutableSet" _lock_alwaysConnectedSources;
B _lock_allowsUnknownDisplays;
B _lock_canPostToBookendObserver;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_callOutQueue) callOutQueue;
@property (TB,R,N) canPostToBookendObserver;
@property (T@"<FBSDisplayObserving>",R,W,N) bookendObserver;
@property (T@"NSArray",R,C,N) observers;
@property (T@"<FBSDisplayTransformer>",R,N,V_transformer) transformer;
@property (T@"FBSDisplayIdentity",R,C,N) mainIdentity;
@property (T@"FBSDisplayConfiguration",R,C,N) mainConfiguration;
@property (T@"NSSet",R,C,N) alwaysConnectedIdentities;
@property (T@"NSSet",R,C,N) connectedIdentities;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSDisplayMonitor callOutQueue];
-[FBSDisplayMonitor debugDescription];
-[FBSDisplayMonitor removeObserver:];
-[FBSDisplayMonitor init];
-[FBSDisplayMonitor add:];
-[FBSDisplayMonitor remove:];
-[FBSDisplayMonitor dealloc];
-[FBSDisplayMonitor addObserver:];
-[FBSDisplayMonitor invalidate];
-[FBSDisplayMonitor transformer];
-[FBSDisplayMonitor description];
-[FBSDisplayMonitor observers];
-[FBSDisplayMonitor alwaysConnectedIdentities];
-[FBSDisplayMonitor configurationForIdentity:];
-[FBSDisplayMonitor mainConfiguration];
-[FBSDisplayMonitor setAllowsUnknownDisplays:];
-[FBSDisplayMonitor bookendObserver];
-[FBSDisplayMonitor updateTransformsWithCompletion:];
-[FBSDisplayMonitor _initWithBookendObserver:transformer:];
-[FBSDisplayMonitor _initWithDisplays:mainDisplay:bookendObserver:transformer:];
-[FBSDisplayMonitor _lock_alwaysConnectedConfigurations];
-[FBSDisplayMonitor _lock_enumerateConnectedWithBlock:];
-[FBSDisplayMonitor _lock_enumerateSourcesWithBlock:];
-[FBSDisplayMonitor _postInitialBookendObserverConnections];
-[FBSDisplayMonitor _sortedSources];
-[FBSDisplayMonitor allowsUnknownDisplays];
-[FBSDisplayMonitor canPostToBookendObserver];
-[FBSDisplayMonitor connectedIdentities];
-[FBSDisplayMonitor initWithInitializationCompletion:];
-[FBSDisplayMonitor initWithTransformer:];
-[FBSDisplayMonitor mainIdentity];
```
