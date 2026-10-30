# `_UIDictationTelephonyMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CXCallObserverDelegate`
- 4 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"CXCallObserver" _callObserver;
B _telephonyActivity;
@? _activityChanged;
```

## Properties

```
@property (TB,R,N,V_telephonyActivity) telephonyActivity;
@property (T@?,C,V_activityChanged) activityChanged;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDictationTelephonyMonitor _backgroundInit];
-[_UIDictationTelephonyMonitor _backgroundReset];
-[_UIDictationTelephonyMonitor telephonyActivity];
-[_UIDictationTelephonyMonitor init];
-[_UIDictationTelephonyMonitor activityChanged];
-[_UIDictationTelephonyMonitor start];
-[_UIDictationTelephonyMonitor callObserver:callChanged:];
-[_UIDictationTelephonyMonitor setActivityChanged:];
```
