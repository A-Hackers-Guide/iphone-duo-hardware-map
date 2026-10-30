# `FBSDisplayLayoutMonitorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
B _needsUserInteractivePriority;
@? _transitionHandler;
```

## Properties

```
@property (T@"BSServiceConnectionEndpoint",R,C,N,V_endpoint) endpoint;
@property (TB,N,V_needsUserInteractivePriority) needsUserInteractivePriority;
@property (T@?,C,N,V_transitionHandler) transitionHandler;
```

## Class methods

```
+[FBSDisplayLayoutMonitorConfiguration configurationForDefaultMainDisplayMonitor];
+[FBSDisplayLayoutMonitorConfiguration configurationWithEndpoint:];
```

## Instance methods

```
-[FBSDisplayLayoutMonitorConfiguration init];
-[FBSDisplayLayoutMonitorConfiguration setTransitionHandler:];
-[FBSDisplayLayoutMonitorConfiguration endpoint];
-[FBSDisplayLayoutMonitorConfiguration _initWithEndpoint:];
-[FBSDisplayLayoutMonitorConfiguration needsUserInteractivePriority];
-[FBSDisplayLayoutMonitorConfiguration transitionHandler];
-[FBSDisplayLayoutMonitorConfiguration setNeedsUserInteractivePriority:];
```
