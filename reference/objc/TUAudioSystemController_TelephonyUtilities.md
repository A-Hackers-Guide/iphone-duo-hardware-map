# `TUAudioSystemController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUAudioController`
- 36 instance variables, 10 properties, 43 instance methods, 5 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _uplinkMutedQueue;
@"NSObject<OS_dispatch_queue>" _downlinkMutedQueue;
@"NSObject<OS_dispatch_queue>" _ttyQueue;
@"NSObject<OS_dispatch_queue>" _pickableRoutesQueue;
@"NSNumber" _isUplinkMutedCached;
@"NSNumber" _isDownlinkMutedCached;
@"NSNumber" _isTTYCached;
@"NSArray" _pickableRoutesForTTY;
@"NSArray" _pickableRoutesForPhoneCall;
@"NSArray" _pickableRoutesForPlayAndRecordVideo;
@"NSArray" _pickableRoutesForPlayAndRecordVoice;
@"NSArray" _pickableRoutesForPlayAndRecordRemoteVoice;
@"NSArray" _pickableRoutesForVoicemail;
@"NSArray" _currentPickableRoutes;
@"NSArray" _currentDisabledRoutes;
@"NSString" _lastPickedRouteIdentifier;
B _isRequestingUplinkMuted;
B _isRequestingDownlinkMuted;
B _isRequestingTTY;
B _isRequestingPickableRoutesForTTY;
B _isRequestingPickableRoutesForPhoneCall;
B _isRequestingPickableRoutesForPlayAndRecordVideo;
B _isRequestingPickableRoutesForPlayAndRecordVoice;
B _isRequestingPickableRoutesForPlayAndRecordRemoteVoice;
B _isRequestingPickableRoutesForVoicemail;
Q _lastUplinkMutedRequestScheduleTime;
Q _lastDownlinkMutedRequestScheduleTime;
Q _lastTTYRequestScheduleTime;
Q _lastTTYPickableRoutesScheduleTime;
Q _lastPhoneCallCategoryRoutesScheduleTime;
Q _lastPlayAndRecordVideoRoutesScheduleTime;
Q _lastPlayAndRecordVoiceRoutesScheduleTime;
Q _lastPlayAndRecordRemoteVoiceRoutesScheduleTime;
Q _lastVoicemailRoutesScheduleTime;
@"<TUFeatureFlags>" _featureFlags;
@"<TUAudioSystemControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<TUAudioSystemControllerDelegate>",W,N,V_delegate) delegate;
@property (Tf,N) activeCategoryVolume;
@property (TB,N,GisUplinkMuted) uplinkMuted;
@property (TB,N,GisDownlinkMuted) downlinkMuted;
@property (TB,R,N,GisTTY) tty;
@property (T@"NSDictionary",R,C,N) pickedRouteAttribute;
@property (T@"NSArray",R,C,N) bestGuessPickableRoutesForAnyCall;
@property (T@"NSArray",R,C,N) pickableRoutesForTTY;
@property (T@"NSArray",R,C,N) disabledRoutes;
@property (TB,R,N) otherSessionsRequestNoRingtoneInterruption;
```

## Class methods

```
+[TUAudioSystemController filteredPickableRoutesFromPickableRoutes:];
+[TUAudioSystemController isPhoneCallAudioCategory:];
+[TUAudioSystemController sharedAudioSystemController];
+[TUAudioSystemController sharedSystemController];
+[TUAudioSystemController sourceIdentifierForRouteID:];
```

## Instance methods

```
-[TUAudioSystemController _mediaServicesWereReset:];
-[TUAudioSystemController _pickableRoutesForVoiceMailWithForceNewRequest:];
-[TUAudioSystemController _pickableRoutesForPlayAndRecordVoiceWithForceNewRequest:];
-[TUAudioSystemController pickableRoutesForActiveCall];
-[TUAudioSystemController switchBluetoothAudioFormats];
-[TUAudioSystemController activeCategoryVolume];
-[TUAudioSystemController pickableRoutesForTTY];
-[TUAudioSystemController init];
-[TUAudioSystemController _handleDownlinkMuteDidChangeNotification:];
-[TUAudioSystemController shouldSuppressCallUsingRoute:];
-[TUAudioSystemController clearUplinkMutedCache];
-[TUAudioSystemController _handlePickableRoutesDidChangeNotification:];
-[TUAudioSystemController dealloc];
-[TUAudioSystemController isUplinkMuted];
-[TUAudioSystemController _updateCachedDisabledRoutes:];
-[TUAudioSystemController setDownlinkMuted:];
-[TUAudioSystemController setActiveCategoryVolume:];
-[TUAudioSystemController _updateCachedState];
-[TUAudioSystemController _pickableRoutesForPlayAndRecordVideoWithForceNewRequest:];
-[TUAudioSystemController _pickableRoutesForPhoneCallWithForceNewRequest:];
-[TUAudioSystemController pickableRouteWithUniqueIdentifier:];
-[TUAudioSystemController setDelegate:];
-[TUAudioSystemController _handleUplinkMuteDidChangeNotification:];
-[TUAudioSystemController _pickableRoutesForTTYWithForceNewRequest:];
-[TUAudioSystemController isTTY];
-[TUAudioSystemController _pickedRouteIdentifier];
-[TUAudioSystemController delegate];
-[TUAudioSystemController setUplinkMuted:];
-[TUAudioSystemController currentlyPickedRouteIdForCategory:andMode:];
-[TUAudioSystemController triggerEndInterruptionForAudioSessionID:];
-[TUAudioSystemController _subscribeToNotificationAttributes];
-[TUAudioSystemController _pickableRoutesForPlayAndRecordRemoteVoiceWithForceNewRequest:];
-[TUAudioSystemController getPickableRoutesForCategory:mode:completion:];
-[TUAudioSystemController pickRoute:error:];
-[TUAudioSystemController bestGuessPickableRoutesForAnyCall];
-[TUAudioSystemController pickedRouteAttribute];
-[TUAudioSystemController isDownlinkMuted];
-[TUAudioSystemController otherSessionsRequestNoRingtoneInterruption];
-[TUAudioSystemController pickableRoutesForCategory:andMode:];
-[TUAudioSystemController _handleVolumeDidChangeNotification:];
-[TUAudioSystemController _loadCurrentPickableRoutesWithCompletion:];
-[TUAudioSystemController disabledRoutes];
-[TUAudioSystemController _getPickableRoutesForCategory:mode:onlyKnownCombinations:completion:];
```
