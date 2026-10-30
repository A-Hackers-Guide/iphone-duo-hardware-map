# `SBSystemAperturePulseSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
d _expandScale;
d _expandDuration;
d _expandDelay;
@"SBFFluidBehaviorSettings" _expandBehaviorSettings;
@"SBFFluidBehaviorSettings" _contractBehaviorSettings;
```

## Properties

```
@property (Td,N,V_expandScale) expandScale;
@property (Td,N,V_expandDuration) expandDuration;
@property (Td,N,V_expandDelay) expandDelay;
@property (T@"SBFFluidBehaviorSettings",&,N,V_expandBehaviorSettings) expandBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_contractBehaviorSettings) contractBehaviorSettings;
```

## Class methods

```
+[SBSystemAperturePulseSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemAperturePulseSettings setDefaultValues];
-[SBSystemAperturePulseSettings setExpandDelay:];
-[SBSystemAperturePulseSettings setExpandScale:];
-[SBSystemAperturePulseSettings contractBehaviorSettings];
-[SBSystemAperturePulseSettings expandBehaviorSettings];
-[SBSystemAperturePulseSettings expandDelay];
-[SBSystemAperturePulseSettings expandDuration];
-[SBSystemAperturePulseSettings expandScale];
-[SBSystemAperturePulseSettings setContractBehaviorSettings:];
-[SBSystemAperturePulseSettings setExpandBehaviorSettings:];
-[SBSystemAperturePulseSettings setExpandDuration:];
```
