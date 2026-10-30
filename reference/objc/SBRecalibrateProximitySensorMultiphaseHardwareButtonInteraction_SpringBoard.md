# `SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SBProximitySensorCoordinatorObserver`, `SBHardwareButtonInteraction`
- 3 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
q _phase;
@"SBProximitySensorCoordinator" _sensorCoordinator;
@"BSAbsoluteMachTimer" _timer;
```

## Properties

```
@property (Tq,N,V_phase) phase;
@property (T@"SBProximitySensorCoordinator",&,N,V_sensorCoordinator) sensorCoordinator;
@property (T@"BSAbsoluteMachTimer",&,N,V_timer) timer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction consumeInitialPressDown];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction disallowsLongPressForReason:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction disallowsTriplePressForReason:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction setTimer:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction phase];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction timer];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction dealloc];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction hardwareButtonGestureParameters];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction initWithProximitySensorCoordinator:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction setPhase:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction disallowsDoublePressForReason:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction disallowsSinglePressForReason:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction descriptionBuilderWithMultilinePrefix:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction _timerDidFire];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction _disallowsAnyPressForReason:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction _transitionToPhase:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction _transitionToPhase:timeout:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction consumeSinglePressUp];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction proximitySensorCoordinator:objectWithinProximityDidChange:];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction sensorCoordinator];
-[SBRecalibrateProximitySensorMultiphaseHardwareButtonInteraction setSensorCoordinator:];
```
