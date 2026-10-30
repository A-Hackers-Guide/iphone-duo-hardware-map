# `CBFrameInfoProvider`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"<FrameInfoProvider>" _frameInfoProvider;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _observers;
```

## Instance methods

```
-[CBFrameInfoProvider dealloc];
-[CBFrameInfoProvider unregisterObserver:];
-[CBFrameInfoProvider initWithFrameInfoProvider:];
-[CBFrameInfoProvider initWithFrameInfoProvider:andQueue:];
-[CBFrameInfoProvider registerObserver:withCallback:];
```
