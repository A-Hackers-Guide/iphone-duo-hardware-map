# `FBSActiveInterfaceOrientationObserver`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSOrientationObserverClientDelegate`, `BSInvalidatable`
- 5 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"FBSOrientationObserverClient" _client;
@"FBSActiveInterfaceOrientationStateUpdate" _lock_freshestUpdate;
@? _lock_updateHandler;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationState];
```

## Instance methods

```
-[FBSActiveInterfaceOrientationObserver client:handleActiveInterfaceOrientationStateUpdate:];
-[FBSActiveInterfaceOrientationObserver _legacy_updateStateUpdateHandler:];
-[FBSActiveInterfaceOrientationObserver _handleActiveInterfaceOrientationStateUpdate:];
-[FBSActiveInterfaceOrientationObserver _resolveAndStoreFreshestUpdate:forced:];
-[FBSActiveInterfaceOrientationObserver init];
-[FBSActiveInterfaceOrientationObserver dealloc];
-[FBSActiveInterfaceOrientationObserver _activateWithStateUpdateHandler:registerInterest:];
-[FBSActiveInterfaceOrientationObserver activateWithStateUpdateHandler:];
-[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationState];
-[FBSActiveInterfaceOrientationObserver _legacy_activeInterfaceOrientationStateUpdateWithCompletion:];
-[FBSActiveInterfaceOrientationObserver invalidate];
-[FBSActiveInterfaceOrientationObserver _lock_resolveAndStoreFreshestUpdate:forced:];
-[FBSActiveInterfaceOrientationObserver handleActiveInterfaceOrientationStateResetForClient:];
-[FBSActiveInterfaceOrientationObserver _initWithClient:callbackQueue:];
-[FBSActiveInterfaceOrientationObserver activeInterfaceOrientationStateWithCompletion:];
-[FBSActiveInterfaceOrientationObserver _setUpdateHandler:];
```
