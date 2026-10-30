# `CBDeviceSettings`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 27 instance variables, 27 properties, 58 instance methods, 0 class methods

## Instance variables

```
c _aclPriority;
C _aclLinkState;
C _adaptiveVolumeConfig;
c _allowsAutoRoute;
c _audioRouteHidden;
C _clickHoldModeLeft;
C _clickHoldModeRight;
C _conversationDetectConfig;
C _crownRotationDirection;
c _doubleTapActionLeft;
c _doubleTapActionRight;
C _endCallConfig;
c _microphoneMode;
C _muteControlConfig;
c _placementMode;
c _relinquishAudioRoute;
C _selectiveSpeechListeningConfig;
c _smartRoutingMode;
c _spatialAudioAllowed;
C _userSelectedDeviceType;
i _listeningMode;
I _listeningModeConfigs;
i _spatialAudioMode;
Q _deviceFlagsMask;
Q _deviceFlagsValue;
@"NSString" _name;
@"CBPowerSource" _powerSourceMock;
```

## Properties

```
@property (T@"CBPowerSource",C,N,V_powerSourceMock) powerSourceMock;
@property (Tc,N,V_aclPriority) aclPriority;
@property (TC,N,V_aclLinkState) aclLinkState;
@property (TC,N,V_adaptiveVolumeConfig) adaptiveVolumeConfig;
@property (Tc,N,V_allowsAutoRoute) allowsAutoRoute;
@property (Tc,N,V_audioRouteHidden) audioRouteHidden;
@property (TC,N,V_clickHoldModeLeft) clickHoldModeLeft;
@property (TC,N,V_clickHoldModeRight) clickHoldModeRight;
@property (TC,N,V_conversationDetectConfig) conversationDetectConfig;
@property (TC,N,V_crownRotationDirection) crownRotationDirection;
@property (TQ,N,V_deviceFlagsMask) deviceFlagsMask;
@property (TQ,N,V_deviceFlagsValue) deviceFlagsValue;
@property (Tc,N,V_doubleTapActionLeft) doubleTapActionLeft;
@property (Tc,N,V_doubleTapActionRight) doubleTapActionRight;
@property (TC,N,V_endCallConfig) endCallConfig;
@property (Ti,N,V_listeningMode) listeningMode;
@property (TI,N,V_listeningModeConfigs) listeningModeConfigs;
@property (Tc,N,V_microphoneMode) microphoneMode;
@property (TC,N,V_muteControlConfig) muteControlConfig;
@property (T@"NSString",C,N,V_name) name;
@property (Tc,N,V_placementMode) placementMode;
@property (Tc,N,V_relinquishAudioRoute) relinquishAudioRoute;
@property (TC,N,V_selectiveSpeechListeningConfig) selectiveSpeechListeningConfig;
@property (Tc,N,V_smartRoutingMode) smartRoutingMode;
@property (Tc,N,V_spatialAudioAllowed) spatialAudioAllowed;
@property (Ti,N,V_spatialAudioMode) spatialAudioMode;
@property (TC,N,V_userSelectedDeviceType) userSelectedDeviceType;
```

## Instance methods

```
-[CBDeviceSettings encodeWithXPCObject:];
-[CBDeviceSettings initWithXPCObject:error:];
-[CBDeviceSettings init];
-[CBDeviceSettings description];
-[CBDeviceSettings setName:];
-[CBDeviceSettings name];
-[CBDeviceSettings listeningMode];
-[CBDeviceSettings setListeningMode:];
-[CBDeviceSettings microphoneMode];
-[CBDeviceSettings setMicrophoneMode:];
-[CBDeviceSettings listeningModeConfigs];
-[CBDeviceSettings selectiveSpeechListeningConfig];
-[CBDeviceSettings setSelectiveSpeechListeningConfig:];
-[CBDeviceSettings adaptiveVolumeConfig];
-[CBDeviceSettings clickHoldModeLeft];
-[CBDeviceSettings clickHoldModeRight];
-[CBDeviceSettings conversationDetectConfig];
-[CBDeviceSettings crownRotationDirection];
-[CBDeviceSettings doubleTapActionLeft];
-[CBDeviceSettings doubleTapActionRight];
-[CBDeviceSettings endCallConfig];
-[CBDeviceSettings muteControlConfig];
-[CBDeviceSettings placementMode];
-[CBDeviceSettings setAdaptiveVolumeConfig:];
-[CBDeviceSettings setClickHoldModeLeft:];
-[CBDeviceSettings setClickHoldModeRight:];
-[CBDeviceSettings setConversationDetectConfig:];
-[CBDeviceSettings setCrownRotationDirection:];
-[CBDeviceSettings setDoubleTapActionLeft:];
-[CBDeviceSettings setDoubleTapActionRight:];
-[CBDeviceSettings setEndCallConfig:];
-[CBDeviceSettings setListeningModeConfigs:];
-[CBDeviceSettings setMuteControlConfig:];
-[CBDeviceSettings setPlacementMode:];
-[CBDeviceSettings setSmartRoutingMode:];
-[CBDeviceSettings setSpatialAudioAllowed:];
-[CBDeviceSettings smartRoutingMode];
-[CBDeviceSettings allowsAutoRoute];
-[CBDeviceSettings powerSourceMock];
-[CBDeviceSettings setAclPriority:];
-[CBDeviceSettings deviceFlagsMask];
-[CBDeviceSettings aclLinkState];
-[CBDeviceSettings aclPriority];
-[CBDeviceSettings audioRouteHidden];
-[CBDeviceSettings deviceFlagsValue];
-[CBDeviceSettings relinquishAudioRoute];
-[CBDeviceSettings setAclLinkState:];
-[CBDeviceSettings setAllowsAutoRoute:];
-[CBDeviceSettings setAudioRouteHidden:];
-[CBDeviceSettings setDeviceFlagsMask:];
-[CBDeviceSettings setDeviceFlagsValue:];
-[CBDeviceSettings setPowerSourceMock:];
-[CBDeviceSettings setRelinquishAudioRoute:];
-[CBDeviceSettings setSpatialAudioMode:];
-[CBDeviceSettings setUserSelectedDeviceType:];
-[CBDeviceSettings spatialAudioAllowed];
-[CBDeviceSettings spatialAudioMode];
-[CBDeviceSettings userSelectedDeviceType];
```
