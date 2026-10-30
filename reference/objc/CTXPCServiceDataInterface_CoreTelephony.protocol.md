# `CTXPCServiceDataInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 45 instance methods, 0 class methods

## Instance methods

```
-[CTXPCServiceDataInterface getCurrentDataSubscriptionContext:];
-[CTXPCServiceDataInterface getCurrentDataServiceDescriptor:];
-[CTXPCServiceDataInterface getSupportDynamicDataSimSwitch:];
-[CTXPCServiceDataInterface addLowLatencyFilter:pdp:queueSetId:uplink:completion:];
-[CTXPCServiceDataInterface deleteLowLatencyFilter:pdp:queueSetId:uplink:completion:];
-[CTXPCServiceDataInterface enterLoopBackMode:];
-[CTXPCServiceDataInterface getActiveConnections:completion:];
-[CTXPCServiceDataInterface getActiveSlicesInfo:];
-[CTXPCServiceDataInterface getAnbrActivationState:completion:];
-[CTXPCServiceDataInterface getConnectionAvailability:connectionType:completion:];
-[CTXPCServiceDataInterface getConnectionState:connectionType:completion:];
-[CTXPCServiceDataInterface getDataStatus:completion:];
-[CTXPCServiceDataInterface getInternationalDataAccess:completion:];
-[CTXPCServiceDataInterface getLowLatencyFilters:queueSetId:completion:];
-[CTXPCServiceDataInterface getNATTKeepAliveOverCell:completion:];
-[CTXPCServiceDataInterface getPTTSlicingCapabilityForBundleId:completion:];
-[CTXPCServiceDataInterface getPacketContextCount:];
-[CTXPCServiceDataInterface getPreferredDataServiceDescriptor:];
-[CTXPCServiceDataInterface getPreferredDataSubscriptionContext:];
-[CTXPCServiceDataInterface getPublicDataBearer:];
-[CTXPCServiceDataInterface getPublicNrFrequencyRange:];
-[CTXPCServiceDataInterface getSliceTrafficDescriptors:];
-[CTXPCServiceDataInterface getSliceTrafficDescriptorsInfo:connectionType:completion:];
-[CTXPCServiceDataInterface getSlicingCapability:];
-[CTXPCServiceDataInterface getTetheringStatus:connectionType:];
-[CTXPCServiceDataInterface isTetheringEditingSupported:completion:];
-[CTXPCServiceDataInterface queryAnbrBitrate:bitrate:direction:completion:];
-[CTXPCServiceDataInterface requestSliceByUUID:completion:];
-[CTXPCServiceDataInterface requestSliceDeactivation:completion:];
-[CTXPCServiceDataInterface resetAPNSettings:];
-[CTXPCServiceDataInterface sendDeadPeerDetection:];
-[CTXPCServiceDataInterface setApplicationCategory:completion:];
-[CTXPCServiceDataInterface setAssertionForConnectionType:enable:completion:];
-[CTXPCServiceDataInterface setCoalescing:udp:completion:];
-[CTXPCServiceDataInterface setInternationalDataAccess:status:completion:];
-[CTXPCServiceDataInterface setPacketContextActiveByServiceType:connectionType:active:completion:];
-[CTXPCServiceDataInterface setPreferredSlice:completion:];
-[CTXPCServiceDataInterface setSupportDynamicDataSimSwitch:completion:];
-[CTXPCServiceDataInterface setSupportDynamicDataSimSwitch:forIccid:completion:];
-[CTXPCServiceDataInterface setTestBundleIdForSlice:completion:];
-[CTXPCServiceDataInterface simulateDataStall:pdp:completion:];
-[CTXPCServiceDataInterface updateAvsTrafficStatus:dataType:completion:];
-[CTXPCServiceDataInterface updateIdsTrafficStatus:dataType:completion:];
-[CTXPCServiceDataInterface updatePTTSlicingCapabilityBundleIds:completion:];
-[CTXPCServiceDataInterface updateVoipCallTrafficStatus:completion:];
```
