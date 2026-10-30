# `AADeviceConfig`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 51 instance variables, 51 properties, 109 instance methods, 1 class methods

## Instance variables

```
C _acceptReplyPlayPauseConfig;
c _aclPriority;
C _adaptiveVolumeConfig;
c _allowsAutoRoute;
c _allowHealthKitDataWrite;
c _allowTemporaryManagedPairing;
c _audioRouteHidden;
C _bobbleConfig;
c _changeDynamicEndOfChargeState;
c _changeOptimizedBatteryChargingState;
C _clickHoldModeLeft;
C _clickHoldModeRight;
C _conversationDetectConfig;
C _crownRotationDirection;
C _declineDismissSkipConfig;
c _doubleTapActionLeft;
c _doubleTapActionRight;
c _enableChargingReminder;
c _enableHearingAidGainSwipe;
c _enableHearingAssist;
c _enableHeartRateMonitor;
c _enableHearingProtectionPPE;
c _enableSiriMultitone;
c _enableSleepDetection;
C _endCallConfig;
c _headGestureToggle;
c _headGestureProxCardShown;
c _hearingAidToggle;
c _hearingAidEnrolled;
c _hearingAidV2SourceRegionSupport;
c _listeningModeOffAllowed;
c _microphoneMode;
C _muteControlConfig;
c _placementMode;
C _preferenceEQGainHigh;
C _preferenceEQGainLow;
C _preferenceEQGainMid;
C _preferenceEQMode;
c _tempEQDisabled;
c _relinquishAudioRoute;
C _remoteCameraControlConfig;
C _selectiveSpeechListeningConfig;
c _smartRoutingMode;
c _spatialAudioAllowed;
S _rawGesturesConfigFlags;
I _autoANCStrength;
i _listeningMode;
I _listeningModeConfigs;
i _spatialAudioMode;
@"NSDate" _audiogramEnrolledTimestamp;
@"NSString" _name;
```

## Properties

```
@property (TC,N,V_acceptReplyPlayPauseConfig) acceptReplyPlayPauseConfig;
@property (Tc,N,V_aclPriority) aclPriority;
@property (TC,N,V_adaptiveVolumeConfig) adaptiveVolumeConfig;
@property (Tc,N,V_allowsAutoRoute) allowsAutoRoute;
@property (Tc,N,V_allowHealthKitDataWrite) allowHealthKitDataWrite;
@property (Tc,N,V_allowTemporaryManagedPairing) allowTemporaryManagedPairing;
@property (TI,N,V_autoANCStrength) autoANCStrength;
@property (T@"NSDate",C,N,V_audiogramEnrolledTimestamp) audiogramEnrolledTimestamp;
@property (Tc,N,V_audioRouteHidden) audioRouteHidden;
@property (TC,N,V_bobbleConfig) bobbleConfig;
@property (Tc,N,V_changeDynamicEndOfChargeState) changeDynamicEndOfChargeState;
@property (Tc,N,V_changeOptimizedBatteryChargingState) changeOptimizedBatteryChargingState;
@property (TC,N,V_clickHoldModeLeft) clickHoldModeLeft;
@property (TC,N,V_clickHoldModeRight) clickHoldModeRight;
@property (TC,N,V_conversationDetectConfig) conversationDetectConfig;
@property (TC,N,V_crownRotationDirection) crownRotationDirection;
@property (TC,N,V_declineDismissSkipConfig) declineDismissSkipConfig;
@property (Tc,N,V_doubleTapActionLeft) doubleTapActionLeft;
@property (Tc,N,V_doubleTapActionRight) doubleTapActionRight;
@property (Tc,N,V_enableChargingReminder) enableChargingReminder;
@property (Tc,N,V_enableHearingAidGainSwipe) enableHearingAidGainSwipe;
@property (Tc,N,V_enableHearingAssist) enableHearingAssist;
@property (Tc,N,V_enableHeartRateMonitor) enableHeartRateMonitor;
@property (Tc,N,V_enableHearingProtectionPPE) enableHearingProtectionPPE;
@property (Tc,N,V_enableSiriMultitone) enableSiriMultitone;
@property (Tc,N,V_enableSleepDetection) enableSleepDetection;
@property (TC,N,V_endCallConfig) endCallConfig;
@property (Tc,N,V_headGestureToggle) headGestureToggle;
@property (Tc,N,V_headGestureProxCardShown) headGestureProxCardShown;
@property (Tc,N,V_hearingAidToggle) hearingAidToggle;
@property (Tc,N,V_hearingAidEnrolled) hearingAidEnrolled;
@property (Tc,N,V_hearingAidV2SourceRegionSupport) hearingAidV2SourceRegionSupport;
@property (Ti,N,V_listeningMode) listeningMode;
@property (TI,N,V_listeningModeConfigs) listeningModeConfigs;
@property (Tc,N,V_listeningModeOffAllowed) listeningModeOffAllowed;
@property (Tc,N,V_microphoneMode) microphoneMode;
@property (TC,N,V_muteControlConfig) muteControlConfig;
@property (T@"NSString",C,N,V_name) name;
@property (Tc,N,V_placementMode) placementMode;
@property (TC,N,V_preferenceEQGainHigh) preferenceEQGainHigh;
@property (TC,N,V_preferenceEQGainLow) preferenceEQGainLow;
@property (TC,N,V_preferenceEQGainMid) preferenceEQGainMid;
@property (TC,N,V_preferenceEQMode) preferenceEQMode;
@property (Tc,N,V_tempEQDisabled) tempEQDisabled;
@property (TS,N,V_rawGesturesConfigFlags) rawGesturesConfigFlags;
@property (Tc,N,V_relinquishAudioRoute) relinquishAudioRoute;
@property (TC,N,V_remoteCameraControlConfig) remoteCameraControlConfig;
@property (TC,N,V_selectiveSpeechListeningConfig) selectiveSpeechListeningConfig;
@property (Tc,N,V_smartRoutingMode) smartRoutingMode;
@property (Tc,N,V_spatialAudioAllowed) spatialAudioAllowed;
@property (Ti,N,V_spatialAudioMode) spatialAudioMode;
```

## Class methods

```
+[AADeviceConfig supportsSecureCoding];
```

## Instance methods

```
-[AADeviceConfig descriptionWithLevel:];
-[AADeviceConfig init];
-[AADeviceConfig encodeWithCoder:];
-[AADeviceConfig description];
-[AADeviceConfig setName:];
-[AADeviceConfig initWithCoder:];
-[AADeviceConfig name];
-[AADeviceConfig setAllowHealthKitDataWrite:];
-[AADeviceConfig listeningMode];
-[AADeviceConfig setListeningMode:];
-[AADeviceConfig microphoneMode];
-[AADeviceConfig setMicrophoneMode:];
-[AADeviceConfig listeningModeConfigs];
-[AADeviceConfig selectiveSpeechListeningConfig];
-[AADeviceConfig setSelectiveSpeechListeningConfig:];
-[AADeviceConfig setTempEQDisabled:];
-[AADeviceConfig autoANCStrength];
-[AADeviceConfig listeningModeOffAllowed];
-[AADeviceConfig setAutoANCStrength:];
-[AADeviceConfig acceptReplyPlayPauseConfig];
-[AADeviceConfig adaptiveVolumeConfig];
-[AADeviceConfig allowHealthKitDataWrite];
-[AADeviceConfig allowTemporaryManagedPairing];
-[AADeviceConfig audiogramEnrolledTimestamp];
-[AADeviceConfig bobbleConfig];
-[AADeviceConfig changeDynamicEndOfChargeState];
-[AADeviceConfig changeOptimizedBatteryChargingState];
-[AADeviceConfig clickHoldModeLeft];
-[AADeviceConfig clickHoldModeRight];
-[AADeviceConfig conversationDetectConfig];
-[AADeviceConfig crownRotationDirection];
-[AADeviceConfig declineDismissSkipConfig];
-[AADeviceConfig doubleTapActionLeft];
-[AADeviceConfig doubleTapActionRight];
-[AADeviceConfig enableChargingReminder];
-[AADeviceConfig enableHearingAidGainSwipe];
-[AADeviceConfig enableHearingAssist];
-[AADeviceConfig enableHearingProtectionPPE];
-[AADeviceConfig enableHeartRateMonitor];
-[AADeviceConfig enableSleepDetection];
-[AADeviceConfig endCallConfig];
-[AADeviceConfig headGestureProxCardShown];
-[AADeviceConfig headGestureToggle];
-[AADeviceConfig hearingAidEnrolled];
-[AADeviceConfig muteControlConfig];
-[AADeviceConfig placementMode];
-[AADeviceConfig preferenceEQGainHigh];
-[AADeviceConfig preferenceEQGainLow];
-[AADeviceConfig preferenceEQGainMid];
-[AADeviceConfig preferenceEQMode];
-[AADeviceConfig remoteCameraControlConfig];
-[AADeviceConfig setAcceptReplyPlayPauseConfig:];
-[AADeviceConfig setAdaptiveVolumeConfig:];
-[AADeviceConfig setAllowTemporaryManagedPairing:];
-[AADeviceConfig setAudiogramEnrolledTimestamp:];
-[AADeviceConfig setBobbleConfig:];
-[AADeviceConfig setChangeDynamicEndOfChargeState:];
-[AADeviceConfig setChangeOptimizedBatteryChargingState:];
-[AADeviceConfig setClickHoldModeLeft:];
-[AADeviceConfig setClickHoldModeRight:];
-[AADeviceConfig setConversationDetectConfig:];
-[AADeviceConfig setCrownRotationDirection:];
-[AADeviceConfig setDeclineDismissSkipConfig:];
-[AADeviceConfig setDoubleTapActionLeft:];
-[AADeviceConfig setDoubleTapActionRight:];
-[AADeviceConfig setEnableChargingReminder:];
-[AADeviceConfig setEnableHearingAidGainSwipe:];
-[AADeviceConfig setEnableHearingAssist:];
-[AADeviceConfig setEnableHearingProtectionPPE:];
-[AADeviceConfig setEnableHeartRateMonitor:];
-[AADeviceConfig setEnableSleepDetection:];
-[AADeviceConfig setEndCallConfig:];
-[AADeviceConfig setHeadGestureProxCardShown:];
-[AADeviceConfig setHeadGestureToggle:];
-[AADeviceConfig setHearingAidEnrolled:];
-[AADeviceConfig setListeningModeConfigs:];
-[AADeviceConfig setListeningModeOffAllowed:];
-[AADeviceConfig setMuteControlConfig:];
-[AADeviceConfig setPlacementMode:];
-[AADeviceConfig setPreferenceEQGainHigh:];
-[AADeviceConfig setPreferenceEQGainLow:];
-[AADeviceConfig setPreferenceEQGainMid:];
-[AADeviceConfig setPreferenceEQMode:];
-[AADeviceConfig setRemoteCameraControlConfig:];
-[AADeviceConfig setSmartRoutingMode:];
-[AADeviceConfig setSpatialAudioAllowed:];
-[AADeviceConfig smartRoutingMode];
-[AADeviceConfig allowsAutoRoute];
-[AADeviceConfig setAclPriority:];
-[AADeviceConfig aclPriority];
-[AADeviceConfig audioRouteHidden];
-[AADeviceConfig relinquishAudioRoute];
-[AADeviceConfig setAllowsAutoRoute:];
-[AADeviceConfig setAudioRouteHidden:];
-[AADeviceConfig setRelinquishAudioRoute:];
-[AADeviceConfig setSpatialAudioMode:];
-[AADeviceConfig spatialAudioAllowed];
-[AADeviceConfig spatialAudioMode];
-[AADeviceConfig hearingAidV2SourceRegionSupport];
-[AADeviceConfig enableSiriMultitone];
-[AADeviceConfig hearingAidToggle];
-[AADeviceConfig needsUpdateToAAController];
-[AADeviceConfig needsUpdateToPairedDevice];
-[AADeviceConfig rawGesturesConfigFlags];
-[AADeviceConfig setEnableSiriMultitone:];
-[AADeviceConfig setHearingAidToggle:];
-[AADeviceConfig setHearingAidV2SourceRegionSupport:];
-[AADeviceConfig setRawGesturesConfigFlags:];
-[AADeviceConfig tempEQDisabled];
```
