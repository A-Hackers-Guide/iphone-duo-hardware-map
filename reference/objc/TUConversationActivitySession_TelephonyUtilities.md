# `TUConversationActivitySession`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 25 instance variables, 26 properties, 63 instance methods, 1 class methods

## Instance variables

```
B _isLocallyInitiated;
B _isLightweightPrimaryInitiated;
B _isFirstJoin;
B _permittedToJoin;
B _localParticipantActive;
B _didAssociateScene;
B _persistentSceneIsEligibleForAutoClose;
B _usingAirplay;
B _isStageInitiated;
@"NSDate" _timestamp;
@"NSUUID" _UUID;
@"TUConversationActivity" _activity;
Q _state;
@"NSXPCListenerEndpoint" _endpoint;
@"NSNumber" _clientAudioSessionID;
@"NSSet" _activeRemoteParticipants;
@"NSArray" _persistentSceneIdentifiers;
@"NSString" _primarySceneAssociationIdentifier;
Q _distributionCount;
Q _applicationState;
@"NSArray" _externalParticipants;
@"TUHandle" _terminatingHandle;
@"NSDate" _localCreationTimestamp;
@"NSDate" _permittedJoinTimestamp;
@"NSDictionary" _participantIdentifierMap;
```

## Properties

```
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"TUConversationActivity",&,N,V_activity) activity;
@property (TQ,N,V_state) state;
@property (T@"NSXPCListenerEndpoint",&,N,V_endpoint) endpoint;
@property (TB,N,V_isLocallyInitiated) isLocallyInitiated;
@property (TB,N,GisUsingAirplay,V_usingAirplay) usingAirplay;
@property (T@"NSDate",&,N,V_localCreationTimestamp) localCreationTimestamp;
@property (T@"NSDate",&,N,V_permittedJoinTimestamp) permittedJoinTimestamp;
@property (TB,N,V_isStageInitiated) isStageInitiated;
@property (T@"NSDictionary",&,N,V_participantIdentifierMap) participantIdentifierMap;
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (T@"NSNumber",&,N,V_clientAudioSessionID) clientAudioSessionID;
@property (TB,N,V_isLightweightPrimaryInitiated) isLightweightPrimaryInitiated;
@property (TB,R,N,V_isFirstJoin) isFirstJoin;
@property (TB,N,GisPermittedToJoin,V_permittedToJoin) permittedToJoin;
@property (TB,R,N,GisLocalParticipantActive,V_localParticipantActive) localParticipantActive;
@property (T@"NSSet",R,N,V_activeRemoteParticipants) activeRemoteParticipants;
@property (T@"NSString",&,N) persistentSceneIdentifier;
@property (T@"NSArray",&,N,V_persistentSceneIdentifiers) persistentSceneIdentifiers;
@property (TB,N,V_didAssociateScene) didAssociateScene;
@property (T@"NSString",&,N,V_primarySceneAssociationIdentifier) primarySceneAssociationIdentifier;
@property (TB,N,V_persistentSceneIsEligibleForAutoClose) persistentSceneIsEligibleForAutoClose;
@property (TQ,N,V_distributionCount) distributionCount;
@property (TQ,R,N,V_applicationState) applicationState;
@property (T@"NSArray",&,N,V_externalParticipants) externalParticipants;
@property (T@"TUHandle",&,N,V_terminatingHandle) terminatingHandle;
```

## Class methods

```
+[TUConversationActivitySession supportsSecureCoding];
```

## Instance methods

```
-[TUConversationActivitySession setTimestamp:];
-[TUConversationActivitySession setActivity:];
-[TUConversationActivitySession setState:];
-[TUConversationActivitySession mutableCopyWithZone:];
-[TUConversationActivitySession setEndpoint:];
-[TUConversationActivitySession applicationState];
-[TUConversationActivitySession setUUID:];
-[TUConversationActivitySession UUID];
-[TUConversationActivitySession timestamp];
-[TUConversationActivitySession endpoint];
-[TUConversationActivitySession activity];
-[TUConversationActivitySession encodeWithCoder:];
-[TUConversationActivitySession hash];
-[TUConversationActivitySession description];
-[TUConversationActivitySession initWithCoder:];
-[TUConversationActivitySession copyWithZone:];
-[TUConversationActivitySession isEqual:];
-[TUConversationActivitySession state];
-[TUConversationActivitySession activeRemoteParticipants];
-[TUConversationActivitySession persistentSceneIdentifier];
-[TUConversationActivitySession setPersistentSceneIdentifier:];
-[TUConversationActivitySession isUsingAirplay];
-[TUConversationActivitySession clientAudioSessionID];
-[TUConversationActivitySession didAssociateScene];
-[TUConversationActivitySession distributionCount];
-[TUConversationActivitySession externalParticipants];
-[TUConversationActivitySession initWithActivity:locallyInitiated:timestamp:isFirstJoin:];
-[TUConversationActivitySession initWithActivity:state:endpoint:locallyInitiated:timestamp:isFirstJoin:];
-[TUConversationActivitySession initWithActivity:state:uuid:endpoint:locallyInitiated:timestamp:isFirstJoin:activeRemoteParticipants:isLocalParticipantActive:applicationState:];
-[TUConversationActivitySession initWithActivity:uuid:locallyInitiated:timestamp:isFirstJoin:];
-[TUConversationActivitySession initWithTUConversationActivitySession:];
-[TUConversationActivitySession isEqualToConversationActivitySession:];
-[TUConversationActivitySession isFirstJoin];
-[TUConversationActivitySession isLightweightPrimaryInitiated];
-[TUConversationActivitySession isLocalParticipantActive];
-[TUConversationActivitySession isLocallyInitiated];
-[TUConversationActivitySession isPermittedToJoin];
-[TUConversationActivitySession isStageInitiated];
-[TUConversationActivitySession launchApplicationWithForcedURL:completion:];
-[TUConversationActivitySession localCreationTimestamp];
-[TUConversationActivitySession participantIdentifierMap];
-[TUConversationActivitySession permittedJoinTimestamp];
-[TUConversationActivitySession persistentSceneIdentifiers];
-[TUConversationActivitySession persistentSceneIsEligibleForAutoClose];
-[TUConversationActivitySession primarySceneAssociationIdentifier];
-[TUConversationActivitySession publicCopy];
-[TUConversationActivitySession setClientAudioSessionID:];
-[TUConversationActivitySession setDidAssociateScene:];
-[TUConversationActivitySession setDistributionCount:];
-[TUConversationActivitySession setExternalParticipants:];
-[TUConversationActivitySession setIsLightweightPrimaryInitiated:];
-[TUConversationActivitySession setIsLocallyInitiated:];
-[TUConversationActivitySession setIsStageInitiated:];
-[TUConversationActivitySession setLocalCreationTimestamp:];
-[TUConversationActivitySession setParticipantIdentifierMap:];
-[TUConversationActivitySession setPermittedJoinTimestamp:];
-[TUConversationActivitySession setPermittedToJoin:];
-[TUConversationActivitySession setPersistentSceneIdentifiers:];
-[TUConversationActivitySession setPersistentSceneIsEligibleForAutoClose:];
-[TUConversationActivitySession setPrimarySceneAssociationIdentifier:];
-[TUConversationActivitySession setTerminatingHandle:];
-[TUConversationActivitySession setUsingAirplay:];
-[TUConversationActivitySession terminatingHandle];
```
