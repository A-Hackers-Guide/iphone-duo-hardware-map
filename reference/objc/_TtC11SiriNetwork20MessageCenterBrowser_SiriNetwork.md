# `_TtC11SiriNetwork20MessageCenterBrowser`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 21 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
Builtin.DefaultActorStorage $defaultActor;
SiriNetwork.MessageCenterUserManager userManager;
_$sSh -> SiriNetwork.MessageCenterUser enrolledUsers;
_$sSD -> SiriNetwork.MessageCenterUser SiriNetwork.MessageCenterEndpointBrowseProtocol userSpecificDeviceBrowser;
SiriNetwork.MessageCenterBrowserDelegate ? delegate;
SiriNetwork.MessageCenterConnectionMetricsDelegate ? metricsDelegate;
os.Logger logger;
Swift.Bool started;
SiriNetwork.MessageCenterEndpointBrowseProtocol _$sSScSg networkDeviceBrowserProvider;
SiriNetwork.MessageCenterConnectionProtocol ? SiriNetwork.MessageCenterEndpointProtocol _$s_SStc networkConnectionProvider;
(objc_protocol 0x2adedec80) ? Foundation.UUID _$s_S2StcSg analyticsStreamProvider;
_$sSDySS Network.NWConnection.PendingDataTransferReport pendingReports;
SiriNetwork.MessageCenterNetworkQualityMetrics _$sSgycSg networkQualityProvider;
_$sSDySS SiriNetwork.MessageCenterConnectionProtocol activeConnectionsByIdsIdentifier;
_$sSDySSSh -> SiriNetwork.MessageCenterEndpoint activeEndpoints;
_$sSDySSSDySS SiriNetwork.MessageCenterStreamProtocol _$sG activeStreams;
_$sSD -> SiriNetwork.MessageCenterBrowser.StreamCreationKey SiriNetwork.MessageCenterBrowser.InFlightStreamCreation inFlightStreamCreations;
_$syyYbcSg inFlightJoinObserverForTesting;
_$sSd streamCreationTimeout;
SiriNetwork.MessageCenterInternalConfigurator internalConfigurator;
SiriNetwork.AsyncSequentialExecutor asyncExecutor;
```
