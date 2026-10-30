# `BLSHCATransactionTelemetryContext`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
Q _beginMachTime;
d _elapsedSecondsActive;
Q _stateHandler;
B _shouldGenerateSeed;
B _hasBegun;
B _active;
I _generatedSeed;
Q _transactionID;
Q _elapsedMSActive;
```

## Properties

```
@property (TQ,R,N,V_transactionID) transactionID;
@property (TI,R,N,V_generatedSeed) generatedSeed;
@property (TB,R,N,GisActive,V_active) active;
@property (TQ,R,N,V_elapsedMSActive) elapsedMSActive;
```

## Class methods

```
+[BLSHCATransactionTelemetryContext telemetryContextWithTransactionID:shouldGenerateSeed:];
```

## Instance methods

```
-[BLSHCATransactionTelemetryContext transactionID];
-[BLSHCATransactionTelemetryContext commit];
-[BLSHCATransactionTelemetryContext begin];
-[BLSHCATransactionTelemetryContext dealloc];
-[BLSHCATransactionTelemetryContext description];
-[BLSHCATransactionTelemetryContext isActive];
-[BLSHCATransactionTelemetryContext elapsedMSActive];
-[BLSHCATransactionTelemetryContext elapsedSecondsActive];
-[BLSHCATransactionTelemetryContext generatedSeed];
-[BLSHCATransactionTelemetryContext initWithTransactionID:shouldGenerateSeed:];
```
