# `BWSphereModeSelector`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 20 properties, 38 instance methods, 1 class methods

## Instance variables

```
@"NSString" _portType;
^{__CFString=} _currentSphereMode;
^{__CFString=} _currentNonLowPowerSphereMode;
f _maximumFrameRate;
B _sphereVideoSupported;
B _sphereVideoEnabled;
B _sphereVideoRecenteringEnabled;
B _avoidsSphereRecentering;
B _enablesSphereWhenAvailable;
B _motionDataInvalid;
B _lowPowerSphereModeEnabled;
B _stillPreviewActiveSupported;
B _zeroShutterLagEnabled;
i _sphereThermalLevel;
B _tripodModeEnabled;
B _depthDataDeliveryEnabled;
B _spherePanoSupported;
B _panoModeEnabled;
B _overCaptureEnabled;
B _trueVideoCaptureEnabled;
B _trueVideoUsesSphereModeVideoHighRange;
B _variableFrameRateVideoEnabled;
f _maximumFrameRateSupported;
B _visualIntelligenceCameraEnabled;
B _magneticInterferenceDetected;
```

## Properties

```
@property (T@"NSString",R) portType;
@property (Tf,N) maximumFrameRate;
@property (TB,R,N) sphereVideoSupported;
@property (TB,N) sphereVideoEnabled;
@property (TB,N) sphereVideoRecenteringEnabled;
@property (TB,N) avoidsSphereRecentering;
@property (TB,N) enablesSphereWhenAvailable;
@property (TB,N) zeroShutterLagEnabled;
@property (TB,N) lowPowerSphereModeEnabled;
@property (Ti,N) systemThermalLevel;
@property (TB,N) tripodModeEnabled;
@property (TB,N) magneticInterferenceDetected;
@property (TB,N) depthDataDeliveryEnabled;
@property (TB,N) panoModeEnabled;
@property (TB,N) overCaptureEnabled;
@property (TB,N) trueVideoCaptureEnabled;
@property (TB,N) variableFrameRateVideoEnabled;
@property (TB,N) visualIntelligenceCameraEnabled;
@property (T^{__CFString=},R) currentSphereMode;
@property (T^{__CFString=},R) currentNonLowPowerSphereMode;
```

## Class methods

```
+[BWSphereModeSelector initialize];
```

## Instance methods

```
-[BWSphereModeSelector setTrueVideoCaptureEnabled:];
-[BWSphereModeSelector sphereVideoEnabled];
-[BWSphereModeSelector avoidsSphereRecentering];
-[BWSphereModeSelector currentNonLowPowerSphereMode];
-[BWSphereModeSelector overCaptureEnabled];
-[BWSphereModeSelector setSphereVideoEnabled:];
-[BWSphereModeSelector setMagneticInterferenceDetected:];
-[BWSphereModeSelector magneticInterferenceDetected];
-[BWSphereModeSelector setOverCaptureEnabled:];
-[BWSphereModeSelector setVariableFrameRateVideoEnabled:];
-[BWSphereModeSelector variableFrameRateVideoEnabled];
-[BWSphereModeSelector visualIntelligenceCameraEnabled];
-[BWSphereModeSelector sphereVideoSupported];
-[BWSphereModeSelector enablesSphereWhenAvailable];
-[BWSphereModeSelector setMaximumFrameRate:];
-[BWSphereModeSelector setAvoidsSphereRecentering:];
-[BWSphereModeSelector trueVideoCaptureEnabled];
-[BWSphereModeSelector panoModeEnabled];
-[BWSphereModeSelector setEnablesSphereWhenAvailable:];
-[BWSphereModeSelector setVisualIntelligenceCameraEnabled:];
-[BWSphereModeSelector sphereVideoRecenteringEnabled];
-[BWSphereModeSelector setPanoModeEnabled:];
-[BWSphereModeSelector currentSphereMode];
-[BWSphereModeSelector portType];
-[BWSphereModeSelector maximumFrameRate];
-[BWSphereModeSelector setSystemThermalLevel:];
-[BWSphereModeSelector zeroShutterLagEnabled];
-[BWSphereModeSelector dealloc];
-[BWSphereModeSelector setZeroShutterLagEnabled:];
-[BWSphereModeSelector tripodModeEnabled];
-[BWSphereModeSelector setTripodModeEnabled:];
-[BWSphereModeSelector lowPowerSphereModeEnabled];
-[BWSphereModeSelector initWithPortType:stillActivePreviewSupported:sphereVideoSupported:sphereVideoMaxFrameRate:spherePanoSupported:trueVideoUsesSphereModeVideoHighRange:];
-[BWSphereModeSelector setLowPowerSphereModeEnabled:];
-[BWSphereModeSelector setDepthDataDeliveryEnabled:];
-[BWSphereModeSelector setSphereVideoRecenteringEnabled:];
-[BWSphereModeSelector depthDataDeliveryEnabled];
-[BWSphereModeSelector systemThermalLevel];
```
