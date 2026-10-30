# `SBBiometricMonitorDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) presenceDetectRunning;
@property (TB,R,N) matchRunning;
@property (TB,R,N) poseIsMarginal;
```

## Instance methods

```
-[SBBiometricMonitorDataSource removeObserver:];
-[SBBiometricMonitorDataSource addObserver:];
-[SBBiometricMonitorDataSource matchRunning];
-[SBBiometricMonitorDataSource poseIsMarginal];
-[SBBiometricMonitorDataSource presenceDetectRunning];
```
