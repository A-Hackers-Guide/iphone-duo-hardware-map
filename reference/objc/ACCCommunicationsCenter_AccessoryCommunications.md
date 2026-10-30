# `ACCCommunicationsCenter`

- Image: [`/System/Library/PrivateFrameworks/AccessoryCommunications.framework/AccessoryCommunications`](../userland/System__Library__PrivateFrameworks__AccessoryCommunications.framework__AccessoryCommunications.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCCommunicationsXPCClientProtocol`
- 11 instance variables, 15 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"<ACCCommunicationsCenterCallStateDelegate>" _callStateDelegate;
@"<ACCCommunicationsCenterCommunicationsDelegate>" _communicationsDelegate;
@"<ACCCommunicationsCenterCallControlsDelegate>" _callControlsDelegate;
@"<ACCCommunicationsCenterListUpdatesDelegate>" _listUpdatesDelegate;
Q _maxRecentsListEntries;
Q _maxFavoritesListEntries;
@"NSXPCConnection" _serverConnection;
@"<ACCCommunicationsXPCServerProtocol>" _remoteObject;
@"NSSet" _subscriberList;
@"NSMutableDictionary" _callStateCache;
@"NSMutableDictionary" _cachedCommStatus;
```

## Properties

```
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

## Instance methods

```
-[ACCCommunicationsCenter connectToServer];
-[ACCCommunicationsCenter init];
-[ACCCommunicationsCenter setRemoteObject:];
-[ACCCommunicationsCenter serverConnection];
-[ACCCommunicationsCenter dealloc];
-[ACCCommunicationsCenter swapCalls];
-[ACCCommunicationsCenter remoteObject];
-[ACCCommunicationsCenter callStateDidChange:];
-[ACCCommunicationsCenter setServerConnection:];
-[ACCCommunicationsCenter updateSubscriberList:withReply:];
-[ACCCommunicationsCenter acceptCallWithAction:callUUID:];
-[ACCCommunicationsCenter cachedCommStatus];
-[ACCCommunicationsCenter callControlsDelegate];
-[ACCCommunicationsCenter callStateCache];
-[ACCCommunicationsCenter callStateDelegate];
-[ACCCommunicationsCenter commStatusDidChange:];
-[ACCCommunicationsCenter communicationsDelegate];
-[ACCCommunicationsCenter endAllCalls];
-[ACCCommunicationsCenter endCallWithAction:callUUID:];
-[ACCCommunicationsCenter favoritesListDidChange];
-[ACCCommunicationsCenter initWithCallStateDelegate:andCommunicationsDelegate:andCallControlsDelegate:andListUpdatesDelegate:];
-[ACCCommunicationsCenter initiateCallToDestination:withService:addressBookID:];
-[ACCCommunicationsCenter initiateCallToVoicemail];
-[ACCCommunicationsCenter initiateRedial];
-[ACCCommunicationsCenter listUpdatesDelegate];
-[ACCCommunicationsCenter maxFavoritesListEntries];
-[ACCCommunicationsCenter maxRecentsListEntries];
-[ACCCommunicationsCenter mergeCalls];
-[ACCCommunicationsCenter recentsListDidChange];
-[ACCCommunicationsCenter sendDTMF:forCallWithUUID:];
-[ACCCommunicationsCenter setCachedCommStatus:];
-[ACCCommunicationsCenter setCallControlsDelegate:];
-[ACCCommunicationsCenter setCallStateCache:];
-[ACCCommunicationsCenter setCallStateDelegate:];
-[ACCCommunicationsCenter setCommunicationsDelegate:];
-[ACCCommunicationsCenter setListUpdatesDelegate:];
-[ACCCommunicationsCenter setSubscriberList:];
-[ACCCommunicationsCenter subscriberList];
-[ACCCommunicationsCenter triggerCallStateUpdatesWithReply:];
-[ACCCommunicationsCenter triggerCommunicationsUpdateWithReply:];
-[ACCCommunicationsCenter triggerUpdateForListType:coalesce:withReply:];
-[ACCCommunicationsCenter updateHoldStatus:forCallWithUUID:];
-[ACCCommunicationsCenter updateMuteStatus:];
```
