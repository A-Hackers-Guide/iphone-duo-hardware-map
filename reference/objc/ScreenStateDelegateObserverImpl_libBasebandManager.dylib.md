# `ScreenStateDelegateObserverImpl`

- Image: [`/usr/lib/libBasebandManager.dylib`](../userland/usr__lib__libBasebandManager.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightStateObserving`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
{function<void (bool)>="__f_"{__value_func<void (bool)>="__buf_"(type="__data"[24C])"__f_"^v}} fCallback;
B fLastScreenOn;
B fHasReportedState;
^{dispatch_queue_s=} fQueue;
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
-[ScreenStateDelegateObserverImpl stop];
-[ScreenStateDelegateObserverImpl dealloc];
-[ScreenStateDelegateObserverImpl start];
-[ScreenStateDelegateObserverImpl backlight:didCompleteUpdateToState:forEvent:];
-[ScreenStateDelegateObserverImpl registerHandler:];
-[ScreenStateDelegateObserverImpl init:];
-[ScreenStateDelegateObserverImpl handleScreenState:];
```
