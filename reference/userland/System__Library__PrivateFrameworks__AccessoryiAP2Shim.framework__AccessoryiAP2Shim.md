# `/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (11)

- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport`
- `/System/Library/PrivateFrameworks/IAP.framework/IAP`
- `/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`
- `/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`
- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 5 classes, 0 protocols, 145 methods, 49 properties

### Class pages

Every class and protocol, with its methods: [`ACCUserDefaults`](../objc/ACCUserDefaults_AccessoryiAP2Shim.md), [`ACCiAP2ShimAccessory`](../objc/ACCiAP2ShimAccessory_AccessoryiAP2Shim.md), [`ACCiAP2ShimServer`](../objc/ACCiAP2ShimServer_AccessoryiAP2Shim.md), [`ACCiAP2ShimServerClient`](../objc/ACCiAP2ShimServerClient_AccessoryiAP2Shim.md), [`ACCiAP2ShimServerUnregisteredClient`](../objc/ACCiAP2ShimServerUnregisteredClient_AccessoryiAP2Shim.md)

### Classes

`ACCUserDefaults`, `ACCiAP2ShimAccessory`, `ACCiAP2ShimServer`, `ACCiAP2ShimServerClient`, `ACCiAP2ShimServerUnregisteredClient`

### Properties

```
@property (T@"NSString",R,V_keyTag) keyTag;
@property (T@"NSString",R,V_keyAccessoryUID) keyAccessoryUID;
@property (T@"NSString",R,V_keyConnectionID) keyConnectionID;
@property (TI,V_connectionID) connectionID;
@property (TI,R,V_featureTypeMask) featureTypeMask;
@property (T@"NSString",R,V_accessoryUID) accessoryUID;
@property (T@"NSString",&,V_name) name;
@property (T@"NSString",&,V_model) model;
@property (T@"NSString",&,V_manufacturer) manufacturer;
@property (T@"NSString",&,V_serialNumber) serialNumber;
@property (T@"NSString",&,V_firmwareVersion) firmwareVersion;
@property (T@"NSString",&,V_hardwareVersion) hardwareVersion;
@property (T@,&,V_context) context;
@property (TB,V_dontPublish) dontPublish;
@property (T@"NSMutableDictionary",&,N,V_delegateList) delegateList;
@property (T@"NSMutableDictionary",&,N,V_accessoryViaKeyUIDList) accessoryViaKeyUIDList;
@property (T@"NSMutableDictionary",&,N,V_accessoryViaConnectionIDList) accessoryViaConnectionIDList;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_listQueue) listQueue;
@property (T@"NSObject<OS_xpc_object>",R,N,V_listener) listener;
@property (TB,R,N,V_isShuttingDown) isShuttingDown;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_iap2dhighPriorityRootQueue) iap2dhighPriorityRootQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_internalListenerQueue) internalListenerQueue;
@property (T{__serverFlags=b1b1b30},R,V_serverFlags) serverFlags;
@property (T@"NSMutableDictionary",R,V_clients) clients;
@property (T@"NSLock",R,V_clientLock) clientLock;
@property (Ti,R,V_iap2AvailableNotifyToken) iap2AvailableNotifyToken;
@property (TB,R,N,V_entitlementForAllAccessories) entitlementForAllAccessories;
@property (T@"NSArray",R,N,V_clientEAProtocols) clientEAProtocols;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_processAssertionQ) processAssertionQ;
@property (T^{SBSProcessAssertion=},R,N,V_processAssertion) processAssertion;
@property (Tq,R,N,V_processAssertionStartTime) processAssertionStartTime;
@property (T@"NSObject<OS_dispatch_source>",R,N,V_processAssertionTimer) processAssertionTimer;
@property (Ti,R,N,V_iapSessionRefCount) iapSessionRefCount;
@property (TI,N,V_applicationState) applicationState;
@property (TI,N,V_clientID) clientID;
@property (Ti,R,N,V_processId) processId;
@property (T@"NSObject<OS_xpc_object>",R,N,V_xpcConnection) xpcConnection;
@property (T@"NSString",R,N,V_bundleId) bundleId;
@property (T{?=[8I]},R,N,V_auditToken) auditToken;
@property (TI,R,N,V_capabilities) capabilities;
@property (TB,N,V_locationSupportedByClient) locationSupportedByClient;
@property (TB,N,V_cameraSupportedByClient) cameraSupportedByClient;
@property (TB,R,N,V_supportsAccessibility) supportsAccessibility;
@property (TB,N,V_clientRequiresAccReset) clientRequiresAccReset;
@property (TB,N,V_interestedInBLENotifications) interestedInBLENotifications;
@property (T^{SBSProcessAssertion=},R,N,V_processAssertion) processAssertion;
@property (Tq,R,N,V_processAssertionStartTime) processAssertionStartTime;
@property (T@"NSString",R,N,V_bundleId) bundleId;
@property (Ti,R,N,V_processId) processId;
```

## Strings (341)

```
com.apple.CoreAccessories
DeviceIdentityPreArmDateOverride
EnableManager2ForTransport
TEST_MANUFACTURER
IAPEAClient Process Assertion Queue
B32@?0@8Q16^B24
ShowHiddenAccessories
EnableChinaInductiveTx
MFi4RelayReadRetryDelayMs
PretendNoDeviceIdentityCerts
ProductType
external-accessory.connect
A1717
A1585
PreArmDeviceIdentityDate
BLEPairingDontEarlyInfoAsDeviceUID
DisableACCAuthProtocolOnInductive
WaitForiAPTrafficDelayMS
MaxOutboundiAP2PacketSize
RegionCode
A1605
NO
HARMAN
Jaguar I-PACE
DisableInductiveAuthTTR
ChargingPowerBehavior
IAPAppAccessoryUIDKey
IdentityCertRefreshInterval
InductiveAuthPretendMatchRxID
UARPActivityTimerS
MPPAuthGetLeafCertFirst
MPPAuthChallengeFirst
---
MIB2
DisableMFi4CertSupport
ForceAccInfoUpdateRelaySupport
PretendAccessoryType
IAP2ServerListenerQueue
DidPreArmDeviceIdentity
PretendWirelessCTAMatch
ACCAuthProtocolAllowMutualAuth
DontSkipInductiveAuthOnCTA
SysdiagnoseOnInductiveCTAFailure
%d
IntelliLink
i
iPL24Z
com.apple.private.externalaccessory.showallaccessories
IgnorePowerSourceUpdateForAvailableCurrent
Disable1WayNFCForInductive
com.apple.iapd.PreferencesDidChangeNotification
Use +[%@ %@] instead of -%@.
A1468
AM002
A2070
SDI Technologies
ForceAuthTimeout
SysdiagnoseInsteadOfAuthTTR
IgnoreIsOnAC
LiveVoicemailFakeRinging
A1505
X533c
P218a
1.0
DisableAuthTimeoutTTRForXR
OverrideCanReceiveInductivePowerOID
SkipGaugeSignatureCheck
ACCAuthProtocolRoleSupport
A2121
com.apple.logging
EnableTrustDialog
PowerSourceUpdateBehavior
DisablePowerUpdateForCurrentDraw
ForceT56RelaySupport
MFi4SigmaIRequired
MFi4ECDSADisallow
modelMatch
Range Rover Velar
com.apple.iapd.accessibility
ForceAuthFail
NFCAnalyticsDate
PacketLoggingPlainTextOnly
PretendBatteryLevel
PearlIDCapability
NFCSecondaryColorOverride
DisableAACPAuth
IAPAppBTPairingIsSupportedKey
TEST_MODEL
%@-%@
v8@?0
A1602
manufacturerMatch
NFCColorOverride
MFi4AuthTimeoutValueS
0.0.0
-[ACCiAP2ShimServer sendToClient:notification:withPayload:]
)
X90
modelContain
AuthTTRForAllTransports
EnableAuthTimeoutTTR
DisableCertSupport
BLEPairingConfigRequestDelayMs
PretendNFCAuthFailed
Beta
A2071
com.apple.accessoryd
DisableAuthFailureTTRForXR
PretendNFCAuthTimeout
IgnoreAccInfoUpdateRelaySupport
USBHiAPEnable
TEST_SER_NUM
<Undefined>
General
X533b
iPhone13,4
KnownAccessories
ACCAuthProtocolPretendAuth
MPPAuthPreferredSlot
EnableWrongOrientationMessage
LAM2
DisableSNOnly
DisableIAPHVCFixForAuth
ForceMFi4AuthOverNFC
TransportSignpost
external-accessory.disconnect
KeepAACPAuthData
UseCertDataPropertyForAuth
IdentityCertRefreshState
BLEPairingDisableOOBPPlusFlow
OverrideMPPAuthSupported
<ACCiAP2ShimAccessory>[_connectionID=%u _accessoryUID=%@ _keyTag=%@ _featureTypeMask=%xh _dontPublish=%d _name='%@']
v24@?0@\"ACCiAP2ShimAccessory\"8^B16
A1765
DisableWirelessCTA
TestCreateBLEPairingOnInductive
IgnoreAuthReset
ReleaseType
A1450
overrideCurrentLimit
iPhone13,1
com.apple.iap2d.xpc
AM003
A2184
Land Rover
TreatAuthCPDEVNAsV3
EnableDEVNCertSupport
BLEPairingAuthTimeoutValueS
MFi4ECDSAOnly
AuthenticationOverride
A2183
v32@?0@8@16^B24
com.apple.iapd
DisableAMSHookUp
IdentityCertUseIndex
AudioAccessory
+[ACCiAP2ShimServer notifyInterestedClientsOfACCBLEAccessoryEvent:withPayload:]
MPPAuthEnablePretendAuth
wapi
<nil>
+[ACCiAP2ShimServer markClientAsInterestedInBleNotifications:]
com.apple.accessories.signposts
nameContain
BypassTrustDialog
IdentityCertUseTime
IdentityCertIsClassD
TEST_NAME
+
-[ACCiAP2ShimServer sendToInterestedClientsACCBLENotification:withPayload:]
Connection
AM001
A2180
IgnoreAACPAuthStatus
AllowMFi4DevCertsOnProdDevice
PretendNoNFCResponse
RejectionOfMultipleLocation
GenericMFiIgnoreCertCaps
D!
EnableACCAuthProtocolOnNFC
DisableNFCAuthTimer
com.apple.CoreAccessories.PreferencesDidChangeNotification
%@-%u
InternalBuild
DeviceClass
v16@?0@\"NSObject<OS_xpc_object>\"8
nameMatch
MyLink
Jaguar
AuthCPStartDelayMs
DisableT56Support
X533
A1523
iPhone13,2
AllowNFCColorOverride
DisableCertVerification
ChargingPowerOverride
com.apple.acciap2shimserver.listQ
v24@?0@\"NSObject<ACCiAP2ShimServerDelegate>\"8^B16
Endpoint
<ACCiAP2ShimServerClient>[clientID=%u bundId=%@ capabilities=%xh supported: location=%d camera=%d accessibility=%d, requiredAccReset=%d]
ProductVersion
BLEPairingIgnoreZeroEarlyInfo
ACCAuthProtocolMaxMessageSize
com.apple.accessories.frameworks
manufacturerContain
EnableIndonesiaInductiveTx
PlatformIDOverride
AllowACCAuthProtocolOnAllTransport
SkipNFCAuth
Transport
A1520
YES
iPhone13,3
shouldOverrideName: %s
[#Server] ERROR: Client sent kXPCIAPCheckInStr xpc message without a reply context
Created log object %s: %s
Failed to create os_log_t object %s: %s!
[#ServerClient] protocol %@ found from accessory
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
[#Server] IAPServer: stopServer, _delegateList count %lu
[#Server] ACCiAP2ShimServer addAccessory %@, after add _accessoryViaKeyUIDList=%@
[#Server] ACCiAP2ShimServer _attachAccessory: should be hiding accessory from settings
[#Server] ERROR - already have client for clientID 0x%08x
[#ServerClient] renewing process assertion - appId=%@ pid=%d
[#Server] IAPServer: init: failed to register notify token!
[#Server] ACCiAP2ShimServer before addDelegate %@, delegateList=%@
[#Server] processXPCMessage: %@ connection: %@, requestType=%s, delegate does not response to selector , delegate=%@
[#Server] removeClientWithID: clientID=%u _clients=%@
acc_policies_deviceNeedsPreArmDeviceIdentity: _parseDate: %@
[#Server] processXPCMessage: %@ connection: %@, requestType=%s, try delegate %@
[#Server] %s: Received nil param. notificationName %@ notificationPayload %@
[#Server] IAPServer: resetServerState: invalid notifyToken!
[#Server] IAPAppConnectedAccessories connectedAccessories=%@
[#Server] IAPCheckIn\n
RequiresChargingCurrentLimit: isApple=%d deviceType=%d checkChargingCurrentLimit=%d chargingCurrentLimit=%d inLimit=%d behavior=%d batteryThreshold=%d
RequiresChargingCurrentLimit: isApple=%d deviceType=%d chargingCurrentLimit=%d inLimit=%d battery=%d threshold=%d
[#Server] IAPServer: stopServer: invalid notifyToken!
[#Server] ACCiAP2ShimServer after addDelegate %@, delegateList=%@
[#Server] ACCiAP2ShimServer _detachAccessory: %@, dontPublish set! connectionID=%d
[#Server] removeClientForXPCConnection: clientConnection=%@ _clients=%@
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
acc_policies_deviceNeedsPreArmDeviceIdentity: override
[#ServerClient] bundleID %@ supportsEAWhenSuspended = %d, supportsEAInBackground = %d, clientAppStateInBackground = %d, clientAppStateInForeground = %d, clientLinksUIApplication = %d, _entitlementForAllAccessories = %d, anyProtocolFound = %
[#Server] ACCiAP2ShimServer _attachAccessory: AccName=%@, AccManufacturer=%@, AccModel=%@, AccSerialNumber=%@, AccFWVersion=%@, AccHWVersion=%@, AccDockType=%@
[#ServerClient] INIT - capability=0x%x
[#Server] addClientWithCapabilities: notifying of connected accessories, client=%@
[#Server] ERROR - couldn't find client for xpc client %@
[#Server] IAPAppConnectedAccessories
[#Server] clientToNotify bundle = %@, request = %s, notificationName = %s, notificationPayload=%@
[#Server] %s: Received nil param. xpc_connection %@
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
[#Server] IAPAppRegisterClient %@ call addClientWithCapabilites:%xh notifyClientOfAlreadyConnectedAccessories:%d
[#Server] ACCiAP2ShimServer removeAccessory %@
[#Server] ACCiAP2ShimServer _detachAccessory: %@, accessoryDict=%@
[#Server] addClientWithCapabilities: skip notifying of connected accessories, client=%@
[#Server] findClientWithID: xpcConnection=%@ _clients=%@
[#Server] post distributed notification %@, userInfo %@
[#Server] IAPAppRegisterClient %@
[#ServerClient] using ea process hysteresis
[#Server] IAPServer: startServer: set_event_handler and resume _listener
[#Server] ACCiAP2ShimServer before removeDelegate %@, delegateList=%@
[#Server] ACCiAP2ShimServer _detachAccessory: accessory with connectionID=%d detached
[#Server] xpc_connection object interested in BLE notifications matches the one for clientID = %u, bundleID = %@
[#Server] _xpc_iap2d_handle_incoming_request event error: %s\n
[#ServerClient] Unable to create security task from audit token.
[#Server] IAPServer: startServer: post kIAP2AvailableNotification notification: 
[#Server] processXPCMessage: %@ connection: %@, None of the delegates processed the message! requestType=%s
[#Server] removeClientWithID: client=%@
[#Server] IAPServer: resetServerState: cancel notify token
[#Server] ACCiAP2ShimServer iterateDelegates, _delegateList=%@
[#Server] ACCiAP2ShimServer iterateAccessories, accessory=%@
[#Server] IAPAppConnectedAccessories call [sharediAP2Server(%@) iterateAccessoriesSync:]
acc_internalSettings: internal-only setting %{public}@ active (%ld)
[#Server] IAPServer: startServer: set kIAP2AvailableNotification state: %d
[#Server] addClientWithCapabilities: client=%@
[#Server] ERROR - couldn't find client for clientID 0x%08x
[#Server] client %@\n
[#Server] ERROR: Client sent kXPCIAPAppConnectedAccessoriesStr xpc message without a reply context
[#Server] IAPServer: startServer: init listener queue and start runloop
[#Server] RequestType not specified in xpc message!
[#Server] _xpc_iap2d_handle_incoming_request unexpected event: %s\n
[#ServerClient] %@ supports EA while suspended = %s
[#Server] IAPServer: stopServer: set kIAP2AvailableNotification state: %d
[#Server] ACCiAP2ShimServer _attachAccessory: %@, dontPublish set! accessoryDict=%@
[#Server] addClientWithCapabilities: notify connected: client=%@ accessory=%@ accessoryInfoDict=%@
[#Server] IAPAppConnectedAccessories iterateAccessoriesSync, accessory=%@, dontPublish=%d, skip adding!
[#Server] ERROR - unable to convert accessories array to plist: %@
shouldHideAccessory: %s, showHiddenAccessories: %s
[#ServerClient] No protocols found for client %@
[#Server] ACCiAP2ShimServer iterateDelegates, no registered delegate! _delegateList=%@
[#Server] post darwin notification %@
[#Server] IAPAppConnectedAccessories iterateAccessoriesSync, accessory=%@, accessoryInfo=%@
[#Server] OwnsConnectionID: connectionID = %u\n
acc_policies_deviceNeedsPreArmDeviceIdentity: _parseDate
[#ServerClient] _entitlementForAllAccessories = %d
[#Server] IAPServer: resetServerState: post kIAP2AvailableNotification notification: 
[#Server] Client sent '%s' xpc message without a reply context
[#Server] IAPServer: startServer: invalid notifyToken!
[#Server] IAPServer: startServer: isIap2dLoaded=%llu
[#Server] IAPServer: resetServerState: kIAP2AvailableNotification state %llu, skip post
[#Server] Client sent unknown '%s' xpc message 
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
RequiresChargingCurrentLimit: isApple=%d, deviceType=%d, batt=%d(%d), %d->%d, return %d
[#ServerClient] Unable to get entitlement '%@', error: %@
[#Server] ACCiAP2ShimServer addAccessory %@
[#Server] ACCiAP2ShimServer removeAccessory %@, after remove _accessoryViaKeyUIDList=%@
[#Server] ACCiAP2ShimServer _attachAccessory %@
[#Server] addClientWithCapabilities:%u auditToken:%xh currentClienID:%u xpcConnection:%@ eaProtocols:%@ notifyOfAlreadyConnectedAccessories:%d andBundleId:%@
[#Server] %s: Received nil param. clientToNotify %@ notificationName %s notificationPayload %@
[#Server] IAPServer: stopServer
[#Server] ACCiAP2ShimServer after removeDelegate %@, delegateList=%@
[#Server] addClientWithCapabilities: _clients=%@
[#Server] interested client does not have entitlement! not marking as interested for BLE notifications. clientID = %u, bundleID = %@
[#Server] _xpc_iap2d_handle_incoming_request connection error: %s\n
[#Server] findClientWithID: client=%@
[#Server] Found client to remove, client bundleID is %@
[#Server] _xpc_iap2d_handle_incoming_request: received messagetype %s
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#ServerClient] creating process assertion - appId=%@ pid=%d
[#Server] ACCiAP2ShimServer iterateAccessories, _accessoryViaKeyUIDList=%@
[#Server] clientToNotify bundle = %@, request = %s, canSendConnectionEvent = %d, accessory=%@
Created %d log object(s)!
[#Server] IAPServer: startServer: Already loaded!
[#ServerClient] DEALLOC - clientID=%d
[#Server] client has required entitlement. marking as interested for BLE notifications. clientID = %u, bundleID = %@
[#Server] IAPAppRegisterClient %@ send back reply, clientID=%u
[#ServerClient] %@ supports EA while backgrounded = %s
[#ServerClient] releasing process assertion - clientID=%d pid=%d
[#Server] IAPServer: stopServer: post kIAP2AvailableNotification notification: 
[#Server] IAPServer: Skip stopServer, there are still %lu delegates registered
[#Server] addClientWithCapabilities: add to _clients, client=%@
[#Server] findClientWithID: clientID=%u _clients=%@
acc_internalSettings: internal-only setting %{public}@ active
[#ServerClient] %@ supports Application state = %s
[#Server] IAPServer: startServer: _listener is not valid!\n
[#Server] %s: iterating clients to find matching xpc_connection object
[#Server] ERROR: Client sent kXPCOwnsConnectionIDStr xpc message without a reply context
[#Server] IAPServer: stopServer: kIAP2AvailableNotification state %llu, skip post
[#Server] ERROR: Client sent kXPCIAPAppRegisterClientStr xpc message without a reply context
[#ServerClient] has %@ entitlement:%d
[#Server] IAPServer: resetServerState: set kIAP2AvailableNotification state: %d
```
