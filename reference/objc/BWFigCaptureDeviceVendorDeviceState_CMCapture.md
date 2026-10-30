# `BWFigCaptureDeviceVendorDeviceState`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 21 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"BWFigCaptureDevice" _device;
^{OpaqueFigCaptureDevice=} _figCaptureDevice;
@"NSObject<OS_dispatch_source>" _deviceCloseTimer;
i _deviceUsageCount;
B _inUseForPublishing;
B _inUseForVibeMitigation;
i _takeBackDeviceCalledForActiveClientID;
q deviceCloseTimerStartTime;
@"NSMutableArray" _controlledStreams;
@"NSMutableArray" _streamsToKeepControlled;
@"NSMutableArray" _streamsInUse;
@"NSMutableArray" _streamsControlledByOtherClients;
@"NSMutableArray" _portTypesAllowingStreamControlLoss;
@"NSMutableSet" _portTypesToCheckForToFAFEstimator;
@"NSMutableDictionary" _tofAFEstimatorResultsByPortType;
@"NSMutableDictionary" _tofAFEstimatorResultsStreamingTimeByPortType;
@"NSMutableDictionary" _tofAFEstimatorClientApplicationIDByPortType;
@"NSMutableSet" _portTypesToCheckForAFDriverShortStatistics;
@"NSMutableDictionary" _afDriverShortStatisticsByPortType;
B _shutDownDueToSystemPressure;
q _deviceCloseTimerStartTime;
```

## Properties

```
@property (T@"BWFigCaptureDevice",R,N,V_device) device;
@property (T^{OpaqueFigCaptureDevice=},R,N,V_figCaptureDevice) figCaptureDevice;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_deviceCloseTimer) deviceCloseTimer;
@property (Ti,N,V_deviceUsageCount) deviceUsageCount;
@property (TB,N,V_inUseForPublishing) inUseForPublishing;
@property (TB,N,V_inUseForVibeMitigation) inUseForVibeMitigation;
@property (Ti,N,V_takeBackDeviceCalledForActiveClientID) takeBackDeviceCalledForActiveClientID;
@property (Tq,N,V_deviceCloseTimerStartTime) deviceCloseTimerStartTime;
@property (T@"NSMutableArray",R,N,V_controlledStreams) controlledStreams;
@property (T@"NSMutableArray",R,N,V_streamsToKeepControlled) streamsToKeepControlled;
@property (T@"NSMutableArray",R,N,V_streamsInUse) streamsInUse;
@property (T@"NSMutableArray",R,N,V_streamsControlledByOtherClients) streamsControlledByOtherClients;
@property (T@"NSMutableArray",&,N,V_portTypesAllowingStreamControlLoss) portTypesAllowingStreamControlLoss;
@property (T@"NSArray",R,N) streamsRequiringControlControlledByOtherClients;
@property (T@"NSMutableSet",R,N,V_portTypesToCheckForToFAFEstimator) portTypesToCheckForToFAFEstimator;
@property (T@"NSMutableDictionary",R,N,V_tofAFEstimatorResultsByPortType) tofAFEstimatorResultsByPortType;
@property (T@"NSMutableDictionary",R,N,V_tofAFEstimatorClientApplicationIDByPortType) tofAFEstimatorClientApplicationIDByPortType;
@property (T@"NSMutableDictionary",R,N,V_tofAFEstimatorResultsStreamingTimeByPortType) tofAFEstimatorResultsStreamingTimeByPortType;
@property (T@"NSMutableSet",R,N,V_portTypesToCheckForAFDriverShortStatistics) portTypesToCheckForAFDriverShortStatistics;
@property (T@"NSMutableDictionary",R,N,V_afDriverShortStatisticsByPortType) afDriverShortStatisticsByPortType;
@property (TB,N,V_shutDownDueToSystemPressure) shutDownDueToSystemPressure;
```

## Instance methods

```
-[BWFigCaptureDeviceVendorDeviceState takeBackDeviceCalledForActiveClientID];
-[BWFigCaptureDeviceVendorDeviceState setDeviceUsageCount:];
-[BWFigCaptureDeviceVendorDeviceState tofAFEstimatorClientApplicationIDByPortType];
-[BWFigCaptureDeviceVendorDeviceState tofAFEstimatorResultsStreamingTimeByPortType];
-[BWFigCaptureDeviceVendorDeviceState deviceUsageCount];
-[BWFigCaptureDeviceVendorDeviceState figCaptureDevice];
-[BWFigCaptureDeviceVendorDeviceState afDriverShortStatisticsByPortType];
-[BWFigCaptureDeviceVendorDeviceState debugDescription];
-[BWFigCaptureDeviceVendorDeviceState setPortTypesAllowingStreamControlLoss:];
-[BWFigCaptureDeviceVendorDeviceState shutDownDueToSystemPressure];
-[BWFigCaptureDeviceVendorDeviceState setTakeBackDeviceCalledForActiveClientID:];
-[BWFigCaptureDeviceVendorDeviceState device];
-[BWFigCaptureDeviceVendorDeviceState streamsControlledByOtherClients];
-[BWFigCaptureDeviceVendorDeviceState dealloc];
-[BWFigCaptureDeviceVendorDeviceState streamsToKeepControlled];
-[BWFigCaptureDeviceVendorDeviceState setDeviceCloseTimer:];
-[BWFigCaptureDeviceVendorDeviceState setShutDownDueToSystemPressure:];
-[BWFigCaptureDeviceVendorDeviceState portTypesAllowingStreamControlLoss];
-[BWFigCaptureDeviceVendorDeviceState inUseForPublishing];
-[BWFigCaptureDeviceVendorDeviceState streamsInUse];
-[BWFigCaptureDeviceVendorDeviceState tofAFEstimatorResultsByPortType];
-[BWFigCaptureDeviceVendorDeviceState portTypesToCheckForToFAFEstimator];
-[BWFigCaptureDeviceVendorDeviceState deviceCloseTimer];
-[BWFigCaptureDeviceVendorDeviceState streamsRequiringControlControlledByOtherClients];
-[BWFigCaptureDeviceVendorDeviceState controlledStreams];
-[BWFigCaptureDeviceVendorDeviceState description];
-[BWFigCaptureDeviceVendorDeviceState setDeviceCloseTimerStartTime:];
-[BWFigCaptureDeviceVendorDeviceState portTypesToCheckForAFDriverShortStatistics];
-[BWFigCaptureDeviceVendorDeviceState setInUseForVibeMitigation:];
-[BWFigCaptureDeviceVendorDeviceState initWithDevice:figCaptureDevice:];
-[BWFigCaptureDeviceVendorDeviceState setInUseForPublishing:];
-[BWFigCaptureDeviceVendorDeviceState inUseForVibeMitigation];
-[BWFigCaptureDeviceVendorDeviceState deviceCloseTimerStartTime];
```
