# `_TtCC7Network13NWActorSystem15ActorConnection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 17 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Network.NWConnection nwConnection;
Network.NWActorSystem.ActorConnection.RemoteCallInvocation _$sYaKcSg -> remoteCallHandler;
Swift.Error _$sSgcSg -> connectionInvalidated;
Distributed.DistributedActor ? Network.NWActorID _$scSg actorResolutionHandler;
Network.NWActorSystemDelegate ? delegate;
Swift.Bool disableCompression;
os.OSAllocatedUnfairLock _$syt lock;
_$sSD -> Foundation.UUID _$sScC -> Network.NWActorSystem.ActorConnection.ReplyResult Swift.Error _$sG inFlightCalls;
_$sSD -> Foundation.UUID _$sScTyyt Swift.Never tasksByCallID;
_$sSD -> Foundation.UUID _$sSS6target_ Distributed.DistributedActor actorInstancet inboundCallInfoByID;
_$sScC -> Network.NWActorID Swift.Error ? resolvedActorIDContinuation;
_$sSa -> Network.NWActorID _associatedActorIDs;
Swift.Bool isDisconnected;
_$sSay -> Swift.Error _$sSgc interruptionHandlers;
Network.NWActivity ? connectionEstablishedActivity;
Network.NWProtocolQUIC.Metadata ? quicConnectionMetadata;
Swift.Bool quicKeepalivesEnabled;
```
