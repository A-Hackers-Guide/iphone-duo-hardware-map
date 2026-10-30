# `UISApplicationSupportService`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `UISApplicationSupportXPCServerInterface`
- 9 instance variables, 7 properties, 17 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSServiceConnectionListener" _listener;
@"BSServiceQueue" _targetQueue;
@"<UISApplicationSupportServiceDelegate>" _lock_delegate;
@"UISApplicationInitializationContext" _lock_defaultContext;
@"NSMutableArray" _lock_launchPendedRequests;
B _lock_started;
B _lock_finishedLaunching;
{?="defaultContext"b1"overrideInitialize"b1"initializeClientSync"b1"initializeClientSyncWithParameters"b1"initializeClientAsync"b1"initializeClientLegacy"b1"requestPasscodeUnlockUI"b1"destroyScenes"b1} _lock_delegateFlags;
```

## Properties

```
@property (TB,R) hasFinishedLaunching;
@property (T@"UISApplicationInitializationContext",C,V_lock_defaultContext) defaultContext;
@property (T@"<UISApplicationSupportServiceDelegate>",&,V_lock_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISApplicationSupportService sharedInstance];
```

## Instance methods

```
-[UISApplicationSupportService _setDelegate:];
-[UISApplicationSupportService defaultContext];
-[UISApplicationSupportService listener:didReceiveConnection:withContext:];
-[UISApplicationSupportService init];
-[UISApplicationSupportService dealloc];
-[UISApplicationSupportService start];
-[UISApplicationSupportService _delegate];
-[UISApplicationSupportService setDelegate:];
-[UISApplicationSupportService delegate];
-[UISApplicationSupportService requestPasscodeUnlockUIWithCompletion:];
-[UISApplicationSupportService initWithCalloutQueue:];
-[UISApplicationSupportService _initWithDelegate:targetQueue:];
-[UISApplicationSupportService _pendRequestUntilLaunch:];
-[UISApplicationSupportService destroyScenesPersistentIdentifiers:animationType:destroySessions:completion:];
-[UISApplicationSupportService hasFinishedLaunching];
-[UISApplicationSupportService initializeClientWithParameters:completion:];
-[UISApplicationSupportService setDefaultContext:];
```
