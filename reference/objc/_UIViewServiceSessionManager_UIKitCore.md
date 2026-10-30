# `_UIViewServiceSessionManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `BSDescriptionStreaming`
- 7 instance variables, 10 properties, 22 instance methods, 7 class methods

## Instance variables

```
@"NSString" _machName;
@"<BSInvalidatable>" _lock_listener;
@"NSMutableArray" _lock_sessions;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _asPlugIn;
@"NSMutableArray" _lock_queuedAuxiliaryConnections;
@"<_UIViewServiceSessionManagerDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N) isExtensionService;
@property (TB,R,N) requiresExtensionContext;
@property (T@"NSString",R,N) viewControllerClassName;
@property (T@"NSString",R,N) containingViewControllerClassName;
@property (T@"NSString",R,N) mainStoryboardName;
@property (T@"<_UIViewServiceSessionManagerDelegate>",R,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewServiceSessionManager startViewServiceSessionManagerAsPlugin:];
+[_UIViewServiceSessionManager hasActiveSessions];
+[_UIViewServiceSessionManager startViewServiceSessionWithDelegate:];
+[_UIViewServiceSessionManager _ensureSessionManagerWithDelegate:asPlugIn:];
+[_UIViewServiceSessionManager sharedManager];
+[_UIViewServiceSessionManager _domainMachName];
+[_UIViewServiceSessionManager bundleIdentifierForConnection:auditToken:];
```

## Instance methods

```
-[_UIViewServiceSessionManager listener:didReceiveConnection:withContext:];
-[_UIViewServiceSessionManager debugDescription];
-[_UIViewServiceSessionManager viewControllerClassName];
-[_UIViewServiceSessionManager _start];
-[_UIViewServiceSessionManager init];
-[_UIViewServiceSessionManager dealloc];
-[_UIViewServiceSessionManager succinctDescription];
-[_UIViewServiceSessionManager containingViewControllerClassName];
-[_UIViewServiceSessionManager delegate];
-[_UIViewServiceSessionManager description];
-[_UIViewServiceSessionManager appendDescriptionToStream:];
-[_UIViewServiceSessionManager _hasActiveSessions];
-[_UIViewServiceSessionManager _initWithDelegate:asPlugIn:];
-[_UIViewServiceSessionManager _startOrStopSystemsForBackgroundRunning];
-[_UIViewServiceSessionManager configureConnection:withContext:];
-[_UIViewServiceSessionManager configureLegacySessionForConnection:];
-[_UIViewServiceSessionManager didCreateServiceViewController:contextToken:];
-[_UIViewServiceSessionManager firstAuxiliaryConnectionPassingTest:];
-[_UIViewServiceSessionManager isExtensionService];
-[_UIViewServiceSessionManager mainStoryboardName];
-[_UIViewServiceSessionManager queuedConnectionInvalidated:];
-[_UIViewServiceSessionManager requiresExtensionContext];
```
