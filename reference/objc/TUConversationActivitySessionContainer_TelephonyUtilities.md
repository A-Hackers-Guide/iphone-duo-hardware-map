# `TUConversationActivitySessionContainer`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 13 instance variables, 14 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
@"NSUUID" _groupUUID;
q _state;
@"NSSet" _activitySessions;
@"NSSet" _remoteMembers;
@"TUConversationMember" _localMember;
@"TUHandle" _initiator;
Q _localParticipantIdentifier;
@"NSSet" _virtualParticipants;
@"TUConversationVirtualParticipantConfig" _virtualParticipantConfig;
@"TUConversationUnreliableMessengerConfig" _unreliableMessengerConfig;
@"NSSet" _activeRemoteParticipants;
Q _capabilities;
```

## Properties

```
@property (T@"NSString",N,R) capabilitiesDescription;
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"NSUUID",&,N,V_groupUUID) groupUUID;
@property (Tq,N,V_state) state;
@property (T@"NSSet",C,N,V_activitySessions) activitySessions;
@property (T@"NSSet",C,N,V_remoteMembers) remoteMembers;
@property (T@"TUConversationMember",&,N,V_localMember) localMember;
@property (T@"TUHandle",&,N,V_initiator) initiator;
@property (TQ,N,V_localParticipantIdentifier) localParticipantIdentifier;
@property (T@"NSSet",C,N,V_virtualParticipants) virtualParticipants;
@property (T@"TUConversationVirtualParticipantConfig",C,N,V_virtualParticipantConfig) virtualParticipantConfig;
@property (T@"TUConversationUnreliableMessengerConfig",C,N,V_unreliableMessengerConfig) unreliableMessengerConfig;
@property (T@"NSSet",C,N,V_activeRemoteParticipants) activeRemoteParticipants;
@property (TQ,N,V_capabilities) capabilities;
```

## Class methods

```
+[TUConversationActivitySessionContainer supportsSecureCoding];
```

## Instance methods

```
-[TUConversationActivitySessionContainer setInitiator:];
-[TUConversationActivitySessionContainer initiator];
-[TUConversationActivitySessionContainer activitySessions];
-[TUConversationActivitySessionContainer setGroupUUID:];
-[TUConversationActivitySessionContainer groupUUID];
-[TUConversationActivitySessionContainer setState:];
-[TUConversationActivitySessionContainer virtualParticipantConfig];
-[TUConversationActivitySessionContainer virtualParticipants];
-[TUConversationActivitySessionContainer setUUID:];
-[TUConversationActivitySessionContainer UUID];
-[TUConversationActivitySessionContainer setActivitySessions:];
-[TUConversationActivitySessionContainer isEqualToContainer:];
-[TUConversationActivitySessionContainer capabilitiesDescription];
-[TUConversationActivitySessionContainer setUnreliableMessengerConfig:];
-[TUConversationActivitySessionContainer setVirtualParticipants:];
-[TUConversationActivitySessionContainer setLocalParticipantIdentifier:];
-[TUConversationActivitySessionContainer encodeWithCoder:];
-[TUConversationActivitySessionContainer setRemoteMembers:];
-[TUConversationActivitySessionContainer capabilities];
-[TUConversationActivitySessionContainer hash];
-[TUConversationActivitySessionContainer setLocalMember:];
-[TUConversationActivitySessionContainer description];
-[TUConversationActivitySessionContainer initWithCoder:];
-[TUConversationActivitySessionContainer setVirtualParticipantConfig:];
-[TUConversationActivitySessionContainer setActiveRemoteParticipants:];
-[TUConversationActivitySessionContainer copyWithZone:];
-[TUConversationActivitySessionContainer localMember];
-[TUConversationActivitySessionContainer setCapabilities:];
-[TUConversationActivitySessionContainer isEqual:];
-[TUConversationActivitySessionContainer unreliableMessengerConfig];
-[TUConversationActivitySessionContainer localParticipantIdentifier];
-[TUConversationActivitySessionContainer state];
-[TUConversationActivitySessionContainer activeRemoteParticipants];
-[TUConversationActivitySessionContainer remoteMembers];
```
