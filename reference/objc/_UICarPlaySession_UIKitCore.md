# `_UICarPlaySession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CARSessionObserving`
- 4 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"CARSessionStatus" _carSessionStatus;
B _sessionInitialized;
@"NSMutableArray" _pendingSessionAccessRequests;
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
-[_UICarPlaySession sessionDidDisconnect:];
-[_UICarPlaySession sessionDidConnect:];
```
