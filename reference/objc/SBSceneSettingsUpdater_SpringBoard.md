# `SBSceneSettingsUpdater`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 14 properties, 31 instance methods, 7 class methods

## Instance variables

```
@"NSString" _traitsRole;
@"TRAParticipant" _traitsParticipant;
@"NSHashTable" _observers;
B _updatesGeometry;
@"FBScene" _scene;
@"NSString" _scenePersistentIdentifier;
@"SBTraitsSceneParticipantDelegate" _sceneTraitsDelegate;
@"FBSDisplayConfiguration" _displayConfiguration;
q _orientationModeOverride;
Q _initialSupportedInterfaceOrientations;
Q _supportedInterfaceOrientationsOverride;
```

## Properties

```
@property (T@"FBScene",R,W,N,V_scene) scene;
@property (T@"NSString",R,C,N,V_scenePersistentIdentifier) scenePersistentIdentifier;
@property (T@"SBTraitsSceneParticipantDelegate",R,N,V_sceneTraitsDelegate) sceneTraitsDelegate;
@property (TB,R,N,GisActive) active;
@property (TB,R,N,V_updatesGeometry) updatesGeometry;
@property (T@"FBSDisplayConfiguration",&,N,V_displayConfiguration) displayConfiguration;
@property (T@"BSCornerRadiusConfiguration",&,N) cornerRadiusConfiguration;
@property (T@"NSString",&,N) traitsRole;
@property (TB,N,GisForeground) foreground;
@property (Td,N) level;
@property (TB,N,GisEnhancedWindowingModeEnabled) enhancedWindowingModeEnabled;
@property (Tq,N,V_orientationModeOverride) orientationModeOverride;
@property (TQ,N,V_initialSupportedInterfaceOrientations) initialSupportedInterfaceOrientations;
@property (TQ,N,V_supportedInterfaceOrientationsOverride) supportedInterfaceOrientationsOverride;
```

## Class methods

```
+[SBSceneSettingsUpdater safeUpdateScene:withSceneLevel:];
+[SBSceneSettingsUpdater __updateSceneInsetSettings:forDisplayConfiguration:];
+[SBSceneSettingsUpdater __updateSceneSettings:forDisplayConfiguration:updateGeometry:];
+[SBSceneSettingsUpdater safeUpdateScene:withBlock:];
+[SBSceneSettingsUpdater safeUpdateScene:withDisplayConfiguration:];
+[SBSceneSettingsUpdater safeUpdateScene:withDisplayConfiguration:updateGeometry:];
+[SBSceneSettingsUpdater safeUpdateScene:withUserInterfaceStyle:];
```

## Instance methods

```
-[SBSceneSettingsUpdater setTraitsParticipantNeedsPreferencesUpdateWithReason:];
-[SBSceneSettingsUpdater setForeground:];
-[SBSceneSettingsUpdater cornerRadiusConfiguration];
-[SBSceneSettingsUpdater displayConfiguration];
-[SBSceneSettingsUpdater sceneTraitsDelegate];
-[SBSceneSettingsUpdater initialSupportedInterfaceOrientations];
-[SBSceneSettingsUpdater setInitialSupportedInterfaceOrientations:];
-[SBSceneSettingsUpdater setCornerRadiusConfiguration:];
-[SBSceneSettingsUpdater orientationModeOverride];
-[SBSceneSettingsUpdater setEnhancedWindowingModeEnabled:];
-[SBSceneSettingsUpdater setOrientationModeOverride:];
-[SBSceneSettingsUpdater dealloc];
-[SBSceneSettingsUpdater scenePersistentIdentifier];
-[SBSceneSettingsUpdater level];
-[SBSceneSettingsUpdater traitsRole];
-[SBSceneSettingsUpdater isEnhancedWindowingModeEnabled];
-[SBSceneSettingsUpdater isForeground];
-[SBSceneSettingsUpdater setDisplayConfiguration:];
-[SBSceneSettingsUpdater supportedInterfaceOrientationsOverride];
-[SBSceneSettingsUpdater addObserver:];
-[SBSceneSettingsUpdater setLevel:];
-[SBSceneSettingsUpdater setSupportedInterfaceOrientationsOverride:];
-[SBSceneSettingsUpdater scene];
-[SBSceneSettingsUpdater _setPersistenceIdentifier:];
-[SBSceneSettingsUpdater __setupTraitsParticipantWithRole:displayIdentity:];
-[SBSceneSettingsUpdater updatesGeometry];
-[SBSceneSettingsUpdater isActive];
-[SBSceneSettingsUpdater initWithScene:persistentIdentifier:level:updatesGeometry:];
-[SBSceneSettingsUpdater _createTraitsParticipantIfNeededWithRole:];
-[SBSceneSettingsUpdater setActive:withTransitionContext:];
-[SBSceneSettingsUpdater setTraitsRole:];
```
