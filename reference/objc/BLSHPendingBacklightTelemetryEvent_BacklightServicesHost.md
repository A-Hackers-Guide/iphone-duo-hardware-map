# `BLSHPendingBacklightTelemetryEvent`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
q _sourceEvent;
@"NSString" _explanation;
Q _startTimestamp;
q _backlightState;
@"BLSBacklightChangeEvent" _changeEvent;
```

## Properties

```
@property (Tq,R,N,V_sourceEvent) sourceEvent;
@property (T@"NSString",R,N,V_explanation) explanation;
@property (TQ,R,N,V_startTimestamp) startTimestamp;
@property (Tq,R,N,V_backlightState) backlightState;
@property (T@"BLSBacklightChangeEvent",R,N,V_changeEvent) changeEvent;
```

## Instance methods

```
-[BLSHPendingBacklightTelemetryEvent explanation];
-[BLSHPendingBacklightTelemetryEvent startTimestamp];
-[BLSHPendingBacklightTelemetryEvent backlightState];
-[BLSHPendingBacklightTelemetryEvent sourceEvent];
-[BLSHPendingBacklightTelemetryEvent changeEvent];
-[BLSHPendingBacklightTelemetryEvent initWithBacklightState:sourceEvent:explanation:startTimestamp:changeEvent:];
```
