# `MLBackgroundWatchdog`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _timer;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_source>",&,V_timer) timer;
```

## Class methods

```
+[MLBackgroundWatchdog watchdogWithTimeout:label:queue:];
+[MLBackgroundWatchdog watchdogWithTimeout:queue:];
```

## Instance methods

```
-[MLBackgroundWatchdog setTimer:];
-[MLBackgroundWatchdog timer];
-[MLBackgroundWatchdog dealloc];
-[MLBackgroundWatchdog invalidate];
```
