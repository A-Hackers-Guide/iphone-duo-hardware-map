# `CBABRamp`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"CBDisplayModule" _displayModule;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _fadeTimer;
@"NSObject<OS_os_log>" _logHandle;
f _maxLinearBrightness;
f _minLinearBrightness;
```

## Instance methods

```
-[CBABRamp dealloc];
-[CBABRamp getVersion];
-[CBABRamp initWithDisplayModule:andQueue:];
-[CBABRamp setPerceptualBrightnessWithFade:length:current:];
-[CBABRamp stopTransition];
-[CBABRamp transitionToBrightness:force:periodOverride:period:];
```
