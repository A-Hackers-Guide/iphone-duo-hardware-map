# `_TtCC7Network18NetworkActorSystem15ActorConnection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 27 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Network.NetworkActorSystem.ActorConnection.Transport transport;
Network.NetworkChannel Network.Framer Network.NetworkActorWireProtocol _$sGGSg -> singleStreamChannel;
_$sSD -> Network.NetworkActorID Network.QUIC.Stream _$sy_ Network.Framer Network.NetworkActorWireProtocol _$sGG -> streamsByActorID;
_$sSD -> Network.NetworkActorID _$sScTyyt Swift.Never readTasksByActorID;
_$sSD -> Network.NetworkActorID Network.ContinuationNotifier Network.NetworkChannel Network.Framer Network.NetworkActorWireProtocol _$sGGG -> streamNotifiersByActorID;
_$sScTyyt Swift.Never ? inboundStreamTask;
Network.NetworkActorSystem.ActorConnection.RemoteCallInvocation _$sYaKcSg -> remoteCallHandler;
Swift.Error _$sSgcSg -> connectionInvalidated;
Distributed.DistributedActor ? Network.NetworkActorID _$scSg actorResolutionHandler;
Swift.Bool disableCompression;
os.OSAllocatedUnfairLock _$syt lock;
_$sSD -> Foundation.UUID _$sScC -> Network.NetworkActorSystem.ActorConnection.ReplyResult Swift.Error _$sG inFlightCalls;
_$sSD -> Foundation.UUID _$sScTyyt Swift.Never tasksByCallID;
_$sScC -> Network.NetworkActorID Swift.Error ? resolvedActorIDContinuation;
_$sScCyyt Swift.Error ? initialStreamContinuation;
_$sSa -> Network.NetworkActorID _associatedActorIDs;
Swift.Bool isDisconnected;
_$sSay -> Swift.Error _$sSgc interruptionHandlers;
Foundation.UUID ? activeFileTransfer;
_$sSD -> Foundation.UUID Network.NetworkActorSystem.ActorConnection.FileTransferContext fileTransfers;
_$sSayScCyyt Swift.Error _$sG pendingRemoteCalls;
_$sSD -> Foundation.UUID Network.NetworkActorFileHandle _sharedFileHandles;
Network.NWActivity ? connectionEstablishedActivity;
_$sScTyyt Swift.Never ? readTask;
Swift.Bool transportStarted;
Swift.Bool server;
Swift.Bool quicKeepalivesEnabled;
```
