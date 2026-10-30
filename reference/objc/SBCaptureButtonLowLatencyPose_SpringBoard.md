# `SBCaptureButtonLowLatencyPose`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 3 instance methods, 0 class methods

## Instance variables

```
d _timeSinceLastStationary;
d _timeSinceLastNonStationary;
```

## Properties

```
@property (Td,R,N,V_timeSinceLastStationary) timeSinceLastStationary;
@property (Td,R,N,V_timeSinceLastNonStationary) timeSinceLastNonStationary;
```

## Instance methods

```
-[SBCaptureButtonLowLatencyPose initWithTimeSinceLastStationary:timeSinceLastNonStationary:];
-[SBCaptureButtonLowLatencyPose timeSinceLastNonStationary];
-[SBCaptureButtonLowLatencyPose timeSinceLastStationary];
```
