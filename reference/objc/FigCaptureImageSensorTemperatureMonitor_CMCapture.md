# `FigCaptureImageSensorTemperatureMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _portType;
[5{?="min"f"max"f}] _systemPressureLevelByImageSensorTemperature;
i _currentSystemPressureFromImageSensorTemperature;
@"NSObject<OS_dispatch_source>" _nominalImageSensorTemperatureMonitorTimer;
```

## Properties

```
@property (Ti,R) systemPressureLevelFromImageSensorTemperature;
```

## Class methods

```
+[FigCaptureImageSensorTemperatureMonitor initialize];
```

## Instance methods

```
-[FigCaptureImageSensorTemperatureMonitor dealloc];
-[FigCaptureImageSensorTemperatureMonitor initWithPortType:sensorThermalLevelsByTemperature:];
-[FigCaptureImageSensorTemperatureMonitor startMonitoringImageSensorTemperatureUntilNominalWithQueue:changeHandler:];
-[FigCaptureImageSensorTemperatureMonitor systemPressureLevelFromImageSensorTemperature];
-[FigCaptureImageSensorTemperatureMonitor updateWithImageSensorTemperature:];
```
