# `PLAudioAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 34 instance variables, 34 properties, 111 instance methods, 24 class methods

## Instance variables

```
B _audioIsActive;
B _headsetIsPlayingAudio;
B _speakerIsPlayingAudio;
i _accessoryPowerState;
@"NSMutableArray" _nsOutputNotifications;
@"NSMutableArray" _nsRoutingNotifications;
@"PLEntryNotificationOperatorComposition" _accessoryPowerCallback;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"PLXPCListenerOperatorComposition" _audioAppXPCListener;
@"PLXPCListenerOperatorComposition" _screenMirroringXPCListener;
@"PLXPCListenerOperatorComposition" _speakerAmpXPCListener;
@"PLXPCListenerOperatorComposition" _hapticsXPCListener;
@"PLXPCListenerOperatorComposition" _hapticsAssertionXPCListener;
@"PLXPCListenerOperatorComposition" _hapticsPrewarmCountListener;
@"PLXPCListenerOperatorComposition" _hapticsRunningCountListener;
@"PLXPCListenerOperatorComposition" _HapticAudioRunningCountListener;
@"PLXPCListenerOperatorComposition" _hapticForceStopListener;
@"PLXPCListenerOperatorComposition" _RMSLoggingXPCListener;
@"PLXPCListenerOperatorComposition" _CoreAudioVADXPCListener;
@"PLXPCListenerOperatorComposition" _shazamRecordingXPCListener;
@"PLXPCListenerOperatorComposition" _mutedTalkerDetectionXPCListener;
@"PLXPCListenerOperatorComposition" _singXPCListener;
@"PLXPCListenerOperatorComposition" _songTransitionXPCListener;
@"PLEntry" _entryRoutingOld;
d _currentVolume;
@"NSString" _audioHardware;
@"NSDictionary" _audioPowerModel;
@"NSDate" _lastAudioStateChangeDate;
@"PLEntryNotificationOperatorComposition" _mediaPlaybackAssertionListener;
@"NSMutableDictionary" _activeMediaPlaybackAssertions;
@"AudioDevice" _defaultOutputDevice;
@"AudioDevice" _defaultInputDevice;
@? _defaultOutputDeviceHandlerBlock;
@? _defaultInputDeviceHandlerBlock;
```

## Properties

```
@property (Ti,V_accessoryPowerState) accessoryPowerState;
@property (T@"NSMutableArray",R,V_nsOutputNotifications) nsOutputNotifications;
@property (T@"NSMutableArray",R,V_nsRoutingNotifications) nsRoutingNotifications;
@property (T@"PLEntryNotificationOperatorComposition",&,V_accessoryPowerCallback) accessoryPowerCallback;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_audioAppXPCListener) audioAppXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_screenMirroringXPCListener) screenMirroringXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_speakerAmpXPCListener) speakerAmpXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_hapticsXPCListener) hapticsXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_hapticsAssertionXPCListener) hapticsAssertionXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_hapticsPrewarmCountListener) hapticsPrewarmCountListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_hapticsRunningCountListener) hapticsRunningCountListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_HapticAudioRunningCountListener) HapticAudioRunningCountListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_hapticForceStopListener) hapticForceStopListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_RMSLoggingXPCListener) RMSLoggingXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_CoreAudioVADXPCListener) CoreAudioVADXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_shazamRecordingXPCListener) shazamRecordingXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_mutedTalkerDetectionXPCListener) mutedTalkerDetectionXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_singXPCListener) singXPCListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_songTransitionXPCListener) songTransitionXPCListener;
@property (T@"PLEntry",&,V_entryRoutingOld) entryRoutingOld;
@property (TB,V_audioIsActive) audioIsActive;
@property (TB,V_headsetIsPlayingAudio) headsetIsPlayingAudio;
@property (TB,V_speakerIsPlayingAudio) speakerIsPlayingAudio;
@property (Td,V_currentVolume) currentVolume;
@property (T@"NSString",R,V_audioHardware) audioHardware;
@property (T@"NSDictionary",R,V_audioPowerModel) audioPowerModel;
@property (T@"NSDate",&,V_lastAudioStateChangeDate) lastAudioStateChangeDate;
@property (T@"PLEntryNotificationOperatorComposition",&,V_mediaPlaybackAssertionListener) mediaPlaybackAssertionListener;
@property (T@"NSMutableDictionary",&,N,V_activeMediaPlaybackAssertions) activeMediaPlaybackAssertions;
@property (T@"AudioDevice",&,N,V_defaultOutputDevice) defaultOutputDevice;
@property (T@"AudioDevice",&,N,V_defaultInputDevice) defaultInputDevice;
@property (T@?,C,N,V_defaultOutputDeviceHandlerBlock) defaultOutputDeviceHandlerBlock;
@property (T@?,C,N,V_defaultInputDeviceHandlerBlock) defaultInputDeviceHandlerBlock;
```

## Class methods

```
+[PLAudioAgent entryEventIntervalDefinitions];
+[PLAudioAgent entryEventPointDefinitions];
+[PLAudioAgent entryEventForwardDefinitions];
+[PLAudioAgent entryEventBackwardDefinitions];
+[PLAudioAgent entryEventNoneDefinitions];
+[PLAudioAgent load];
+[PLAudioAgent entryEventForwardDefinitionRouting];
+[PLAudioAgent entryEventPointDefinitionHapticForceStop];
+[PLAudioAgent entryEventPointDefinitionSpeakerAmp];
+[PLAudioAgent entryEventPointDefinitionAudioApp];
+[PLAudioAgent entryEventPointDefinitionHaptics];
+[PLAudioAgent entryEventForwardDefinitionNowPlaying];
+[PLAudioAgent entryEventIntervalDefinitionRMSLogging];
+[PLAudioAgent entryEventForwardDefinitionHapticAudioRunningCount];
+[PLAudioAgent entryEventPointDefinitionHapticsAssertion];
+[PLAudioAgent isEnabled];
+[PLAudioAgent entryEventForwardDefinitionHapticsPrewarmCount];
+[PLAudioAgent entryEventForwardDefinitionMutedTalkerDetection];
+[PLAudioAgent entryEventIntervalDefinitionShazamRecording];
+[PLAudioAgent entryEventForwardDefinitionOutput];
+[PLAudioAgent entryEventForwardDefinitionHapticsRunningCount];
+[PLAudioAgent entryEventIntervalDefinitionCoreAudioVAD];
+[PLAudioAgent entryEventForwardDefinitionAudioDevice];
+[PLAudioAgent entryAggregateDefinitions];
```

## Instance methods

```
-[PLAudioAgent activeMediaPlaybackAssertions];
-[PLAudioAgent audioIsActive];
-[PLAudioAgent createAudioAccountingEvents:];
-[PLAudioAgent defaultOutputDeviceHandlerBlock];
-[PLAudioAgent setSongTransitionXPCListener:];
-[PLAudioAgent setHapticAudioRunningCountListener:];
-[PLAudioAgent outputCategory];
-[PLAudioAgent hapticsRunningCountListener];
-[PLAudioAgent setupAVSystemController];
-[PLAudioAgent nsOutputNotifications];
-[PLAudioAgent setCoreAudioVADXPCListener:];
-[PLAudioAgent modelAudioPower];
-[PLAudioAgent volume];
-[PLAudioAgent headphonesConnected];
-[PLAudioAgent setHapticsRunningCountListener:];
-[PLAudioAgent speakerAmpXPCListener];
-[PLAudioAgent init];
-[PLAudioAgent modelAudioPowerCodec:];
-[PLAudioAgent lastAudioStateChangeDate];
-[PLAudioAgent setEntryRoutingOld:];
-[PLAudioAgent currentVolume];
-[PLAudioAgent initOperatorDependancies];
-[PLAudioAgent defaultInputDeviceHandlerBlock];
-[PLAudioAgent logEventForwardHapticAudioRunningCount:];
-[PLAudioAgent buildCallBack:withGroup:withHandler:];
-[PLAudioAgent logEventPointAudioApp:];
-[PLAudioAgent setHeadsetIsPlayingAudio:];
-[PLAudioAgent speakerIsPlayingAudio];
-[PLAudioAgent createCarPlayAccountingEvents:];
-[PLAudioAgent CoreAudioVADXPCListener];
-[PLAudioAgent setAudioAppXPCListener:];
-[PLAudioAgent handleNowPlayingApplicationIsPlayingDidChange:];
-[PLAudioAgent handleLightningStatusCallback:];
-[PLAudioAgent setThermalMonitorListener:];
-[PLAudioAgent returnVolumeOrOutPutCategory:];
-[PLAudioAgent hapticsAssertionXPCListener];
-[PLAudioAgent logEventForwardHapticsPrewarmCount:];
-[PLAudioAgent audioHardware];
-[PLAudioAgent setHapticForceStopListener:];
-[PLAudioAgent setAccessoryPowerCallback:];
-[PLAudioAgent setHapticsPrewarmCountListener:];
-[PLAudioAgent setActiveMediaPlaybackAssertions:];
-[PLAudioAgent logEventIntervalRMSLogging:];
-[PLAudioAgent BTEndpointType];
-[PLAudioAgent nowPlayingAppBundleID:];
-[PLAudioAgent RMSLoggingXPCListener];
-[PLAudioAgent logEventPointSpeakerAmp:];
-[PLAudioAgent logEventForwardSing:];
-[PLAudioAgent hapticForceStopListener];
-[PLAudioAgent logEventForwardMutedTalkerDetection:];
-[PLAudioAgent createBluetoothAccountingEvents:];
-[PLAudioAgent mediaPlaybackAssertionListener];
-[PLAudioAgent handleMediaPlaybackAssertionEntry:];
-[PLAudioAgent createAirPlayAccountingEvents:];
-[PLAudioAgent setSingXPCListener:];
-[PLAudioAgent nsRoutingNotifications];
-[PLAudioAgent setMediaPlaybackAssertionListener:];
-[PLAudioAgent setSpeakerIsPlayingAudio:];
-[PLAudioAgent mutedTalkerDetectionXPCListener];
-[PLAudioAgent setDefaultInputDevice:];
-[PLAudioAgent setAudioIsActive:];
-[PLAudioAgent defaultInputDevice];
-[PLAudioAgent defaultOutputDevice];
-[PLAudioAgent shazamRecordingXPCListener];
-[PLAudioAgent accessoryPowerState];
-[PLAudioAgent setHapticsXPCListener:];
-[PLAudioAgent logEventForwardAudioDevice:];
-[PLAudioAgent setHapticsAssertionXPCListener:];
-[PLAudioAgent convertSpeakerProtectionModeledPowerToTotalSpeakerPower:];
-[PLAudioAgent logEventPointHaptics:];
-[PLAudioAgent setDefaultOutputDevice:];
-[PLAudioAgent logEventForwardSongTransitions:];
-[PLAudioAgent setDefaultOutputDeviceHandlerBlock:];
-[PLAudioAgent audioAppXPCListener];
-[PLAudioAgent logEventIntervalCoreAudioVAD:];
-[PLAudioAgent setSpeakerAmpXPCListener:];
-[PLAudioAgent headsetHasInput];
-[PLAudioAgent setRMSLoggingXPCListener:];
-[PLAudioAgent initDefaultAudioDevice:];
-[PLAudioAgent hapticsXPCListener];
-[PLAudioAgent closeAudioAccountingEvents];
-[PLAudioAgent singXPCListener];
-[PLAudioAgent log];
-[PLAudioAgent shouldModelAudioPowerSpeakerTemp];
-[PLAudioAgent screenMirroringXPCListener];
-[PLAudioAgent modelAudioPowerWithVolume:];
-[PLAudioAgent activeRoute];
-[PLAudioAgent setAccessoryPowerState:];
-[PLAudioAgent songTransitionXPCListener];
-[PLAudioAgent entryRoutingOld];
-[PLAudioAgent HapticAudioRunningCountListener];
-[PLAudioAgent setLastAudioStateChangeDate:];
-[PLAudioAgent audioPowerModel];
-[PLAudioAgent hapticsPrewarmCountListener];
-[PLAudioAgent accessoryPowerCallback];
-[PLAudioAgent addDefaultAudioDeviceListener:];
-[PLAudioAgent setScreenMirroringXPCListener:];
-[PLAudioAgent logEventIntervalShazamRecording:];
-[PLAudioAgent modelAudioPowerSpeaker:];
-[PLAudioAgent thermalMonitorListener];
-[PLAudioAgent logEventForwardHapticsRunningCount:];
-[PLAudioAgent setMutedTalkerDetectionXPCListener:];
-[PLAudioAgent setCurrentVolume:];
-[PLAudioAgent logEventPointHapticsAssertion:];
-[PLAudioAgent logEventForwardRouting];
-[PLAudioAgent headsetIsPlayingAudio];
-[PLAudioAgent logEventForwardOutput];
-[PLAudioAgent setShazamRecordingXPCListener:];
-[PLAudioAgent logEventPointHapticForceStop:];
-[PLAudioAgent setDefaultInputDeviceHandlerBlock:];
-[PLAudioAgent audioPowerForRoute:forVolume:];
```
