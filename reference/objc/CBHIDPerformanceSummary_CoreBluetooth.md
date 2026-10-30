# `CBHIDPerformanceSummary`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 17 properties, 34 instance methods, 0 class methods

## Instance variables

```
c _rssi;
B _finalSummary;
@"CBDevice" _device;
@"NSError" _error;
d _errorRate;
d _intervalSecondsExpected;
d _intervalSecondsMax;
d _P50;
d _P50Max;
d _P75;
d _P75Max;
d _P90;
d _P90Max;
d _P95;
d _P95Max;
d _P99;
d _P99Max;
```

## Properties

```
@property (T@"CBDevice",&,N,V_device) device;
@property (T@"NSError",C,N,V_error) error;
@property (Td,N,V_errorRate) errorRate;
@property (Td,N,V_intervalSecondsExpected) intervalSecondsExpected;
@property (Td,N,V_intervalSecondsMax) intervalSecondsMax;
@property (Td,N,V_P50) P50;
@property (Td,N,V_P50Max) P50Max;
@property (Td,N,V_P75) P75;
@property (Td,N,V_P75Max) P75Max;
@property (Td,N,V_P90) P90;
@property (Td,N,V_P90Max) P90Max;
@property (Td,N,V_P95) P95;
@property (Td,N,V_P95Max) P95Max;
@property (Td,N,V_P99) P99;
@property (Td,N,V_P99Max) P99Max;
@property (Tc,N,V_rssi) rssi;
@property (TB,N,V_finalSummary) finalSummary;
```

## Instance methods

```
-[CBHIDPerformanceSummary rssi];
-[CBHIDPerformanceSummary setError:];
-[CBHIDPerformanceSummary setDevice:];
-[CBHIDPerformanceSummary device];
-[CBHIDPerformanceSummary setRssi:];
-[CBHIDPerformanceSummary error];
-[CBHIDPerformanceSummary setP75:];
-[CBHIDPerformanceSummary setP99:];
-[CBHIDPerformanceSummary setP50:];
-[CBHIDPerformanceSummary setP90:];
-[CBHIDPerformanceSummary setP95:];
-[CBHIDPerformanceSummary P75];
-[CBHIDPerformanceSummary P95];
-[CBHIDPerformanceSummary P75Max];
-[CBHIDPerformanceSummary P95Max];
-[CBHIDPerformanceSummary P50];
-[CBHIDPerformanceSummary P90];
-[CBHIDPerformanceSummary P99];
-[CBHIDPerformanceSummary P50Max];
-[CBHIDPerformanceSummary P90Max];
-[CBHIDPerformanceSummary P99Max];
-[CBHIDPerformanceSummary errorRate];
-[CBHIDPerformanceSummary finalSummary];
-[CBHIDPerformanceSummary intervalSecondsExpected];
-[CBHIDPerformanceSummary intervalSecondsMax];
-[CBHIDPerformanceSummary setErrorRate:];
-[CBHIDPerformanceSummary setFinalSummary:];
-[CBHIDPerformanceSummary setIntervalSecondsExpected:];
-[CBHIDPerformanceSummary setIntervalSecondsMax:];
-[CBHIDPerformanceSummary setP50Max:];
-[CBHIDPerformanceSummary setP75Max:];
-[CBHIDPerformanceSummary setP90Max:];
-[CBHIDPerformanceSummary setP95Max:];
-[CBHIDPerformanceSummary setP99Max:];
```
