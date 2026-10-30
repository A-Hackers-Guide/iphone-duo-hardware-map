# `FBWorkspaceEventDispatcherSource`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 6 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"RBSProcessHandle" _processHandle;
@? _lock_invalidationBlock;
@"NSSet" _lock_remnants;
@"NSMutableDictionary" _lock_requestsByTargetIdentifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _invalidationLock;
```

## Properties

```
@property (T@"RBSProcessHandle",R,N,V_processHandle) processHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBWorkspaceEventDispatcherSource enqueueSceneRequest:];
-[FBWorkspaceEventDispatcherSource noteHandshakeWithRemnants:];
-[FBWorkspaceEventDispatcherSource init];
-[FBWorkspaceEventDispatcherSource dealloc];
-[FBWorkspaceEventDispatcherSource dequeueSceneRequestsForTargetIdentifier:];
-[FBWorkspaceEventDispatcherSource _initWithProcessHandle:invalidationBlock:];
-[FBWorkspaceEventDispatcherSource invalidate];
-[FBWorkspaceEventDispatcherSource processHandle];
-[FBWorkspaceEventDispatcherSource consumeRemnantsPassingTest:];
```
