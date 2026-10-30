# `_ANEPerformanceStats`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 10 class methods

## Instance variables

```
Q _hwExecutionTime;
@"NSData" _pStatsRawData;
@"NSData" _perfCounterData;
```

## Properties

```
@property (T@"NSData",R,N,V_perfCounterData) perfCounterData;
@property (TQ,R,N,V_hwExecutionTime) hwExecutionTime;
@property (T@"NSData",R,N,V_pStatsRawData) pStatsRawData;
```

## Class methods

```
+[_ANEPerformanceStats new];
+[_ANEPerformanceStats stringForEventType:];
+[_ANEPerformanceStats decodeDescriptor:perTdPerfCounters:];
+[_ANEPerformanceStats decodePerformanceStats:withOptions:];
+[_ANEPerformanceStats decodeRawStatsData:];
+[_ANEPerformanceStats driverMaskForANEFMask:];
+[_ANEPerformanceStats dumpPerformanceStatsRawData:];
+[_ANEPerformanceStats statsWithHardwareExecutionNS:];
+[_ANEPerformanceStats statsWithReconstructed:hardwareExecutionNS:aneStatsRawData:];
+[_ANEPerformanceStats statsWithRequestPerformanceBuffer:statsBufferSize:];
```

## Instance methods

```
-[_ANEPerformanceStats init];
-[_ANEPerformanceStats description];
-[_ANEPerformanceStats hwExecutionTime];
-[_ANEPerformanceStats perfCounterData];
-[_ANEPerformanceStats emitPerfcounterSignpostsWithModelStringID:];
-[_ANEPerformanceStats initWithHardwareExecution:perfCounterData:ANEStatsRawData:];
-[_ANEPerformanceStats initWithReconstructedData:hardwareExecutionNS:];
-[_ANEPerformanceStats initWithRequestPerformanceBuffer:statsBufferSize:];
-[_ANEPerformanceStats pStatsRawData];
-[_ANEPerformanceStats performanceCounters];
-[_ANEPerformanceStats stringForPerfCounter:];
```
