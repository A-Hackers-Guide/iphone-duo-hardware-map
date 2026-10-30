# `WiFiAwareDataSessionStatisticsReport`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 40 instance variables, 40 properties, 82 instance methods, 1 class methods

## Instance variables

```
B _infraRelayOperationStatus;
@"WiFiMACAddress" _peerAddress;
@"NSNumber" _infrastructureChannel;
@"NSArray" _txCCAHistogram;
@"NSArray" _rxRSSIHistogram;
@"NSArray" _rxFWDelayHistogram;
@"NSArray" _rxIPCDelayHistogram;
@"NSArray" _txConsecutiveErrorsHistogram;
@"NSArray" _txPacketExpiryHistogram;
@"NSNumber" _preferred2GChannelsCount;
@"NSNumber" _preferred5GChannelsCount;
@"NSNumber" _dfsChannelsCount;
@"NSNumber" _csaCount;
@"NSNumber" _quietIECount;
@"NSNumber" _txErrorCount;
@"NSNumber" _packetsOn2GCount;
@"NSNumber" _packetsNAVOn2GCount;
@"NSNumber" _packetsHOFOn2GCount;
@"NSNumber" _packetsOverridenOn5GCount;
@"NSNumber" _packetsOn5GCount;
@"NSNumber" _infraRelayRequestersCount;
@"NSNumber" _txExpiredCount;
@"NSNumber" _txNoACKCount;
@"NSNumber" _txFailedCount;
@"NSNumber" _txNoResourcesCount;
@"NSNumber" _txIOErrorCount;
@"NSNumber" _txMemoryErrorCount;
@"NSNumber" _txChipModeErrorCount;
@"NSNumber" _txNoRemotePeerCount;
@"NSNumber" _txInternalErrorCount;
@"NSNumber" _txDroppedCount;
@"NSNumber" _txFirmwareFreePacketCount;
@"NSNumber" _txMaxRetriesCount;
@"NSNumber" _txForceLifetimeExpiredCount;
@"NSNumber" _channelSequenceMismatchOn5GCount;
@"NSNumber" _channelSequenceMismatchOn2GCount;
@"NSNumber" _infraScanCount;
@"NSNumber" _infraAssocCount;
@"NSNumber" _infraDisassocCount;
@"NSString" _countryCode;
```

## Properties

```
@property (TB,N,V_infraRelayOperationStatus) infraRelayOperationStatus;
@property (T@"NSNumber",C,N,V_infraRelayRequestersCount) infraRelayRequestersCount;
@property (T@"NSNumber",C,N,V_preferred2GChannelsCount) preferred2GChannelsCount;
@property (T@"NSNumber",C,N,V_preferred5GChannelsCount) preferred5GChannelsCount;
@property (T@"NSNumber",C,N,V_dfsChannelsCount) dfsChannelsCount;
@property (T@"NSNumber",C,N,V_csaCount) csaCount;
@property (T@"NSNumber",C,N,V_quietIECount) quietIECount;
@property (T@"NSNumber",C,N,V_txErrorCount) txErrorCount;
@property (T@"NSNumber",C,N,V_packetsOn2GCount) packetsOn2GCount;
@property (T@"NSNumber",C,N,V_packetsNAVOn2GCount) packetsNAVOn2GCount;
@property (T@"NSNumber",C,N,V_packetsHOFOn2GCount) packetsHOFOn2GCount;
@property (T@"NSNumber",C,N,V_packetsOn5GCount) packetsOn5GCount;
@property (T@"NSNumber",C,N,V_packetsOverridenOn5GCount) packetsOverridenOn5GCount;
@property (T@"NSNumber",C,N,V_txExpiredCount) txExpiredCount;
@property (T@"NSNumber",C,N,V_txNoACKCount) txNoACKCount;
@property (T@"NSNumber",C,N,V_txFailedCount) txFailedCount;
@property (T@"NSNumber",C,N,V_txNoResourcesCount) txNoResourcesCount;
@property (T@"NSNumber",C,N,V_txIOErrorCount) txIOErrorCount;
@property (T@"NSNumber",C,N,V_txMemoryErrorCount) txMemoryErrorCount;
@property (T@"NSNumber",C,N,V_txChipModeErrorCount) txChipModeErrorCount;
@property (T@"NSNumber",C,N,V_txNoRemotePeerCount) txNoRemotePeerCount;
@property (T@"NSNumber",C,N,V_txInternalErrorCount) txInternalErrorCount;
@property (T@"NSNumber",C,N,V_txDroppedCount) txDroppedCount;
@property (T@"NSNumber",C,N,V_txFirmwareFreePacketCount) txFirmwareFreePacketCount;
@property (T@"NSNumber",C,N,V_txMaxRetriesCount) txMaxRetriesCount;
@property (T@"NSNumber",C,N,V_txForceLifetimeExpiredCount) txForceLifetimeExpiredCount;
@property (T@"NSNumber",C,N,V_channelSequenceMismatchOn5GCount) channelSequenceMismatchOn5GCount;
@property (T@"NSNumber",C,N,V_channelSequenceMismatchOn2GCount) channelSequenceMismatchOn2GCount;
@property (T@"NSNumber",C,N,V_infraScanCount) infraScanCount;
@property (T@"NSNumber",C,N,V_infraAssocCount) infraAssocCount;
@property (T@"NSNumber",C,N,V_infraDisassocCount) infraDisassocCount;
@property (T@"NSArray",C,N,V_txConsecutiveErrorsHistogram) txConsecutiveErrorsHistogram;
@property (T@"NSArray",C,N,V_rxFWDelayHistogram) rxFWDelayHistogram;
@property (T@"NSArray",C,N,V_rxIPCDelayHistogram) rxIPCDelayHistogram;
@property (T@"NSArray",C,N,V_txPacketExpiryHistogram) txPacketExpiryHistogram;
@property (T@"NSArray",C,N,V_txCCAHistogram) txCCAHistogram;
@property (T@"NSArray",C,N,V_rxRSSIHistogram) rxRSSIHistogram;
@property (T@"WiFiMACAddress",R,N,V_peerAddress) peerAddress;
@property (T@"NSNumber",R,N,V_infrastructureChannel) infrastructureChannel;
@property (T@"NSString",R,N,V_countryCode) countryCode;
```

## Class methods

```
+[WiFiAwareDataSessionStatisticsReport supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDataSessionStatisticsReport peerAddress];
-[WiFiAwareDataSessionStatisticsReport countryCode];
-[WiFiAwareDataSessionStatisticsReport encodeWithCoder:];
-[WiFiAwareDataSessionStatisticsReport description];
-[WiFiAwareDataSessionStatisticsReport initWithCoder:];
-[WiFiAwareDataSessionStatisticsReport isEqual:];
-[WiFiAwareDataSessionStatisticsReport infraAssocCount];
-[WiFiAwareDataSessionStatisticsReport rxRSSIHistogram];
-[WiFiAwareDataSessionStatisticsReport channelSequenceMismatchOn2GCount];
-[WiFiAwareDataSessionStatisticsReport channelSequenceMismatchOn5GCount];
-[WiFiAwareDataSessionStatisticsReport csaCount];
-[WiFiAwareDataSessionStatisticsReport dfsChannelsCount];
-[WiFiAwareDataSessionStatisticsReport infraDisassocCount];
-[WiFiAwareDataSessionStatisticsReport infraRelayOperationStatus];
-[WiFiAwareDataSessionStatisticsReport infraRelayRequestersCount];
-[WiFiAwareDataSessionStatisticsReport infraScanCount];
-[WiFiAwareDataSessionStatisticsReport infrastructureChannel];
-[WiFiAwareDataSessionStatisticsReport packetsHOFOn2GCount];
-[WiFiAwareDataSessionStatisticsReport packetsNAVOn2GCount];
-[WiFiAwareDataSessionStatisticsReport packetsOn2GCount];
-[WiFiAwareDataSessionStatisticsReport packetsOn5GCount];
-[WiFiAwareDataSessionStatisticsReport packetsOverridenOn5GCount];
-[WiFiAwareDataSessionStatisticsReport preferred2GChannelsCount];
-[WiFiAwareDataSessionStatisticsReport preferred5GChannelsCount];
-[WiFiAwareDataSessionStatisticsReport quietIECount];
-[WiFiAwareDataSessionStatisticsReport rxFWDelayHistogram];
-[WiFiAwareDataSessionStatisticsReport rxIPCDelayHistogram];
-[WiFiAwareDataSessionStatisticsReport txCCAHistogram];
-[WiFiAwareDataSessionStatisticsReport txChipModeErrorCount];
-[WiFiAwareDataSessionStatisticsReport txConsecutiveErrorsHistogram];
-[WiFiAwareDataSessionStatisticsReport txDroppedCount];
-[WiFiAwareDataSessionStatisticsReport txErrorCount];
-[WiFiAwareDataSessionStatisticsReport txExpiredCount];
-[WiFiAwareDataSessionStatisticsReport txFailedCount];
-[WiFiAwareDataSessionStatisticsReport txFirmwareFreePacketCount];
-[WiFiAwareDataSessionStatisticsReport txForceLifetimeExpiredCount];
-[WiFiAwareDataSessionStatisticsReport txIOErrorCount];
-[WiFiAwareDataSessionStatisticsReport txInternalErrorCount];
-[WiFiAwareDataSessionStatisticsReport txMaxRetriesCount];
-[WiFiAwareDataSessionStatisticsReport txMemoryErrorCount];
-[WiFiAwareDataSessionStatisticsReport txNoACKCount];
-[WiFiAwareDataSessionStatisticsReport txNoRemotePeerCount];
-[WiFiAwareDataSessionStatisticsReport txNoResourcesCount];
-[WiFiAwareDataSessionStatisticsReport txPacketExpiryHistogram];
-[WiFiAwareDataSessionStatisticsReport setTxForceLifetimeExpiredCount:];
-[WiFiAwareDataSessionStatisticsReport initWithPeerAddress:infrastructureChannel:txCCAHistogram:rxRSSIHistogram:preferred2GChannelsCount:preferred5GChannelsCount:dfsChannelsCount:csaCount:quietIECount:txErrorCount:packetsOn2GCount:packetsNAVOn2GCount:packetsHOFOn2GCount:packetsOn5GCount:packetsOverridenOn5GCount:infraRelayOperationStatus:infraRelayRequestersCount:txExpiredCount:txNoACKCount:txFailedCount:txNoResourcesCount:txIOErrorCount:txMemoryErrorCount:txChipModeErrorCount:txNoRemotePeerCount:txInternalErrorCount:txDroppedCount:txFirmwareFreePacketCount:txMaxRetriesCount:txForceLifetimeExpiredCount:channelSequenceMismatchOn5GCount:channelSequenceMismatchOn2GCount:infraScanCount:infraAssocCount:infraDisassocCount:countryCode:txConsecutiveErrorsHistogram:rxFWDelayHistogram:rxIPCDelayHistogram:txPacketExpiryHistogram:];
-[WiFiAwareDataSessionStatisticsReport setChannelSequenceMismatchOn2GCount:];
-[WiFiAwareDataSessionStatisticsReport setChannelSequenceMismatchOn5GCount:];
-[WiFiAwareDataSessionStatisticsReport setCsaCount:];
-[WiFiAwareDataSessionStatisticsReport setDfsChannelsCount:];
-[WiFiAwareDataSessionStatisticsReport setInfraAssocCount:];
-[WiFiAwareDataSessionStatisticsReport setInfraDisassocCount:];
-[WiFiAwareDataSessionStatisticsReport setInfraRelayOperationStatus:];
-[WiFiAwareDataSessionStatisticsReport setInfraRelayRequestersCount:];
-[WiFiAwareDataSessionStatisticsReport setInfraScanCount:];
-[WiFiAwareDataSessionStatisticsReport setPacketsHOFOn2GCount:];
-[WiFiAwareDataSessionStatisticsReport setPacketsNAVOn2GCount:];
-[WiFiAwareDataSessionStatisticsReport setPacketsOn2GCount:];
-[WiFiAwareDataSessionStatisticsReport setPacketsOn5GCount:];
-[WiFiAwareDataSessionStatisticsReport setPacketsOverridenOn5GCount:];
-[WiFiAwareDataSessionStatisticsReport setPreferred2GChannelsCount:];
-[WiFiAwareDataSessionStatisticsReport setPreferred5GChannelsCount:];
-[WiFiAwareDataSessionStatisticsReport setQuietIECount:];
-[WiFiAwareDataSessionStatisticsReport setRxFWDelayHistogram:];
-[WiFiAwareDataSessionStatisticsReport setRxIPCDelayHistogram:];
-[WiFiAwareDataSessionStatisticsReport setRxRSSIHistogram:];
-[WiFiAwareDataSessionStatisticsReport setTxCCAHistogram:];
-[WiFiAwareDataSessionStatisticsReport setTxChipModeErrorCount:];
-[WiFiAwareDataSessionStatisticsReport setTxConsecutiveErrorsHistogram:];
-[WiFiAwareDataSessionStatisticsReport setTxDroppedCount:];
-[WiFiAwareDataSessionStatisticsReport setTxErrorCount:];
-[WiFiAwareDataSessionStatisticsReport setTxExpiredCount:];
-[WiFiAwareDataSessionStatisticsReport setTxFailedCount:];
-[WiFiAwareDataSessionStatisticsReport setTxFirmwareFreePacketCount:];
-[WiFiAwareDataSessionStatisticsReport setTxIOErrorCount:];
-[WiFiAwareDataSessionStatisticsReport setTxInternalErrorCount:];
-[WiFiAwareDataSessionStatisticsReport setTxMaxRetriesCount:];
-[WiFiAwareDataSessionStatisticsReport setTxMemoryErrorCount:];
-[WiFiAwareDataSessionStatisticsReport setTxNoACKCount:];
-[WiFiAwareDataSessionStatisticsReport setTxNoRemotePeerCount:];
-[WiFiAwareDataSessionStatisticsReport setTxNoResourcesCount:];
-[WiFiAwareDataSessionStatisticsReport setTxPacketExpiryHistogram:];
```
