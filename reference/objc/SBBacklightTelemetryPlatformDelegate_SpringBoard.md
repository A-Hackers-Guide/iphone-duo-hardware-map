# `SBBacklightTelemetryPlatformDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHTelemetryServicePlatformDelegate`
- 1 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"SBAlwaysOnTelemetryEmitter" _alwaysOnTelemetryEmitter;
```

## Properties

```
@property (T@"SBAlwaysOnTelemetryEmitter",W,N,V_alwaysOnTelemetryEmitter) alwaysOnTelemetryEmitter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBacklightTelemetryPlatformDelegate sharedInstance];
```

## Instance methods

```
-[SBBacklightTelemetryPlatformDelegate alwaysOnTelemetryEmitter];
-[SBBacklightTelemetryPlatformDelegate setAlwaysOnTelemetryEmitter:];
-[SBBacklightTelemetryPlatformDelegate telemetryBLSBacklightEventTelemetryEnabled];
-[SBBacklightTelemetryPlatformDelegate telemetryBLSSystemWakeTelemetryEnabled];
-[SBBacklightTelemetryPlatformDelegate telemetryContextForBacklightEvent:];
-[SBBacklightTelemetryPlatformDelegate telemetryContextForSystemWakeMetrics:];
-[SBBacklightTelemetryPlatformDelegate telemetryEventKeyForSystemWakeMetrics];
-[SBBacklightTelemetryPlatformDelegate telemetryLogSystemWakeMetricsToPowerLog:];
-[SBBacklightTelemetryPlatformDelegate telemetryPowerLogPayloadForBacklightEvent:changeEvent:];
```
