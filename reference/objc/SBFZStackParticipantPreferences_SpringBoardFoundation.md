# `SBFZStackParticipantPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionStreaming`
- 17 instance variables, 20 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _policyPreferencesByPolicyClass;
B _suppressSystemApertureForSystemChromeSuppression;
q _activationPolicyForParticipantsBelow;
@"NSIndexSet" _assertIsAboveParticipantIdentifiers;
q _homeGestureConsumption;
q _homeAffordanceDrawingSuppression;
@"NSSet" _associatedBundleIdentifiersToSuppressInSystemAperture;
@"NSSet" _associatedSceneIdentifiersToSuppressInSystemAperture;
@"NSArray" _physicalButtonSceneTargets;
@"NSArray" _captureButtonFullFidelityEventRequestingScenes;
@"NSArray" _foregroundCaptureSceneTargets;
@"NSSet" _audioCategoriesDisablingVolumeHUD;
q _allowsDimmingWhenForegroundInactive;
q _allowsKeyboardArbiterToDetermineFocusTarget;
@"SBKeyboardFocusTarget" _overrideKeyboardFocusTarget;
q _allowCameraButtonDeferringWhileFocusLocked;
@"SBFZStackParticipant" _updatingParticipant;
```

## Properties

```
@property (T@"SBFZStackParticipant",W,N,G_updatingParticipant,S_setUpdatingParticipant:,V_updatingParticipant) updatingParticipant;
@property (Tq,N,V_activationPolicyForParticipantsBelow) activationPolicyForParticipantsBelow;
@property (T@"NSIndexSet",C,N,V_assertIsAboveParticipantIdentifiers) assertIsAboveParticipantIdentifiers;
@property (Tq,N,V_homeGestureConsumption) homeGestureConsumption;
@property (Tq,N,V_homeAffordanceDrawingSuppression) homeAffordanceDrawingSuppression;
@property (TB,N,V_suppressSystemApertureForSystemChromeSuppression) suppressSystemApertureForSystemChromeSuppression;
@property (T@"NSSet",C,N,V_associatedBundleIdentifiersToSuppressInSystemAperture) associatedBundleIdentifiersToSuppressInSystemAperture;
@property (T@"NSSet",C,N,V_associatedSceneIdentifiersToSuppressInSystemAperture) associatedSceneIdentifiersToSuppressInSystemAperture;
@property (T@"NSArray",C,N,V_physicalButtonSceneTargets) physicalButtonSceneTargets;
@property (T@"NSArray",C,N,V_captureButtonFullFidelityEventRequestingScenes) captureButtonFullFidelityEventRequestingScenes;
@property (T@"NSArray",C,N,V_foregroundCaptureSceneTargets) foregroundCaptureSceneTargets;
@property (T@"NSSet",C,N,V_audioCategoriesDisablingVolumeHUD) audioCategoriesDisablingVolumeHUD;
@property (Tq,N,V_allowsDimmingWhenForegroundInactive) allowsDimmingWhenForegroundInactive;
@property (Tq,N,V_allowsKeyboardArbiterToDetermineFocusTarget) allowsKeyboardArbiterToDetermineFocusTarget;
@property (T@"SBKeyboardFocusTarget",&,N,V_overrideKeyboardFocusTarget) overrideKeyboardFocusTarget;
@property (Tq,N,V_allowCameraButtonDeferringWhileFocusLocked) allowCameraButtonDeferringWhileFocusLocked;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFZStackParticipantPreferences setAssociatedSceneIdentifiersToSuppressInSystemAperture:];
-[SBFZStackParticipantPreferences foregroundCaptureSceneTargets];
-[SBFZStackParticipantPreferences debugDescription];
-[SBFZStackParticipantPreferences physicalButtonSceneTargets];
-[SBFZStackParticipantPreferences setAssociatedBundleIdentifiersToSuppressInSystemAperture:];
-[SBFZStackParticipantPreferences _preferenceForPolicyClass:creatingIfNecessary:];
-[SBFZStackParticipantPreferences associatedSceneIdentifiersToSuppressInSystemAperture];
-[SBFZStackParticipantPreferences initInternal];
-[SBFZStackParticipantPreferences setAllowsKeyboardArbiterToDetermineFocusTarget:];
-[SBFZStackParticipantPreferences setCaptureButtonFullFidelityEventRequestingScenes:];
-[SBFZStackParticipantPreferences audioCategoriesDisablingVolumeHUD];
-[SBFZStackParticipantPreferences allowCameraButtonDeferringWhileFocusLocked];
-[SBFZStackParticipantPreferences setAllowCameraButtonDeferringWhileFocusLocked:];
-[SBFZStackParticipantPreferences _setUpdatingParticipant:];
-[SBFZStackParticipantPreferences homeAffordanceDrawingSuppression];
-[SBFZStackParticipantPreferences setAudioCategoriesDisablingVolumeHUD:];
-[SBFZStackParticipantPreferences overrideKeyboardFocusTarget];
-[SBFZStackParticipantPreferences homeGestureConsumption];
-[SBFZStackParticipantPreferences _describeDifferencesFromOriginal:differenceStream:];
-[SBFZStackParticipantPreferences allowsKeyboardArbiterToDetermineFocusTarget];
-[SBFZStackParticipantPreferences activationPolicyForParticipantsBelow];
-[SBFZStackParticipantPreferences associatedBundleIdentifiersToSuppressInSystemAperture];
-[SBFZStackParticipantPreferences succinctDescription];
-[SBFZStackParticipantPreferences allowsDimmingWhenForegroundInactive];
-[SBFZStackParticipantPreferences setSuppressSystemApertureForSystemChromeSuppression:];
-[SBFZStackParticipantPreferences setPhysicalButtonSceneTargets:];
-[SBFZStackParticipantPreferences setHomeGestureConsumption:];
-[SBFZStackParticipantPreferences setOverrideKeyboardFocusTarget:];
-[SBFZStackParticipantPreferences setHomeAffordanceDrawingSuppression:];
-[SBFZStackParticipantPreferences suppressSystemApertureForSystemChromeSuppression];
-[SBFZStackParticipantPreferences captureButtonFullFidelityEventRequestingScenes];
-[SBFZStackParticipantPreferences setForegroundCaptureSceneTargets:];
-[SBFZStackParticipantPreferences _appendBodyDescriptionToStream:];
-[SBFZStackParticipantPreferences description];
-[SBFZStackParticipantPreferences _setPolicyPreference:forPolicyClass:];
-[SBFZStackParticipantPreferences appendDescriptionToStream:];
-[SBFZStackParticipantPreferences _updatingParticipant];
-[SBFZStackParticipantPreferences copyWithZone:];
-[SBFZStackParticipantPreferences preferenceForPolicyClass:];
-[SBFZStackParticipantPreferences isEqual:];
-[SBFZStackParticipantPreferences setAllowsDimmingWhenForegroundInactive:];
-[SBFZStackParticipantPreferences setActivationPolicyForParticipantsBelow:];
-[SBFZStackParticipantPreferences setAssertIsAboveParticipantIdentifiers:];
-[SBFZStackParticipantPreferences assertIsAboveParticipantIdentifiers];
```
