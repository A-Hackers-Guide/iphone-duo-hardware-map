# `CAMPrimaryConstituentDeviceSwitchingBehaviorCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
q __behavior;
Q __restrictedSwitchingConditions;
```

## Properties

```
@property (Tq,R,N,V__behavior) _behavior;
@property (TQ,R,N,V__restrictedSwitchingConditions) _restrictedSwitchingConditions;
```

## Class methods

```
+[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand _avCaptureBehaviorForBehavior:];
+[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand _avCaptureRestrictionsConditionsForConditions:];
```

## Instance methods

```
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand initWithBehavior:];
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand executeWithContext:];
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand copyWithZone:];
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand _behavior];
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand _restrictedSwitchingConditions];
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand initWithBehavior:restrictedSwitchingConditions:];
-[CAMPrimaryConstituentDeviceSwitchingBehaviorCommand initWithSubcommands:];
```
