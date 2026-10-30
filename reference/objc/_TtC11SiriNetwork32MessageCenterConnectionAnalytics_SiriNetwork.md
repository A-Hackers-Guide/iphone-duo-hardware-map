# `_TtC11SiriNetwork32MessageCenterConnectionAnalytics`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 25 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Builtin.DefaultActorStorage $defaultActor;
Foundation.UUID connectionId;
_$sSS remoteIdsIdentifier;
__C.NETSchemaNETProvider connectionProvider;
(objc_protocol 0x2adedec80) stream;
SiriNetwork.MessageCenterNetworkQualityMetrics _$sSgycSg networkQualityProvider;
SiriNetwork.AsyncSequentialExecutor emissionExecutor;
DispatchQueue dataTransferReportQueue;
Swift.UInt32 currentSequenceNumber;
Swift.Bool shouldEmitDebugEvents;
Swift.Bool lifecycleEventsEmitted;
Swift.Bool failureEventEmitted;
Foundation.UUID ? lastFailureEmittedBatchId;
Swift.Bool failureRecorded;
Swift.Error ? failureError;
Swift.UInt64 ? preparationTimestamp;
Swift.ContinuousClock.Instant ? preparationTime;
Swift.UInt64 ? readyTimestamp;
SiriNetwork.MessageCenterPreparationReport ? preparationReport;
SiriNetwork.MessageCenterEstablishmentReport ? establishmentReport;
Swift.ContinuousClock.Instant ? readyTime;
Network.NWPath.Status ? readyPathStatus;
_$sSSSg readyPrimaryInterfaceName;
_$sSa -> SiriNetwork.MessageCenterInterfaceInfo readyInterfaces;
_$sSa -> SiriNetwork.ConnectionTCPInfoMetrics readyTCPInfo;
```
