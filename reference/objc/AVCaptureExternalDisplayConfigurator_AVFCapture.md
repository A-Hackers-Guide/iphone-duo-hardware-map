# `AVCaptureExternalDisplayConfigurator`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCaptureVisibilityHelperLayerDelegate`
- 15 instance variables, 10 properties, 39 instance methods, 6 class methods

## Instance variables

```
@"AVWeakReference" _configuratorWeakReference;
@"AVWeakReference" _deviceWeakReference;
@"AVWeakReference" _previewLayerWeakReference;
@"NSObject<OS_dispatch_queue>" _queue;
@"AVCaptureExternalDisplayConfiguration" _configuration;
@? _configurationBlock;
@? _configurationTimeoutBlock;
@"AVCaptureVisibilityHelperLayer" _observationLayer;
B _active;
B _retryConfiguration;
B _observingDeviceColorspace;
B _observingDeviceFramerate;
B _registered;
d _activeExternalDisplayFrameRate;
@"NSUUID" _identifier;
```

## Properties

```
@property (TB,N,V_retryConfiguration) retryConfiguration;
@property (TB,R,N) externalDisplayAndCaptureDeviceSynchronized;
@property (TB,N,GisActive,V_active) active;
@property (Td,N,V_activeExternalDisplayFrameRate) activeExternalDisplayFrameRate;
@property (TB,N,V_observingDeviceColorspace) observingDeviceColorspace;
@property (TB,N,V_observingDeviceFramerate) observingDeviceFramerate;
@property (TB,N,V_registered) registered;
@property (T@"NSUUID",R,N,V_identifier) identifier;
@property (T@"AVCaptureDevice",R,W,N) device;
@property (T@"CALayer",R,W,N) previewLayer;
```

## Class methods

```
+[AVCaptureExternalDisplayConfigurator initialize];
+[AVCaptureExternalDisplayConfigurator isSupported];
+[AVCaptureExternalDisplayConfigurator isBypassingColorSpaceConversionSupported];
+[AVCaptureExternalDisplayConfigurator isMatchingFrameRateSupported];
+[AVCaptureExternalDisplayConfigurator isPreferredResolutionSupported];
+[AVCaptureExternalDisplayConfigurator registerConfigurator:withDisplayIdentifier:];
```

## Instance methods

```
-[AVCaptureExternalDisplayConfigurator _setup];
-[AVCaptureExternalDisplayConfigurator setRegistered:];
-[AVCaptureExternalDisplayConfigurator observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureExternalDisplayConfigurator identifier];
-[AVCaptureExternalDisplayConfigurator device];
-[AVCaptureExternalDisplayConfigurator stop];
-[AVCaptureExternalDisplayConfigurator dealloc];
-[AVCaptureExternalDisplayConfigurator setActive:];
-[AVCaptureExternalDisplayConfigurator registered];
-[AVCaptureExternalDisplayConfigurator description];
-[AVCaptureExternalDisplayConfigurator isActive];
-[AVCaptureExternalDisplayConfigurator _configureExternalDisplay];
-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayColorspace];
-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayFrameRate];
-[AVCaptureExternalDisplayConfigurator _deviceColorspaceChangeMonitorConfigure];
-[AVCaptureExternalDisplayConfigurator _deviceColorspaceChangeMonitorTeardown];
-[AVCaptureExternalDisplayConfigurator _deviceFramerateChangedMonitorConfigure];
-[AVCaptureExternalDisplayConfigurator _deviceFramerateChangedMonitorTeardown];
-[AVCaptureExternalDisplayConfigurator _dispatchConfiguration];
-[AVCaptureExternalDisplayConfigurator _displayConfigurationChangedMonitorConfigure];
-[AVCaptureExternalDisplayConfigurator _displayConfigurationChangedMonitorTeardown];
-[AVCaptureExternalDisplayConfigurator _externalDisplayConfigurationChangedHandler];
-[AVCaptureExternalDisplayConfigurator _getConfigurationWithCompletion:];
-[AVCaptureExternalDisplayConfigurator _makeInActive];
-[AVCaptureExternalDisplayConfigurator activeExternalDisplayFrameRate];
-[AVCaptureExternalDisplayConfigurator dispatchConfiguration];
-[AVCaptureExternalDisplayConfigurator externalDisplayAndCaptureDeviceSynchronized];
-[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:];
-[AVCaptureExternalDisplayConfigurator initWithDevice:previewLayer:configuration:];
-[AVCaptureExternalDisplayConfigurator observingDeviceColorspace];
-[AVCaptureExternalDisplayConfigurator observingDeviceFramerate];
-[AVCaptureExternalDisplayConfigurator previewLayer];
-[AVCaptureExternalDisplayConfigurator registerSelfForDisplay:];
-[AVCaptureExternalDisplayConfigurator retryConfiguration];
-[AVCaptureExternalDisplayConfigurator setActiveExternalDisplayFrameRate:];
-[AVCaptureExternalDisplayConfigurator setObservingDeviceColorspace:];
-[AVCaptureExternalDisplayConfigurator setObservingDeviceFramerate:];
-[AVCaptureExternalDisplayConfigurator setRetryConfiguration:];
-[AVCaptureExternalDisplayConfigurator visibilityHelperLayer:visibilityChanged:];
```
