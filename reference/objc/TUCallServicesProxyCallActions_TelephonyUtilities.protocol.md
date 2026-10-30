# `TUCallServicesProxyCallActions` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 45 instance methods, 0 class methods

## Instance methods

```
-[TUCallServicesProxyCallActions disconnectAllCalls];
-[TUCallServicesProxyCallActions pullHostedCallsFromPairedHostDevice];
-[TUCallServicesProxyCallActions setHasEmergencyVideoStream:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setTTYType:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setBluetoothAudioFormatForCallWithUniqueProxyIdentifier:bluetoothAudioFormat:];
-[TUCallServicesProxyCallActions reportDegradation:forGroupUUID:];
-[TUCallServicesProxyCallActions setScreenShareAttributesForCallWithUniqueProxyIdentifier:attributes:];
-[TUCallServicesProxyCallActions disconnectCurrentCall];
-[TUCallServicesProxyCallActions setRemoteVideoPresentationSizeForCallWithUniqueProxyIdentifier:size:];
-[TUCallServicesProxyCallActions willEnterBackgroundForAllCalls];
-[TUCallServicesProxyCallActions addScreenSharingType:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions disconnectCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setIsSendingVideo:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions swapCalls];
-[TUCallServicesProxyCallActions setEmergencyMediaItems:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions requestVideoUpgradeForCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions groupCallWithUniqueProxyIdentifier:withOtherCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setDownlinkMuted:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setUplinkMuted:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions updateCallWithProxy:];
-[TUCallServicesProxyCallActions pushHostedCallsToDestination:];
-[TUCallServicesProxyCallActions answerCallWithRequest:];
-[TUCallServicesProxyCallActions setRemoteVideoPresentationStateForCallWithUniqueProxyIdentifier:presentationState:];
-[TUCallServicesProxyCallActions enteredBackgroundForAllCalls];
-[TUCallServicesProxyCallActions setMixesVoiceWithMedia:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setSharingScreen:attributes:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions holdCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions sendHardPauseDigitsForCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setVideoPaused:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions sendUserScoreToRTCReporting:withScore:];
-[TUCallServicesProxyCallActions setSharingScreen:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions enteredForegroundForCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions pushRelayingCallsToHostWithSourceIdentifier:];
-[TUCallServicesProxyCallActions playDTMFToneForCallWithUniqueProxyIdentifier:key:];
-[TUCallServicesProxyCallActions shouldAllowRingingCallStatusIndicator:];
-[TUCallServicesProxyCallActions pullRelayingCallsFromClient];
-[TUCallServicesProxyCallActions sendMMIOrUSSDCodeWithRequest:];
-[TUCallServicesProxyCallActions disconnectCurrentCallAndActivateHeld];
-[TUCallServicesProxyCallActions shouldSuppressInCallStatusBar:];
-[TUCallServicesProxyCallActions ungroupCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setLiveVoicemailUnavailableReason:forCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions activateInCallUIWithActivityContinuationIdentifier:];
-[TUCallServicesProxyCallActions pullRelayingGFTCallsFromClientIfNecessary];
-[TUCallServicesProxyCallActions unholdCallWithUniqueProxyIdentifier:];
-[TUCallServicesProxyCallActions setVideoCaptureMode:forCallWithUniqueProxyIdentifier:];
```
