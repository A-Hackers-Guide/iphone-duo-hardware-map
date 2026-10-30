# `SBProximitySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUISettings`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _colorScreenEdgeWhenObjectInProximity;
B _allowTouchesInJindoWhenObjectInProximity;
d _initialBacklightDebounceDuration;
d _subsequentBacklightDebounceDuration;
d _nonTelephonyTouchAllowanceGracePeriodDuration;
```

## Properties

```
@property (Td,N,V_initialBacklightDebounceDuration) initialBacklightDebounceDuration;
@property (Td,N,V_subsequentBacklightDebounceDuration) subsequentBacklightDebounceDuration;
@property (TB,N,V_colorScreenEdgeWhenObjectInProximity) colorScreenEdgeWhenObjectInProximity;
@property (TB,N,V_allowTouchesInJindoWhenObjectInProximity) allowTouchesInJindoWhenObjectInProximity;
@property (Td,N,V_nonTelephonyTouchAllowanceGracePeriodDuration) nonTelephonyTouchAllowanceGracePeriodDuration;
```

## Class methods

```
+[SBProximitySettings settingsControllerModule];
```

## Instance methods

```
-[SBProximitySettings setDefaultValues];
-[SBProximitySettings allowTouchesInJindoWhenObjectInProximity];
-[SBProximitySettings colorScreenEdgeWhenObjectInProximity];
-[SBProximitySettings initialBacklightDebounceDuration];
-[SBProximitySettings nonTelephonyTouchAllowanceGracePeriodDuration];
-[SBProximitySettings setAllowTouchesInJindoWhenObjectInProximity:];
-[SBProximitySettings setColorScreenEdgeWhenObjectInProximity:];
-[SBProximitySettings setInitialBacklightDebounceDuration:];
-[SBProximitySettings setNonTelephonyTouchAllowanceGracePeriodDuration:];
-[SBProximitySettings setSubsequentBacklightDebounceDuration:];
-[SBProximitySettings subsequentBacklightDebounceDuration];
```
