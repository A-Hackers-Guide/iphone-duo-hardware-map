# `SBBiometricMonitorPearlDataSource`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKDevicePearlDelegate`, `SBUIBiometricResourceObserver`, `SBBiometricMonitorDataSource`
- 5 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"BKDevicePearl" _pearlDevice;
@"NSHashTable" _observers;
B _matching;
B _faceDetecting;
B _poseIsMarginal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) presenceDetectRunning;
@property (TB,R,N) matchRunning;
@property (TB,R,N) poseIsMarginal;
```

## Instance methods

```
-[SBBiometricMonitorPearlDataSource removeObserver:];
-[SBBiometricMonitorPearlDataSource init];
-[SBBiometricMonitorPearlDataSource dealloc];
-[SBBiometricMonitorPearlDataSource addObserver:];
-[SBBiometricMonitorPearlDataSource device:pearlEventOccurred:];
-[SBBiometricMonitorPearlDataSource device:pearlStateChanged:];
-[SBBiometricMonitorPearlDataSource biometricResource:observeEvent:];
-[SBBiometricMonitorPearlDataSource _forEachObserver:];
-[SBBiometricMonitorPearlDataSource _updateMatching];
-[SBBiometricMonitorPearlDataSource _setFaceDetecting:];
-[SBBiometricMonitorPearlDataSource _setMatching:];
-[SBBiometricMonitorPearlDataSource _setPoseIsMarginal:];
-[SBBiometricMonitorPearlDataSource _updateFaceDetecting];
-[SBBiometricMonitorPearlDataSource initWithPearlDevice:];
-[SBBiometricMonitorPearlDataSource matchRunning];
-[SBBiometricMonitorPearlDataSource poseIsMarginal];
-[SBBiometricMonitorPearlDataSource presenceDetectRunning];
```
