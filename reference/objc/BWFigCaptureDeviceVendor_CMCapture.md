# `BWFigCaptureDeviceVendor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 25 instance variables, 8 properties, 48 instance methods, 4 class methods

## Instance variables

```
^? _defaultDeviceCreateFunction;
^? _cmioExtensionDeviceCreateFunction;
@"NSMutableDictionary" _devicesStatesByDeviceID;
@"NSMutableArray" _registeredDeviceClients;
@"NSMutableArray" _activeDeviceClients;
@"NSMutableArray" _victimizedDeviceClients;
@"NSObject<OS_dispatch_queue>" _deviceQueue;
@"NSObject<OS_dispatch_source>" _defaultDeviceOpenTimer;
d _deviceCloseTimeoutSeconds;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@"NSObject<OS_os_transaction>" _activeForClientAssertion;
B _preventingSystemSleep;
I _preventSystemSleepAssertion;
@"NSMutableDictionary" _cameraPoseMatricesByPortTypeByDeviceID;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _calibrationStatusLock;
B _calibrationStatusQueried;
B _rearCameraCalibrationValid;
i _createDeviceTime;
@"CMIOExtensionDiscoverySession" _cmioDiscoverySession;
@"FigCaptureOSStateHandle" _osStateHandle;
@"NSMutableArray" _defaultDeviceCreationHistory;
@"NSMutableArray" _cmioDeviceCreationHistory;
@"NSDateFormatter" _deviceDateFormatter;
@"NSMutableSet" _defaultDevicePriorStreamPortTypes;
@"FigCaptureGameModeMonitor" _gameModeMonitor;
```

## Properties

```
@property (T@"NSArray",R,N) deviceIDs;
@property (Ti,R) activeClientPriority;
@property (TB,R) rearCameraCalibrationValid;
@property (Ti,R,N,V_createDeviceTime) createDeviceTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWFigCaptureDeviceVendor initialize];
+[BWFigCaptureDeviceVendor sharedCaptureDeviceVendor];
+[BWFigCaptureDeviceVendor sharedCaptureDeviceVendorWithDefaultDeviceCreateFunction:];
+[BWFigCaptureDeviceVendor videoCaptureDeviceFirmwareIsLoaded];
```

## Instance methods

```
-[BWFigCaptureDeviceVendor osStatePropertyList];
-[BWFigCaptureDeviceVendor streamsControlledByOtherClientsForDevice:];
-[BWFigCaptureDeviceVendor keepControlOfStreamsWithPositions:deviceTypes:forDevice:];
-[BWFigCaptureDeviceVendor defaultDeviceCreationHistory];
-[BWFigCaptureDeviceVendor copyStreamFromDevice:position:deviceType:deviceClientPriority:allowsStreamControlLoss:error:];
-[BWFigCaptureDeviceVendor controlledStreamsForDevice:];
-[BWFigCaptureDeviceVendor usageCountForDevice:];
-[BWFigCaptureDeviceVendor copyStreamsFromDevice:positions:deviceTypes:deviceClientPriority:allowsStreamControlLoss:error:];
-[BWFigCaptureDeviceVendor takeBackStreams:device:totalStreamingDuration:];
-[BWFigCaptureDeviceVendor copyDeviceForPublishingWithID:error:];
-[BWFigCaptureDeviceVendor deviceWithID:];
-[BWFigCaptureDeviceVendor requestControlOfStreams:device:deviceClientPriority:];
-[BWFigCaptureDeviceVendor activeDeviceClient];
-[BWFigCaptureDeviceVendor dealloc];
-[BWFigCaptureDeviceVendor streamsInUseForDevice:];
-[BWFigCaptureDeviceVendor structuredLightProjectorStandbyTemperatureWithError:];
-[BWFigCaptureDeviceVendor hasActiveForClientAssertion];
-[BWFigCaptureDeviceVendor copyStreamWithoutControlFromDevice:position:deviceType:error:];
-[BWFigCaptureDeviceVendor registeredDeviceClients];
-[BWFigCaptureDeviceVendor unregisterClient:];
-[BWFigCaptureDeviceVendor updateClientPriority:clientPriority:];
-[BWFigCaptureDeviceVendor cmioDeviceCreationHistory];
-[BWFigCaptureDeviceVendor _handleCMIOExtensionDevicesChangedNotification:];
-[BWFigCaptureDeviceVendor registeredDeviceClientWithID:];
-[BWFigCaptureDeviceVendor createDeviceTime];
-[BWFigCaptureDeviceVendor copyDefaultDeviceForVibeMitigation:];
-[BWFigCaptureDeviceVendor prewarmDefaultVideoDeviceForPID:completionHandler:];
-[BWFigCaptureDeviceVendor initWithDefaultDeviceCreateFunction:];
-[BWFigCaptureDeviceVendor isActiveDefaultDeviceAvailableToFlashlight:];
-[BWFigCaptureDeviceVendor copyDeviceWithID:forClient:informClientWhenDeviceAvailableAgain:error:];
-[BWFigCaptureDeviceVendor activeDeviceClients];
-[BWFigCaptureDeviceVendor shutDownSystemPressuredDevice:];
-[BWFigCaptureDeviceVendor deviceIDs];
-[BWFigCaptureDeviceVendor _deviceWithID:];
-[BWFigCaptureDeviceVendor registerClientWithAuditToken:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:];
-[BWFigCaptureDeviceVendor resumeSystemPressuredDevice];
-[BWFigCaptureDeviceVendor victimizedDeviceClients];
-[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:prefersDeviceInvalidatedImmediately:];
-[BWFigCaptureDeviceVendor invalidateVideoDevice:forPID:];
-[BWFigCaptureDeviceVendor copyStreamsWithoutControlFromDevice:positions:deviceTypes:error:];
-[BWFigCaptureDeviceVendor cameraPoseMatrixForStreamWithPosition:deviceType:deviceID:];
-[BWFigCaptureDeviceVendor copyDeviceForClient:informClientWhenDeviceAvailableAgain:error:];
-[BWFigCaptureDeviceVendor activeClientPriority];
-[BWFigCaptureDeviceVendor initWithDefaultDeviceCreateFunction:cmioExtensionDeviceCreateFunction:cmioDiscoverySession:];
-[BWFigCaptureDeviceVendor copyStreamsWithUniqueIDs:forDevice:deviceClientPriority:error:];
-[BWFigCaptureDeviceVendor _copyStreamsFromDevice:positions:deviceTypes:requestControl:deviceClientPriority:allowsStreamControlLoss:error:];
-[BWFigCaptureDeviceVendor registerClientWithAuditToken:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:];
-[BWFigCaptureDeviceVendor rearCameraCalibrationValid];
```
