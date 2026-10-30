# `FBSDisplayLayoutMonitor`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 10 instance variables, 5 properties, 14 instance methods, 6 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"_FBSDisplayLayoutServiceAssertion" _lock_handlerAssertion;
B _lock_invalidated;
@"BSServiceConnectionEndpoint" _deprecated_endpoint;
@? _lock_deprecated_handler;
@"NSMapTable" _lock_deprecated_observerAssertions;
c _deprecated_qos;
q _deprecated_displayType;
B _deprecated_singleton;
B _deprecated_mutable;
```

## Properties

```
@property (T@"FBSDisplayLayout",R,N) currentLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSDisplayLayoutMonitor _endpointForDisplayType:];
+[FBSDisplayLayoutMonitor monitorWithConfiguration:];
+[FBSDisplayLayoutMonitor interface];
+[FBSDisplayLayoutMonitor sharedMonitorForDisplayType:];
+[FBSDisplayLayoutMonitor serviceIdentifier];
+[FBSDisplayLayoutMonitor mainDisplayInstanceIdentifier];
```

## Instance methods

```
-[FBSDisplayLayoutMonitor displayType];
-[FBSDisplayLayoutMonitor removeObserver:];
-[FBSDisplayLayoutMonitor init];
-[FBSDisplayLayoutMonitor _initWithConfiguration:singleton:needsDefaultPriority:mutable:displayType:mutableHandler:];
-[FBSDisplayLayoutMonitor dealloc];
-[FBSDisplayLayoutMonitor setHandler:];
-[FBSDisplayLayoutMonitor qualityOfService];
-[FBSDisplayLayoutMonitor currentLayout];
-[FBSDisplayLayoutMonitor initWithDisplayType:];
-[FBSDisplayLayoutMonitor addObserver:];
-[FBSDisplayLayoutMonitor invalidate];
-[FBSDisplayLayoutMonitor handler];
-[FBSDisplayLayoutMonitor initWithDisplayType:handler:];
-[FBSDisplayLayoutMonitor initWithDisplayType:qualityOfService:handler:];
```
