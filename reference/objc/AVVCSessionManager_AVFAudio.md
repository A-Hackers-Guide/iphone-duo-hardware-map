# `AVVCSessionManager`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 36 instance variables, 14 properties, 85 instance methods, 0 class methods

## Instance variables

```
B mShouldDuckOthers;
B mIsMiniDuckingEnabled;
B mShouldEnableMiniDucking;
B mShouldDisableMiniDucking;
B mSessionNeedsVolumeControl;
B mSessionNeedsRoutingControl;
B mSessionOutputIsWirelessSplitter;
B mIsOtherAudioPlaying;
B mRouteHasDoAPSupport;
B mOutputSupportsSWVolume;
B mDeviceIsIOSAccessory;
B mDeviceIsOlderWatch;
I mSessionActivationOptions;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} mSessionManagerLock;
Q mPreviousHardwareControlFlags;
q mPreviousActivationMode;
@"NSString" mPreviousActivationDeviceUID;
@"NSString" mPreviousSessionCategory;
@"NSString" mPreviousSessionMode;
Q mPreviousSessionCategoryOptions;
i mPreviousIOBufferFrameSize;
B mEnableSmartRoutingConsideration;
B _isPrimary;
B _clientRequestsRecording;
B _forceGetSessionProperties;
i _sessionState;
f _deviceGain;
q _reporterID;
d _inputLatency;
d _outputLatency;
d _inputSafetyOffset;
d _outputSafetyOffset;
d _outputVolume;
q _currentActivationMode;
@"AVAudioSession" _audioSession;
@"NSString" _playbackRoute;
```

## Properties

```
@property (T@"AVAudioSession",&,N,V_audioSession) audioSession;
@property (Ti,N,V_sessionState) sessionState;
@property (TB,R,N,V_isPrimary) isPrimary;
@property (TB,N,V_clientRequestsRecording) clientRequestsRecording;
@property (Tf,N,V_deviceGain) deviceGain;
@property (T@"NSString",&,N,V_playbackRoute) playbackRoute;
@property (TB,N,V_forceGetSessionProperties) forceGetSessionProperties;
@property (Td,R,N,V_inputLatency) inputLatency;
@property (Td,R,N,V_outputLatency) outputLatency;
@property (Td,R,N,V_inputSafetyOffset) inputSafetyOffset;
@property (Td,R,N,V_outputSafetyOffset) outputSafetyOffset;
@property (Td,R,N,V_outputVolume) outputVolume;
@property (Tq,R,V_reporterID) reporterID;
@property (Tq,R,N,V_currentActivationMode) currentActivationMode;
```

## Instance methods

```
-[AVVCSessionManager currentRoute];
-[AVVCSessionManager sessionState];
-[AVVCSessionManager audioSession];
-[AVVCSessionManager isSessionActive];
-[AVVCSessionManager isPrimary];
-[AVVCSessionManager siriInputSource];
-[AVVCSessionManager dealloc];
-[AVVCSessionManager outputSafetyOffset];
-[AVVCSessionManager outputLatency];
-[AVVCSessionManager pickedRoute];
-[AVVCSessionManager siriRemoteInputIdentifier];
-[AVVCSessionManager inputLatency];
-[AVVCSessionManager setSessionState:];
-[AVVCSessionManager setAudioSession:];
-[AVVCSessionManager inputSafetyOffset];
-[AVVCSessionManager reporterID];
-[AVVCSessionManager initWithSession:];
-[AVVCSessionManager playbackRoute];
-[AVVCSessionManager setCategory:mode:routeSharingPolicy:options:error:];
-[AVVCSessionManager setActivationContext:error:];
-[AVVCSessionManager setActive:withOptions:error:];
-[AVVCSessionManager outputVolume];
-[AVVCSessionManager setCategory:mode:options:error:];
-[AVVCSessionManager speechDetectionDeviceSampleRate];
-[AVVCSessionManager clearInputPreferences:];
-[AVVCSessionManager inputNumberOfChannels];
-[AVVCSessionManager isInputAvailable];
-[AVVCSessionManager setAudioHardwareControlFlags:error:];
-[AVVCSessionManager setDuckToLevelDB:error:];
-[AVVCSessionManager setDuckToLevelScalar:error:];
-[AVVCSessionManager setDuckingFadeOutDuration:fadeInDuration:error:];
-[AVVCSessionManager setIAmTheAssistant:error:];
-[AVVCSessionManager setPreferredSampleRate:error:];
-[AVVCSessionManager setPrefersAggressiveEchoCancellation:error:];
-[AVVCSessionManager setRecordingFromRemoteInput:error:];
-[AVVCSessionManager isBTDeviceInEar];
-[AVVCSessionManager isPickedRouteW1];
-[AVVCSessionManager setMicrophoneAttribution:error:];
-[AVVCSessionManager _applyAudioHardwareControlFlagsIfChanged:logContext:];
-[AVVCSessionManager activateAudioSessionWithPrewarm:error:];
-[AVVCSessionManager changeDuckOthersOption:];
-[AVVCSessionManager clientRequestsRecording];
-[AVVCSessionManager currentActivationMode];
-[AVVCSessionManager deactivateAudioSessionWithOptions:error:];
-[AVVCSessionManager deviceGain];
-[AVVCSessionManager enableSmartRoutingConsideration:];
-[AVVCSessionManager forceGetSessionProperties];
-[AVVCSessionManager getActiveSessionDisplayIDsAsString];
-[AVVCSessionManager getClientRequestsRecording];
-[AVVCSessionManager getDeviceGain];
-[AVVCSessionManager getForceGetSessionProperties];
-[AVVCSessionManager getHypotheticalRouteAndUpdateStates];
-[AVVCSessionManager getOpaqueSessionID];
-[AVVCSessionManager getPlaybackRoute];
-[AVVCSessionManager getSessionActivationOptions];
-[AVVCSessionManager getSiriInputSource:withIdentifier:];
-[AVVCSessionManager isAirplayOneOfTheOutputRoutes:];
-[AVVCSessionManager isCurrentInputBuiltInMic];
-[AVVCSessionManager isMiniDuckingEnabled];
-[AVVCSessionManager isSWVolumeSupportedOnPickedRoute];
-[AVVCSessionManager isSessionInSiriCategory];
-[AVVCSessionManager isSessionInSiriCategoryModeAndOptions:];
-[AVVCSessionManager isSessionOutputInWirelessSplitterMode];
-[AVVCSessionManager predictIfMicrophoneShouldBeUsedForActivationMode:];
-[AVVCSessionManager removeSessionNotifications:];
-[AVVCSessionManager sessionCurrentInputRoutes];
-[AVVCSessionManager sessionCurrentOutputRoutes];
-[AVVCSessionManager setClientRequestsRecording:];
-[AVVCSessionManager setDeviceGain:];
-[AVVCSessionManager setDuckOthers:mixWithOthers:error:];
-[AVVCSessionManager setEnableBTTriangleMode:error:];
-[AVVCSessionManager setForceGetSessionProperties:];
-[AVVCSessionManager setIsUsingBuiltInMicForRecording:error:];
-[AVVCSessionManager setPlaybackRoute:];
-[AVVCSessionManager setPrefersBeingInterruptedByNextActiveRecordingClient:error:];
-[AVVCSessionManager setSessionActivationContext:];
-[AVVCSessionManager setSessionActivationOptions:];
-[AVVCSessionManager setSessionAudioHWControlFlagsForActivationMode:withOptions:];
-[AVVCSessionManager setSessionBufferSize:];
-[AVVCSessionManager setSessionCategoryModeOptionsForActivationMode:withOptions:];
-[AVVCSessionManager setSessionSampleRateForActivationMode:];
-[AVVCSessionManager setSessionStateWithoutLock:];
-[AVVCSessionManager setupOneTimeSessionSettingsForClient:];
-[AVVCSessionManager setupSessionNotifications:];
-[AVVCSessionManager shouldEnableMiniDucking:withOptions:];
```
