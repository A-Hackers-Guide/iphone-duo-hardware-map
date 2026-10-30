# `CAMModeAndDeviceCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 7 instance variables, 7 properties, 38 instance methods, 0 class methods

## Instance variables

```
B __outputToExternalStorage;
i __requestID;
@"CAMCaptureGraphConfiguration" __desiredGraphConfiguration;
@"CAMCaptureGraphConfiguration" __resolvedGraphConfiguration;
d __minimumExecutionTime;
@"NSError" __configurationError;
q __deviceIntegrity;
```

## Properties

```
@property (T@"CAMCaptureGraphConfiguration",R,N,V__desiredGraphConfiguration) _desiredGraphConfiguration;
@property (T@"CAMCaptureGraphConfiguration",&,N,S_setResolvedGraphConfiguration:,V__resolvedGraphConfiguration) _resolvedGraphConfiguration;
@property (Td,R,N,V__minimumExecutionTime) _minimumExecutionTime;
@property (Ti,R,N,V__requestID) _requestID;
@property (TB,R,N,V__outputToExternalStorage) _outputToExternalStorage;
@property (T@"NSError",&,N,S_setConfigurationError:,V__configurationError) _configurationError;
@property (Tq,N,S_setDeviceIntegrity:,V__deviceIntegrity) _deviceIntegrity;
```

## Instance methods

```
-[CAMModeAndDeviceCommand requiresSessionModification];
-[CAMModeAndDeviceCommand _requestID];
-[CAMModeAndDeviceCommand _wantsLowLightBoostForMode:device:];
-[CAMModeAndDeviceCommand _specificEncodingBehaviorCommandForGraphConfiguration:];
-[CAMModeAndDeviceCommand _resolvedGraphConfiguration];
-[CAMModeAndDeviceCommand _secondaryInputsBecomingPrimaryWithContext:desiredPrimaryInputs:];
-[CAMModeAndDeviceCommand sessionModificationLogReason];
-[CAMModeAndDeviceCommand _desiredConnectionWithCaptureEngineSecondaryDevice:secondaryVideoPreviewLayer:];
-[CAMModeAndDeviceCommand userInfo];
-[CAMModeAndDeviceCommand _reapplyPrimaryDeviceFormatIfNeededWithEngineDevice:graphConfiguration:captureSession:];
-[CAMModeAndDeviceCommand _existingOutputsWithContext:without:];
-[CAMModeAndDeviceCommand _sanitizeDeviceUsingContext:];
-[CAMModeAndDeviceCommand _desiredConnectionWithCaptureEngineDuplicateDevice:duplicateVideoPreviewLayer:];
-[CAMModeAndDeviceCommand _minimumExecutionTime];
-[CAMModeAndDeviceCommand _desiredPrimaryInputsWithContext:captureEngineDevice:];
-[CAMModeAndDeviceCommand _setDeviceIntegrity:];
-[CAMModeAndDeviceCommand _configurationError];
-[CAMModeAndDeviceCommand executeWithContext:];
-[CAMModeAndDeviceCommand _specificFramerateCommandForGraphConfiguration:withContext:configureSecondaryDevice:];
-[CAMModeAndDeviceCommand _secondaryEngineDeviceWithContext:graphConfiguration:resolvedDevice:];
-[CAMModeAndDeviceCommand _performPostConfigurationSetupForGraphConfiguration:withContext:];
-[CAMModeAndDeviceCommand _setConfigurationError:];
-[CAMModeAndDeviceCommand _primaryEngineDeviceWithContext:graphConfiguration:resolvedDevice:];
-[CAMModeAndDeviceCommand _performDeviceIntegrityCheckForMode:deviceType:captureDevice:];
-[CAMModeAndDeviceCommand _outputToExternalStorage];
-[CAMModeAndDeviceCommand initWithGraphConfiguration:minimumExecutionTime:requestID:outputToExternalStorage:];
-[CAMModeAndDeviceCommand sessionModificationMinimumExecutionTime];
-[CAMModeAndDeviceCommand _performPostConfigurationSanityCheckForGraphConfiguration:withContext:];
-[CAMModeAndDeviceCommand copyWithZone:];
-[CAMModeAndDeviceCommand _existingVideoPreviewLayersWithContext:without:];
-[CAMModeAndDeviceCommand _deviceIntegrity];
-[CAMModeAndDeviceCommand _existingInputsWithContext:without:];
-[CAMModeAndDeviceCommand _isStillImageMode:];
-[CAMModeAndDeviceCommand _shouldEnableLivePhotoCaptureForMode:device:];
-[CAMModeAndDeviceCommand _setResolvedGraphConfiguration:];
-[CAMModeAndDeviceCommand _wantsLivePhotoMetadataInVideosForMode:device:];
-[CAMModeAndDeviceCommand _desiredSecondaryInputsWithCaptureEngineSecondaryDevice:];
-[CAMModeAndDeviceCommand _desiredGraphConfiguration];
```
