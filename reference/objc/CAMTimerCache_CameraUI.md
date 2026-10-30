# `CAMTimerCache`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<CAMTimerCacheDelegate>" _delegate;
@"NSMutableDictionary" __timersByType;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__timersByType) _timersByType;
@property (T@"<CAMTimerCacheDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CAMTimerCache init];
-[CAMTimerCache setDelegate:];
-[CAMTimerCache delegate];
-[CAMTimerCache cancelAllTimers];
-[CAMTimerCache _handleTimer:forKey:];
-[CAMTimerCache _timersByType];
-[CAMTimerCache cancelTimerForKey:];
-[CAMTimerCache isRunningTimerForKey:];
-[CAMTimerCache startTimerForKey:duration:];
```
