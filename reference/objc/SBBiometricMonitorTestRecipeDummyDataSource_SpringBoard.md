# `SBBiometricMonitorTestRecipeDummyDataSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBiometricMonitorDataSource`
- 3 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _observers;
q _state;
B _poseIsMarginal;
```

## Properties

```
@property (TB,R,N) presenceDetectRunning;
@property (TB,R,N) matchRunning;
@property (TB,R,N,V_poseIsMarginal) poseIsMarginal;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBiometricMonitorTestRecipeDummyDataSource removeObserver:];
-[SBBiometricMonitorTestRecipeDummyDataSource addObserver:];
-[SBBiometricMonitorTestRecipeDummyDataSource cycleState];
-[SBBiometricMonitorTestRecipeDummyDataSource matchRunning];
-[SBBiometricMonitorTestRecipeDummyDataSource poseIsMarginal];
-[SBBiometricMonitorTestRecipeDummyDataSource presenceDetectRunning];
```
