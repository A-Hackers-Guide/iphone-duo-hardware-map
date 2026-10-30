# `_UIViewServiceHostSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSNSXPCConnectionEventObserver`, `BSDescriptionStreaming`
- 13 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _loggingIdentifier;
@"NSString" _appViewServiceBundleIdentifier;
@"_UIRemoteViewService" _service;
@"<_UIViewServiceHostSessionDelegate>" _delegate;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
i _lock_pid;
@"RBSAssertion" _lock_assertion;
@"BSServiceConnectionEndpoint" _lock_endpoint;
@"FBSceneSynchronizer" _lock_synchronizer;
@"NSHashTable" _lock_connections;
B _lock_hasInvalidatedConnections;
@"FBSceneSynchronizer" _sceneSynchronizer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIViewServiceHostSession debugDescription];
-[_UIViewServiceHostSession dealloc];
-[_UIViewServiceHostSession succinctDescription];
-[_UIViewServiceHostSession description];
-[_UIViewServiceHostSession appendDescriptionToStream:];
-[_UIViewServiceHostSession connection:didHaltWithEvent:];
```
