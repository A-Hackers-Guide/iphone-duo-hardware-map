# `_UIDisplayObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayObserving`
- 1 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _pendingCarDisplays;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_pendingCarDisplays) pendingCarDisplays;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDisplayObserver sharedObserver];
```

## Instance methods

```
-[_UIDisplayObserver displayMonitor:didUpdateIdentity:withConfiguration:];
-[_UIDisplayObserver displayMonitor:willDisconnectIdentity:];
-[_UIDisplayObserver displayMonitor:didConnectIdentity:withConfiguration:];
-[_UIDisplayObserver connectDisplayWithConfiguration:];
-[_UIDisplayObserver pendingCarDisplays];
-[_UIDisplayObserver setPendingCarDisplays:];
```
