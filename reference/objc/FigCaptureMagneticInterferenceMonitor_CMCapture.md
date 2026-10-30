# `FigCaptureMagneticInterferenceMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} _hidSystemClient;
@"NSObject<OS_dispatch_queue>" _monitorQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _magneticInterferenceDetected;
B _isMonitoring;
B _stylusDataReceivedDuringSession;
@? _magneticInterferenceHandler;
@"FigStateMachine" _stateMachine;
@"NSObject<OS_dispatch_source>" _exitZoneTimer;
I _exitZoneDuration;
@"NSMutableSet" _innerDisplaySenderIDs;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _magneticInterferenceZone;
```

## Properties

```
@property (TB,R,N) magneticInterferenceDetected;
@property (TB,R,N) isMonitoring;
@property (TB,N,V_stylusDataReceivedDuringSession) stylusDataReceivedDuringSession;
```

## Class methods

```
+[FigCaptureMagneticInterferenceMonitor initialize];
```

## Instance methods

```
-[FigCaptureMagneticInterferenceMonitor magneticInterferenceDetected];
-[FigCaptureMagneticInterferenceMonitor isMonitoring];
-[FigCaptureMagneticInterferenceMonitor init];
-[FigCaptureMagneticInterferenceMonitor dealloc];
-[FigCaptureMagneticInterferenceMonitor setStylusDataReceivedDuringSession:];
-[FigCaptureMagneticInterferenceMonitor stopMonitoring];
-[FigCaptureMagneticInterferenceMonitor stylusDataReceivedDuringSession];
-[FigCaptureMagneticInterferenceMonitor setMagneticInterferenceHandler:];
-[FigCaptureMagneticInterferenceMonitor startMonitoringWithZone:];
```
