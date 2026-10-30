# `_FBSDisplayLayoutService`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `FBSDisplayLayoutMonitorClientInterface`
- 7 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
@"BSServiceDispatchQueue" _callOutQueue;
@"BSServiceConnection" _connection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMapTable" _lock_keyedObservers;
@"FBSDisplayLayout" _lock_layout;
Q _lock_layoutGeneration;
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
-[_FBSDisplayLayoutService updateLayout:withTransition:];
-[_FBSDisplayLayoutService dealloc];
-[_FBSDisplayLayoutService endpoint];
-[_FBSDisplayLayoutService _noteDisconnected];
-[_FBSDisplayLayoutService currentLayout];
-[_FBSDisplayLayoutService _initWithEndpoint:qos:];
-[_FBSDisplayLayoutService invalidate];
-[_FBSDisplayLayoutService addObserver:forKey:];
-[_FBSDisplayLayoutService removeObserverForKey:];
```
