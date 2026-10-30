# `SBAmbientMotionDetectionWakeAttributeMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _observers;
B _shouldEnableMotionDetectionWake;
```

## Properties

```
@property (TB,N,S_setShouldEnableMotionDetectionWake:,V_shouldEnableMotionDetectionWake) shouldEnableMotionDetectionWake;
```

## Class methods

```
+[SBAmbientMotionDetectionWakeAttributeMonitor sharedInstance];
```

## Instance methods

```
-[SBAmbientMotionDetectionWakeAttributeMonitor removeObserver:];
-[SBAmbientMotionDetectionWakeAttributeMonitor init];
-[SBAmbientMotionDetectionWakeAttributeMonitor addObserver:];
-[SBAmbientMotionDetectionWakeAttributeMonitor shouldEnableMotionDetectionWake];
-[SBAmbientMotionDetectionWakeAttributeMonitor _setShouldEnableMotionDetectionWake:];
```
