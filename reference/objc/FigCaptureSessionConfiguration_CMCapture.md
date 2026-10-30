# `FigCaptureSessionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`, `FigXPCCoding`, `NSCopying`
- 25 instance variables, 33 properties, 69 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _connections;
q _configurationID;
Q _clientSDKVersionToken;
@"NSString" _sessionPreset;
B _usesAppAudioSession;
B _configuresAppAudioSession;
B _configuresAppAudioSessionToMixWithOthers;
B _configuresAppAudioSessionForBluetoothHighQualityRecording;
B _allowedToRunInMultitaskingMode;
B _isMultiCamSession;
B _xctestAuthorizedToStealDevice;
B _continuityCameraIsWired;
i _continuityCameraClientDeviceClass;
B _clientIsVOIP;
B _suppressVideoEffects;
@"NSObject<OS_tcc_identity>" _tccIdentity;
B _checkIfFileAlreadyExistForMFO;
B _clientExpectsCameraMountedInLandscapeOrientation;
B _smartStyleRenderingEnabled;
q _smartStyleControlMode;
@"FigCaptureSmartStyle" _smartStyle;
B _textureStyleEnabled;
@"FigCaptureTextureStyle" _textureStyle;
B _automaticallyRunsDeferredStart;
B _visualIntelligenceCameraEnabled;
```

## Properties

```
@property (Tq,N,V_configurationID) configurationID;
@property (TQ,N,V_clientSDKVersionToken) clientSDKVersionToken;
@property (TB,R,N) coexistenceWithInfraredSourceEnabled;
@property (T@"NSArray",R,N) connectionConfigurations;
@property (T@"NSArray",R,N) sourceConfigurations;
@property (T@"NSArray",R,N) sinkConfigurations;
@property (T@"NSString",&,N,V_sessionPreset) sessionPreset;
@property (TB,N,V_usesAppAudioSession) usesAppAudioSession;
@property (TB,N,V_configuresAppAudioSession) configuresAppAudioSession;
@property (TB,N,V_configuresAppAudioSessionToMixWithOthers) configuresAppAudioSessionToMixWithOthers;
@property (TB,N,V_configuresAppAudioSessionForBluetoothHighQualityRecording) configuresAppAudioSessionForBluetoothHighQualityRecording;
@property (TB,N,V_allowedToRunInMultitaskingMode) allowedToRunInMultitaskingMode;
@property (TB,N,GisMultiCamSession,V_isMultiCamSession) multiCamSession;
@property (TB,N,V_xctestAuthorizedToStealDevice) xctestAuthorizedToStealDevice;
@property (TB,N,V_continuityCameraIsWired) continuityCameraIsWired;
@property (Ti,N,V_continuityCameraClientDeviceClass) continuityCameraClientDeviceClass;
@property (TB,N,V_clientIsVOIP) clientIsVOIP;
@property (TB,N,V_suppressVideoEffects) suppressVideoEffects;
@property (T@"NSObject<OS_tcc_identity>",&,N,V_tccIdentity) tccIdentity;
@property (TB,N,V_checkIfFileAlreadyExistForMFO) checkIfFileAlreadyExistForMFO;
@property (TB,N,V_clientExpectsCameraMountedInLandscapeOrientation) clientExpectsCameraMountedInLandscapeOrientation;
@property (TB,R,N) allCameraSourcesAreMetadataCameras;
@property (TB,N,V_smartStyleRenderingEnabled) smartStyleRenderingEnabled;
@property (Tq,N,V_smartStyleControlMode) smartStyleControlMode;
@property (T@"FigCaptureSmartStyle",C,N,V_smartStyle) smartStyle;
@property (TB,N,V_textureStyleEnabled) textureStyleEnabled;
@property (T@"FigCaptureTextureStyle",C,N,V_textureStyle) textureStyle;
@property (TB,N,V_automaticallyRunsDeferredStart) automaticallyRunsDeferredStart;
@property (TB,N,V_visualIntelligenceCameraEnabled) visualIntelligenceCameraEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureSessionConfiguration initialize];
```

## Instance methods

```
-[FigCaptureSessionConfiguration setSmartStyleRenderingEnabled:];
-[FigCaptureSessionConfiguration setContinuityCameraClientDeviceClass:];
-[FigCaptureSessionConfiguration osStatePropertyList];
-[FigCaptureSessionConfiguration setContinuityCameraIsWired:];
-[FigCaptureSessionConfiguration continuityCameraIsWired];
-[FigCaptureSessionConfiguration clientIsVOIP];
-[FigCaptureSessionConfiguration setSmartStyleControlMode:];
-[FigCaptureSessionConfiguration visualIntelligenceCameraEnabled];
-[FigCaptureSessionConfiguration configuresAppAudioSessionToMixWithOthers];
-[FigCaptureSessionConfiguration isMultiCamSession];
-[FigCaptureSessionConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureSessionConfiguration setVisualIntelligenceCameraEnabled:];
-[FigCaptureSessionConfiguration smartStyleRenderingEnabled];
-[FigCaptureSessionConfiguration sessionPreset];
-[FigCaptureSessionConfiguration sinkConfigurations];
-[FigCaptureSessionConfiguration checkIfFileAlreadyExistForMFO];
-[FigCaptureSessionConfiguration setTccIdentity:];
-[FigCaptureSessionConfiguration tccIdentity];
-[FigCaptureSessionConfiguration reasonForNotEqualingConfigurationIgnoringConfigurationID:];
-[FigCaptureSessionConfiguration removeConnectionConfiguration:];
-[FigCaptureSessionConfiguration init];
-[FigCaptureSessionConfiguration setConfigurationID:];
-[FigCaptureSessionConfiguration textureStyle];
-[FigCaptureSessionConfiguration clientExpectsCameraMountedInLandscapeOrientation];
-[FigCaptureSessionConfiguration smartStyle];
-[FigCaptureSessionConfiguration smartStyleControlMode];
-[FigCaptureSessionConfiguration automaticallyRunsDeferredStart];
-[FigCaptureSessionConfiguration setMultiCamSession:];
-[FigCaptureSessionConfiguration allCameraSourcesAreMetadataCameras];
-[FigCaptureSessionConfiguration setSmartStyle:];
-[FigCaptureSessionConfiguration configurationID];
-[FigCaptureSessionConfiguration dealloc];
-[FigCaptureSessionConfiguration configuresAppAudioSession];
-[FigCaptureSessionConfiguration suppressVideoEffects];
-[FigCaptureSessionConfiguration setClientIsVOIP:];
-[FigCaptureSessionConfiguration setCheckIfFileAlreadyExistForMFO:];
-[FigCaptureSessionConfiguration briefDescription];
-[FigCaptureSessionConfiguration setConfiguresAppAudioSessionForBluetoothHighQualityRecording:];
-[FigCaptureSessionConfiguration setTextureStyleEnabled:];
-[FigCaptureSessionConfiguration textureStyleEnabled];
-[FigCaptureSessionConfiguration setUsesAppAudioSession:];
-[FigCaptureSessionConfiguration setXctestAuthorizedToStealDevice:];
-[FigCaptureSessionConfiguration setTextureStyle:];
-[FigCaptureSessionConfiguration eligibleToAttachToExistingCaptureSession];
-[FigCaptureSessionConfiguration continuityCameraClientDeviceClass];
-[FigCaptureSessionConfiguration setConfiguresAppAudioSession:];
-[FigCaptureSessionConfiguration setAllowedToRunInMultitaskingMode:];
-[FigCaptureSessionConfiguration usesAppAudioSession];
-[FigCaptureSessionConfiguration setClientSDKVersionToken:];
-[FigCaptureSessionConfiguration clientSDKVersionToken];
-[FigCaptureSessionConfiguration sourceConfigurations];
-[FigCaptureSessionConfiguration connectionConfigurations];
-[FigCaptureSessionConfiguration initWithXPCEncoding:clientAuditToken:];
-[FigCaptureSessionConfiguration allowedToRunInMultitaskingMode];
-[FigCaptureSessionConfiguration addConnectionConfiguration:];
-[FigCaptureSessionConfiguration copyXPCEncoding];
-[FigCaptureSessionConfiguration description];
-[FigCaptureSessionConfiguration setAutomaticallyRunsDeferredStart:];
-[FigCaptureSessionConfiguration initWithXPCEncoding:];
-[FigCaptureSessionConfiguration setSessionPreset:];
-[FigCaptureSessionConfiguration configuresAppAudioSessionForBluetoothHighQualityRecording];
-[FigCaptureSessionConfiguration coexistenceWithInfraredSourceEnabled];
-[FigCaptureSessionConfiguration supportsAttachingSessionConfiguration:];
-[FigCaptureSessionConfiguration copyWithZone:];
-[FigCaptureSessionConfiguration isEqual:];
-[FigCaptureSessionConfiguration setSuppressVideoEffects:];
-[FigCaptureSessionConfiguration xctestAuthorizedToStealDevice];
-[FigCaptureSessionConfiguration setClientExpectsCameraMountedInLandscapeOrientation:];
-[FigCaptureSessionConfiguration setConfiguresAppAudioSessionToMixWithOthers:];
```
