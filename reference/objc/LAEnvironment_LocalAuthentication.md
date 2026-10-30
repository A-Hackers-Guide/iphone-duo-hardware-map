# `LAEnvironment`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"LAEnvironmentState" _state;
@"NSHashTable" _observers;
@"LAEnvironmentServiceXPCClient" _xpcClient;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@"NSObject<OS_dispatch_queue>" _observerQueue;
i _notifyToken;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
```

## Properties

```
@property (T@"LAEnvironmentState",R,N) state;
```

## Class methods

```
+[LAEnvironment currentUser];
```

## Instance methods

```
-[LAEnvironment _updateState];
-[LAEnvironment removeObserver:];
-[LAEnvironment init];
-[LAEnvironment dealloc];
-[LAEnvironment addObserver:];
-[LAEnvironment state];
-[LAEnvironment _handleDarwinNotification];
-[LAEnvironment _notifyObserversAboutUpdateFrom:];
-[LAEnvironment _registerDarwinNotification];
-[LAEnvironment _unregisterDarwinNotification];
-[LAEnvironment _updateStateWithSynchronousProxyToEnvironmentService:];
-[LAEnvironment waitForStateUpdate];
```
