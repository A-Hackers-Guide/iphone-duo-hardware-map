# `SBSystemUIScenesCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFSceneWorkspaceControlling`, `SBWindowSceneAttachmentObserving`
- 25 instance variables, 27 properties, 60 instance methods, 9 class methods

## Instance variables

```
@"NSMutableArray" _sceneControllers;
@"NSMutableArray" _allKnownProcessIdentities;
@"SBAccessibilityUIServerUISceneController" _accessibilityUIServerUISceneController;
@"SBAssistiveTouchUISceneController" _assistiveTouchUISceneController;
@"SBCameraOverlayUISceneController" _cameraOverlayUISceneController;
@"SBDisplayYoinkingUISceneController" _displayYoinkingUISceneController;
@"SBDruidUISceneController" _druidUISceneController;
@"SBEnsembleUISceneController" _ensembleUISceneController;
@"SBEyedropperUISceneController" _eyedropperUISceneController;
@"SBFullKeyboardAccessUISceneController" _fullKeyboardAccessUISceneController;
@"SBInputUISceneController" _inputUISceneController;
@"SBInternalPerfPowerHUDSceneController" _internalPerfPowerHUDUISceneController;
@"SBMomentsUISceneController" _momentsUISceneController;
@"SBOverlayUISceneController" _overlayUISceneController;
@"SBPerfPowerHUDSceneController" _perfPowerHUDUISceneController;
@"SBAudioHUDSceneController" _audioHUDUISceneController;
@"SBVoiceControlUISceneController" _voiceControlUISceneController;
@"SBProximityReaderUISceneController" _proximityReaderUISceneController;
@"SBMagnifierUISceneController" _magnifierUISceneController;
@"SBSiriHUDSceneController" _siriHUDSceneController;
@"SBAssistantIslandStageCoordinator" _assistantIslandStageCoordinator;
@"SBScreenSharingOverlayUISceneController" _screenSharingOverlayUISceneController;
@"SBGlitchHUDSceneController" _glitchHUDUISceneController;
@"SBAudioHUDSceneController" _audioHUDSceneController;
@"SBPrototypeToolsSceneController" _prototypeToolsSceneController;
```

## Properties

```
@property (T@"SBAccessibilityUIServerUISceneController",&,N,V_accessibilityUIServerUISceneController) accessibilityUIServerUISceneController;
@property (T@"SBAssistiveTouchUISceneController",&,N,V_assistiveTouchUISceneController) assistiveTouchUISceneController;
@property (T@"SBCameraOverlayUISceneController",&,N,V_cameraOverlayUISceneController) cameraOverlayUISceneController;
@property (T@"SBDisplayYoinkingUISceneController",&,N,V_displayYoinkingUISceneController) displayYoinkingUISceneController;
@property (T@"SBDruidUISceneController",&,N,V_druidUISceneController) druidUISceneController;
@property (T@"SBEnsembleUISceneController",&,N,V_ensembleUISceneController) ensembleUISceneController;
@property (T@"SBEyedropperUISceneController",&,N,V_eyedropperUISceneController) eyedropperUISceneController;
@property (T@"SBPerfPowerHUDSceneController",&,N,V_perfPowerHUDUISceneController) perfPowerHUDUISceneController;
@property (T@"SBInternalPerfPowerHUDSceneController",&,N,V_internalPerfPowerHUDUISceneController) internalPerfPowerHUDUISceneController;
@property (T@"SBGlitchHUDSceneController",&,N,V_glitchHUDUISceneController) glitchHUDUISceneController;
@property (T@"SBAudioHUDSceneController",&,N,V_audioHUDSceneController) audioHUDSceneController;
@property (T@"SBFullKeyboardAccessUISceneController",&,N,V_fullKeyboardAccessUISceneController) fullKeyboardAccessUISceneController;
@property (T@"SBInputUISceneController",&,N,V_inputUISceneController) inputUISceneController;
@property (T@"SBMomentsUISceneController",&,N,V_momentsUISceneController) momentsUISceneController;
@property (T@"SBOverlayUISceneController",&,N,V_overlayUISceneController) overlayUISceneController;
@property (T@"SBVoiceControlUISceneController",&,N,V_voiceControlUISceneController) voiceControlUISceneController;
@property (T@"SBProximityReaderUISceneController",&,N,V_proximityReaderUISceneController) proximityReaderUISceneController;
@property (T@"SBMagnifierUISceneController",&,N,V_magnifierUISceneController) magnifierUISceneController;
@property (T@"SBPrototypeToolsSceneController",&,N,V_prototypeToolsSceneController) prototypeToolsSceneController;
@property (T@"SBSiriHUDSceneController",&,N,V_siriHUDSceneController) siriHUDSceneController;
@property (T@"SBAssistantIslandStageCoordinator",&,N,V_assistantIslandStageCoordinator) assistantIslandStageCoordinator;
@property (T@"SBScreenSharingOverlayUISceneController",&,N,V_screenSharingOverlayUISceneController) screenSharingOverlayUISceneController;
@property (T@"SBAudioHUDSceneController",R,N,V_audioHUDUISceneController) audioHUDUISceneController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSystemUIScenesCoordinator _sceneControllersConfigurations];
+[SBSystemUIScenesCoordinator _configurationForSystemUISceneSessionRoles];
+[SBSystemUIScenesCoordinator _isSystemUISceneBoundClient:];
+[SBSystemUIScenesCoordinator _isSystemUISceneBoundClientHandlingNewSceneRequests:];
+[SBSystemUIScenesCoordinator _isSystemUISceneDynamicClient:withSceneRequestOptions:];
+[SBSystemUIScenesCoordinator _systemUISceneBoundProcessIdentities];
+[SBSystemUIScenesCoordinator _systemUISceneBoundProcessIdentitiesSupportingNewSceneRequests];
+[SBSystemUIScenesCoordinator _systemUISceneSessionRoles];
+[SBSystemUIScenesCoordinator shouldHandleSceneRequestsForProcess:withOptions:];
```

## Instance methods

```
-[SBSystemUIScenesCoordinator enumerateScenesWithBlock:];
-[SBSystemUIScenesCoordinator destroyScenesWithPersistentIdentifiers:processIdentity:completion:];
-[SBSystemUIScenesCoordinator setVoiceControlUISceneController:];
-[SBSystemUIScenesCoordinator _willEnableSecureRendering:];
-[SBSystemUIScenesCoordinator momentsUISceneController];
-[SBSystemUIScenesCoordinator setMomentsUISceneController:];
-[SBSystemUIScenesCoordinator _createSystemUISceneControllerForConfiguration:];
-[SBSystemUIScenesCoordinator assistiveTouchUISceneController];
-[SBSystemUIScenesCoordinator setScreenSharingOverlayUISceneController:];
-[SBSystemUIScenesCoordinator setMagnifierUISceneController:];
-[SBSystemUIScenesCoordinator accessibilityUIServerUISceneController];
-[SBSystemUIScenesCoordinator displayYoinkingUISceneController];
-[SBSystemUIScenesCoordinator setGlitchHUDUISceneController:];
-[SBSystemUIScenesCoordinator init];
-[SBSystemUIScenesCoordinator windowSceneDidDisconnect:];
-[SBSystemUIScenesCoordinator setOverlayUISceneController:];
-[SBSystemUIScenesCoordinator setDruidUISceneController:];
-[SBSystemUIScenesCoordinator cameraOverlayUISceneController];
-[SBSystemUIScenesCoordinator prototypeToolsSceneController];
-[SBSystemUIScenesCoordinator dealloc];
-[SBSystemUIScenesCoordinator setAccessibilityUIServerUISceneController:];
-[SBSystemUIScenesCoordinator glitchHUDUISceneController];
-[SBSystemUIScenesCoordinator _createSceneWorkspaceControllerForProcessIdentity:jobLabel:options:];
-[SBSystemUIScenesCoordinator activateSceneForProcessIdentity:withHandle:options:completion:];
-[SBSystemUIScenesCoordinator setCameraOverlayUISceneController:];
-[SBSystemUIScenesCoordinator magnifierUISceneController];
-[SBSystemUIScenesCoordinator druidUISceneController];
-[SBSystemUIScenesCoordinator setProximityReaderUISceneController:];
-[SBSystemUIScenesCoordinator setDisplayYoinkingUISceneController:];
-[SBSystemUIScenesCoordinator proximityReaderUISceneController];
-[SBSystemUIScenesCoordinator setInternalPerfPowerHUDUISceneController:];
-[SBSystemUIScenesCoordinator setInputUISceneController:];
-[SBSystemUIScenesCoordinator sceneFromIdentityToken:];
-[SBSystemUIScenesCoordinator fullKeyboardAccessUISceneController];
-[SBSystemUIScenesCoordinator perfPowerHUDUISceneController];
-[SBSystemUIScenesCoordinator ensembleUISceneController];
-[SBSystemUIScenesCoordinator screenSharingOverlayUISceneController];
-[SBSystemUIScenesCoordinator inputUISceneController];
-[SBSystemUIScenesCoordinator setPerfPowerHUDUISceneController:];
-[SBSystemUIScenesCoordinator audioHUDUISceneController];
-[SBSystemUIScenesCoordinator eyedropperUISceneController];
-[SBSystemUIScenesCoordinator setAssistiveTouchUISceneController:];
-[SBSystemUIScenesCoordinator setFullKeyboardAccessUISceneController:];
-[SBSystemUIScenesCoordinator setPrototypeToolsSceneController:];
-[SBSystemUIScenesCoordinator siriHUDSceneController];
-[SBSystemUIScenesCoordinator setAssistantIslandStageCoordinator:];
-[SBSystemUIScenesCoordinator internalPerfPowerHUDUISceneController];
-[SBSystemUIScenesCoordinator _didDisableSecureRendering:];
-[SBSystemUIScenesCoordinator setEyedropperUISceneController:];
-[SBSystemUIScenesCoordinator _levelForClientConfiguration:];
-[SBSystemUIScenesCoordinator setAudioHUDSceneController:];
-[SBSystemUIScenesCoordinator windowSceneDidConnect:];
-[SBSystemUIScenesCoordinator sceneWorkspaceControllerForProcessIdentity:];
-[SBSystemUIScenesCoordinator assistantIslandStageCoordinator];
-[SBSystemUIScenesCoordinator audioHUDSceneController];
-[SBSystemUIScenesCoordinator setSiriHUDSceneController:];
-[SBSystemUIScenesCoordinator sceneFromIdentityTokenStringRepresentation:];
-[SBSystemUIScenesCoordinator voiceControlUISceneController];
-[SBSystemUIScenesCoordinator overlayUISceneController];
-[SBSystemUIScenesCoordinator setEnsembleUISceneController:];
```
