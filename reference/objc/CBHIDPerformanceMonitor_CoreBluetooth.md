# `CBHIDPerformanceMonitor`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBActivatable`
- 50 instance variables, 10 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _activateCalled;
B _invalidateCalled;
B _invalidateDone;
B _finishWait;
^^{IOHIDDeviceInterface} _hidInterface;
^{__IOHIDManager=} _hidManager;
B _hidOpen;
^^{IOCFPlugInInterfaceStruct} _hidPluginInterface;
I _hidProductID;
I _hidService;
B _hidStartedErrorRateMode;
@"CBPacketLoggerClient" _packetLoggerClient;
B _startWait;
@"CBDevice" _targetDevice;
@"NSString" _targetBTAddrData;
@"NSString" _targetBTAddrKey;
Q _targetDeviceIndex;
@"NSArray" _targetDevices;
d _testSecondsActual;
@"NSObject<OS_dispatch_source>" _timeoutTimer;
c _statsLastRSSI;
S _statsLastConnectionHandle;
Q _statsPacketMicsStart;
Q _statsPacketMicsEnd;
Q _statsPacketMicsStartInterim;
Q _statsPacketMicsPrevious;
Q _statsPacketCountActual;
Q _statsPacketCountExpected;
Q _statsPacketCountInterim;
Q _statsPacketIntervalMicsExpected;
Q _statsPacketIntervalMicsMax;
d _statsPacketP50Max;
d _statsPacketP75Max;
d _statsPacketP90Max;
d _statsPacketP95Max;
d _statsPacketP99Max;
@"NSMutableArray" _statsPacketDeltaMics;
@"NSMutableArray" _intrmPacketDeltaMics;
Q _statsPacketExcessiveInterval;
@"NSDate" _slidingWindowDate;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _invalidationHandler;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSArray" _devices;
@? _excessiveIntervalHandler;
d _excessiveMs;
d _intervalMs;
d _slideWindowSec;
@? _summaryHandler;
d _testSeconds;
```

## Properties

```
@property (T@"NSArray",C,N,V_devices) devices;
@property (T@?,C,N,V_excessiveIntervalHandler) excessiveIntervalHandler;
@property (Td,N,V_excessiveMs) excessiveMs;
@property (Td,N,V_intervalMs) intervalMs;
@property (Td,N,V_slideWindowSec) slideWindowSec;
@property (T@?,C,N,V_summaryHandler) summaryHandler;
@property (Td,N,V_testSeconds) testSeconds;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Instance methods

```
-[CBHIDPerformanceMonitor setWorkQueue:];
-[CBHIDPerformanceMonitor setDevices:];
-[CBHIDPerformanceMonitor dispatchQueue];
-[CBHIDPerformanceMonitor activateWithCompletion:];
-[CBHIDPerformanceMonitor setInvalidationHandler:];
-[CBHIDPerformanceMonitor init];
-[CBHIDPerformanceMonitor _invalidate];
-[CBHIDPerformanceMonitor workQueue];
-[CBHIDPerformanceMonitor setDispatchQueue:];
-[CBHIDPerformanceMonitor invalidate];
-[CBHIDPerformanceMonitor devices];
-[CBHIDPerformanceMonitor _activateWithCompletion:];
-[CBHIDPerformanceMonitor invalidationHandler];
-[CBHIDPerformanceMonitor _invalidated];
-[CBHIDPerformanceMonitor _packetLoggerProcessPacketData:];
-[CBHIDPerformanceMonitor setExcessiveMs:];
-[CBHIDPerformanceMonitor setTestSeconds:];
-[CBHIDPerformanceMonitor _calculatePercentile:percentile:];
-[CBHIDPerformanceMonitor _findDevicesAndReturnError:];
-[CBHIDPerformanceMonitor _hidSetFeatureWithReportID:value:error:];
-[CBHIDPerformanceMonitor _hidStartAndReturnError:];
-[CBHIDPerformanceMonitor _hidStartPERAndRetunError:];
-[CBHIDPerformanceMonitor _hidStop];
-[CBHIDPerformanceMonitor _hidStopPERAndRetunError:];
-[CBHIDPerformanceMonitor _isAppleOldHIDs:];
-[CBHIDPerformanceMonitor _isMac];
-[CBHIDPerformanceMonitor _packetLoggerStart];
-[CBHIDPerformanceMonitor _packetLoggerStop];
-[CBHIDPerformanceMonitor _rssiAndHandleRead];
-[CBHIDPerformanceMonitor _showSummaryResult:isFinal:packetMics:statsDelta:deltaMics:countActual:];
-[CBHIDPerformanceMonitor _testEnd];
-[CBHIDPerformanceMonitor _testEnded];
-[CBHIDPerformanceMonitor _testStart];
-[CBHIDPerformanceMonitor _timerStart];
-[CBHIDPerformanceMonitor excessiveIntervalHandler];
-[CBHIDPerformanceMonitor excessiveMs];
-[CBHIDPerformanceMonitor intervalMs];
-[CBHIDPerformanceMonitor setExcessiveIntervalHandler:];
-[CBHIDPerformanceMonitor setIntervalMs:];
-[CBHIDPerformanceMonitor setSlideWindowSec:];
-[CBHIDPerformanceMonitor setSummaryHandler:];
-[CBHIDPerformanceMonitor slideWindowSec];
-[CBHIDPerformanceMonitor summaryHandler];
-[CBHIDPerformanceMonitor testSeconds];
```
