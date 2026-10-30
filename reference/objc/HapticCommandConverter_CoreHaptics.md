# `HapticCommandConverter`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"HapticServerConfig" _serverConfig;
```

## Properties

```
@property (T@"HapticServerConfig",R,V_serverConfig) serverConfig;
```

## Instance methods

```
-[HapticCommandConverter transientHapticEventTypeFromSharpness:];
-[HapticCommandConverter eventForLegacyTransientHapticAtTime:params:duration:];
-[HapticCommandConverter limitEventParameter:value:parameter:eventType:];
-[HapticCommandConverter serverConfig];
-[HapticCommandConverter eventForParameterCurveEntry:];
-[HapticCommandConverter transientHapticEventTypeForDefaultSharpness];
-[HapticCommandConverter eventForDynamicParameterEntry:];
-[HapticCommandConverter limitDynamicParameter:value:parameter:];
-[HapticCommandConverter eventForAudioEventType:time:eventParams:duration:];
-[HapticCommandConverter eventForTransientHapticAtTime:params:duration:];
-[HapticCommandConverter eventTypeForBuiltInAudioEventType:];
-[HapticCommandConverter eventForEventEntry:engine:privileged:];
-[HapticCommandConverter initWithServerConfig:];
-[HapticCommandConverter continuousHapticEventTypeForDefaultSharpness:];
-[HapticCommandConverter continuousHapticEventTypeFromSharpness:sustained:];
-[HapticCommandConverter CHtoAVParameterCurve:];
-[HapticCommandConverter defaultEventParameterValueForParameter:eventType:];
-[HapticCommandConverter eventForSPIEventType:time:eventParams:duration:];
-[HapticCommandConverter eventForContinuousHapticEventType:time:params:duration:];
```
