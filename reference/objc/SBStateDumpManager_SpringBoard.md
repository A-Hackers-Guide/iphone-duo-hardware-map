# `SBStateDumpManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBStateDumpMultipeerControllerDelegate`, `RSPeerToPeerConnectionControllerDataSource`, `RSPeerToPeerConnectionControllerDelegate`
- 20 instance variables, 8 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"SBStateDumpDefaults" _defaults;
@"NSMutableDictionary" _registeredDomains;
@"NSMutableDictionary" _clientSubscriptions;
@"NSMutableDictionary" _fileHandles;
@"NSMutableDictionary" _displayLinks;
@"NSMutableDictionary" _displayObservers;
@"NSMutableDictionary" _displaysByID;
@"NSMutableDictionary" _fileSubscriptions;
@"NSMutableDictionary" _pendingFileWriteRequests;
@"NSMapTable" _pendingToActiveAssertionMap;
@"SBStateDumpMultipeerController" _multipeerController;
@"NSTimer" _remoteStreamingTimer;
@"NSDate" _remoteStreamingTimerStartDate;
d _remoteStreamingTimerDuration;
@? _startWorkItem;
@"RSPeerToPeerServerController" _stateDumpServerController;
Q _stateDumpServiceRevision;
@"NSDate" _remoteDumpTimerStartDate;
d _remoteDumpTimerDuration;
@"NSObject<OS_dispatch_queue>" _syncQueue;
```

## Properties

```
@property (T@"SBStateDumpDefaults",R,N,V_defaults) defaults;
@property (TB,R,N) isRemoteStreamingEnabled;
@property (Td,R,N) remoteStreamingTimeRemaining;
@property (Td,R,N) remoteDumpTimeRemaining;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStateDumpManager _displayLinkFired:];
-[SBStateDumpManager defaults];
-[SBStateDumpManager disableRemoteStateDumpWithCompletion:];
-[SBStateDumpManager enableRemoteStateDumpWithTimeout:completion:];
-[SBStateDumpManager init];
-[SBStateDumpManager stop];
-[SBStateDumpManager start];
-[SBStateDumpManager enableRemoteStreamingWithTimeout:completion:];
-[SBStateDumpManager disableRemoteStreamingWithCompletion:];
-[SBStateDumpManager lastEntriesForDomain:count:error:];
-[SBStateDumpManager _updateRegistry];
-[SBStateDumpManager _actuallyStartWritingDomain:toFile:error:];
-[SBStateDumpManager _cancelPendingFileWriteRequest:forDomain:];
-[SBStateDumpManager _cleanupTempFilesIfNeeded];
-[SBStateDumpManager _domainMatchesAnyPattern:inPatterns:];
-[SBStateDumpManager _domainsDirectory];
-[SBStateDumpManager _dumpStateCaptureData];
-[SBStateDumpManager _ensureDisplayLinkForDisplay:];
-[SBStateDumpManager _ensureFileHandleForDomain:];
-[SBStateDumpManager _filePathForDomain:];
-[SBStateDumpManager _fulfillPendingFileWriteRequestsForDomain:];
-[SBStateDumpManager _hasSubscribersForDisplay:];
-[SBStateDumpManager _isFileWritingEnabledForDisplay:];
-[SBStateDumpManager _metadataForDisplay:displayLink:];
-[SBStateDumpManager _pushToSubscribedClients:forDomain:];
-[SBStateDumpManager _reevaluateDisplayLinksForDomains:reason:];
-[SBStateDumpManager _removeDisplayObserver:];
-[SBStateDumpManager _scheduleRemoteStreamingTimerWithDuration:];
-[SBStateDumpManager _screenForDisplay:];
-[SBStateDumpManager _setupFileStructure];
-[SBStateDumpManager _shouldWriteDefaultFileForDomain:];
-[SBStateDumpManager _startAdvertisingImmediately];
-[SBStateDumpManager _stopWritingDomain:toFile:];
-[SBStateDumpManager _streamBuddyDirectory];
-[SBStateDumpManager _writeStateToAllFiles:forDomain:shouldWriteDefaultFile:];
-[SBStateDumpManager allowedRemotePeerDisplayNames];
-[SBStateDumpManager availableDomains];
-[SBStateDumpManager availableFiles];
-[SBStateDumpManager broadcastStateCaptureToConnectedRemotePeers:];
-[SBStateDumpManager client:subscribeToDomains:];
-[SBStateDumpManager client:unsubscribeFromDomains:];
-[SBStateDumpManager didConnectToRemotePeer:];
-[SBStateDumpManager didDisconnectFromRemotePeer:];
-[SBStateDumpManager didReceiveState:withInfo:fromPeer:];
-[SBStateDumpManager domainRegistry];
-[SBStateDumpManager dumpLoggingStateCaptureToTextFileAtPath:];
-[SBStateDumpManager dumpLoggingStateCaptureWithCompletion:];
-[SBStateDumpManager isRemoteStateDumpEnabled];
-[SBStateDumpManager isRemoteStreamingEnabled];
-[SBStateDumpManager localPeerDisplayName];
-[SBStateDumpManager multipeerController:clientConnected:];
-[SBStateDumpManager multipeerController:clientDisconnected:];
-[SBStateDumpManager multipeerController:didReceiveMessage:fromClient:];
-[SBStateDumpManager observeDisplayUpdatesForDomain:display:updateBlock:];
-[SBStateDumpManager registerDomain:description:];
-[SBStateDumpManager remoteDumpTimeRemaining];
-[SBStateDumpManager remoteStreamingTimeRemaining];
-[SBStateDumpManager startWritingDomain:toFile:error:];
-[SBStateDumpManager stateForStateType:withCompletionHandler:];
-[SBStateDumpManager streamState:forDomain:];
-[SBStateDumpManager supportedStateTypes];
-[SBStateDumpManager transferFile:toClient:];
-[SBStateDumpManager willConnectToRemotePeer:];
```
