# `SBFZStackParticipantSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 14 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) activationState;
@property (TB,R,N) ownsHomeGesture;
@property (TB,R,N) homeAffordanceDrawingSuppressed;
@property (TB,R,N) systemApertureSuppressedForSystemChromeSuppression;
@property (T@"NSSet",R,C,N) associatedBundleIdentifiersToSuppressInSystemAperture;
@property (T@"NSSet",R,C,N) associatedSceneIdentifiersToSuppressInSystemAperture;
@property (T@"NSArray",R,C,N) physicalButtonSceneTargets;
@property (T@"NSArray",R,C,N) captureButtonFullFidelityEventRequestingScenes;
@property (T@"NSArray",R,C,N) foregroundCaptureSceneTargets;
@property (T@"NSSet",R,C,N) audioCategoriesDisablingVolumeHUD;
@property (TB,R,N) participantBelowAllowsDimming;
@property (TB,R,N) allowsKeyboardArbiterToDetermineFocusTarget;
@property (T@"SBKeyboardFocusTarget",R,N) overrideKeyboardFocusTarget;
@property (TB,R,N) allowCameraButtonDeferringWhileFocusLocked;
```

## Instance methods

```
-[SBFZStackParticipantSettings foregroundCaptureSceneTargets];
-[SBFZStackParticipantSettings ownsHomeGesture];
-[SBFZStackParticipantSettings physicalButtonSceneTargets];
-[SBFZStackParticipantSettings associatedSceneIdentifiersToSuppressInSystemAperture];
-[SBFZStackParticipantSettings systemApertureSuppressedForSystemChromeSuppression];
-[SBFZStackParticipantSettings audioCategoriesDisablingVolumeHUD];
-[SBFZStackParticipantSettings allowCameraButtonDeferringWhileFocusLocked];
-[SBFZStackParticipantSettings overrideKeyboardFocusTarget];
-[SBFZStackParticipantSettings allowsKeyboardArbiterToDetermineFocusTarget];
-[SBFZStackParticipantSettings associatedBundleIdentifiersToSuppressInSystemAperture];
-[SBFZStackParticipantSettings homeAffordanceDrawingSuppressed];
-[SBFZStackParticipantSettings captureButtonFullFidelityEventRequestingScenes];
-[SBFZStackParticipantSettings activationState];
-[SBFZStackParticipantSettings participantBelowAllowsDimming];
```
