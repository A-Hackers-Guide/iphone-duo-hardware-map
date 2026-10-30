# `FigCameraUsageListener`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MCProfileConnectionObserver`
- 3 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
B _isProhibited;
^{OpaqueFigSimpleMutex=} _isProhibitedLock;
@? _changeHandler;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCameraUsageListener initialize];
```

## Instance methods

```
-[FigCameraUsageListener profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[FigCameraUsageListener dealloc];
-[FigCameraUsageListener initWithChangeHandler:];
```
