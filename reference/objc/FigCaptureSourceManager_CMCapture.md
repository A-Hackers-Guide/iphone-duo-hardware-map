# `FigCaptureSourceManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 33 instance variables, 0 properties, 45 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _captureSourceBackings;
B _useSharedCaptureSourceBackingsProvider;
@"NSMutableArray" _activeVideoCaptureSources;
^{OpaqueFigSimpleMutex=} _activeVideoCaptureSourceLock;
@"NSMutableArray" _allVideoCaptureSources;
^{OpaqueFigSimpleMutex=} _allVideoCaptureSourcesLock;
@"FigCaptureSourceVibeMitigation" _vibeMitigation;
B _timeOfFlightAFEnabled;
B _timeOfFlightAFSuspended;
B _directTimeOfFlightAFAssistStreamControlSupported;
B _directTimeOfFlightAFAssistStreamControlEnabled;
i _timeOfFlightAFProjectorMode;
@"BWFigCaptureStream" _timeOfFlightAFAssistStream;
B _structuredLightAFEnabled;
B _structuredLightAFSuspended;
@"BWFigCaptureStream" _structuredLightAFAssistStream;
@"BWFigCaptureStream" _structuredLightAFAssistStreamControlledByAnotherClient;
@"BWFigCaptureStream" _structuredLightAFTargetStream;
^{OpaqueFigCaptureSource=} _structuredLightAFTargetStreamSource;
B _structuredLightAFTargetStreamStreaming;
i _previousMaxSystemPressureLevel;
@"FigCaptureThermalMonitor" _thermalMonitor;
@"FigCapturePowerMonitor" _powerMonitor;
@"FigCaptureSystemPressureMonitor" _systemPressureMonitor;
@"FigCaptureAngleMonitor" _angleMonitor;
q _primaryDisplayRegion;
@"NSMutableSet" _angleMonitorClientBundleIDs;
B _renoOccluded;
B _omahaRenoAngleWithinDropZone;
q _deviceAngleState;
^{OpaqueFigSimpleMutex=} _displayAngleStateLock;
@"FigCaptureMagneticInterferenceMonitor" _magneticInterferenceMonitor;
@"NSObject<OS_dispatch_queue>" _faceIDUnwrapQueue;
```

## Class methods

```
+[FigCaptureSourceManager initialize];
+[FigCaptureSourceManager captureSourceManagerWithBackings:];
+[FigCaptureSourceManager sharedCaptureSourceManager];
```

## Instance methods

```
-[FigCaptureSourceManager startFaceIDUnwrap];
-[FigCaptureSourceManager _requestStructuredLightAFAssistStreamControlledByAnotherClientFromDeviceVendor:captureDevice:];
-[FigCaptureSourceManager _handleStructuredLightAFTargetStreamStoppedNotificationFromStream:];
-[FigCaptureSourceManager _configureTimeOfFlightStreamForAFAssist];
-[FigCaptureSourceManager deactivateAttachedVideoSource:device:];
-[FigCaptureSourceManager _updateTimeOfFlightAFEnabledStatus];
-[FigCaptureSourceManager layoutMonitor:didUpdateLayout:];
-[FigCaptureSourceManager _updateStructuredLightAFEnabledStatus];
-[FigCaptureSourceManager copySourcesWithType:clientAuditToken:clientIsBincompat:];
-[FigCaptureSourceManager copySourcesWithType:];
-[FigCaptureSourceManager _copyActiveCaptureDevice];
-[FigCaptureSourceManager _clearDeviceAngleState];
-[FigCaptureSourceManager enableTimeOfFlightAutoFocusIfSupported];
-[FigCaptureSourceManager dealloc];
-[FigCaptureSourceManager _magneticInterferenceZoneFromActiveSources];
-[FigCaptureSourceManager _handleStructuredLightAFAssistStreamControlRelinquishedByAnotherClientNotificationFromStream:];
-[FigCaptureSourceManager _updateFaceIDUnwrapResultWithStatus:pearlSecureSessionError:cameraStreamError:];
-[FigCaptureSourceManager _structuredLightAFAssistUnregisterForTargetStreamNotifications];
-[FigCaptureSourceManager _structuredLightAFAssistRegisterForTargetStreamNotifications];
-[FigCaptureSourceManager _handleOmahaRenoAngleWithinDropZoneState:];
-[FigCaptureSourceManager _handleStructuredLightAFAssistStreamControlTakenByAnotherClientNotificationFromStream:];
-[FigCaptureSourceManager _resetTimeOfFlightAutoFocusWithDevice:];
-[FigCaptureSourceManager needsDeferredTimeOfFlightAutoFocusEnablement];
-[FigCaptureSourceManager _handleSystemPressureChange:systemPressureLevelFromPeakPower:systemPressureLevelFromDepthModuleTemperature:systemPressureLevelFromSystemStress:systemPressureLevelFromImageSensorTemperatureByPortType:];
-[FigCaptureSourceManager activateAttachedVideoSource:hostVideoSource:attachedSessionID:];
-[FigCaptureSourceManager _handleMagneticInterferenceChange:];
-[FigCaptureSourceManager _handleThermalPressureOrPowerChange:powerPressureLevel:maxTorchLevel:];
-[FigCaptureSourceManager initWithBackings:fineGrainThermalMonitoringEnabled:apsCalibrationMonitorEnabled:useSharedCaptureSourceBackingsProvider:];
-[FigCaptureSourceManager _handleStructuredLightAFTargetStreamStartedNotificationFromStream:];
-[FigCaptureSourceManager activateVideoSources:activationOptions:clientApplicationID:tccIdentity:mediaEnvironment:captureDevicesByID:stereoVideoCaptureEnabled:multiCamClientCompositingEnabled:rebuildingGraphForTrueVideoTeleTransition:devicesOut:];
-[FigCaptureSourceManager _configureStructuredLightStreamForAFAssist];
-[FigCaptureSourceManager _structuredLightAFAssistRegisterForAssistStreamNotificationsFromStream:];
-[FigCaptureSourceManager _updateOccludedState];
-[FigCaptureSourceManager _returnCaptureStream:toVendor:captureDevice:];
-[FigCaptureSourceManager _structuredLightAFAssistUnregisterForAssistStreamNotificationsFromStream:];
-[FigCaptureSourceManager imageSensorTemperatureChanged:portType:];
-[FigCaptureSourceManager _resetStructuredLightAutoFocus];
-[FigCaptureSourceManager pearlProjectorTemperatureChanged:];
-[FigCaptureSourceManager _startFaceIDUnwrapWithStream:outError:];
-[FigCaptureSourceManager _updateStructuredLightAFTargetStreamResources];
-[FigCaptureSourceManager willDeactivateVideoCaptureSourceWithCaptureDevice:];
-[FigCaptureSourceManager willInvalidateVideoCaptureSource:];
-[FigCaptureSourceManager deactivateVideoSources:devices:keepTimeOfFlightAutoFocusEnabled:];
-[FigCaptureSourceManager _updateDeviceAngleState];
-[FigCaptureSourceManager _clearOmahaRenoAngleWithinDropZone];
```
