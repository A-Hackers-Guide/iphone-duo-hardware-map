# `CMActivityManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (T@?,C) activityHandler;
@property (TB,R,N,GisActivityAvailable) activityAvailable;
```

## Instance methods

```
-[CMActivityManager init];
-[CMActivityManager dealloc];
-[CMActivityManager setActivityHandler:];
-[CMActivityManager activityHandler];
-[CMActivityManager isActivityAvailable];
-[CMActivityManager overrideOscarSideband:withState:];
-[CMActivityManager simulateMotionState:withState:];
-[CMActivityManager simulateMotionState:withState:withHint:];
-[CMActivityManager simulateMotionStateYouthWithState:];
```
