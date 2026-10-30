# `SBFZStackParticipant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionStreaming`, `SBFZStackParticipantSettings`, `SBFZStackResolvedPolicyProvider`
- 19 instance variables, 23 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _ownsHomeGesture;
B _homeAffordanceDrawingSuppressed;
B _systemApertureSuppressedForSystemChromeSuppression;
B _participantBelowAllowsDimming;
B _allowsKeyboardArbiterToDetermineFocusTarget;
B _allowCameraButtonDeferringWhileFocusLocked;
q _identifier;
@"NSUUID" _UUID;
@"<SBFZStackParticipantDelegate>" _delegate;
q _activationState;
@"NSSet" _associatedBundleIdentifiersToSuppressInSystemAperture;
@"NSSet" _associatedSceneIdentifiersToSuppressInSystemAperture;
@"NSArray" _physicalButtonSceneTargets;
@"NSArray" _captureButtonFullFidelityEventRequestingScenes;
@"NSArray" _foregroundCaptureSceneTargets;
@"NSSet" _audioCategoriesDisablingVolumeHUD;
@"SBKeyboardFocusTarget" _overrideKeyboardFocusTarget;
@"SBFZStackResolver" _resolver;
@"SBFZStackParticipantPreferences" _preferences;
```

## Properties

```
@property (Tq,N,V_activationState) activationState;
@property (TB,N,V_ownsHomeGesture) ownsHomeGesture;
@property (TB,N,V_homeAffordanceDrawingSuppressed) homeAffordanceDrawingSuppressed;
@property (TB,N,V_systemApertureSuppressedForSystemChromeSuppression) systemApertureSuppressedForSystemChromeSuppression;
@property (T@"NSSet",C,N,V_associatedBundleIdentifiersToSuppressInSystemAperture) associatedBundleIdentifiersToSuppressInSystemAperture;
@property (T@"NSSet",C,N,V_associatedSceneIdentifiersToSuppressInSystemAperture) associatedSceneIdentifiersToSuppressInSystemAperture;
@property (T@"NSArray",C,N,V_physicalButtonSceneTargets) physicalButtonSceneTargets;
@property (T@"NSArray",C,N,V_captureButtonFullFidelityEventRequestingScenes) captureButtonFullFidelityEventRequestingScenes;
@property (T@"NSArray",C,N,V_foregroundCaptureSceneTargets) foregroundCaptureSceneTargets;
@property (T@"NSSet",C,N,V_audioCategoriesDisablingVolumeHUD) audioCategoriesDisablingVolumeHUD;
@property (TB,N,V_participantBelowAllowsDimming) participantBelowAllowsDimming;
@property (TB,N,V_allowsKeyboardArbiterToDetermineFocusTarget) allowsKeyboardArbiterToDetermineFocusTarget;
@property (T@"SBKeyboardFocusTarget",&,N,V_overrideKeyboardFocusTarget) overrideKeyboardFocusTarget;
@property (TB,N,V_allowCameraButtonDeferringWhileFocusLocked) allowCameraButtonDeferringWhileFocusLocked;
@property (T@"SBFZStackResolver",W,N,V_resolver) resolver;
@property (T@"SBFZStackParticipantPreferences",C,N,V_preferences) preferences;
@property (Tq,R,N,V_identifier) identifier;
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (T@"<SBFZStackParticipantDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFZStackParticipant resolver];
-[SBFZStackParticipant setParticipantBelowAllowsDimming:];
-[SBFZStackParticipant setNeedsUpdateZOrderPreferencesWithReason:];
-[SBFZStackParticipant setAssociatedSceneIdentifiersToSuppressInSystemAperture:];
-[SBFZStackParticipant foregroundCaptureSceneTargets];
-[SBFZStackParticipant ownsHomeGesture];
-[SBFZStackParticipant debugDescription];
-[SBFZStackParticipant setResolver:];
-[SBFZStackParticipant physicalButtonSceneTargets];
-[SBFZStackParticipant identifier];
-[SBFZStackParticipant setPreferences:];
-[SBFZStackParticipant setAssociatedBundleIdentifiersToSuppressInSystemAperture:];
-[SBFZStackParticipant _updatePreferencesNotifyingResolver:];
-[SBFZStackParticipant associatedSceneIdentifiersToSuppressInSystemAperture];
-[SBFZStackParticipant systemApertureSuppressedForSystemChromeSuppression];
-[SBFZStackParticipant setAllowsKeyboardArbiterToDetermineFocusTarget:];
-[SBFZStackParticipant UUID];
-[SBFZStackParticipant preferences];
-[SBFZStackParticipant setCaptureButtonFullFidelityEventRequestingScenes:];
-[SBFZStackParticipant audioCategoriesDisablingVolumeHUD];
-[SBFZStackParticipant allowCameraButtonDeferringWhileFocusLocked];
-[SBFZStackParticipant setAllowCameraButtonDeferringWhileFocusLocked:];
-[SBFZStackParticipant setAudioCategoriesDisablingVolumeHUD:];
-[SBFZStackParticipant overrideKeyboardFocusTarget];
-[SBFZStackParticipant allowsKeyboardArbiterToDetermineFocusTarget];
-[SBFZStackParticipant associatedBundleIdentifiersToSuppressInSystemAperture];
-[SBFZStackParticipant succinctDescription];
-[SBFZStackParticipant invalidate];
-[SBFZStackParticipant setPhysicalButtonSceneTargets:];
-[SBFZStackParticipant setOverrideKeyboardFocusTarget:];
-[SBFZStackParticipant homeAffordanceDrawingSuppressed];
-[SBFZStackParticipant captureButtonFullFidelityEventRequestingScenes];
-[SBFZStackParticipant setForegroundCaptureSceneTargets:];
-[SBFZStackParticipant setSystemApertureSuppressedForSystemChromeSuppression:];
-[SBFZStackParticipant setActivationState:];
-[SBFZStackParticipant setNeedsUpdatePreferencesWithReason:];
-[SBFZStackParticipant setOwnsHomeGesture:];
-[SBFZStackParticipant delegate];
-[SBFZStackParticipant setHomeAffordanceDrawingSuppressed:];
-[SBFZStackParticipant description];
-[SBFZStackParticipant initWithIdentifier:delegate:];
-[SBFZStackParticipant activationState];
-[SBFZStackParticipant appendDescriptionToStream:];
-[SBFZStackParticipant participantBelowAllowsDimming];
-[SBFZStackParticipant copyWithZone:];
-[SBFZStackParticipant _updatePreferences];
```
