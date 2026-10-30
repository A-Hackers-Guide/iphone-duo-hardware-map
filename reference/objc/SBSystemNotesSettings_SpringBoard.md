# `SBSystemNotesSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 8 instance variables, 8 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"SBSystemNotesAppearanceSettings" _appearanceSettings;
@"SBSystemNotesLaunchSettings" _launchSettings;
@"SBPIPStashVisualSettings" _stashVisualSettings;
@"SBPIPShadowSettings" _shadowSettings;
@"SBSystemNotesInteractionSettings" _interactionSettings;
@"SBSystemNotesSwipeMetricSettings" _cornerSwipeMetricSettings;
@"SBCornerPencilPanGestureSettings" _pencilSwipeGestureTuningSettings;
@"SBCornerFingerPanGestureSettings" _fingerSwipeGestureTuningSettings;
```

## Properties

```
@property (T@"SBSystemNotesAppearanceSettings",&,N,V_appearanceSettings) appearanceSettings;
@property (T@"SBSystemNotesLaunchSettings",&,N,V_launchSettings) launchSettings;
@property (T@"SBPIPStashVisualSettings",&,N,V_stashVisualSettings) stashVisualSettings;
@property (T@"SBPIPShadowSettings",&,N,V_shadowSettings) shadowSettings;
@property (T@"SBSystemNotesInteractionSettings",&,N,V_interactionSettings) interactionSettings;
@property (T@"SBSystemNotesSwipeMetricSettings",&,N,V_cornerSwipeMetricSettings) cornerSwipeMetricSettings;
@property (T@"SBCornerPencilPanGestureSettings",&,N,V_pencilSwipeGestureTuningSettings) pencilSwipeGestureTuningSettings;
@property (T@"SBCornerFingerPanGestureSettings",&,N,V_fingerSwipeGestureTuningSettings) fingerSwipeGestureTuningSettings;
```

## Class methods

```
+[SBSystemNotesSettings ignoresKey:];
+[SBSystemNotesSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemNotesSettings setDefaultValues];
-[SBSystemNotesSettings setShadowSettings:];
-[SBSystemNotesSettings shadowSettings];
-[SBSystemNotesSettings appearanceSettings];
-[SBSystemNotesSettings interactionSettings];
-[SBSystemNotesSettings launchSettings];
-[SBSystemNotesSettings cornerSwipeMetricSettings];
-[SBSystemNotesSettings fingerSwipeGestureTuningSettings];
-[SBSystemNotesSettings pencilSwipeGestureTuningSettings];
-[SBSystemNotesSettings setAppearanceSettings:];
-[SBSystemNotesSettings setCornerSwipeMetricSettings:];
-[SBSystemNotesSettings setFingerSwipeGestureTuningSettings:];
-[SBSystemNotesSettings setInteractionSettings:];
-[SBSystemNotesSettings setLaunchSettings:];
-[SBSystemNotesSettings setPencilSwipeGestureTuningSettings:];
-[SBSystemNotesSettings setStashVisualSettings:];
-[SBSystemNotesSettings stashVisualSettings];
```
