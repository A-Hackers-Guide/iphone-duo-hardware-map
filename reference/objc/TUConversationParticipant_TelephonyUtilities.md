# `TUConversationParticipant`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 30 instance variables, 31 properties, 70 instance methods, 1 class methods

## Instance variables

```
B _muted;
B _audioEnabled;
B _videoEnabled;
B _screenEnabled;
B _audioPaused;
B _lightweight;
B _localAccountHandle;
B _isAccessibilityInterpreter;
B _guestModeEnabled;
B _spatialPersonaEnabled;
B _cameraMixedWithScreen;
B _isNearbySharePlay;
Q _identifier;
@"TUHandle" _handle;
Q _audioVideoMode;
Q _videoCaptureMode;
@"TUConversationParticipantCapabilities" _capabilities;
q _streamToken;
q _secondaryStreamToken;
q _screenToken;
q _captionsToken;
q _audioPriority;
q _videoPriority;
@"NSString" _avcIdentifier;
@"NSString" _activeIDSDestination;
@"TUConversationParticipantAssociation" _association;
@"TUConversationParticipantLinkAssociation" _linkAssociation;
Q _presentationMode;
@"NSString" _senderCorrelationIdentifier;
@"TUConversationParticipantCluster" _cluster;
```

## Properties

```
@property (TB,N,GisMuted,V_muted) muted;
@property (TB,N,GisAudioEnabled,V_audioEnabled) audioEnabled;
@property (TB,N,GisVideoEnabled,V_videoEnabled) videoEnabled;
@property (TQ,N,V_videoCaptureMode) videoCaptureMode;
@property (TQ,N) videoMode;
@property (TB,N,GisScreenEnabled,V_screenEnabled) screenEnabled;
@property (TB,N,GisAudioPaused,V_audioPaused) audioPaused;
@property (TB,N,GisLightweight,V_lightweight) lightweight;
@property (TB,N,GisNearbySharePlay,V_isNearbySharePlay) isNearbySharePlay;
@property (TB,N,GisLocalAccountHandle,V_localAccountHandle) localAccountHandle;
@property (TB,N,GisGuestModeEnabled,V_guestModeEnabled) guestModeEnabled;
@property (TQ,N,V_audioVideoMode) audioVideoMode;
@property (TQ,N,V_presentationMode) presentationMode;
@property (TB,N,GisSpatialPersonaEnabled,V_spatialPersonaEnabled) spatialPersonaEnabled;
@property (TB,N,GisCameraMixedWithScreen,V_cameraMixedWithScreen) cameraMixedWithScreen;
@property (Tq,N,V_streamToken) streamToken;
@property (Tq,N,V_secondaryStreamToken) secondaryStreamToken;
@property (Tq,N,V_screenToken) screenToken;
@property (Tq,N,V_captionsToken) captionsToken;
@property (Tq,N,V_audioPriority) audioPriority;
@property (Tq,N,V_videoPriority) videoPriority;
@property (T@"NSString",C,N,V_avcIdentifier) avcIdentifier;
@property (T@"NSString",C,N,V_activeIDSDestination) activeIDSDestination;
@property (T@"TUConversationParticipantCapabilities",C,N,V_capabilities) capabilities;
@property (T@"TUConversationParticipantAssociation",C,N,V_association) association;
@property (T@"TUConversationParticipantLinkAssociation",C,N,V_linkAssociation) linkAssociation;
@property (TB,N,V_isAccessibilityInterpreter) isAccessibilityInterpreter;
@property (T@"TUConversationParticipantCluster",C,N,V_cluster) cluster;
@property (TQ,R,N,V_identifier) identifier;
@property (T@"TUHandle",R,C,N,V_handle) handle;
@property (T@"NSString",R,C,N,V_senderCorrelationIdentifier) senderCorrelationIdentifier;
```

## Class methods

```
+[TUConversationParticipant supportsSecureCoding];
```

## Instance methods

```
-[TUConversationParticipant setMuted:];
-[TUConversationParticipant isScreenEnabled];
-[TUConversationParticipant isMuted];
-[TUConversationParticipant setStreamToken:];
-[TUConversationParticipant setCameraMixedWithScreen:];
-[TUConversationParticipant isVideoEnabled];
-[TUConversationParticipant secondaryStreamToken];
-[TUConversationParticipant presentationMode];
-[TUConversationParticipant setAudioPaused:];
-[TUConversationParticipant setAudioEnabled:];
-[TUConversationParticipant videoCaptureMode];
-[TUConversationParticipant mutableCopyWithZone:];
-[TUConversationParticipant setPresentationMode:];
-[TUConversationParticipant isAudioEnabled];
-[TUConversationParticipant setCluster:];
-[TUConversationParticipant setSpatialPersonaEnabled:];
-[TUConversationParticipant videoMode];
-[TUConversationParticipant streamToken];
-[TUConversationParticipant videoPriority];
-[TUConversationParticipant setScreenToken:];
-[TUConversationParticipant setVideoEnabled:];
-[TUConversationParticipant setScreenEnabled:];
-[TUConversationParticipant setVideoCaptureMode:];
-[TUConversationParticipant setGuestModeEnabled:];
-[TUConversationParticipant isAudioPaused];
-[TUConversationParticipant identifier];
-[TUConversationParticipant setLinkAssociation:];
-[TUConversationParticipant initWithIdentifier:handle:senderCorrelationIdentifier:];
-[TUConversationParticipant setCaptionsToken:];
-[TUConversationParticipant isLightweight];
-[TUConversationParticipant setVideoMode:];
-[TUConversationParticipant setIsNearbySharePlay:];
-[TUConversationParticipant captionsToken];
-[TUConversationParticipant audioPriority];
-[TUConversationParticipant setAudioPriority:];
-[TUConversationParticipant isNearbySharePlay];
-[TUConversationParticipant setIsAccessibilityInterpreter:];
-[TUConversationParticipant setLocalAccountHandle:];
-[TUConversationParticipant avcIdentifier];
-[TUConversationParticipant setAvcIdentifier:];
-[TUConversationParticipant setAssociation:];
-[TUConversationParticipant isEqualToParticipant:];
-[TUConversationParticipant handle];
-[TUConversationParticipant setVideoPriority:];
-[TUConversationParticipant senderCorrelationIdentifier];
-[TUConversationParticipant association];
-[TUConversationParticipant initWithConversationParticipant:];
-[TUConversationParticipant encodeWithCoder:];
-[TUConversationParticipant setSecondaryStreamToken:];
-[TUConversationParticipant capabilities];
-[TUConversationParticipant hash];
-[TUConversationParticipant setAudioVideoMode:];
-[TUConversationParticipant isGuestModeEnabled];
-[TUConversationParticipant cluster];
-[TUConversationParticipant isLocalAccountHandle];
-[TUConversationParticipant description];
-[TUConversationParticipant initWithCoder:];
-[TUConversationParticipant setLightweight:];
-[TUConversationParticipant copyWithZone:];
-[TUConversationParticipant activeIDSDestination];
-[TUConversationParticipant linkAssociation];
-[TUConversationParticipant setCapabilities:];
-[TUConversationParticipant isEqual:];
-[TUConversationParticipant audioVideoMode];
-[TUConversationParticipant isAccessibilityInterpreter];
-[TUConversationParticipant isCameraMixedWithScreen];
-[TUConversationParticipant screenToken];
-[TUConversationParticipant setActiveIDSDestination:];
-[TUConversationParticipant initWithIdentifier:handle:];
-[TUConversationParticipant isSpatialPersonaEnabled];
```
