# `AVCaptureSmartFramingMonitor`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 4 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _monitorWeakReference;
@"AVWeakReference" _deviceWeakReference;
@"NSArray" _photoModeFramings;
@"NSArray" _photoModeSmartFramings;
@"NSArray" _photoModeFieldsOfView;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _framingsLock;
@"NSArray" _supportedFramings;
@"AVCaptureFraming" _recommendedFraming;
@"NSArray" _enabledFramings;
@"NSArray" _supportedSmartFramings;
@"AVCaptureSmartFraming" _recommendedSmartFraming;
@"NSArray" _enabledSmartFramings;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _isMonitoringLock;
B _isMonitoring;
@"AVCaptureSmartFramingMonitorObservationRegistrar" _observationRegistrar;
```

## Properties

```
@property (T@"NSArray",R,N) supportedFramings;
@property (T@"NSArray",C,N) enabledFramings;
@property (T@"AVCaptureFraming",R,N) recommendedFraming;
@property (TB,R,N,GisMonitoring) monitoring;
```

## Class methods

```
+[AVCaptureSmartFramingMonitor initialize];
```

## Instance methods

```
-[AVCaptureSmartFramingMonitor recommendedFraming];
-[AVCaptureSmartFramingMonitor setEnabledSmartFramings:];
-[AVCaptureSmartFramingMonitor isMonitoring];
-[AVCaptureSmartFramingMonitor observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureSmartFramingMonitor debugDescription];
-[AVCaptureSmartFramingMonitor device];
-[AVCaptureSmartFramingMonitor startMonitoringWithError:];
-[AVCaptureSmartFramingMonitor supportedSmartFramings];
-[AVCaptureSmartFramingMonitor setEnabledFramings:];
-[AVCaptureSmartFramingMonitor dealloc];
-[AVCaptureSmartFramingMonitor updateRecommendedSmartFramingWithFieldOfView:];
-[AVCaptureSmartFramingMonitor recommendedSmartFraming];
-[AVCaptureSmartFramingMonitor initWithDevice:smartFramingZoomFactorsByFieldOfView:];
-[AVCaptureSmartFramingMonitor stopMonitoring];
-[AVCaptureSmartFramingMonitor _updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForFramings:];
-[AVCaptureSmartFramingMonitor _updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForSmartFramings:];
-[AVCaptureSmartFramingMonitor enabledSmartFramings];
-[AVCaptureSmartFramingMonitor description];
-[AVCaptureSmartFramingMonitor enabledFramings];
-[AVCaptureSmartFramingMonitor startMonitoring:];
-[AVCaptureSmartFramingMonitor _handleChangedActiveFormat:];
-[AVCaptureSmartFramingMonitor supportedFramings];
-[AVCaptureSmartFramingMonitor _populatePhotoModeSmartFramingsAndFieldsOfViewFromZoomFactorsByFieldOfView:];
```
