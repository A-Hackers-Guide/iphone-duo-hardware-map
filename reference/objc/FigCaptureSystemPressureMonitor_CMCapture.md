# `FigCaptureSystemPressureMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@? _systemPressureLevelChangedHandler;
@"NSObject<OS_dispatch_queue>" _systemPressureLevelChangedHandlerQueue;
i _thermalPressureNotificationToken;
[5i] _systemPressureLevelByThermalPressureLevel;
i _currentSystemPressureFromThermalPressure;
B _fineGrainThermalMonitoringEnabled;
i _thermalLevelNotificationToken;
[5i] _systemPressureLevelByThermalLevel;
i _currentSystemPressureFromThermalLevel;
i _peakPowerNotificationToken;
[5i] _systemPressureLevelByPeakPowerLevel;
i _currentSystemPressureFromPeakPower;
i _currentSystemPressureFromSystemStress;
[5{?="min"f"max"f}] _systemPressureLevelByProjectorTemperature;
i _currentSystemPressureFromProjectorTemperature;
@"NSObject<OS_dispatch_source>" _pearlPollTimer;
{?="value"q"timescale"i"flags"I"epoch"q} _pollingTimerStopTime;
@"NSMutableDictionary" _imageSensorTemperatureMonitorByPortType;
```

## Properties

```
@property (T@?,C) systemPressureLevelChangedHandler;
@property (Ti,R) systemPressureLevelFromPearlProjector;
```

## Class methods

```
+[FigCaptureSystemPressureMonitor initialize];
```

## Instance methods

```
-[FigCaptureSystemPressureMonitor dealloc];
-[FigCaptureSystemPressureMonitor callSystemPressureLevelChangedHandler];
-[FigCaptureSystemPressureMonitor initWithPearlModuleType:sensorThermalLevelsByTemperatureByPortType:fineGrainThermalMonitoringEnabled:];
-[FigCaptureSystemPressureMonitor setSystemPressureLevelChangedHandler:];
-[FigCaptureSystemPressureMonitor startMonitoringImageSensorTemperatureUntilNominalWithPortType:];
-[FigCaptureSystemPressureMonitor startMonitoringPearlProjectorTemperatureUntilNominal];
-[FigCaptureSystemPressureMonitor systemPressureLevelChangedHandler];
-[FigCaptureSystemPressureMonitor systemPressureLevelFromImageSensorWithPortType:];
-[FigCaptureSystemPressureMonitor systemPressureLevelFromPearlProjector];
-[FigCaptureSystemPressureMonitor updateWithPearlProjectorTemperature:];
-[FigCaptureSystemPressureMonitor updateWithPortType:imageSensorTemperature:];
```
