# `/System/Library/PrivateFrameworks/AccessoryCommunications.framework/AccessoryCommunications`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 2 classes, 3 protocols, 82 methods, 19 properties

### Class pages

Every class and protocol, with its methods: [`ACCCommunicationsCenter`](../objc/ACCCommunicationsCenter_AccessoryCommunications.md), [`ACCCommunicationsXPCClientProtocol`](../objc/ACCCommunicationsXPCClientProtocol_AccessoryCommunications.protocol.md), [`ACCCommunicationsXPCServerProtocol`](../objc/ACCCommunicationsXPCServerProtocol_AccessoryCommunications.protocol.md), [`NSObject`](../objc/NSObject_AccessoryCommunications.protocol.md)

### Classes

`ACCCommunicationsCenter`, `NSArray`

### Protocols

`ACCCommunicationsXPCClientProtocol`, `ACCCommunicationsXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCCommunicationsXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSSet",&,N,V_subscriberList) subscriberList;
@property (T@"NSMutableDictionary",&,V_callStateCache) callStateCache;
@property (T@"NSMutableDictionary",&,V_cachedCommStatus) cachedCommStatus;
@property (T@"<ACCCommunicationsCenterCallStateDelegate>",W,N,V_callStateDelegate) callStateDelegate;
@property (T@"<ACCCommunicationsCenterCommunicationsDelegate>",W,N,V_communicationsDelegate) communicationsDelegate;
@property (T@"<ACCCommunicationsCenterCallControlsDelegate>",W,N,V_callControlsDelegate) callControlsDelegate;
@property (T@"<ACCCommunicationsCenterListUpdatesDelegate>",W,N,V_listUpdatesDelegate) listUpdatesDelegate;
@property (TQ,R,N,V_maxRecentsListEntries) maxRecentsListEntries;
@property (TQ,R,N,V_maxFavoritesListEntries) maxFavoritesListEntries;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (120)

```
com.apple.accessories.communications
Duration
e
General
accessoryServer_isServerAvailableForServiceEntry
Direction
AddressBookID
SignalStrength
FaceTimeAudioEnabled
HoldAndAcceptAvailable
com.apple.accessories.frameworks
Endpoint
MuteStatus
v16@?0@\"NSError\"8
v8@?0
CallUUID
MergeAvailable
Occurrences
ListUpdates_Favorites
CurrentCallCount
Transport
DisconnectReason
AirplaneModeStatus
i
<Undefined>
_SetupAvailabilityChangedHandlerForServiceEntry
StartTimestamp
SwapAvailable
Connection
RegistrationStatus
TelephonyEnabled
FaceTimeVideoEnabled
HoldAvailable
ListUpdates_Recents
UnixTimestamp
ListUpdates_Recents_Coalesced
TTYStatus
YES
InitiateCallAvailable
v12@?0B8
Label
EndAndAcceptAvailable
CallStateUpdates
null
NO
Status
NewVoicemailCount
com.apple.accessories.communications.availability-changed
v12@?0i8
com.apple.accessories.signposts
DisplayName
CellularSupported
Type
RemoteID
Service
CommunicationsUpdates
IsConferenced
ConferenceGroup
CarrierName
%s cannot get server state (%d, %s)
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
filteredCommStatus: %@
XPC connection interrupted!
commStatus: %@
Received recents list update! (coalesced)
Triggering communications update...
Created %d log object(s)!
Register AvailabilityChangedHandler (%d, %s)
Trying to connect to server...
Removing call state from cache (callUUID: %@)...
Getting remote object...
Accepting call with acceptAction: %{coreacc:ACCCommunications_CallControls_AcceptAction_t}d, callUUID: %@
%s (%d)
Triggering call state updates for current calls...
shouldStayConnected: %d
recentsList.count: %lu (capped) (coalesced)
Received favorites list update!
This client doesn't handle %{coreacc:ACCCommunications_ListUpdate_Type_t}d list updates!
%s did not register for notification (%d, %s), token (%d)
XPC connection invalidated!
XPC connection error: %@
recentsList.count: %lu
favoritesList.count: %lu
Updating hold status to: %s for callUUID: %@...
Failed to create os_log_t object %s: %s!
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
Unregister AvailabilityChangedHandler (%d, %s)
Ignoring duplicate call state update for callUUID: %@!
Received comm status update!
favoritesList.count: %lu (capped)
Initiating call to destinationID: %{private}@, withService: %{coreacc:ACCCommunications_CallService_t}d, addressBookID: %@...
Ending all calls...
Server availability changed! State: %d
Received subscriberList update: %@
This client doesn't handle call state updates!
Initiating redial...
Merging calls...
Sending DTMF tone: %{coreacc:ACCCommunications_CallControls_DTMFTone_t}d for callUUID: %@
List unavailable! (listType: %{coreacc:ACCCommunications_ListUpdate_Type_t}d)
Initiating call to voicemail...
%s (%d, %s)
Received call state update for callUUID: %@!
callState: %@
cachedCallState: %@
recentsList.count: %lu (coalesced)
Swapping calls...
Updating mute status to: %s...
Created log object %s: %s
Server available: %d
Connecting to XPC server...
recentsList.count: %lu (capped)
Triggering list update... (listType: %{coreacc:ACCCommunications_ListUpdate_Type_t}d, coalesce: %s)
Ending call with endAction: %{coreacc:ACCCommunications_CallControls_EndAction_t}d, callUUID: %@
Updating call state to cache (callUUID: %@)...
Adding call state to cache (callUUID: %@)...
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Received recents list update!
```
