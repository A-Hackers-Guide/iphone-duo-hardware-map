# `LACDTOLocationProviderCRAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOLocationProvider`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"RTRoutineManager" _manager;
@"LACDTOLocationState" _locationState;
@"<LACDTOTelemetryReporting>" _telemetry;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOLocationProviderCRAdapter description];
-[LACDTOLocationProviderCRAdapter _checkIsInFamiliarLocationWithCompletion:];
-[LACDTOLocationProviderCRAdapter _locationStateRawValueFromLocationEnum:];
-[LACDTOLocationProviderCRAdapter checkIsInFamiliarLocationWithCompletion:];
-[LACDTOLocationProviderCRAdapter initWithTelemetry:];
```
