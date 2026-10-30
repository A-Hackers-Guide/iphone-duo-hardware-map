# `SBRecalibrateProximitySensorHardwareButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SBProximitySensorCoordinatorObserver`, `SBHardwareButtonInteraction`
- 2 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _didResetProxCalibration;
@"SBProximitySensorCoordinator" _sensorCoordinator;
```

## Properties

```
@property (T@"SBProximitySensorCoordinator",&,N,V_sensorCoordinator) sensorCoordinator;
@property (TB,N,V_didResetProxCalibration) didResetProxCalibration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRecalibrateProximitySensorHardwareButtonInteraction consumeInitialPressDown];
-[SBRecalibrateProximitySensorHardwareButtonInteraction disallowsLongPressForReason:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction disallowsTriplePressForReason:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction hardwareButtonGestureParameters];
-[SBRecalibrateProximitySensorHardwareButtonInteraction initWithProximitySensorCoordinator:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction disallowsDoublePressForReason:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction disallowsSinglePressForReason:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction descriptionBuilderWithMultilinePrefix:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction _disallowsAnyPressForReason:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction consumeSinglePressUp];
-[SBRecalibrateProximitySensorHardwareButtonInteraction didResetProxCalibration];
-[SBRecalibrateProximitySensorHardwareButtonInteraction sensorCoordinator];
-[SBRecalibrateProximitySensorHardwareButtonInteraction setDidResetProxCalibration:];
-[SBRecalibrateProximitySensorHardwareButtonInteraction setSensorCoordinator:];
```
