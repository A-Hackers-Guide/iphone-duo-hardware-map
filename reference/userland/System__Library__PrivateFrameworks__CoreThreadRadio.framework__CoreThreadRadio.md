# `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`

iOS 27.2 dyld shared cache image. Version `446.0.4.0.0`. **[DSC]**

## Linked libraries (8)

- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce`
- `/usr/lib/libTelephonyUtilDynamic.dylib`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 22 classes, 2 protocols, 319 methods, 183 properties

### Class pages

Every class and protocol, with its methods: [`CtrAccessoryInfoType`](../objc/CtrAccessoryInfoType_CoreThreadRadio.md), [`CtrAccessorySpecificThreadInfoInput`](../objc/CtrAccessorySpecificThreadInfoInput_CoreThreadRadio.md), [`CtrAccessorySpecificThreadInfoOutput`](../objc/CtrAccessorySpecificThreadInfoOutput_CoreThreadRadio.md), [`CtrAccessorySpecificTriggerResult`](../objc/CtrAccessorySpecificTriggerResult_CoreThreadRadio.md), [`CtrClient`](../objc/CtrClient_CoreThreadRadio.md), [`CtrClientSysdiag`](../objc/CtrClientSysdiag_CoreThreadRadio.md), [`CtrMeshDiagAnalysisResults`](../objc/CtrMeshDiagAnalysisResults_CoreThreadRadio.md), [`CtrMeshDiagAsymmetricLinkInfo`](../objc/CtrMeshDiagAsymmetricLinkInfo_CoreThreadRadio.md), [`CtrMeshDiagAsymmetricLinksResult`](../objc/CtrMeshDiagAsymmetricLinksResult_CoreThreadRadio.md), [`CtrMeshDiagBottleneckNodeInfo`](../objc/CtrMeshDiagBottleneckNodeInfo_CoreThreadRadio.md), [`CtrMeshDiagBottleneckNodesResult`](../objc/CtrMeshDiagBottleneckNodesResult_CoreThreadRadio.md), [`CtrMeshDiagCriticalNodeInfo`](../objc/CtrMeshDiagCriticalNodeInfo_CoreThreadRadio.md), [`CtrMeshDiagCriticalNodesResult`](../objc/CtrMeshDiagCriticalNodesResult_CoreThreadRadio.md), [`CtrMeshDiagResilienceMetadata`](../objc/CtrMeshDiagResilienceMetadata_CoreThreadRadio.md), [`CtrMeshDiagResilienceResult`](../objc/CtrMeshDiagResilienceResult_CoreThreadRadio.md), [`CtrMeshDiagUnreachableNodeInfo`](../objc/CtrMeshDiagUnreachableNodeInfo_CoreThreadRadio.md), [`CtrMeshDiagUnreachableNodesResult`](../objc/CtrMeshDiagUnreachableNodesResult_CoreThreadRadio.md), [`CtrMeshDiagUnreliableNodeInfo`](../objc/CtrMeshDiagUnreliableNodeInfo_CoreThreadRadio.md), [`CtrMeshDiagUnreliableNodesResult`](../objc/CtrMeshDiagUnreliableNodesResult_CoreThreadRadio.md), [`CtrMeshDiagUnsupportedEnhancedDiagnosticsNodeInfo`](../objc/CtrMeshDiagUnsupportedEnhancedDiagnosticsNodeInfo_CoreThreadRadio.md), [`CtrMeshDiagUnsupportedEnhancedDiagnosticsResult`](../objc/CtrMeshDiagUnsupportedEnhancedDiagnosticsResult_CoreThreadRadio.md), [`CtrTriggerResult`](../objc/CtrTriggerResult_CoreThreadRadio.md), [`NSCoding`](../objc/NSCoding_CoreThreadRadio.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_CoreThreadRadio.protocol.md)

### Classes

`CtrAccessoryInfoType`, `CtrAccessorySpecificThreadInfoInput`, `CtrAccessorySpecificThreadInfoOutput`, `CtrAccessorySpecificTriggerResult`, `CtrClient`, `CtrClientSysdiag`, `CtrMeshDiagAnalysisResults`, `CtrMeshDiagAsymmetricLinkInfo`, `CtrMeshDiagAsymmetricLinksResult`, `CtrMeshDiagBottleneckNodeInfo`, `CtrMeshDiagBottleneckNodesResult`, `CtrMeshDiagCriticalNodeInfo`, `CtrMeshDiagCriticalNodesResult`, `CtrMeshDiagResilienceMetadata`, `CtrMeshDiagResilienceResult`, `CtrMeshDiagUnreachableNodeInfo`, `CtrMeshDiagUnreachableNodesResult`, `CtrMeshDiagUnreliableNodeInfo`, `CtrMeshDiagUnreliableNodesResult`, `CtrMeshDiagUnsupportedEnhancedDiagnosticsNodeInfo`, `CtrMeshDiagUnsupportedEnhancedDiagnosticsResult`, `CtrTriggerResult`

### Protocols

`NSCoding`, `NSSecureCoding`

### Properties

```
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSString",R,V_name) name;
@property (T@"NSString",R,V_ipaddr) ipaddr;
@property (TB,R,V_isMatter) isMatter;
@property (TB,R,V_isBatteryPowered) isBatteryPowered;
@property (T@"NSString",R,V_accessoryManufacturer) accessoryManufacturer;
@property (T@"NSString",R,V_accessoryModel) accessoryModel;
@property (T@"NSString",R,V_hostName) hostName;
@property (T@"NSString",R,V_serviceInstanceName) serviceInstanceName;
@property (T@"NSString",R,V_ipv6Address) ipv6Address;
@property (Tq,R,V_browseStatus) browseStatus;
@property (Tq,R,V_resolveStatus) resolveStatus;
@property (Tq,R,V_transactionStatus) transactionStatus;
@property (TB,R,V_isWrite) isWrite;
@property (TB,R,V_isLinkFallBack) isLinkFallBack;
@property (Tq,R,V_communicationProtocol) communicationProtocol;
@property (Tq,R,V_hapThreadAccessoryCapabilities) hapThreadAccessoryCapabilities;
@property (TQ,R,V_errorCode) errorCode;
@property (TQ,R,V_hapCoAPTokenInfo) hapCoAPTokenInfo;
@property (TQ,R,V_matterSessionInfo) matterSessionInfo;
@property (TQ,R,V_consecutiveFailureCount) consecutiveFailureCount;
@property (TQ,R,V_consecutiveSuccessCount) consecutiveSuccessCount;
@property (TQ,R,V_durationSecondsSinceLastSuccessfulRequest) durationSecondsSinceLastSuccessfulRequest;
@property (Tq,R,V_threadMeshError) threadMeshError;
@property (TQ,R,V_threadMeshUnderlyingStatusBitmap) threadMeshUnderlyingStatusBitmap;
@property (Tq,R,V_threadTXError) threadTXError;
@property (TQ,R,V_threadTXUnderlyingStatusBitmap) threadTXUnderlyingStatusBitmap;
@property (TQ,R,V_threadRXUnderlyingStatusBitmap) threadRXUnderlyingStatusBitmap;
@property (Tq,R,V_srpError) srpError;
@property (TQ,R,V_srpUnderlyingStatusBitmap) srpUnderlyingStatusBitmap;
@property (T@"NSString",R,N,V_ip_addr) ip_addr;
@property (T@"NSString",R,N,V_name) name;
@property (Tq,R,N,V_tx_total) tx_total;
@property (Tq,R,N,V_tx_total_success) tx_total_success;
@property (Tq,R,N,V_rx_total) rx_total;
@property (Tq,R,N,V_rx_total_success) rx_total_success;
@property (Tq,R,N,V_tx_icmp_total) tx_icmp_total;
@property (Tq,R,N,V_rx_icmp_total) rx_icmp_total;
@property (T@"NSString",R,N,V_last_known_role) last_known_role;
@property (TB,R,N,V_is_current_node_parent) is_current_node_parent;
@property (TB,R,N,V_is_link_loss_detected) is_link_loss_detected;
@property (TB,R,N,V_is_neighbor_table_removal_detected) is_neighbor_table_removal_detected;
@property (TB,R,N,V_is_direct_link) is_direct_link;
@property (Tq,R,N,V_avg_rssi) avg_rssi;
@property (Tq,R,N,V_tx_success_perc) tx_success_perc;
@property (Tq,R,N,V_rx_success_perc) rx_success_perc;
@property (Tq,R,N,V_tx_delayavg) tx_delayavg;
@property (Tq,R,N,V_tx_delaymin) tx_delaymin;
@property (Tq,R,N,V_tx_delaymax) tx_delaymax;
@property (T@"CtrMeshDiagCriticalNodesResult",R,V_criticalNodesResult) criticalNodesResult;
@property (T@"CtrMeshDiagUnreliableNodesResult",R,V_unreliableNodesResult) unreliableNodesResult;
@property (T@"CtrMeshDiagUnreachableNodesResult",R,V_unreachableNodesResult) unreachableNodesResult;
@property (T@"CtrMeshDiagAsymmetricLinksResult",R,V_asymmetricLinksResult) asymmetricLinksResult;
@property (T@"CtrMeshDiagBottleneckNodesResult",R,V_bottleneckNodesResult) bottleneckNodesResult;
@property (T@"CtrMeshDiagUnsupportedEnhancedDiagnosticsResult",R,V_unsupportedEnhancedDiagnosticsResult) unsupportedEnhancedDiagnosticsResult;
@property (T@"CtrMeshDiagResilienceResult",R,V_resilienceResult) resilienceResult;
@property (TS,R,V_version) version;
@property (T@"NSData",R,V_nodeAExtAddress) nodeAExtAddress;
@property (TS,R,V_nodeARloc16) nodeARloc16;
@property (TC,R,V_nodeARouterId) nodeARouterId;
@property (T@"NSString",R,V_nodeAVendorName) nodeAVendorName;
@property (T@"NSString",R,V_nodeAVendorModel) nodeAVendorModel;
@property (T@"NSData",R,V_nodeBExtAddress) nodeBExtAddress;
@property (TS,R,V_nodeBRloc16) nodeBRloc16;
@property (TC,R,V_nodeBRouterId) nodeBRouterId;
@property (T@"NSString",R,V_nodeBVendorName) nodeBVendorName;
@property (T@"NSString",R,V_nodeBVendorModel) nodeBVendorModel;
@property (TC,R,V_forwardLinkCost) forwardLinkCost;
@property (TC,R,V_reverseLinkCost) reverseLinkCost;
@property (TC,R,V_costDifference) costDifference;
@property (T@"NSArray",R,V_nodeAIpv6Addresses) nodeAIpv6Addresses;
@property (T@"NSArray",R,V_nodeBIpv6Addresses) nodeBIpv6Addresses;
@property (TC,R,V_asymmetricLinkCount) asymmetricLinkCount;
@property (T@"NSArray",R,V_asymmetricLinks) asymmetricLinks;
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TS,R,V_version) version;
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (TI,R,V_trafficThroughput) trafficThroughput;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
@property (TC,R,V_bottleneckNodeCount) bottleneckNodeCount;
@property (T@"NSArray",R,V_bottleneckNodes) bottleneckNodes;
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TS,R,V_version) version;
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (TB,R,V_hasEnhancedRoute) hasEnhancedRoute;
@property (TB,R,V_hasVendorRoute) hasVendorRoute;
@property (TB,R,V_hasOffgridRoute) hasOffgridRoute;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSData",R,V_linkQualities) linkQualities;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
@property (TC,R,V_criticalNodeCount) criticalNodeCount;
@property (T@"NSArray",R,V_criticalNodes) criticalNodes;
@property (Tf,R,V_penaltyCriticalNodes) penaltyCriticalNodes;
@property (Tf,R,V_penaltyBottlenecks) penaltyBottlenecks;
@property (Tf,R,V_penaltyAsymmetricLinks) penaltyAsymmetricLinks;
@property (Tf,R,V_penaltyUnreliableNodes) penaltyUnreliableNodes;
@property (Tf,R,V_penaltyUnreachableNodes) penaltyUnreachableNodes;
@property (Tf,R,V_weightCriticalNodes) weightCriticalNodes;
@property (Tf,R,V_weightBottlenecks) weightBottlenecks;
@property (Tf,R,V_weightAsymmetricLinks) weightAsymmetricLinks;
@property (Tf,R,V_weightUnreliableNodes) weightUnreliableNodes;
@property (Tf,R,V_weightUnreachableNodes) weightUnreachableNodes;
@property (T@"NSString",R,V_scoreSummary) scoreSummary;
@property (TC,R,V_healthScore) healthScore;
@property (T@"CtrMeshDiagResilienceMetadata",R,V_metadata) metadata;
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TB,R,V_extAddressKnown) extAddressKnown;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (TC,R,V_unreachableNodeCount) unreachableNodeCount;
@property (T@"NSArray",R,V_unreachableNodes) unreachableNodes;
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TS,R,V_version) version;
@property (TS,R,V_reasonFlags) reasonFlags;
@property (TS,R,V_userActionFlags) userActionFlags;
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
@property (TC,R,V_unreliableNodeCount) unreliableNodeCount;
@property (T@"NSArray",R,V_unreliableNodes) unreliableNodes;
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TS,R,V_version) version;
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
@property (TC,R,V_unsupportedNodeCount) unsupportedNodeCount;
@property (T@"NSArray",R,V_unsupportedNodes) unsupportedNodes;
@property (Tq,R,N,V_num_apple_BRs) num_apple_BRs;
@property (Tq,R,N,V_num_thirdparty_BRs) num_thirdparty_BRs;
@property (Tq,R,N,V_num_thread_networks) num_thread_networks;
@property (Tq,R,N,V_max_simultaneous_prefix_detected) max_simultaneous_prefix_detected;
@property (Tq,R,N,V_tx_total) tx_total;
@property (Tq,R,N,V_tx_total_success) tx_total_success;
@property (Tq,R,N,V_tx_success_perc) tx_success_perc;
@property (Tq,R,N,V_rx_total) rx_total;
@property (Tq,R,N,V_rx_total_success) rx_total_success;
@property (Tq,R,N,V_rx_success_perc) rx_success_perc;
@property (Tq,R,N,V_tx_delayavg) tx_delayavg;
@property (Tq,R,N,V_tx_delaymin) tx_delaymin;
@property (Tq,R,N,V_tx_delaymax) tx_delaymax;
@property (Tq,R,N,V_coex_tx_denied_requests_percentage) coex_tx_denied_requests_percentage;
@property (Tq,R,N,V_coex_rx_denied_requests_percentage) coex_rx_denied_requests_percentage;
@property (TB,R,N,V_is_leader_thirdparty) is_leader_thirdparty;
@property (T@"NSString",R,N,V_last_known_device_role) last_known_device_role;
@property (TB,R,N,V_is_partition_id_change_detected) is_partition_id_change_detected;
@property (T@"NSString",R,N,V_leader_name) leader_name;
@property (T@"NSString",R,N,V_num_routers) num_routers;
@property (T@"NSString",R,N,V_thread_mesh_size) thread_mesh_size;
@property (TB,R,N,V_is_parent_change_detected) is_parent_change_detected;
@property (TB,R,N,V_is_threaddaemon_crash_detected) is_threaddaemon_crash_detected;
@property (TB,R,N,V_is_threadfw_crash_detected) is_threadfw_crash_detected;
@property (TB,R,N,V_is_role_detach_disable_detected) is_role_detach_disable_detected;
@property (TB,R,N,V_is_border_router_advertised) is_border_router_advertised;
@property (Tq,R,N,V_num_border_routers_advertised) num_border_routers_advertised;
@property (T@"NSMutableArray",R,N,V_accessory_result) accessory_result;
@property (Tq,R,N,V_duration) duration;
```

## Strings (724)

```
EventServerStateChange
num_third_party_border_routers
v16@?0{object=^v}8
unreachableNodesResult
txTotalSuccess
Leave
geoAvailable
partition_id_changes_count
-err
lastKnownRole
accessoryOutputArray
setChannel
isWrite
threadTxError
threadTxStatusBitmap
(
CtrXpcClient_generatePSKc_interface_helper
\nDIAGNOSIS: This error indicates that the device is not in a state where\nit can complete your request, typically because a request is already in progress or\nthe NCP is already in the requested state.\nIf you are getting this error persis
EventSystemExitingLowPower
WpanctlCmd
name
large
configure
eventsOn
Joiner:Vendor:SwVersion
tx_success_perc
alert
unsupportedNodeCount
healthScore
InvalidWhenDisabled
com.nestlabs.WPANTunnelDriver
ca_trigger_based_counters_num_firmware_resets
rxTotalSuccess
daemonCrashed
nodeARouterId
com.apple.private.fillmore.prefix.modification
ClientHostName
kCommandError
srpStatusBitMap
costDifference
eMACAddress is required if it is wed device
JoinFailedAtScan
Joiner: not a valid cmd
srpErrorEnum
v8@?0
com.apple.private.fillmore.service.remove
PropertyEmpty
JoinFailedAtAuthenticate
Bad Prefix
Prefix is not given
primaryResidentInfo
threadStart
ss
numThreadCapableResidentsInHome
metadata
sleepy-end-device
tx_app_pkt_success
currOutput
Busy
InProgress
com.apple.private.ctr.thread
Not checked in
all
PropGet
xpanid
ConfigGateway
JoinFailedUnknown
commandResult
tx_delayavg
ret
num1PRouters
PropVal
ServiceRemove
joined
detached_role_count
JoinerFailed_Security
commissioner
ServiceNotificationName
EventServerSIGTERM
kNotSupported
-[CtrClient getThreadMeshWirelessInsights:completionHandler:]_block_invoke
MissingXPANID
/com/nestlabs/WPANTunnelDriver
event
Joiner:Vendor:Data
ca_trigger_based_counters_num_daemon_restart_due_to_crashes_or_jetsams
 Info:'
nodeBRloc16
property_type
threadMeshError
isLeader
com.apple.private.fillmore.masterkey.get
checkIn
tx_app_pkt_failure
hapThreadAccessoryCapabilities
criticalNodes
criticalNodeCount
EntitlementCheck_Failed for this property
nodeAIpv6Addresses
eventNotification
threadStop
rx_success_perc
-alert
getName
0x%04X
num_border_routers_advertised
kInvalidErrorCode
create
Invalid Input
isPrimaryResident
init_block_invoke
Reset
disabled_role_count
leaderIsThirdParty
durationSecondsSinceLastSuccessfulRequest
srpStatusBitmap
bottleneckNodesResult
service_data
[\n
property_value_length
com.threadradiod.ctr
com.apple.private.fillmore.masterkey.set
com.apple.private.fillmore.provideEmac
com.apple.private.fillmore.startFWUpdate
FeatureNotSupported
NCPFatal
browseStatus
key_index
rx_total
ssed
EventSystemEnteringLowPower
Invalid Msg Sub Type v_type = %llu \n
router
tx_delaymax
threadTXReachabilityStatusBitMap
NetScanStart
ServerStateStopping
very large
fCheckInState: NotCheckedIn, aborting command\n
fNotificationName
penaltyBottlenecks
Q
void CtrXPC::Client::processClientApiWithCompletion(Cmd_data &, ResultBlock, const std::string &)
trafficThroughput
PropSet
extendedMACAddress
true
num_apple_border_routers
TrmCmd
CtrXPCClient.cpp
Server data is not Given
tx_total
perform_sync_block_invoke
bottleneckNodes
hasNetworkKey
rx_icmp_err
Server not available
0123456789ABCDEF
vendorModel
penaltyUnreliableNodes
NCPInvalidArgument
Results are invalid
com.apple.private.fillmore.stopPairing
No inputs were given
nodeAVendorName
uniqueNetworkId
pass_phrase
unknown
\nDIAGNOSIS: The requested operation can't be completed because the NCP\nis busy doing something else, like scanning or joining. If you are persistently\ngetting this error, try resetting the NCP via the \"reset\" command. You can\nhelp dia
'
Scan Type is Invalid
threadMeshStatusBitmap
nodeAVendorModel
\nDIAGNOSIS: Join failed while authenticating. This is typically due to using the wrong\nkey or because this NCP's network stack is not compatible with this network.\n\n
network_key
mesh_local_prefix
prefixesDetected
txTotal
com.apple.private.fillmore.commissionOrFormNetwork
num2PSED
ServerHostName
bottleneckNodeCount
numHAPSleepyThreadAccessories
JoinerStop
ServerEnableSignalHandler
entrust
last_known_device_role
prefix_len_in_bits
resilienceResult
0x%02X
\nDIAGNOSIS: This error indicates that the NCP could not find a device in\nrange that would allow it to join the given network. This can occur if\nthe closest device on the network you are trying to join is out of range,\nthe devices on the
ServiceXPCName
kInternalError
rxSuccessPerc
vendorName
%
ThreadRadioCapability
org.wpantund.v1
wait_for_sync
thread_version
accessoryInputArray
-[CtrClient captureTriggerData:triggerId:accessoryInfoList:completionHandler:]
com.apple.private.fillmore.attachToNetwork
prefix
triggerType
is_nw_found
UpdateAccessoryData
/org/wpantund
Network name is not given
sed
6
kWPANTUNDProperty_NetworkXPANID
statsTimestamp
TdmCmd
kPermissionDenied
isPrimaryResidentThreadCapable
synchronized
\nDIAGNOSIS: Entitlement Check Failed for this property.\n\n
fwCrashed
-[CtrClient updateHomeThreadInfo:]
nodeBRouterId
validLifetime
end
Join
LinkQualityIn
com.apple.private.fillmore.service.add
list
LastRssi
Command Error
com.apple.private.fillmore.getTriggerStats
SocketReset
TnmCmd
tx_delaymin
numHAPThreadAccessories
kWPANTUNDProperty_NetworkName
ServerStateStarted
inUniqueId or activeOperationalDataset parameter is required
isPrimaryUser
JoinerStart
JoinerAttach
false
%lf
legacy_prefix
tx_app_total
dhcp
PSKc
txDelayAvg
success
isThisDeviceParent
Invalid Msg Type with v_type = %llu \n
network_name
channel_mask
threadMeshReachabilityStatusBitMap
com.apple.private.fillmore.pskc.set
kWPANTUNDProperty_NCPChannel
ExtAddress
statsDuration
partitionChanged
version
TryAgainLater
unreliableNodesResult
property_name
connect
wpantund.daemon.ready
warn
randomized
com.apple.private.fillmore.pskc.get
com.apple.private.fillmore.startPairing
Ok
num2PRouters
GeneratePSKc
KeyTimestampString
kServerError
errorCode
priority
isLinkFallback
unsupportedEnhancedDiagnosticsResult
%d
v_type
node_type
stopFWUpdate
,
enterprise number is invalid, given as(0)
All
thirdPartyBRs
threadNwsKey
userActionFlags
unsupportedEnhancedDiagnostics
txSuccessPerc
extAddress
failed to interpret eMACAddress
masterKey
ClientCommand.cpp
nodeBExtAddress
Failed to start pairing
numMatterSleepyThreadAccessories
Joiner:ReturnImmediatelyOnStart
Timeout
method
txDelayMin
Failure
InvalidRange
updateHomeThreadInfo
com.apple.private.fillmore.updatePrimaryResident
eventsOff
enddevice
sleepy
hasEnhancedRoute
unreliableNodeCount
HardReset
nl-lurker
Network Name not Given
-notice
-info
txDelayMax
weightCriticalNodes
NCP-Specific Errorcode
clientName
property_value
e
NetworkDiagnostics
borderRouterFound
-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]_block_invoke
eMAC is required if router mode is on
stable
num1PSED
consecutiveSuccessCount
onMesh
extAddressKnown
meshSize
penaltyUnreachableNodes
Already
JoinerFailed_ResponseTimeout
5
triggerId
com.apple.private.fillmore.stopFWUpdate
eventData
numRouters
isLinkFallBack
-[CtrClient updatePrimaryResident:isPrimaryResidentThreadCapable:primaryResidentInfo:]
kWPANTUNDProperty_NetworkNodeType
pan_id_filter
\t\"%s\"
key
err
unreachableNodes
-[CtrClient threadStart:activeOperationalDataSet:geoAvailable:routerMode:eMAC:waitForSync:completion:]_block_invoke
stopPairing
NCPReset
s
Form
tx_success
coexTxDeniedReqsPerc
duration
inputSequenceNumber
startPairing
FeatureNotImplemented
psk value is not given
\nDIAGNOSIS: This error indicates that this operation is not valid when the interface\nis disabled. Enable the interface first and try again. You can enable the interface\nwith the command `setprop enabled true`.\n\n
KeyErrorCode
Error: threadstart failed !
enable_filtering
srpError
outputSequenceNumber
Output pointer is not given
Joiner command operation is not provided
0x%016llX
ip_addr
-warn
asymmetricLinksResult
ServerEnablePowerObserver
Result:'
-emerg
host_info
serviceInstanceName
%u
isThisDevice
resilience
Reply is not a dictionary
r
Invalid size:%zu for kWPANTUNDProperty_NCPHardwareAddress
Joiner:Vendor:Name
Joiner:Vendor:Model
debug
rloc16
\"%s\" \n
leader
ed
KeyServerState
\"%s\"
idle
EventSystemShuttingDown
small
kNotAvailable
-debug
unreliableNodes
Attach
kWPANTUNDProperty_NCPHardwareAddress
is_current_node_parent
kRetry
hapCoAPTokenInfo
InterfaceNotFound
preferred
startFWUpdate
routerMode
discover
num_third_party_border_routers_in_cur_nw
prefix_length
channel
 => 
crit
notice
nodeBVendorName
-crit
meshDiagAnalysisResults
com.apple.private.fillmore.AccessoryInfo.modification
Empty
Service data is not Given
v16@?0^v8
server_data
l
tx_app_success_perc
is_border_router_advertised
isWED
commandData
GetInterfaces
numResidentsInHome
parent_changes_count
-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]
weightAsymmetricLinks
Network:Key
JoinerFailed_NoPeers
\nDIAGNOSIS: This error is specific to this specific type of NCP. The error\ncode is %d (0x%02X). Consult the NCP documentation for an explantion of this\nerror code.\n\n
KeyErrorString
v16@?0{dict={object=^v}}8
roleDisableDetached
DiscoverScanStart
rxTotal
threadTXErrorEnum
isBorderRouter
ServiceAdd
getTriggerBasedStats
hasVendorRoute
ipv6Addresses
unreachableNodeCount
unsupportedNodes
threadMeshWirelessInsights
Failed to stop FW Update
threadRxStatusBitmap
interface
EventSystemPoweredOn
kBusy
ipaddr_lookup
hasOffgridRoute
penaltyCriticalNodes
EnergyScanStart
delayWedConnectionRetryRequest
nodeARloc16
penaltyAsymmetricLinks
InvalidArgument
\nDIAGNOSIS: This action was aborted due to a change in the NCP's state.\nThis can occur if the interface is disabled while you were trying to join,\nor if AutoDeepSleep kicked in for some reason.\n\n
tx_failure
num_thread_networks
threadMeshInfoForHomeMetrics
NCPCrashed
$
Leaving current WPAN. . .\n
accessoryManufacturer
com.apple.private.fillmore.threadLeave
defaultRoute
slaac
WPANCTL: Invalid type while looping through Array \n
networkName
end-device
KeyTimeout
destination
tlv
tx_icmp_err
Failed to stop pairing
Pass phrase is not given
provideEmac
rx_failure
linkQualities
updatePrimaryResident
ServerStateStopped
attachToNetwork
GenerateDiagnostics
path
2
4
void CtrXPC::Client::processClientApiAsyncWithCompletion(Cmd_data &, ResultBlockWithData, const std::string &)
com.apple.wpantund.xpc
com.apple.private.fillmore.threadStart
activeOperationalDataset
RSSI
void CtrXPC::Client::processClientApiAsyncWithCompletion(Cmd_data &, ResultBlockWithData, const std::string &)_block_invoke
numOnMeshPrefixes
ipv6Address
transactionStatus
Failed to start FW Update
PropertyNotFound
threadLeave
ServerStateStarting
Timeout waiting for response from helper server
accessoryModel
threadMeshReachabilityErrorEnum
nodeAExtAddress
com.apple.private.fillmore.threadMeshInfoForHomeMetrics
InvalidType
commissionOrFormNetwork
Network:PSKc
Canceled
weightUnreachableNodes
JoinerFailed_Unknown
criticalNodesResult
connected
matterSessionInfo
asymmetricLinks
com.apple.private.fillmore.threadMeshWirelessInsights
joiner_flag
eventList
consecutiveFailureCount
v40@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8
info
hostName
Joiner:PSKd
synchronized-sleepy-end-device
v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8{dict={object=^v}}40
-all
parentChanged
activeOperationalDataset parameter is encoded incorrectly
reasonFlags
reverseLinkCost
%02X
num_apple_border_routers_in_cur_nw
threadMeshRXErrorEnum
FormFailedAtScan
basic_string
communicationProtocol
activeOperationalDataset parameter is required
nodeBIpv6Addresses
nodeBVendorModel
enterprise_number
medium
ipaddr_add
invalid
Joiner:ProvisioningUrl
%s
\nDIAGNOSIS: This error indicates that either the device in a state where your\nrequest makes no sense or the parameters of your request were invalid. Check your\narguments and verify that you are allowed to perform the given operation when
threadRXReachabilityStatusBitMap
scoreSummary
NCPInvalidRange
%d \n
kWPANTUNDProperty_NestLabs_NetworkAllowingJoin
numAppleBRs
asymmetricLinkCount
ipAddress
%s/%s
3
emerg
coexRxDeniedReqsPerc
leaderName
panid
\nDIAGNOSIS: The NCP has unexpectedly crashed and rebooted. Please see the\nwpantund logs for more information and try again.\n\n
RLOC16
kWPANTUNDProperty_NetworkPANID
\nDIAGNOSIS: The requested operation can't be completed because the given\nnetwork interface doesn't exist or it isn't managed by wpantund. If you are\nusing wpanctl in interactive mode, you can use the `ls` command to get a list\nof valid 
Unknown internal error
routerId
forwardLinkCost
rx_success
resolveStatus
InvalidForCurrentState
preferredLifetime
Invalid Channel number provided
lurker
ServerStateError
outputUniqueNetworkId
prevOutput
-[CtrClient getThreadMeshWirelessInsights:completionHandler:]
-[CtrClient threadStart:geoAvailable:isPrimaryUser:waitForSync:completion:]_block_invoke
com.apple.private.fillmore.channel.set
numMatterThreadAccessories
-[CtrClient init:]
-[CtrClient threadMeshInfoForHomeMetrics:completionHandler:]_block_invoke_2
command
value
weightBottlenecks
clearThreadCredentials
weightUnreliableNodes
is_direct_link
AverageRssi
Performing command: %s
getEntitlementFromMethodName: method: %s, property_name: %s, serach_entitelement: %s, ret: %s
Gateway configured.\n
Successfully stopped FW update... \n
%s:%d Array element %hhu: threadTXErrorEnum:%llu threadMeshRXErrorEnum:%llu threadMeshReachabilityErrorEnum:%llu srpErrorEnum:%llu threadRXReachabilityStatusBitMap: %llu threadTXReachabilityStatusBitMap:%llu threadRXReachabilityStatusBitMap
%s:%d: Even after the success, output value is nil
Updating home thread info ... \n
%s : xpanid:0x%016llX
%s:%d Returning client api call
%s failed to start FW update with error %d. %s\n
Daemon ready received
routerMode flag : %d\n
%s:%d: Even after the success, output value is nil, returning error
Successfully Scan Completed!\n
Starting Scan of Type %d \n
Could not create CtrXPCClient, verify parameters\n
%s:%d Returning Error
%s:%d: threadstart is successful !
Sucessfully formed the Network... \n
Destroy server connection
Partial (insecure) join. Credentials needed. Update key to continue.
Successfully attached... \n
Create server connection
Get Thread Mesh Wireless Insights succeeded ... \n
%s:%d Returning client api call for sequenceNumber : %llu
has network key: (boolean : [%u])
Sucessfully sent nw diag req - \"%s\" \n
getTriggerData response is a dictionary \n
Failure: %s
Server connection pid:%d is not same as reply connection pid:%d. Server possibly getting destroyed
%s threadInfoForMetricsInputList is empty
eMAC : %@\n
Service is added.\n
%s failed to stop pairing with error %d. %s\n
Checked in state is %u, skipping
Changing checked in state from %u -> %u
waitForSync flag : %d \n
%s:%d: threadstart failed !
Output UUID : %@, UUID-NSSTRING : %@ \n
channel:%u
panid:0x%04X
Bad Prefix \"%s\", errno=%d (%s)\n
Parsed wireless insights - critical: %u, unreliable: %u, unreachable: %u, asymmetric links: %u, bottleneck: %u, unsupported: %u, health score: %u
Leaving the Network... \n
%s failed to attach with error %d. %s\n
Client::processStatsDataPerAccessory Reply is not a dictionary.
Successful: %s
Get Thread Mesh Wireless Insights: randomized=%d
Resume command success.\n
, key:[%s]
Server Ready
Sent reply for: %s
getServer_sync failed
Successfully started Pairing... \n
eMAC str : %@\n
%s failed to start pairing with error %d. %s\n
Connection \"%s\" not allowed for: %s \n
Reply is not a dictionary \n
Running Thread Diagnostics Monitor... \n
Sucessfully generated PSKc ... \n
Client::processStatsData Reply is not a dictionary.
Get Thread Info for Metrics succeeded send to server ... \n
geoAvailable flag : %d\n
isPrimaryUser flag : %d\n
Attaching to WPAN with properties
Successfully started FW Update... \n
, channel-mask:0x%x
Forming WPAN \"%s\"\n
, key-index:%d
Joiner command is successful.\n
joiner: cmd: %s, pspskd: %s \n
Sucessfully sent nw diag req method- \"%s\" \n
Events state is %u, so skipping
Started on name '%s'
Updating primary resident information... \n
%s:%d:Error Client \"%s\" Destroyed
primaryInfo=%@,  isPrimaryResident=%d, isPrimaryResidentThreadCapable=%d\n
%s failed to stop FW update with error %d. %s\n
Invalid hex string length %zu for extended address (must be even): %s
%s failed with error %d. %s\n
Successfully stopped pairing... \n
Left current WPAN. . .\n
, legacy-prefix:\"%s\"
%s %d
activeOperationalDataset : %@ \n
Reset command success.\n
Set Property: Property type is neither String nor Data
Using prefix \"%s\"\n
Successfully formed!\n
Changing event state from %u -> %u
%s:%d:Failed here errorCode:%d
Connection \"%s\" allowed for: %s \n
WPANCTL: Resetting NCP. . .\n
Client \"%s\" Destroyed
WPANCTL: Hard Resetting NCP. . .\n
%s: xpc connection obj in clinet: %p: \n %s
entitlements in Server: %s
Response is: %s
Response is: %s \n
Sucessfully Started the Network... \n
Sucessfully set the property - \"%s\" \n
Output Network ID = %s.\n
xpanid:0x%016llX
Interface(%zu) -> (%s)\n
Resuming saved WPAN. . .\n
, mesh-local-prefix:\"%s\"
Reply not sent for: %s
Accessory Cache updated\n
, xpanid:0x%016llX
Client \"%s\" Destroyed, Release Notification Center Observer
Client received notification: %s
Watching for notification: %s
Message From Server: %s
inUniqueId string : %@ \n
, channel:%d
Failed to set channel %d Channel value is not in valid range
Service is removed.\n
getTriggerData response is not a dictionary \n
Extra increased to: %d
Extra decreased to %u
%s:%d: Thread radio is not supported on this device.
Bad prefix \"%s\"\n
Forming WPAN \"%s\" as node type \"%s\"
Joined network.\n
dict_out = %s
%s valid completion handler was not provided
WPANCTL error: Bad type for interface list \n
name:%s
key:[%s]
, panid:0x%04X
CtrXPCClient GetCmd Helper: Not handled V Type = %llu \n
Sucessfully Attached to the Network \n
```
