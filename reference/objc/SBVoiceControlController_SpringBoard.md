# `SBVoiceControlController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBVoiceControlTransientOverlayViewControllerDelegate`
- 11 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _delayedAssistantActivationPending;
B _headsetDownDelayedActionPerformed;
@"NSArray" _nextRecognitionAudioInputPaths;
@"SBVoiceControlTransientOverlayViewController" _transientOverlayViewController;
@"SiriLongPressButtonSource" _siriHeadsetDeviceSource;
@"<SiriAssertion>" _siriPreheatAssertion;
@"SBConferenceManager" _conferenceManager;
@"SBPolicyAggregator" _policyAggregator;
@"SBTelephonyManager" _telephonyManager;
@"SBTransientOverlayPresentationManager" _transientOverlayPresentationManager;
@"SBMainWorkspace" _workspace;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBVoiceControlController isVisible];
-[SBVoiceControlController _spokenLanguageDidChange:];
-[SBVoiceControlController bluetoothDeviceEndedVoiceControl:];
-[SBVoiceControlController bluetoothDeviceInitiatedVoiceControl:];
-[SBVoiceControlController _assistantActivationSettingsDidChange:];
-[SBVoiceControlController _cancelDelayedHeadsetAction];
-[SBVoiceControlController _newVoiceControlTransientOverlayViewControllerWithSource:];
-[SBVoiceControlController _performDelayedHeadsetActionForAssistant];
-[SBVoiceControlController _performDelayedHeadsetActionForVoiceControl];
-[SBVoiceControlController _prepareDelayedHeadsetAction];
-[SBVoiceControlController _shouldAllowSensitiveActionsInWindowScene:];
-[SBVoiceControlController _shouldEnterVoiceControl];
-[SBVoiceControlController _updateNextRecognitionAudioInputPaths:];
-[SBVoiceControlController dismissTransientOverlay];
-[SBVoiceControlController handleHeadsetButtonDownWithClickCount:];
-[SBVoiceControlController handleHeadsetButtonUp];
-[SBVoiceControlController handleHeadsetButtonUpNotInCall];
-[SBVoiceControlController handleHomeButtonHeld];
-[SBVoiceControlController headsetAvailabilityChanged];
-[SBVoiceControlController initWithConferenceManager:policyAggregator:telephonyManager:transientOverlayPresentationManager:workspace:];
-[SBVoiceControlController siriBluetoothDeviceSource:];
-[SBVoiceControlController voiceControlTransientOverlayViewControllerDidDisappear:];
-[SBVoiceControlController voiceControlTransientOverlayViewControllerRequestsDismissal:];
-[SBVoiceControlController voiceControlTransientOverlayViewControllerShouldAllowSensitiveActions:];
```
