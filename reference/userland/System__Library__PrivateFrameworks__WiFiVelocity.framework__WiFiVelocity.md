# `/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`

iOS 27.2 dyld shared cache image. Version `1190.20.0.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/Frameworks/CoreData.framework/CoreData`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration`
- `/usr/lib/libarchive.2.dylib`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`
- `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`
- `/System/Library/PrivateFrameworks/Bom.framework/Bom`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 30 classes, 5 protocols, 838 methods, 234 properties

### Class pages

Every class and protocol, with its methods: [`NSCoding`](../objc/NSCoding_WiFiVelocity.protocol.md), [`NSCopying`](../objc/NSCopying_WiFiVelocity.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_WiFiVelocity.protocol.md), [`W5AWDLStatus`](../objc/W5AWDLStatus_WiFiVelocity.md), [`W5ActivityManager`](../objc/W5ActivityManager_WiFiVelocity.md), [`W5BluetoothDevice`](../objc/W5BluetoothDevice_WiFiVelocity.md), [`W5BluetoothStatus`](../objc/W5BluetoothStatus_WiFiVelocity.md), [`W5Client`](../objc/W5Client_WiFiVelocity.md), [`W5DebugConfiguration`](../objc/W5DebugConfiguration_WiFiVelocity.md), [`W5DiagnosticsMode`](../objc/W5DiagnosticsMode_WiFiVelocity.md), [`W5DiagnosticsModePeer`](../objc/W5DiagnosticsModePeer_WiFiVelocity.md), [`W5DiagnosticsTestRequest`](../objc/W5DiagnosticsTestRequest_WiFiVelocity.md), [`W5DiagnosticsTestResult`](../objc/W5DiagnosticsTestResult_WiFiVelocity.md), [`W5Event`](../objc/W5Event_WiFiVelocity.md), [`W5FeatureAvailability`](../objc/W5FeatureAvailability_WiFiVelocity.md), [`W5LogItemReceipt`](../objc/W5LogItemReceipt_WiFiVelocity.md), [`W5LogItemRequest`](../objc/W5LogItemRequest_WiFiVelocity.md), [`W5NetworkStatus`](../objc/W5NetworkStatus_WiFiVelocity.md), [`W5Peer`](../objc/W5Peer_WiFiVelocity.md), [`W5PeerDiscoveryConfiguration`](../objc/W5PeerDiscoveryConfiguration_WiFiVelocity.md), [`W5PeerDiscoveryEvent`](../objc/W5PeerDiscoveryEvent_WiFiVelocity.md), [`W5PingResult`](../objc/W5PingResult_WiFiVelocity.md), [`W5PowerStatus`](../objc/W5PowerStatus_WiFiVelocity.md), [`W5Status`](../objc/W5Status_WiFiVelocity.md), [`W5SummaryFaults`](../objc/W5SummaryFaults_WiFiVelocity.md), [`W5SummaryLinkTests`](../objc/W5SummaryLinkTests_WiFiVelocity.md), [`W5SummaryRecoveries`](../objc/W5SummaryRecoveries_WiFiVelocity.md), [`W5WiFiChannel`](../objc/W5WiFiChannel_WiFiVelocity.md), [`W5WiFiLinkQualityUpdate`](../objc/W5WiFiLinkQualityUpdate_WiFiVelocity.md), [`W5WiFiPreferredNetwork`](../objc/W5WiFiPreferredNetwork_WiFiVelocity.md), [`W5WiFiScanResult`](../objc/W5WiFiScanResult_WiFiVelocity.md), [`W5WiFiStatus`](../objc/W5WiFiStatus_WiFiVelocity.md), [`W5XPCEventDelegate`](../objc/W5XPCEventDelegate_WiFiVelocity.protocol.md), [`W5XPCRequestDelegate`](../objc/W5XPCRequestDelegate_WiFiVelocity.protocol.md)

### Classes

`NSTask`, `W5AWDLStatus`, `W5ActivityManager`, `W5BluetoothDevice`, `W5BluetoothStatus`, `W5Client`, `W5DebugConfiguration`, `W5DiagnosticsMode`, `W5DiagnosticsModePeer`, `W5DiagnosticsTestRequest`, `W5DiagnosticsTestResult`, `W5Event`, `W5FeatureAvailability`, `W5LogItemReceipt`, `W5LogItemRequest`, `W5NetworkStatus`, `W5Peer`, `W5PeerDiscoveryConfiguration`, `W5PeerDiscoveryEvent`, `W5PingResult`, `W5PowerStatus`, `W5Status`, `W5SummaryFaults`, `W5SummaryLinkTests`, `W5SummaryRecoveries`, `W5WiFiChannel`, `W5WiFiLinkQualityUpdate`, `W5WiFiPreferredNetwork`, `W5WiFiScanResult`, `W5WiFiStatus`

### Protocols

`NSCoding`, `NSCopying`, `NSSecureCoding`, `W5XPCEventDelegate`, `W5XPCRequestDelegate`

### Properties

```
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSString",C,N,V_macAddress) macAddress;
@property (T@"NSString",C,N,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSArray",C,N,V_ipv6Addresses) ipv6Addresses;
@property (TB,N,V_power) power;
@property (T@"NSData",C,N,V_awdlSyncEnabled) awdlSyncEnabled;
@property (T@"NSData",C,N,V_awdlSyncState) awdlSyncState;
@property (T@"NSData",C,N,V_awdlSyncChannelSequence) awdlSyncChannelSequence;
@property (T@"NSData",C,N,V_awdlStrategy) awdlStrategy;
@property (T@"NSData",C,N,V_awdlElectionParameters) awdlElectionParameters;
@property (T@"NSData",C,N,V_awdlMasterChannel) awdlMasterChannel;
@property (T@"NSData",C,N,V_awdlSecondaryMasterChannel) awdlSecondaryMasterChannel;
@property (T@"NSData",C,N,V_awdlOpMode) awdlOpMode;
@property (T@"NSData",C,N,V_awdlSyncParameters) awdlSyncParameters;
@property (T@"NSData",C,N,V_awdlPeerDatabase) awdlPeerDatabase;
@property (T@"NSData",C,N,V_awdlSidecarDiagnostics) awdlSidecarDiagnostics;
@property (TB,N,V_isAWDLRealTimeMode) isAWDLRealTimeMode;
@property (Tq,N,V_airDropDiscoverableMode) airDropDiscoverableMode;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,V_transactionsStarted) transactionsStarted;
@property (T@"NSDate",&,V_dateFirstTransaction) dateFirstTransaction;
@property (TQ,V_transactionsCompleted) transactionsCompleted;
@property (T@?,C,N,V_alternateExecutionBlockForCleanExit) alternateExecutionBlockForCleanExit;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_address) address;
@property (TB,N,V_isPaired) isPaired;
@property (TB,N,V_isCloudPaired) isCloudPaired;
@property (TB,N,V_isConnected) isConnected;
@property (TB,N,V_isAppleDevice) isAppleDevice;
@property (TB,N,V_isLowEnergy) isLowEnergy;
@property (TQ,N,V_majorClass) majorClass;
@property (TQ,N,V_minorClass) minorClass;
@property (Tq,N,V_rssi) rssi;
@property (T@"NSString",C,N,V_afhMap) afhMap;
@property (Tq,N,V_connectionMode) connectionMode;
@property (TQ,N,V_connectionModeInterval) connectionModeInterval;
@property (Tq,N,V_manufacturer) manufacturer;
@property (TQ,N,V_lmpVersion) lmpVersion;
@property (TQ,N,V_lmpSubversion) lmpSubversion;
@property (Tq,N,V_role) role;
@property (TB,N,V_powerOn) powerOn;
@property (T@"NSString",C,N,V_address) address;
@property (TB,N,V_isDiscoverable) isDiscoverable;
@property (TB,N,V_isConnectable) isConnectable;
@property (TB,N,V_isScanning) isScanning;
@property (T@"NSArray",C,N,V_devices) devices;
@property (T@?,C,N,V_eventCallback) eventCallback;
@property (T@"W5DiagnosticsMode",&,N,V_diagnosticsMode) diagnosticsMode;
@property (Tq,N,V_wifi) wifi;
@property (Tq,N,V_megaWiFiProfile) megaWiFiProfile;
@property (Tq,N,V_noLoggingWiFiProfile) noLoggingWiFiProfile;
@property (Tq,N,V_eapol) eapol;
@property (Tq,N,V_bluetooth) bluetooth;
@property (Tq,N,V_stbc) stbc;
@property (T@"NSArray",&,N,V_peers) peers;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (T@"NSDictionary",&,N,V_info) info;
@property (T@"NSMutableDictionary",&,N,V_timestamps) timestamps;
@property (Tq,R,N,V_state) state;
@property (T@"NSMutableDictionary",&,N,V_info) info;
@property (T@"W5Peer",&,N,V_peer) peer;
@property (Tq,N,V_role) role;
@property (T@"NSUUID",C,N,V_uuid) uuid;
@property (Tq,N,V_testID) testID;
@property (T@"NSDictionary",C,N,V_configuration) configuration;
@property (T@"NSUUID",C,N,V_uuid) uuid;
@property (Tq,N,V_testID) testID;
@property (TB,N,V_result) result;
@property (TB,N,V_didPass) didPass;
@property (T@"NSDictionary",C,N,V_configuration) configuration;
@property (T@"NSDictionary",C,N,V_info) info;
@property (T@"NSError",C,N,V_error) error;
@property (Td,N,V_testStarted) testStarted;
@property (Td,N,V_testCompleted) testCompleted;
@property (Tq,N,V_eventID) eventID;
@property (Td,N,V_timestamp) timestamp;
@property (T@"NSDictionary",C,N,V_info) info;
@property (T@"W5Peer",C,N,V_peer) peer;
@property (T@"W5LogItemRequest",C,N,V_request) request;
@property (T@"NSArray",C,N,V_relativeURLs) relativeURLs;
@property (T@"NSDictionary",C,N,V_info) info;
@property (Td,N,V_startedAt) startedAt;
@property (Td,N,V_completedAt) completedAt;
@property (T@"NSUUID",C,N,V_uuid) uuid;
@property (Tq,N,V_itemID) itemID;
@property (T@"NSDictionary",C,N,V_configuration) configuration;
@property (T@"NSString",C,N,V_primaryIPv4InterfaceName) primaryIPv4InterfaceName;
@property (T@"NSString",C,N,V_primaryIPv4ServiceName) primaryIPv4ServiceName;
@property (T@"NSString",C,N,V_primaryIPv6InterfaceName) primaryIPv6InterfaceName;
@property (T@"NSString",C,N,V_primaryIPv6ServiceName) primaryIPv6ServiceName;
@property (T@"NSString",C,N,V_primaryIPv4ServiceID) primaryIPv4ServiceID;
@property (T@"NSString",C,N,V_primaryIPv6ServiceID) primaryIPv6ServiceID;
@property (T@"NSArray",C,N,V_primaryIPv4Addresses) primaryIPv4Addresses;
@property (T@"NSArray",C,N,V_primaryIPv6Addresses) primaryIPv6Addresses;
@property (T@"NSString",C,N,V_primaryIPv4Router) primaryIPv4Router;
@property (T@"NSString",C,N,V_primaryIPv6Router) primaryIPv6Router;
@property (T@"NSArray",C,N,V_primaryDNSAddresses) primaryDNSAddresses;
@property (TI,N,V_isAppleReachable) isAppleReachable;
@property (T@"RPCompanionLinkDevice",&,N,V_device) device;
@property (T@"NSString",C,N,V_peerID) peerID;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_build) build;
@property (T@"NSString",C,N,V_os) os;
@property (T@"NSString",C,N,V_version) version;
@property (T@"NSData",C,N,V_iconImage) iconImage;
@property (Tq,R,D,N) type;
@property (TB,N,V_nearby) nearby;
@property (Tq,N,V_proximity) proximity;
@property (Tq,N,V_discoveryFlags) discoveryFlags;
@property (Tq,N,V_controlFlags) controlFlags;
@property (Tq,N,V_discoveryFlags) discoveryFlags;
@property (Tq,N,V_controlFlags) controlFlags;
@property (T@"NSArray",&,N,V_peersFound) peersFound;
@property (T@"NSArray",&,N,V_peersLost) peersLost;
@property (T@"NSDictionary",&,N,V_info) info;
@property (T@"NSString",C,N,V_address) address;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (Td,N,V_timeout) timeout;
@property (Td,N,V_wait) wait;
@property (Td,N,V_interval) interval;
@property (Tq,N,V_count) count;
@property (Tq,N,V_trafficClass) trafficClass;
@property (TQ,N,V_dataLength) dataLength;
@property (Td,N,V_packetLoss) packetLoss;
@property (Td,N,V_min) min;
@property (Td,N,V_max) max;
@property (Td,N,V_avg) avg;
@property (Td,N,V_stddev) stddev;
@property (T@"NSString",C,N,V_command) command;
@property (T@"NSString",C,N,V_output) output;
@property (Td,D,N) timestamp;
@property (Td,N,V_startedAt) startedAt;
@property (Td,N,V_endedAt) endedAt;
@property (Tq,N,V_powerSourceType) powerSourceType;
@property (Ti,N,V_batteryWarningLevel) batteryWarningLevel;
@property (Td,N,V_internalBatteryLevel) internalBatteryLevel;
@property (TI,N,V_powerStateCaps) powerStateCaps;
@property (T@"W5WiFiStatus",C,N,V_wifi) wifi;
@property (T@"W5AWDLStatus",C,N,V_awdl) awdl;
@property (T@"W5BluetoothStatus",C,N,V_bluetooth) bluetooth;
@property (T@"W5NetworkStatus",C,N,V_network) network;
@property (T@"W5PowerStatus",C,N,V_power) power;
@property (T@"NSArray",C,N,V_diagnosticsModes) diagnosticsModes;
@property (T@"W5SummaryFaults",C,N,V_lastHrFaults) lastHrFaults;
@property (T@"W5SummaryLinkTests",C,N,V_lastHrLinkTests) lastHrLinkTests;
@property (T@"W5SummaryRecoveries",C,N,V_lastHrRecoveries) lastHrRecoveries;
@property (T@"NSArray",&,N,V_lastHrFaults) lastHrFaults;
@property (T@"NSArray",&,N,V_lastHrLinkTests) lastHrLinkTests;
@property (T@"NSArray",&,N,V_lastHrRecoveries) lastHrRecoveries;
@property (Tq,R,N,V_channel) channel;
@property (TI,R,N,V_flags) flags;
@property (Tq,N,V_rssi) rssi;
@property (Tq,N,V_txRate) txRate;
@property (Tf,N,V_cca) cca;
@property (Td,N,V_timestamp) timestamp;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_ssidString) ssidString;
@property (T@"NSData",C,N,V_ssid) ssid;
@property (Tq,N,V_security) security;
@property (TB,N,V_isEnabled) isEnabled;
@property (TB,N,V_isPasspoint) isPasspoint;
@property (T@"NSString",C,N,V_domainName) domainName;
@property (TB,N,V_isCaptive) isCaptive;
@property (TB,N,V_isHidden) isHidden;
@property (TB,N,V_isMultiAP) isMultiAP;
@property (T@"NSDate",C,N,V_lastJoinedTimestamp) lastJoinedTimestamp;
@property (T@"NSDictionary",C,N,V_scanRecord) scanRecord;
@property (T@"NSData",C,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_ssidString) ssidString;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (T@"NSArray",C,N,V_supportedSecurityTypes) supportedSecurityTypes;
@property (Ti,N,V_supportedPHYModes) supportedPHYModes;
@property (Tq,N,V_rssi) rssi;
@property (Tq,N,V_noise) noise;
@property (TB,N,V_isIBSS) isIBSS;
@property (T@"NSString",C,N,V_countryCode) countryCode;
@property (Tq,N,V_beaconInterval) beaconInterval;
@property (TB,N,V_isPasspoint) isPasspoint;
@property (TB,N,V_isPersonalHotspot) isPersonalHotspot;
@property (TB,N,V_isAppleSWAP) isAppleSWAP;
@property (T@"NSString",C,N,V_airPortBaseStationModelName) airPortBaseStationModelName;
@property (T@"W5WiFiChannel",C,N,V_channel) channel;
@property (TB,N,V_supportsWEPCipher) supportsWEPCipher;
@property (TB,N,V_supportsTKIPCipher) supportsTKIPCipher;
@property (T@"NSString",C,N,V_macAddress) macAddress;
@property (T@"NSString",C,N,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSArray",C,N,V_capabilities) capabilities;
@property (TB,N,V_powerOn) powerOn;
@property (T@"NSData",C,N,V_power) power;
@property (Ti,N,V_opMode) opMode;
@property (T@"NSString",C,N,V_ssidString) ssidString;
@property (T@"NSData",C,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (Tq,N,V_rssi) rssi;
@property (TQ,N,V_cca) cca;
@property (Tq,N,V_noise) noise;
@property (TQ,N,V_txPacketErrorRate) txPacketErrorRate;
@property (Td,N,V_txRate) txRate;
@property (Tq,N,V_security) security;
@property (TI,N,V_eapolControlMode) eapolControlMode;
@property (TI,N,V_eapolSupplicantState) eapolSupplicantState;
@property (Ti,N,V_phyMode) phyMode;
@property (TQ,N,V_mcsIndex) mcsIndex;
@property (TQ,N,V_guardInterval) guardInterval;
@property (TQ,N,V_numberOfSpacialStreams) numberOfSpacialStreams;
@property (T@"W5WiFiChannel",C,N,V_channel) channel;
@property (T@"NSArray",C,N,V_linkQualityUpdates) linkQualityUpdates;
@property (T@"NSArray",C,N,V_supportedChannels) supportedChannels;
@property (T@"NSString",C,N,V_countryCode) countryCode;
@property (T@"NSString",C,N,V_networkServiceID) networkServiceID;
@property (Tq,N,V_ipv4ConfigMethod) ipv4ConfigMethod;
@property (Tq,N,V_ipv6ConfigMethod) ipv6ConfigMethod;
@property (T@"NSArray",C,N,V_ipv4Addresses) ipv4Addresses;
@property (T@"NSArray",C,N,V_ipv6Addresses) ipv6Addresses;
@property (T@"NSString",C,N,V_ipv4RouterAddress) ipv4RouterAddress;
@property (T@"NSString",C,N,V_ipv6RouterAddress) ipv6RouterAddress;
@property (T@"NSArray",C,N,V_dnsAddresses) dnsAddresses;
@property (Ti,N,V_btcMode) btcMode;
@property (T@"NSData",C,N,V_chainAck) chainAck;
@property (T@"NSData",C,N,V_txChainPower) txChainPower;
@property (T@"NSData",C,N,V_desense) desense;
@property (T@"NSData",C,N,V_desenseLevel) desenseLevel;
@property (T@"NSData",C,N,V_btcConfig) btcConfig;
@property (T@"NSData",C,N,V_btcProfiles2GHz) btcProfiles2GHz;
@property (T@"NSData",C,N,V_btcProfiles5GHz) btcProfiles5GHz;
@property (T@"W5WiFiScanResult",C,N,V_lastJoinedScanResult) lastJoinedScanResult;
@property (T@"W5WiFiPreferredNetwork",C,N,V_lastJoinedPreferredNetwork) lastJoinedPreferredNetwork;
@property (T@"NSArray",C,N,V_cachedScanResults) cachedScanResults;
@property (TB,N,V_smartCCADesenseSupported) smartCCADesenseSupported;
@property (TB,N,V_smartCCADesenseUSBPresence) smartCCADesenseUSBPresence;
@property (TB,N,V_isSnifferSupported) isSnifferSupported;
```

## Strings (1,417)

```
com.apple.wifivelocity.task.%@
__W5ArchiveAddURLToArchive
Internal Battery Level: %.0f\n
_mcsIndex
Delay
Apple Watch
VO
    802.1X Supplicant    : %s\n
q
Bluetooth                 : %s\n
::
Uncommon Beacon Interval
[kextstat]
Bonjour Records
Additional Log
KC Technology
Supports 6e: %s\n
Wi-Fi Profile (Mega)      : %s\n
No Wi-Fi Security (Open)
Wi-Fi Status
Integrated System Solution
Nordic
/var/mobile/Library/Logs/CrashReporter/CoreCapture/WiFi
Pass: %@\n
Rapport 
Terax
    Sniffer Supported    : %s\n
com.apple.wifivelocityd
-[W5SummaryFaults initWithSummaryFaults:]
Max: %.2fms\n
%@ has good signal (RSSI=%lddBm, SNR=%lddB)
Modem
HiFi
Infineon
_network
isPasspoint: %s\n
Hidden Network
Broadcom
Master Channel: %u\n
Interface Name: %@\n
WIFI\n
IPv4Addresses
For Dump Logs Event
Helmet
Avago
-[W5Event setInfo:]
    %s\n
_endedAt
RealityDevice
Mode: %@\n
a
  Distance From Top     %u\n
Scan + RealtimeData
Failed to perform speed test
Dynamic Store
DNS-SD State & Cached Local Records
5GHz[%i,%i] lvl %i
6to4
kW5LocWiFiDiagnosticsName
W5DiagnosticsMode.m
  Flags                 0x%x\n
Home Theather
IPv4ServiceName
\nLastHr Recoveries=>\n%@
_countryCode
AdoptedCountryCode
%@ is not Passpoint
System Profiler
_phyMode
_identifier
Run ping test to peer
Disconnected
0x%lx
    Country Code         : %s\n
      Sidecar Tx Latency   : %ums\n
Collected peer device info from %@: found %lu devices
Heart Rate Monitor
com.apple.WiFiVelocity
/Library/Logs/CrashReporter
_isEnabled
%ld PNL networks have conflicting PHY modes (802.11ac).
Scanner
    Power                : %s [%s]\n
AWDL is active
Staccato
_primaryIPv6ServiceName
Lucent
Mitsubishi
Eclipse
Current network is 'leaky'
Event History
Ping /24 Subnet
System and Chips
_timestamps
WiFiStats (Post)
Accel Semi
AirDrop Discoverable Mode: %@\n
terminationStatus
_batteryWarningLevel
PreferredNetworks
END Wi-Fi Default Route
Socket Comms
    Sync State             : %s\n
AudioAccessory
Video Monitor
Conexant
EMMicro
26.4
Role: %@\n
_btcConfig
_min
POWER\n
RSSI
IPv6InterfaceName
numberOfIOSDevices
Server
                                                                                     %@ / %.2fms / %@ / %ld bytes / i=%fs / W=%fs / t=%fs / c=%ld\n
Low Power
Atmel
      Extension Length     : %d\n
-[W5Client collectLogs:configuration:update:reply:]
%ld (%ld GHz) / %ld MHz
Address: %@\n
_stbc
\t%@\n
Uncommon DTIM Interval
Could retrieve 'https://captive.apple.com' over Wi-Fi
com.apple.wifi.plist
Disabled
Avg: %.2fms\n
AirPlay Logs
/var/mobile/Library/Logs/CrashReporter/WiFi/WiFiManager
Compress
_isConnectable
Diagnostics Mode UUID='%@' State='%@ (%ld)' with peers='%@' info='%@'
AWDL Real Time Mode
[top]
_isCloudPaired
, 
W5DiagnosticsModePeer.m
isCaptive: %s\n
Power: %s\n
stop
Detects if the current network name is ambiguous or common
No Wi-Fi networks are visible
IPv6ServiceName
For sysdiagnose (BT)
Interop ID
    Primary IPv6         : None\n
Sniffer: %s\n
STBC: %@\n
FailedToStop
      Election ID          : %u\n
      PeerDB Count         : %u\n
_manufacturer
IPv6Router
AVM Berlin
APT
BTC Profile 2.4 GHz: %s\n
_interfaceName
_dataLength
TCP Dump (Post)
For Datapath Stall Event
Full TDM Preempt
%@WiFi RSSI Threshold / Hysteresis: %i/%i\n
Marvell
Info: %@\n
Signia
q24@?0@\"NSNumber\"8@\"NSNumber\"16
isHidden: %s\n
_interval
Qualcomm
    Noise                : %i dBm\n
_ssidString
_state
Digital Pen
      Desense Lvl               : %i\n
v24@?0@\"NSTask\"8@\"NSError\"16
Wi-Fi                     : %s\n
Network Status Changed
%@Max SISO Resp Power: [
Parthus
      Desense Thr               : [%i,%i]\n
/Library/Preferences/com.apple.wifi.known-networks.plist
Peer DB Count: %ld peers\n
IPv4 Addresses: %lu\n
_capabilities
    Paired           : %s\n
_diagnosticsMode
NE Master
Stop
Unknown (%ld)
Primary
Could not resolve 'captive.apple.com'
Lightweight
v16@?0@\"NSError\"8
_lastJoinedPreferredNetwork
iPhone
AUTO
Reserved
W5NoMemErr
_connectionMode
? (%lu)
Beacon interval is %ldms
For Tap-to-Radar
%@ConnectionOnTraffic: %s\n
_btcMode
  Self Metric           0x%x\n
slave [%02X:%02X:%02X:%02X:%02X:%02X]
Rohde and Schwarz
_peersLost
DNS Addresses: %lu\n
_ssid
Bluetooth: %@\n
Ping WAN (CFNetwork)
Bluetooth Status
v8@?0
_megaWiFiProfile
_isIBSS
Detect is the current network is hosted by a 'leaky' access point
System
Full TDM
%@Desense: %@\n
Yes
Scan + Data
/RemoteListener
Detected double NAT
WPA/WPA2 Enterprise
    DNS Addresses        : %s\n
    Security             : %s\n
com.apple.wifi-private-mac-networks.plist
Tx Per: %ld\n
isEnabled: %s\n
_os
%@ does not use WEP security (%@)
STA
Vehicle
Nokia
    Interface Name       : %s\n
W5PeerDiscoveryEvent.m
_isCaptive
2GHzChannel
RIM
Manufacturer: %@ (0x%lx, 0x%02lx)\n
Connectable: %s\n
STBC                      : %s\n
    IPv4 Config Method   : %s\n
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:startBlock:updateBlock:endBlock:]
_numberOfSpacialStreams
Wi-Fi Profile (NoLogging) : %s\n
Uses curl to load 'https://captive.apple.com'
IPv4Router
IPv6Addresses
[netstat]
WiFiDiagnostics
Mega WiFi Profile: %@\n
Diagnostics               : %@\n
Detects if custom DNS settings are configured for the Wi-Fi network service
Car
JandM
    Address              : %s\n
    IPv6 Address           : %s\n
/Library/Logs/wifi.log
-[W5PeerDiscoveryEvent initWithPeersFound:peersLost:info:]
\n
EAPOL                     : %s\n
Conflicting PHY Mode 11n
                         : %s\n
v24@?0@\"NSError\"8@\"W5Status\"16
Custom IPv4
%@ has poor signal (RSSI=%lddBm, SNR=%lddB)
No PNL networks have conflicting PHY modes (802.11ac).
Nearby
Matsushita
W5SummaryLinkTests.m
Primary IPv4 is Wi-Fi
-[W5ActivityManager osTransactionComplete:]_block_invoke
SSID: %@ (%@)\n
,
Wi-Fi Scan Results
      Min                : %i\n
      SISO Resp Enable          : [
_power
%@ is captive
RD
    Security             : None\n
    Desense              : %s\n
Siri
Did not detect custom DNS settings
AWDL Status Changed
    Channel Sequence       : %s\n
Ends Wi-Fi network service as the default route
IPv4InterfaceName
Tx
    Devices              : %lu (paired=%lu cloud=%lu connected=%lu)\n\n
Election Params:\n%@
_role
_channel
Security
2GHz[%i,%i] lvl %i
Active
 
No
_isPasspoint
Hidden Wi-Fi Scan Results
PingsReceived
Portable
_uuid
_stddev
WIFI LINK TESTS LAST HOUR\n
[mobilewifitool]
3Com
wifi.log
v32@?0@\"NSError\"8@\"NSArray\"16@\"NSURL\"24
_wifi
Detects if RSSI is < -70 dBm, or signal-to-noise ratio is < 10 dBm
Ping6 AWDL
not 
For Key Chord Trigger
/usr/local/
StartedAt: %@\n
Previous
Could reach 'www.apple.com'
%.1f%%
numberOfWatchOSDevices
Dynamic WEP
Pager
Hitachi
    BTC Mode             : %s\n
BSSID: %@\n
_airPortBaseStationModelName
Gathers #peers by OS type
Detects if bluetooth coexistence is active
NetworkName
Mobilian
wifivelocityd
WIFI FAULTS LAST HOUR\n
Found %ld hidden network(s)
IPConfig Logs
For WiFi Diagnostics Extension
WPA2 Personal
SiRF
    Scan Cache Count     : %lu\n
    Supported Channels   : %s\n
Last Joined: %@\n
Conflicting PHY Mode 11ac
11b
Blood Pressure Monitor
      Offset             : %i\n
Real Time Mode: %s\n
W5Event.m
:
PNL Contains Hidden
Automatic
Pulse Oximeter
LinkTests in last Hour: %lu\n
Conn Interval: %ld\n
On
%@ is marked as hidden
CoreCapture (Post)
    NetworkServiceID     : %s\n
_guardInterval
-[W5DiagnosticsMode updatePeer:]
Detects if any nearby Wi-Fi networks have the same SSID as the current preferred network, but use a conflicting security type
Could resolve 'captive.apple.com'
5GHz band is not congested
Unique Antennae
]\n
_connectionModeInterval
BLUETOOTH\n
    Power                  : %s\n
-[W5WiFiChannel init] unavailable
Tx Rate: %.1f\n
_hardwareMACAddress
5GHz band is congested
AWDL Status
Authenticating
Wearable
      Top Master           : %02X:%02X:%02X:%02X:%02X:%02X\n
type
IOPlatformExpertDevice
Sensor
      Desense                   : %s\n
    Master Channel         : n/a\n
%@ is using 802.11b
WPA2/WPA3 Personal
Sony Ericsson
yyyy-MM-dd_HH.mm.ss.SSS
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:outputFileHandle:errorFileHandle:launchHandler:reply:]_block_invoke
v32@?0@\"NSNumber\"8@\"NSDate\"16^B24
/Sniffer
None
Large PNL
Detects if the 2.4GHz band is congested
Wi-Fi is using '%@' for IPv6
-[W5Client collectLogsDiagnosticMode:update:reply:]
Tx Chain Power[%i]: %@\n
_domainName
BTConnectedCount
Collected diagnostics from %lu device(s)
Power Status Changed
WPA3 Enterprise
Starting
Leaky AP
Pings the currently assigned router address for the Wi-Fi network service to determine LAN connectivity using CFNetwork
Pings AWDL to exercise AWDL datapath
Wi-Fi is not associated
ScanResults
WAPI (Cert)
    Reason               : %s\n
              %@\n
_awdlOpMode
/AppleInternal/
%ldg%ld/%ld
_testStarted
Apple: %s\n\n
MCS Index: %ld\n
_packetLoss
[arp]
%@Reachable: %s\n
v40@?0@\"NSError\"8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSUUID\"32
com.apple.wifivelocity
iPod
Running
RSSI: %ld\n
No Scan Results
Found conflicting security types
Bluetooth Logs
    Primary IPv4         : %s (%s / %s)\n
\tInterface: %@\n
Wi-Fi does not have IPv4 assigned
Set Top Box
Integrated Silicon Solution
    Schedule State         : %s\n
Apple Reachable: 0x%X\n%@\n
SUSPENDED
    NSS                  : %i\n
/Library/Preferences/SystemConfiguration/com.apple.wifi.plist
Schedule State: %@\n
_primaryIPv4ServiceID
Could curl 'https://captive.apple.com'
-[W5Client queryDatabaseForPeer:fetch:reply:]_block_invoke
BT Coex Active
Legacy Wi-Fi Security (WEP)
AWDL is not active
Current network
Conn Mode: %@\n
%@ is an iOS PH
Handheld Scanner
_smartCCADesenseSupported
HH:mm:ss.SSS
Dext Coredumps
Inactive
2GHz
TTPCom
      Current            : %i\n
This file was generated because a log collection request is already in progress. When we detect this condition, we will attempt to collect basic WiFi logs inline.
_supportedChannels
WIFI RECOVERIES LAST HOUR\n
Current channel (%ld) is NOT congested (CCA = %@)
System Log
Link Local
MewTel
CTL
      Chain Tx Power Offset     : [
date
EAPOL: %@\n
Master
PDA
    Guard Interval       : %i\n
BTC Mode: %@\n
Diagnostics
Device Analytics Entity CSVs
%@Chain Tx Power Offset: [
<%ld>
MANUAL
Hold
%ld/%@
ENOENT
Passpoint
%@(%ld)
Detects adjacent/co-channel interference on the current channel
WirelessProx Logs
Sniff
CCA: %f%%\n
Determines if Wi-Fi is the primary IPv6 network service
[sysdiagnose]
Access Point
      AW Period            : %d\n
/Library/Preferences/SystemConfiguration/com.apple.wifi-networks.plist
_security
_lastJoinedTimestamp
AirPort Base Station
AirPortModelName
Gennum
    CCA                  : %i %%\n
%@ uses open security
MediaTek
v32@?0@\"NSTask\"8@\"NSData\"16@\"NSData\"24
eager-exit-timeout
_isHidden
New Logic
LEGACY_com.apple.wifi-networks.plist
    CloudPaired      : %s\n
      Sync Frame Period    : %d (Non-Election Master=%d)\n
tgz
UUID
%-43.43s%-12.3f%-10.10s%-20.12s%s\n
WaitingForCollection
Detects if the current network is marked as hidden
Gathers number of peers by OS type using Rapport framework over BLE
Custom DNS
Paired Bluetooth device count (%ld)
WiFiStats (Pre)
%@TransientConnection: %s\n
Card Reader
Renesas
yyyy'-'MM'-'dd HH:mm:ss.SSS
_isConnected
Off
NameOverride
IPextreme
    Tx Rate              : %.1f Mbps\n
    Op Mode                : %s\n
_result
_supportsTKIPCipher
PNLCount
Desktop
NEC
Synopsys
?
Glasses
Symbol
Norwood
_awdlSyncChannelSequence
txRate: %ld Mbps\n
Double NAT
IPv4ConfigMethod
PeerDiagnosticsResults
Display
Central
      Mode                      : %s\n
_internalBatteryLevel
Completed: %@\n
Supported Channels: %@\n
_txChainPower
Secondary
/Library/Preferences/SystemConfiguration/com.apple.wifi-private-mac-networks.plist
Power: %s [%@]\n
_noise
/Primary
Retrieve Apple
Conflicting Wi-Fi CC
%@BT RSSI Threshold / Hysteresis: %i/%i\n
_awdlElectionParameters
IPv4ConfigMethod: %@\n
_desense
Discoverable: %s\n
_peers
Data Length: %ldb\n
Mac
rProd
PNL contains hidden networks
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:startBlock:updateBlock:endBlock:]_block_invoke_7
  AW Length             %d\n
Peer Updated
%@InterventionRequired: %s\n
Inventel
3DSP
OAM
    Election Params        : n/a\n
Detects if the DTIM interval is not 3
ISDN
RSSI: %ld dBm\n
DetectedFaults
com.apple.wifivelocityd.rapportWake
SpeedTest (Download)
For Feedback Assistant
CONWISE
BTPairedCount
AWDL real time mode is active
Found conflicting country code(s) (%@)
%@ is not captive
? (%ld)
Network Preferences
errno
\nDiagnostics Modes=>\n%@
_count
Detects if the current Wi-Fi network is using 802.11b
YES
SmartCCA/Desense: %s (USB=%d)\n
Interval: %f\n
Concurrent
[darwinup]
CoreCapture (24h)
EAPOL Logs
Peripheral
    Primary IPv6         : %s (%s / %s)\n
Runs several diagnostics tests concurrently
Could ping DNS server(s) (%ld)
      Chain Ack                 : [
_awdlMasterChannel
_awdlPeerDatabase
\nAWDL=>\n%@
_macAddress
Packet Loss: %.2f%%\n
PeerDevicesInfo
System Log (24h)
    BSSID                : %s\n
_itemID
_awdlSyncState
ENOMEM
Description: %@\n
iOS Personal Hotspot
Primary IPv6 is Wi-Fi
Secondary Master Channel: %u\n
Noop
SystemConfiguration
%@Desense Threshold: [%i,%i]\n
Intel
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:outputFileHandle:errorFileHandle:launchHandler:reply:]_block_invoke_2
_lmpVersion
TCP Dump (Pre)
Gaming Console
Diagnostics Mode: %@\n
_eapol
%u.%u%@
RealTimeData
[wl curpower]
__BUSY__
MAC Address: %@ (hw=%@)\n
Noise: %ld\n
PingResults
Begins discovery of nearby devices
Detects if the 5GHz band is congested
_lmpSubversion
%u
For Background Event
Handheld
Seiko Epson
Fault: %@\n
Did not detect double NAT
Multiple
    DNS Addresses        : None\n
    Discoverable         : %s\n
_peersFound
AWDL\n
Wi-Fi Link
Begins Wi-Fi network service as the default route
Detected custom DNS settings
[ping]
Wave Plus
    Chain Ack            : [%s]\n
_avg
Slave
Wi-Fi PNL count (%ld)
Parrot
com.apple.wifivelocity.client.%@
v24@?0@\"W5DiagnosticsMode\"8@\"NSError\"16
com.apple.wifi.known-networks.plist
_testCompleted
Discovery='%@' Control='%@'
_command
No peers or no response
    802.1X Mode          : %s\n
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:startBlock:updateBlock:endBlock:]_block_invoke
Info=%@, 
_supportedPHYModes
 (error=%@)
_lastJoinedScanResult
_chainAck
Device Count: %lu (paired=%lu cloud=%lu connected=%lu)\n\n
Device Analytics Deployment Graph
PPP
Detects if the current Wi-Fi network is marked as a captive portal
Could not ping IP address(es) (%ld)
WPA2 Enterprise
    None\n
Sync State: %@\n
URLs: %@\n
Congested Wi-Fi 5GHz Band
WPA/WPA2 Personal
%@ - %@
Ericsson
com.apple.wifivelocity.features
BT Paired Count
For WiFi Diagnostics App
Apple TV
WEP
Configuration: %@\n
_completedAt
Op Mode: %s\n
\tDate: %@\n
<redacted>
Detects if the preferred networks list contains any hidden networks
%@Mode: %@\n
_awdlSecondaryMasterChannel
Enabled
Std Dev: %.2fms\n
Atheros Comms
v24@?0@\"NSError\"8@\"NSArray\"16
\nNetwork=>\n%@
IPv6 Assigned
Legacy Wi-Fi Rates (802.11b)
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:outputFilePath:errorFilePath:redirectErrorToOutput:launchHandler:reply:]
Nearby=%d, 
UNKNOWN
Detects if AWDL is enabled
40 MHz
%@Desense Level: %i\n
Desense: %@\n
Reach Apple
%@ is Passpoint
Misc
%@ is not an AirPort Base Station
Early
_controlFlags
IPv4ServiceID
[wl cca_get_stats]
Macronix
Park
v16@?0@\"NSNotification\"8
[ipconfig]
LoginWindow
_txPacketErrorRate
_networkServiceID
Custom Web Proxy
Cordless
Printer
v24@?0@\"NSError\"8@\"W5DebugConfiguration\"16
_isMultiAP
Camcorder
KeepParent
_powerOn
_isAppleSWAP
Detects if AWDL real time mode is active
No response
Battery
Gesture
Microsoft
EAPOL Supplicant: %@\n
interface
_request
Timeout: %f\n
+
2.4GHz band is congested
Ping (using IMFoundation)
CoreCapture Dump
Headset
CacheSysdiagnose
Battery Warning Level: %@\n
%s: Found preference value in domain: %@ key: %@
Country Code: %@\n
WiFi Status Changed
IBSS
BOOTP
Harmon
Reachability
%@
Poor Wi-Fi Signal
[ifconfig]
Device Analytics Store
Open Interface
    IPv6 Config Method   : %s\n
      Distance From Top    : %u\n
    Battery Warning Level: %s\n
_flags
W5ActivityManager
AWDL OpMode: %s
2.4GHz band is not congested
%s
    Channel              : %s\n
Reason
Error: %@\n
-[W5DebugConfiguration initDiagnosticsMode:wifiState:megaWiFiProfileState:noLoggingWiFiProfileState:eapolState:bluetoothState:]
Bluegiga
_discoveryFlags
ForceBLE 
[ioreg]
Authenticated
W5TimeoutErr
AFH Map: %@\n
_isAppleDevice
_info
_peer
%@ (%@)
????????????
Ping WAN
_ipv4ConfigMethod
Wait: %f\n
Traffic Class: %@\n
Detects if an IPv4 router and IP address have been assigned for the Wi-Fi network service
Detects if the current Wi-Fi network is Passpoint
Uses the CFHost API to attempt to resolve 'captive.apple.com'
Uses the SCNetworkReachability API to determine reachability to 'www.apple.com'
Held
Wi-Fi networks are visible
Datapath Stats
5GHz
Remote
Glucose Meter
Alcatel
    AWDL Enabled           : %s\n
_awdlStrategy
_name
_eapolControlMode
numberOfMacOSDevices
Digianswer
W5NotPermittedErr
%@ is not marked as hidden
\nBluetooth=>\n%@
    LE               : %s\n
 timestamps='%@'
iPad
Pings DNS server(s) to determine WAN connectivity using IMFoundation
%@ is not ambiguous
%@Offset: %i\n
Free2Move
Infra Priority
IPv6ConfigMethod
Ping (using CFNetwork)
[swvers]
%@IsDirect: %s\n
UPS
%@Min: %i\n
Reachable
Not Supported
Connected Bluetooth device count (%ld)
[spindump]
Jacket
-[W5ActivityManager debugTimerEnabled]
-[W5DebugConfiguration initDiagnosticsMode:wifiState:megaWiFiProfileState:noLoggingWiFiProfileState:eapolState:bluetoothState:stbcState:]
  Top Master Metric     0x%x\n
RFC Micro
IncludeEvents
\tRecovery Reason: %@\n
_btcProfiles5GHz
LOCAL
  Sync Frame Period     %d (NE Master=%d)\n
Pings DNS server(s) to determine WAN connectivity
Detects if any 40MHz (wide) Wi-Fi networks are using the 2.4GHz band
    IPv6 Address         : %s\n
    |> %s
_txRate
Captive Portal
Hosts
Final
_lastHrFaults
Detects if an IPv6 router and IP address have been assigned for the Wi-Fi network service
    DNS                  : %s\n
_isLowEnergy
NSS: %ld\n
Noise
Current network is not 'leaky'
Wi-Fi Preferences
    MAC Address          : %s (hw=%s)\n
    Tx Power [%i]         : %s\n
    |> %s (NSDictionary not followed)
_devices
Legacy Wi-Fi Security (WPA)
Pings the currently assigned router address for the Wi-Fi network service to determine LAN connectivity using IMFoundation
Wi-Fi has IPv4 assigned (router=%@ ip=%@)
Zeevo
_afhMap
_powerStateCaps
Detects if custom web proxy settings are configured for the Wi-Fi network service
_linkQualityUpdates
Could retrieve 'https://captive.apple.com'
NoAuthenticator
Gamepad
    Interface Name         : %s\n
Power Source Type: %@\n
Did not find conflicting security types
isCloudPaired %@\n
__W5ArchiveAddFileURLToArchive
    Type             : %s\n
11ac
Video Display
/Secondary
Audio
IBM
Tenovis
initiatingReason
      Top Master Metric    : %u\n
_minorClass
_proximity
%@ does not use WPA security (%@)
Apple
W5TaskUtil.m
_dnsAddresses
BSSID %@\n
Tablet
    Scanning             : %s\n
_cachedScanResults
_isSnifferSupported
_supportedSecurityTypes
Could not ping DNS server(s) (%ld)
Could %sping DNS server (%@ / %.2fms / %@ / %ld bytes / i=%fs / W=%fs / t=%fs / c=%ld)
CCA
2GHz[%i,%i] 5GHz[%i,%i] lvl %i
GCT Semi
/bin/sh
Peer=%@, 
Guard Interval: %ld\n
_isAppleReachable
    Sync Params            : n/a\n
: %s\n
_primaryIPv6InterfaceName
HT40 2.4GHz Networks
%@Max: %i\n
Data Display
%@_%@
/Library/Logs/CoreCapture/WiFi
W5ParamErr
AWDL Enabled
Detects if preferred networks list has 10 or more entries
? (0x%X)
Smartphone
_opMode
[traceroute]
11ax
_bluetooth
    Apple            : %s\n
WiFi: %@\n
_max
Bluetooth coexistence is active
BeaconInterval
? (%d)
DHCP
Determines if any hidden Wi-Fi networks are nearby
Bluetooth Status Changed
Wi-Fi Logs (Dump)
Stopping
Health
isConnected %@\n
Detected custom web proxy settings
No PNL networks have conflicting PHY modes (802.11n).
%@ is not an iOS PH
    IPv4 Router          : %s\n
    Sync Params\n
Address %@\n
\nLastHr Faults=>\n%@
_relativeURLs
%@%@
Video Camera
Joystick
Action Figure
Continental Auto
Timestamp=%@, 
    Address          : %s\n
Could %sping IP address (%@ / %.2fms / %@ / %ld bytes / i=%fs / W=%fs / t=%fs / c=%ld)
Found HT40 network(s) in 2.4GHz
Completed speed test (%ld Mbps)
%@Chain Ack: [
    Op Mode              : %s\n
    RSSI                 : %i dBm\n
Peers
Could ping IP address(es) (%ld)
VI
    IPv4 Address         : %s\n
isPaired %@\n
W5MiscUtil.m
WPA3 Personal
%i
    AirDrop Disc Mode      : %s\n
Channel Sequence: %@\n
_awdlSidecarDiagnostics
WiFi=>\n%@
Detects if any nearby Wi-Fi networks are 802.11n-only, and the local device does not support 802.11n
CurrentChannel
%@ does not use open security (%@)
Red M Comms
recoveryType
_wait
Detects if the IPv4 config method is not 'DHCP' for the Wi-Fi network service
For Internal Wi-Fi Settings
80 MHz
      Self Metric          : %u\n
_awdlSyncParameters
Power State: %@\n
_diagnosticsModes
BTC Profile 5 GHz: %s\n
_scanRecord
_model
NETWORK\n
  Extension Length      %d\n
Congested Wi-Fi Channel CCA
[%@] %@ / %@, 
Finished
Determines if any Wi-Fi networks are visible
Could %sping AWDL (%@ / %.2fms / %@ / %ld bytes / w=%fs / c=%ld)
Did not find any hidden networks
%@ uses WEP security
%@IsWWAN: %s
_majorClass
v20@?0@\"NSError\"8B16
ControlFlags=%lu, 
%@ 
Peer Diagnostics
HOSTAP
Headphones
    Primary IPv4         : None\n
EAPOL Mode: %@\n
.%u
%@, 
Name                                       Duration    Result    Timestamp           Description        \n
%@ is not using 802.11b
CATC
RV
    Master Channel         : %u/%u\n
IPv6ConfigMethod: %@\n
RemoteListener
Runs a progressive upload speed test
Current channel (%ld) is congested (CCA = %@)
%@ uses WPA security
CoreCapture (Pre)
Plantronics
    Fault                : %s\n
_isPaired
_btcProfiles2GHz
isMultiAP: %s\n
Congested Wi-Fi Channel
Wi-Fi Logs (24h)
Wi-Fi Device Config
Computer
Not Reachable
%@IsLocalAddress: %s\n
Cambridge
-[W5Client receivedPeerDiscoveryEvent:]_block_invoke
_address
_powerSourceType
IPv6 Addresses: %lu\n
_trafficClass
_nearby
.
  Election ID           %u\n
Retrieve Apple Over WiFi
_bssid
Pings DNS server(s) to determine WAN connectivity using CFNetwork
Detects if the current Wi-Fi network is an iOS Personal Hotspot
Determines if Wi-Fi is currently associated to a network
[ndp]
Crash/Spin (24h)
Bluetooth SIG
v24@?0@\"NSError\"8@\"NSURL\"16
Channel: %@\n
_primaryIPv6ServiceID
Detects if any nearby Wi-Fi networks are 802.11ac-only, and the local device does not support 802.11ac
Detects if the current Wi-Fi network is using Open security
Detects if the current Wi-Fi network is using WPA security
AWDL real time mode is not active
Leaky AP Stats
11g
Could not retrieve 'https://captive.apple.com'
WAPI (PSK)
Toshiba
Texas Instruments
/var/mobile/Library/Logs/CrashReporter/Retired
IPv6 Address: %@\n
eager-exit-debug
Runs traceroute with TTL=2 and looks at the output to determine if the current Wi-Fi connection is in a double NAT configuration
Unclassified
    BTC Profile 5GHz     : %s\n
    MAC Address            : %s (hw=%s)\n
v24@?0@\"NSError\"8@\"W5Peer\"16
/Library/Logs/CrashReporter/CoreCapture/WiFi
  AW Period             %d\n
Detects if the IPv6 config method is not 'Automatic' for the Wi-Fi network service
Wi-Fi is associated to '%@'
Widcomm
_desenseLevel
_beaconInterval
_output
Data
Did not detect custom web proxy settings
DNS-SD BrowseAll
Timestamp: %f\n
Min: %.2fms\n
Detects if the Wi-Fi network is hosted by an AirPort Base Station
Handsfree
Scale
This file was generated because the XPC call to collect WiFi diagnostics/logs was interrupted or invalidated (most likely jetsam'd). When we detect this condition, we will collect basic WiFi logs inline and try to capture the corresponding 
DISABLED
CCA: %ld\n
\t
Could not retrieve 'https://captive.apple.com' over Wi-Fi
Wi-Fi has IPv6 assigned (router=%@ ip=%@)
WPA Personal
Sync Params:\n%@
HomePod
IPv4 Assigned
Logoff
11a
    Power Source         : %s\n
Recoveries in last Hour: %lu\n
_airDropDiscoverableMode
_primaryIPv6Router
Controller
Did not find conflicting country code(s) (%@)
Watch
Monitoring
Default
Silicon Wave
UUID: %@\n
    Connected        : %s\n
User
__CRASH__
_ipv4Addresses
Custom IPv6
Acquired
non-election master [%02X:%02X:%02X:%02X:%02X:%02X]
Everyone
    Apple                : %s%s\n
 (WWAN)
    Connectable          : %s\n
_rssi
_timestamp
_primaryIPv4InterfaceName
Count: %ld\n
  Top Master            %02X:%02X:%02X:%02X:%02X:%02X\n
Uses NSURLSession to retrieve 'https://captive.apple.com' via HTTPS
Fault Detected
    Election Params\n
err
Upload Performance Test Updated
WPA Enterprise
Transilica
\nPower=>\n%@
SpeedTest (Upload)
Detects if bluetooth devices are paired
Load Webpage
Pings the currently assigned router address for the Wi-Fi network service to determine LAN connectivity
11n
Restricted
Phone
%@ConnectionRequired: %s\n
Started: %@\n
W5DebugConfiguration.m
Bluetooth coexistence is not active
Mbps
For AutoBugCapture
    IPv6 Router          : %s\n
    |> Age               : %02ld:%02ld:%02ld HH:MM:SS Ago\n
Name: %@ (%ld)\n
_testID
Scanning: %s\n
_peerID
Could not reach 'www.apple.com'
-[W5Client init]_block_invoke_2
_error
[%@] 
Unknown (%u)
Ping LAN (IMFoundation)
Sharing Logs
VCR
RXT Telecom
recoveryReason
      Max                : %i\n
+[NSTask(WiFiVelocity) runTaskWithLaunchPath:arguments:timeout:startBlock:updateBlock:endBlock:]_block_invoke_2
_awdl
_cca
_noLoggingWiFiProfile
PNL does not contain hidden networks
Manual
Microphone
W5SummaryRecoveries.m
LE: %s\n
_configuration
Supported
master [%02X:%02X:%02X:%02X:%02X:%02X]
FaultDetected
Uses NSURLSession (allowsCellularAccess==NO) to retrieve 'https://captive.apple.com' via HTTPS
Unsupported
Thermometer
ST Micro
    MCS Index            : %i\n
    Power                : %s\n
ENABLED
W5ResourceErr
_ipv6RouterAddress
Security: %@\n
_primaryIPv6Addresses
-
<%li>
Connecting
Keyboard
    SSID                 : %s\n
com.apple.wifivelocity.error
\nLastHr LinkTests=>\n%@
_supportsWEPCipher
_primaryIPv4ServiceName
_primaryIPv4Addresses
Ping Broadcast
2GHz 5GHz
    PHY Mode             : %s\n
Faults in last Hour: %lu\n
_build
Ping WAN (IMFoundation)
3Bars Cache
Recovery Type: %@\n
Faults
Discovery
W5SummaryFaults.m
PHY Mode: %@\n
_smartCCADesenseUSBPresence
Gather WiFi diagnostics from peer devices using Rapport framework over BLE
Router Advertisement
Camera
Game
IPv4 Router: %@\n
Resolve DNS
WiFiVelocity Log
Imaging
-[W5DiagnosticsModePeer initWithRole:peer:info:]
AppleTV
DiscoveryFlags=%lu, 
Did not find HT40 network(s) in 2.4GHz
IPv6ServiceID
[pmset]
Motorola
Type %@\n
i
_ipv6Addresses
Diagnostics Mode Peer role='%@ (%ld)' with peer='%@' info='%@'
Bandspeed
_didPass
_awdlSyncEnabled
PingResult
%@ is ambiguous
[security]
    |> Date              : %s\n
_isAWDLRealTimeMode
NetworkServiceID: %@\n
Primary IPv6: %@ (%@)\n
5GHzChannel
Runs a progressive download speed test
Wi-Fi Logs
20 MHz
Commil
W5Client.m
Detects if bluetooth devices are connected
Initiating Reason: %@\n
-[W5DiagnosticsMode initWithConfiguration:uuid:]
CoreCapture Collect
Loudspeaker
TZero
_ipv6ConfigMethod
Conflicting Wi-Fi Security
Detects if the beacon interval is not 100 ms
Wi-Fi is using '%@' for IPv4
BK_SYS
      Flags                : 0x%x\n
Could not curl 'https://captive.apple.com'
Per-SSID Diagnostics History
AC
INFORM
/var/mobile/Library/Logs/CrashReporter
Primary IPv4: %@ (%@)\n
fe80
Piggyback Scan + Data
BT Connected Count
Mitel
    System Caps          : %s\n
Wi-Fi Memory Usage
? (%i)
Toy
      Max SISO Resp Power       : [
v16@?0@\"NSTimer\"8
WiFi Peer Diagnostics
MONITOR
Rx
Laptop
Philips
Forced
Sniffer
Begins discovery of nearby devices belonging to same iCloud account and Friends & Family
Wi-Fi does not have IPv6 assigned
%@ (%@ / %@)
      BT RSSI Thresh / Hyst     : %i/%i\n
Timeout
AllowCachedSysdiagnose
_eventID
IPv6 Router: %@\n
_device
Could %sping router (%@ / %.2fms / %@ / %ld bytes / i=%fs / W=%fs t=%fs / c=%ld)
Video Conferencing
3DiJoy
OutputDirectory
Idle
Ambiguous Network Name
n/a
Visio
_ipv4RouterAddress
No Logging WiFi Profile: %@\n
_timeout
DeviceModel
Network Status
Hybrid (WLTX)
    Supports 6e          : %s\n
W5CreateTarball
_lastHrRecoveries
Airplay Audio
Combo
NO
Result: %@\n
_primaryIPv4Router
AV
    |> %s (NSArray not followed)
Sidecar Tx Latency: %ld ms\n
_isScanning
Domain Name: %@\n
_version
Ping LAN
Curl Apple
Mansella
BE
_lastHrLinkTests
Chain Ack: [%@]\n
%@ConnectionOnDemand: %s\n
%@Current: %i\n
Cellular
Robot
_primaryDNSAddresses
++
Congested Wi-Fi 2.4GHz Band
BEGIN Wi-Fi Default Route
For sysdiagnose
Wi-Fi Perf Logs
%@SISO Resp Enable: [
AWDL is %s\n
Name: %@\n
_startedAt
Hybrid
_isPersonalHotspot
5GHzNonDFSChannel
Unknown
Mouse
    BTC Profile 2.4GHz   : %s\n
Scan Cache Count: %lu\n
EndedAt: %@\n
Detects if the current Wi-Fi network is using WEP security
Determines if Wi-Fi is the primary IPv4 network service
DTIM interval is %ldms
%ld PNL networks have conflicting PHY modes (802.11n).
Link Quality Updates: %lu\n
BK
                           : %s\n
      AW Length            : %d\n
-[W5SummaryRecoveries initWithSummaryRecoveries:]
_eapolSupplicantState
_isDiscoverable
Timestamp    Name                          Duration    Result    Description                            \n
CTechnologies
-[W5SummaryLinkTests initWithSummaryLinkTests:]
Contacts Only
Detects if any nearby Wi-Fi networks use a country code that differs from the currently adopted country code
      WiFi RSSI Thresh / Hyst   : %i/%i\n
IOPlatformSerialNumber
Ping LAN (CFNetwork)
numberOfTVOSDevices
[wifivelocity] W5ActivityManager debugTimer already setup
[wifivelocity] W5ActivityManager configuring _periodicActiveListTimer
[wifivelocity] W5ActivityManager osTransactionComplete %s
[wifivelocity] %s (%s:%u) generating UUID='%{public}@' for configuration='%{public}@'
[wifivelocity] %s (%s:%u) NSTask exception for %{public}@, exception=%{public}@
[wifivelocity] FAILED to complete operation within %{public}.1fs, continuing
[wifivelocity] %s (%s:%u) Archiving '%{public}@' (size=%lld) --> '%{public}@'
[wifivelocity] W5ActivityManager empty, configuring eager exit timer in %f seconds
[wifivelocity] %s (%s:%u) <%{public}@> FAILED to create file handle for error path '%{public}@'
[wifivelocity] Bytes written does not equal file size (file='%{public}s', size=%{public}lld, written=%{public}zd)
[wifivelocity] Failed to start monitoring events %{public}@, returned error %{public}@
[wifivelocity] %s (%s:%u) received peer discovery event='%{public}@'
[wifivelocity] W5ActivityManager osTransactionCreate %s, active count is now %lu, total started is now %lu
[wifivelocity] CLEANUP obsolete busy fallback WiFi log content (delay=%ds, path='%{public}@')
[wifivelocity] '%{public}s' not allowed on non-internal install variants, will not run task
[wifivelocity] '%{public}s' does not exist, will not run task
[wifivelocity] %s (%s:%u) <%{public}@> START (error=%{public}@) - '%{public}@ %{public}@'
[wifivelocity] %s (%s:%u) Failed to open pseduo-terminal for stdout, returned error %d
[wifivelocity] %s (%s:%u) Adding contents of directory '%{public}@' (size=%lld) to archive...
[wifivelocity] %s (%s:%u) Adding file '%{public}@' (size=%lld) to archive
[wifivelocity] CLEANUP obsolete jetsam fallback WiFi log content (delay=%ds, path='%{public}@')
[wifivelocity] %s (%s:%u) FAILED to add directory archive entry '%{public}@', returned error %ld
[wifivelocity] W5ActivityManager osTransactionCreate, timer was running, invalidating and freeing
[wifivelocity] W5ActivityManager Completed %lu transactions within uptime of %f seconds
[wifivelocity] %s (%s:%u) FAILED to get contents at URL '%{public}@', returned error %ld
[wifivelocity] archive_write_header() FAILED for %{public}s, returned %{public}d (%{public}s)
[wifivelocity] %s (%s:%u) %s: init error!
[wifivelocity] %s (%s:%u) [NSKeyedUnarchiver unarchivedObjectOfClasses:fromData:error:] failed with error (%{public}@)
[wifivelocity] W5ActivityManager init error!
[wifivelocity] W5ActivityManager Cannot eager exit, still outstanding transactions
[wifivelocity] %s - Peer version: %@ - Fetch type forced to Dictionary
[wifivelocity] W5ActivityManager osTransactionComplete %s, TRANSACTION NOT FOUND, active count is now %lu
[wifivelocity] %s (%s:%u) Failed to open pseduo-terminal for stderr, returned error %d
[wifivelocity] %s (%s:%u) <%{public}@> END%{public}@ - '%{public}@ %{public}@'
[wifivelocity] Unexpected zero-length file encountered for %{public}s
[wifivelocity] %s (%s:%u) WiFi log collection requested (proc=%{public}@[%d], uuid=%{public}@)
[wifivelocity] %s (%s:%u) [NSFileHandle writeData:] failed with exception %{public}@
[wifivelocity] W5ActivityManager Attempting Daemon Eager Exit due to inactivity timeout of %f seconds
[wifivelocity] %s (%s:%u) <%{public}@> START%{public}@ - '%{public}@ %{public}@'
[wifivelocity] %s (%s:%u) FAILED to create archive '%{public}@', returned error %ld
[wifivelocity] %s (%s:%u) [NSKeyedArchiver archivedDataWithRootObject:requiringSecureCoding:error:] failed with error (%{public}@)
[wifivelocity] %s (%s:%u) XPC connection interrupted
[wifivelocity] %s (%s:%u) <%{public}@> FAILED to create file handle for output path '%{public}@'
[wifivelocity] %s (%s:%u) Successfuly archived '%{public}@' --> '%{public}@'
[wifivelocity] %s (%s:%u) FAILED to add file archive entry '%{public}@', returned error %ld
[wifivelocity] W5ActivityManager activeTransactions %lu
[wifivelocity] W5ActivityManager activeTransaction %s
[wifivelocity] W5ActivityManager empty, extending running eager exit timer to %f seconds
[wifivelocity] W5ActivityManager empty, eager exit timer disabled via defaults write
[wifivelocity] %s (%s:%u) %s: peer='%@' not found in peers list='%@'
[wifivelocity] %s (%s:%u) XPC connection invalidated
[wifivelocity] PURGE obsolete WiFi log content, path='%{public}@'
[wifivelocity] FAILED to copy WiFi log item to final destination '%{public}@' --> '%{public}@', returned error [%{public}@]
[wifivelocity] %s (%s:%u) init error!
[wifivelocity] W5ActivityManager osTransactionComplete TRANSACTION NOT FOUND ASSERT
[wifivelocity] %s (%s:%u) peers is nil for configuration='%{public}@'
[wifivelocity] FAILED to copy WiFi logs to final destination '%{public}@' --> '%{public}@', returned error [%{public}@]
```
