# `TUCallNotificationManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 85 instance methods, 0 class methods

## Instance variables

```
B _wantsCallNotifications;
@"NSNotificationCenter" _notificationCenter;
@"NSMutableArray" _deferredNotificationBlocks;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_deferredNotificationBlocks) deferredNotificationBlocks;
@property (TB,R,N,V_wantsCallNotifications) wantsCallNotifications;
@property (T@"NSNotificationCenter",R,N,V_notificationCenter) notificationCenter;
```

## Instance methods

```
-[TUCallNotificationManager notificationCenter];
-[TUCallNotificationManager videoCaptureModeChangedForCall:];
-[TUCallNotificationManager anyRemoteSupportsRequestToScreenShareChangedForCall:];
-[TUCallNotificationManager callTranslationAvailabilityChangedForCall:newValue:];
-[TUCallNotificationManager isOnHoldChangedForCall:];
-[TUCallNotificationManager audioPropertiesChangedForCall:];
-[TUCallNotificationManager prefersExclusiveAccessToCellularNetworkChangedForCall:];
-[TUCallNotificationManager isEmergencyChangedForCall:];
-[TUCallNotificationManager receptionistSessionChangedForCall:];
-[TUCallNotificationManager remoteUplinkMutedChangedForCall:];
-[TUCallNotificationManager initWithNotificationCenter:wantsCallNotifications:];
-[TUCallNotificationManager postNotificationsForCall:afterUpdatesInBlock:];
-[TUCallNotificationManager wantsHoldMusicChangedForCall:];
-[TUCallNotificationManager callRecordingAvailabilityChangedForCall:];
-[TUCallNotificationManager faceTimeIDStatusChangedForCall:];
-[TUCallNotificationManager cameraTypeChangedForCall:];
-[TUCallNotificationManager mixesVoiceWithMediaChangedForCall:];
-[TUCallNotificationManager callSubtypeChangedForCall:];
-[TUCallNotificationManager hasBeenRedirectedChangedForCall:];
-[TUCallNotificationManager remoteCameraOrientationChangedForCall:];
-[TUCallNotificationManager hasSentInvitationChangedForCall:];
-[TUCallNotificationManager deferNotificationsUntilAfterPerformingBlock:];
-[TUCallNotificationManager displayContextChangedForCall:];
-[TUCallNotificationManager connectedChangedForCall:];
-[TUCallNotificationManager wantsCallNotifications];
-[TUCallNotificationManager isUsingBasebandChangedForCall:];
-[TUCallNotificationManager sharingScreenChangedForCall:];
-[TUCallNotificationManager postNotificationsForCallContainer:afterUpdatesInBlock:];
-[TUCallNotificationManager canAnswerCallChangedForCall:];
-[TUCallNotificationManager ttyTypeChangedForCall:];
-[TUCallNotificationManager remoteAspectRatioChangedForCall:];
-[TUCallNotificationManager shouldSuppressRingtoneChangedForCall:];
-[TUCallNotificationManager providerContextChangedForCall:];
-[TUCallNotificationManager _postNotificationName:object:];
-[TUCallNotificationManager postNotificationsForCall:usingComparisonCall:];
-[TUCallNotificationManager statusChangedForCall:];
-[TUCallNotificationManager connectingChangedForCall:];
-[TUCallNotificationManager isScreeningChangedForCall:];
-[TUCallNotificationManager callGroupUUIDChangedForCall:];
-[TUCallNotificationManager answeringMachineStreamTokenChangedForCall:];
-[TUCallNotificationManager supportsDTMFUpdatesChangedForCall:];
-[TUCallNotificationManager conferenceParticipantCallsChangedForCallContainer:conferenceParticipantCalls:];
-[TUCallNotificationManager isThirdPartyVideoChangedForCall:];
-[TUCallNotificationManager callRecordingStateChanged:];
-[TUCallNotificationManager mediaTokensChangedForCall:];
-[TUCallNotificationManager nearbyModeChangedForCall:];
-[TUCallNotificationManager videoStreamTokenChangedForCall:];
-[TUCallNotificationManager conversationChangedForCall:];
-[TUCallNotificationManager needsManualInCallSoundsChangedForCall:];
-[TUCallNotificationManager hasReceptionistSessionChangedFromOldSession:newSession:];
-[TUCallNotificationManager smartHoldingSessionChanged:];
-[TUCallNotificationManager remoteScreenOrientationChangedForCall:];
-[TUCallNotificationManager callTranslationStateChanged:];
-[TUCallNotificationManager remoteVideoContentRectChangedForCall:];
-[TUCallNotificationManager bluetoothAudioFormatChangedForCall:];
-[TUCallNotificationManager isFailureExpectedChangedForCall:];
-[TUCallNotificationManager isSharePlayCapableChangedForCall:];
-[TUCallNotificationManager _postNotificationName:object:userInfo:];
-[TUCallNotificationManager receptionistStateChangedForCall:oldValue:];
-[TUCallNotificationManager postNotificationsForCall:usingComparisonCall:afterUpdatesInBlock:];
-[TUCallNotificationManager modelChangedForCall:];
-[TUCallNotificationManager setDeferredNotificationBlocks:];
-[TUCallNotificationManager endpointOnCurrentDeviceChangedForCall:];
-[TUCallNotificationManager receptionistMessageChangedForCall:];
-[TUCallNotificationManager remoteScreenAspectRatioChangedForCall:];
-[TUCallNotificationManager initWithNotificationCenter:];
-[TUCallNotificationManager isUplinkMutedChangedForCall:];
-[TUCallNotificationManager screeningAnnouncementFinishedChangedForCall:];
-[TUCallNotificationManager mediaPropertiesChangedForCall:remoteAspectRatioDidChange:remoteCameraOrientationDidChange:];
-[TUCallNotificationManager resolvedStatusChangedForCall:];
-[TUCallNotificationManager supportsTTYWithVoiceChangedForCall:];
-[TUCallNotificationManager videoDegradedChangedForCall:];
-[TUCallNotificationManager supportsEmergencyFallbackChangedForCall:];
-[TUCallNotificationManager videoPausedChangedForCall:];
-[TUCallNotificationManager localSenderIdentityAccountUUIDChangedForCall:];
-[TUCallNotificationManager destinationIDChangedForCall:];
-[TUCallNotificationManager hardPauseDigitsStateChangedForCall:];
-[TUCallNotificationManager conversationGroupUUIDChangedForCall:];
-[TUCallNotificationManager hasSmartHoldingSessionChangedFromOldSession:newSession:];
-[TUCallNotificationManager videoMirroredChangedForCall:];
-[TUCallNotificationManager isSendingAudioChangedForCall:];
-[TUCallNotificationManager callContextCardsChanged:];
-[TUCallNotificationManager isSendingVideoChangedForCall:];
-[TUCallNotificationManager deferredNotificationBlocks];
-[TUCallNotificationManager mediaStalledChangedForCall:];
```
