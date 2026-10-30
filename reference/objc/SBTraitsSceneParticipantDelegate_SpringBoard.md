# `SBTraitsSceneParticipantDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `SBSceneHandleObserver`, `BSInvalidatable`, `SBTraitsParticipantDelegate`, `SBTraitsSceneSettingsUpdater`
- 23 instance variables, 22 properties, 72 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"SBTraitsSceneOrientationRequestsAssistant" _orientationRequestActionAssistant;
@"UIApplicationSceneClientSettingsDiffInspector" _sceneClientSettingsDiffInspector;
@"NSDictionary" _bundleOrientationProperties;
@"BKSAnimationFenceHandle" _fallbackFence_90210730;
@"NSMutableDictionary" _orientationModeForDisplayIdentities;
B _needsActuationForDisplayIdentityChange;
B _canDetermineActiveOrientation;
B _canDetermineKeyboardOrientation;
B _orientationActuationEnabled;
B _orientationActuationAnimatable;
@"FBScene" _scene;
@"SBSceneHandle" _sceneHandle;
@"TRAArbiter" _arbiter;
@"TRAParticipant" _participant;
@"NSNumber" _preferredSceneLevel;
q _orientationModeOverride;
Q _initialSupportedOrientationsOverride;
Q _supportedOrientationsOverride;
@"SBWindowScene" _orientationResolutionWindowScene;
@? _actuateZOrderAlongsideBlock;
@? _actuateOrientationAlongsideBlock;
@? _actuateOrientationSettingsAlongsideBlock;
```

## Properties

```
@property (TB,N,V_canDetermineActiveOrientation) canDetermineActiveOrientation;
@property (TB,N,V_canDetermineKeyboardOrientation) canDetermineKeyboardOrientation;
@property (T@"NSNumber",&,N,V_preferredSceneLevel) preferredSceneLevel;
@property (TB,N,GisOrientationActuationEnabled,V_orientationActuationEnabled) orientationActuationEnabled;
@property (TB,N,GisOrientationActuationAnimatable,V_orientationActuationAnimatable) orientationActuationAnimatable;
@property (Tq,N,V_orientationModeOverride) orientationModeOverride;
@property (TQ,N,V_initialSupportedOrientationsOverride) initialSupportedOrientationsOverride;
@property (TQ,N,V_supportedOrientationsOverride) supportedOrientationsOverride;
@property (T@"SBWindowScene",W,N,V_orientationResolutionWindowScene) orientationResolutionWindowScene;
@property (T@?,C,N,V_actuateZOrderAlongsideBlock) actuateZOrderAlongsideBlock;
@property (T@?,C,N,V_actuateOrientationAlongsideBlock) actuateOrientationAlongsideBlock;
@property (T@?,C,N,V_actuateOrientationSettingsAlongsideBlock) actuateOrientationSettingsAlongsideBlock;
@property (T@"FBScene",W,N,V_scene) scene;
@property (T@"SBSceneHandle",W,N,V_sceneHandle) sceneHandle;
@property (T@"TRAArbiter",W,N,V_arbiter) arbiter;
@property (T@"TRAParticipant",W,N,V_participant) participant;
@property (Tq,R,N) sceneCurrentOrientation;
@property (TB,R,N) scenePrefersOrientationLocked;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsSceneParticipantDelegate sceneHandle:didDestroyScene:];
-[SBTraitsSceneParticipantDelegate sceneHandle:didCreateScene:];
-[SBTraitsSceneParticipantDelegate actuateOrientationSettingsWithContext:];
-[SBTraitsSceneParticipantDelegate actuateOrientationAlongsideBlock];
-[SBTraitsSceneParticipantDelegate updatePreferencesWithUpdater:];
-[SBTraitsSceneParticipantDelegate sceneHandle];
-[SBTraitsSceneParticipantDelegate canDetermineActiveOrientation];
-[SBTraitsSceneParticipantDelegate participant];
-[SBTraitsSceneParticipantDelegate initialSupportedOrientationsOverride];
-[SBTraitsSceneParticipantDelegate isOrientationActuationEnabled];
-[SBTraitsSceneParticipantDelegate setActuateOrientationAlongsideBlock:];
-[SBTraitsSceneParticipantDelegate lazyOrientationRequestActionAssistant];
-[SBTraitsSceneParticipantDelegate setScene:];
-[SBTraitsSceneParticipantDelegate orientationModeOverride];
-[SBTraitsSceneParticipantDelegate _displayConfigurationForOrientationResolutionWithProposedConfiguration:];
-[SBTraitsSceneParticipantDelegate setCanDetermineKeyboardOrientation:];
-[SBTraitsSceneParticipantDelegate setOrientationModeOverride:];
-[SBTraitsSceneParticipantDelegate preferredSceneLevel];
-[SBTraitsSceneParticipantDelegate dealloc];
-[SBTraitsSceneParticipantDelegate _orientationModeForDisplayConfiguration:windowScene:];
-[SBTraitsSceneParticipantDelegate sceneContentStateDidChange:];
-[SBTraitsSceneParticipantDelegate arbiter];
-[SBTraitsSceneParticipantDelegate initWithSceneHandle:];
-[SBTraitsSceneParticipantDelegate didChangeSettingsForParticipant:context:];
-[SBTraitsSceneParticipantDelegate _isAllowedToHavePortraitUpsideDownInWindowScene:];
-[SBTraitsSceneParticipantDelegate updatePreferencesForParticipant:updater:];
-[SBTraitsSceneParticipantDelegate initWithScene:];
-[SBTraitsSceneParticipantDelegate _angleFromScreenReferenceSpaceForSettings:displayIdentity:];
-[SBTraitsSceneParticipantDelegate _bestGuessSupportedInterfaceOrientationsForWindowScene:];
-[SBTraitsSceneParticipantDelegate invalidate];
-[SBTraitsSceneParticipantDelegate setSupportedOrientationsOverride:];
-[SBTraitsSceneParticipantDelegate actuateUserInterfaceStyleSettingsWithContext:];
-[SBTraitsSceneParticipantDelegate setActuateOrientationSettingsAlongsideBlock:];
-[SBTraitsSceneParticipantDelegate setOrientationActuationAnimatable:];
-[SBTraitsSceneParticipantDelegate supportedOrientationsOverride];
-[SBTraitsSceneParticipantDelegate setPreferredSceneLevel:];
-[SBTraitsSceneParticipantDelegate scene];
-[SBTraitsSceneParticipantDelegate scenePrefersOrientationLocked];
-[SBTraitsSceneParticipantDelegate updateOrientationSceneSettingsForParticipant:];
-[SBTraitsSceneParticipantDelegate participantCanDetermineKeyboardOrientation:];
-[SBTraitsSceneParticipantDelegate canDetermineKeyboardOrientation];
-[SBTraitsSceneParticipantDelegate setActuateZOrderAlongsideBlock:];
-[SBTraitsSceneParticipantDelegate _allLegalOrientationsForWindowScene:];
-[SBTraitsSceneParticipantDelegate _evaluateOrientationTransitionContext:];
-[SBTraitsSceneParticipantDelegate _application];
-[SBTraitsSceneParticipantDelegate actuateZOrderAlongsideBlock];
-[SBTraitsSceneParticipantDelegate description];
-[SBTraitsSceneParticipantDelegate actuateZOrderLevelSettings];
-[SBTraitsSceneParticipantDelegate setArbiter:];
-[SBTraitsSceneParticipantDelegate _bestGuessDisplayConfiguration];
-[SBTraitsSceneParticipantDelegate needsActuationForUpdateReasons:];
-[SBTraitsSceneParticipantDelegate appendDescriptionForParticipant:withBuilder:multilinePrefix:];
-[SBTraitsSceneParticipantDelegate participantAssociatedSceneIdentityTokens:];
-[SBTraitsSceneParticipantDelegate _canActuateHostedSceneSettings];
-[SBTraitsSceneParticipantDelegate _hostReferenceAngleModeForDisplayIdentity:];
-[SBTraitsSceneParticipantDelegate orientationResolutionWindowScene];
-[SBTraitsSceneParticipantDelegate _sanitizedMask:forApplication:windowScene:];
-[SBTraitsSceneParticipantDelegate setOrientationActuationEnabled:];
-[SBTraitsSceneParticipantDelegate setSceneHandle:];
-[SBTraitsSceneParticipantDelegate _resetToInitialState];
-[SBTraitsSceneParticipantDelegate _supportedOrientations];
-[SBTraitsSceneParticipantDelegate sceneCurrentOrientation];
-[SBTraitsSceneParticipantDelegate actuateOrientationSettingsAlongsideBlock];
-[SBTraitsSceneParticipantDelegate _preferredOrientation];
-[SBTraitsSceneParticipantDelegate setCanDetermineActiveOrientation:];
-[SBTraitsSceneParticipantDelegate participantWillInvalidate:];
-[SBTraitsSceneParticipantDelegate isOrientationActuationAnimatable];
-[SBTraitsSceneParticipantDelegate scene:didUpdateClientSettings:];
-[SBTraitsSceneParticipantDelegate setInitialSupportedOrientationsOverride:];
-[SBTraitsSceneParticipantDelegate setParticipant:];
-[SBTraitsSceneParticipantDelegate updateOrientationLockGrantedIfNeeded:];
-[SBTraitsSceneParticipantDelegate setOrientationResolutionWindowScene:];
```
