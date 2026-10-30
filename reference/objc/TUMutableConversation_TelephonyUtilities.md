# `TUMutableConversation`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TUConversation`
- 1 instance variables, 51 properties, 2 instance methods, 0 class methods

## Instance variables

```
B _relaying;
```

## Properties

```
@property (TQ,D,N) avMode;
@property (TQ,D,N) presentationMode;
@property (T@"TUConversationLink",&,D,N) link;
@property (Tq,D,N) state;
@property (Tq,D,N) letMeInRequestState;
@property (Tq,D,N) avcSessionToken;
@property (Tq,D,N) localCaptionToken;
@property (T@"NSString",C,D,N) avcSessionIdentifier;
@property (TB,D,N,GisAudioEnabled) audioEnabled;
@property (TB,D,N,GisVideoEnabled) videoEnabled;
@property (TQ,D,N) videoCaptureMode;
@property (TQ,D,N) videoMode;
@property (TB,D,N,GisScreenEnabled) screenEnabled;
@property (TB,D,N,GisLocallyCreated) locallyCreated;
@property (TB,D,N,GhasJoined) hasJoined;
@property (TB,D,N,GisVideo) video;
@property (T@"TUConversationMember",&,D,N) localMember;
@property (TQ,D,N) localParticipantIdentifier;
@property (T@"NSSet",C,D,N) remoteMembers;
@property (T@"NSSet",C,D,N) pendingMembers;
@property (T@"NSSet",C,D,N) rejectedMembers;
@property (T@"NSSet",C,D,N) lightweightMembers;
@property (T@"NSUUID",&,D,N) messagesGroupUUID;
@property (T@"NSSet",C,D,N) participantHandles;
@property (T@"NSSet",C,D,N) activeRemoteParticipants;
@property (T@"NSSet",C,D,N) activeQROnlyParticipants;
@property (T@"TUHandle",&,D,N) initiator;
@property (T@"NSString",C,D,N) messagesGroupName;
@property (Tq,D,N) maxVideoDecodesAllowed;
@property (T@"NSObject",&,D,N) reportingHierarchyToken;
@property (T@"NSObject",&,D,N) reportingHierarchySubToken;
@property (T@"TUConversationReport",C,D,N) report;
@property (TB,D,N,GisOneToOneModeEnabled) oneToOneModeEnabled;
@property (T@"TUConversationParticipantAssociation",&,D,N) localParticipantAssociation;
@property (TB,D,N,GisOneToOneHandoffOngoing) oneToOneHandoffOngoing;
@property (T@"TUConversationHandoffEligibility",&,D,N) handoffEligibility;
@property (TB,D,N,GisBackedByGroupSession) backedByGroupSession;
@property (T@"NSSet",C,D,N) activitySessions;
@property (T@"NSSet",C,D,N) systemActivitySessions;
@property (T@"NSSet",C,D,N) virtualParticipants;
@property (T@"NSSet",C,D,N) invitationPreferences;
@property (TB,D,N,GisScreening) screening;
@property (TB,N,GisRelaying,V_relaying) relaying;
@property (T@"<TUFeatureFlags>",&,D,N) featureFlags;
@property (TB,D,N,GisSpatialPersonaEnabled) spatialPersonaEnabled;
@property (TB,D,N,GisCameraMixedWithScreen) cameraMixedWithScreen;
@property (T@"TUConversationHandoffContext",&,D,N) handoffContext;
@property (T@"TUConversationParticipantCluster",C,D,N) localParticipantCluster;
@property (TB,D,N,GisNearbySession) nearbySession;
@property (TB,D,N) isNearbySharePlay;
@property (T@"NSArray",C,D,N) supportedMediaTypes;
```

## Instance methods

```
-[TUMutableConversation setRelaying:];
-[TUMutableConversation isRelaying];
```
