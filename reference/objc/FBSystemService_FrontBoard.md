# `FBSystemService`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `FBSOpenApplicationServiceServerInterface`
- 9 instance variables, 8 properties, 37 instance methods, 3 class methods

## Instance variables

```
@"BSServiceDispatchQueue" _queue;
@"BSServiceConnectionListener" _legacyOpenServiceListener;
i _pendingExit;
@"<FBSApplicationInfoProvider>" _lock_defaultInfoProvider;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _defaultInfoProviderLock;
^{_AKSEvent=} _aksEvent;
d _BTLPMTimeout;
@"NSObject<OS_dispatch_group>" _BTLPMTimeoutFetchGroup;
@"<FBSystemServiceDelegate>" _delegate;
```

## Properties

```
@property (T@"<FBSApplicationInfoProvider>",R,N) _applicationInfoProvider;
@property (T@"BSServiceDispatchQueue",R,N,V_queue) queue;
@property (TB,R,GisPendingExit) pendingExit;
@property (T@"<FBSystemServiceDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSystemService sharedInstance];
+[FBSystemService sharedInstanceIfExists];
+[FBSystemService currentOpenApplicationInstance];
```

## Instance methods

```
-[FBSystemService terminateApplication:forReason:andReport:withDescription:completion:];
-[FBSystemService initWithQueue:];
-[FBSystemService listener:didReceiveConnection:withContext:];
-[FBSystemService init];
-[FBSystemService dealloc];
-[FBSystemService queue];
-[FBSystemService shutdownWithOptions:];
-[FBSystemService setDelegate:];
-[FBSystemService delegate];
-[FBSystemService terminateApplicationGroup:forReason:andReport:withDescription:completion:];
-[FBSystemService canOpenApplication:completion:];
-[FBSystemService openApplication:withOptions:originator:requestID:completion:];
-[FBSystemService setPendingExit:];
-[FBSystemService _activateBundleID:requestID:isTrusted:options:serviceInstance:source:originalSourceToken:withResult:];
-[FBSystemService _applicationInfoProvider];
-[FBSystemService _beginFetchBTLPMTimeout];
-[FBSystemService _bluetoothLPMTimeoutWithFetchTimeout:];
-[FBSystemService _isAllowListedLaunchSuspendedApp:];
-[FBSystemService _isTrustedRequest:forCaller:fromClient:forBundleInfo:withOptions:fatalError:];
-[FBSystemService _mapShutdownOptionsToOptions:];
-[FBSystemService _performExitTasksForRelaunch:];
-[FBSystemService _reallyActivateApplication:requestID:options:serviceInstance:source:originalSourceToken:isTrusted:sequenceNumber:cacheGUID:ourSequenceNumber:ourCacheGUID:withResult:];
-[FBSystemService _setInfoProvider];
-[FBSystemService _shouldPendRequestForClientSequenceNumber:clientCacheGUID:ourSequenceNumber:ourCacheGUID:];
-[FBSystemService _terminateProcesses:forReason:andReport:withDescription:completion:];
-[FBSystemService exitAndRelaunch:];
-[FBSystemService exitAndRelaunch:withOptions:];
-[FBSystemService handleActions:source:withResult:];
-[FBSystemService isPasscodeLockedOrBlockedWithResult:];
-[FBSystemService isPendingExit];
-[FBSystemService prepareDisplaysForExit];
-[FBSystemService prepareForExitAndRelaunch:];
-[FBSystemService setSystemIdleSleepDisabled:forReason:];
-[FBSystemService shutdownAndReboot:];
-[FBSystemService shutdownUsingOptions:];
-[FBSystemService shutdownWithOptions:forSource:];
-[FBSystemService shutdownWithOptions:origin:];
```
