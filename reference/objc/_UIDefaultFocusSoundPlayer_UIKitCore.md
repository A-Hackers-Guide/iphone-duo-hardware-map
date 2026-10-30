# `_UIDefaultFocusSoundPlayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusSoundPlayer`
- 4 instance variables, 8 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _urlPools;
@"NSMutableDictionary" _focusSoundPools;
@"NSObject<OS_dispatch_queue>" _soundQueue;
@"NSTimer" _unregisterTimer;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_urlPools) urlPools;
@property (T@"NSMutableDictionary",&,N,V_focusSoundPools) focusSoundPools;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_soundQueue) soundQueue;
@property (T@"NSTimer",&,N,V_unregisterTimer) unregisterTimer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIDefaultFocusSoundPlayer sharedInstance];
```

## Instance methods

```
-[_UIDefaultFocusSoundPlayer dealloc];
-[_UIDefaultFocusSoundPlayer _init];
-[_UIDefaultFocusSoundPlayer focusSoundPools];
-[_UIDefaultFocusSoundPlayer unregisterTimer];
-[_UIDefaultFocusSoundPlayer _playSoundFromPool:withVolume:pan:];
-[_UIDefaultFocusSoundPlayer _registerForSystemSoundsIfNecessary];
-[_UIDefaultFocusSoundPlayer playSoundWithFocusSound:volume:pan:];
-[_UIDefaultFocusSoundPlayer playSoundWithURL:volume:pan:];
-[_UIDefaultFocusSoundPlayer setFocusSoundPools:];
-[_UIDefaultFocusSoundPlayer setSoundQueue:];
-[_UIDefaultFocusSoundPlayer setUnregisterTimer:];
-[_UIDefaultFocusSoundPlayer setUrlPools:];
-[_UIDefaultFocusSoundPlayer soundQueue];
-[_UIDefaultFocusSoundPlayer urlPools];
```
