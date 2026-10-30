# `/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 8 classes, 8 protocols, 301 methods, 80 properties

### Class pages

Every class and protocol, with its methods: [`ACCPlatformIOKitPowerPluginProtocol`](../objc/ACCPlatformIOKitPowerPluginProtocol_IOKit.protocol.md), [`ACCPlatformPluginIOKit`](../objc/ACCPlatformPluginIOKit_IOKit.md), [`ACCPlatformPluginProtocol`](../objc/ACCPlatformPluginProtocol_IOKit.protocol.md), [`ACCPlatformSleepAssertionPluginProtocol`](../objc/ACCPlatformSleepAssertionPluginProtocol_IOKit.protocol.md), [`ACCPlatformUSBCableTypePluginProtocol`](../objc/ACCPlatformUSBCableTypePluginProtocol_IOKit.protocol.md), [`ACCPlatformUSBCameraKitHubPluginProtocol`](../objc/ACCPlatformUSBCameraKitHubPluginProtocol_IOKit.protocol.md), [`ACCPlatformUSBFaultPluginProtocol`](../objc/ACCPlatformUSBFaultPluginProtocol_IOKit.protocol.md), [`ACCPluginProtocol`](../objc/ACCPluginProtocol_IOKit.protocol.md), [`ACCUserDefaults`](../objc/ACCUserDefaults_IOKit.md), [`IAPUIDManager`](../objc/IAPUIDManager_IOKit.md), [`NSObject`](../objc/NSObject_IOKit.protocol.md), [`PowerMonitor`](../objc/PowerMonitor_IOKit.md), [`SleepAssertionManager`](../objc/SleepAssertionManager_IOKit.md), [`USBCableTypeMonitor`](../objc/USBCableTypeMonitor_IOKit.md), [`USBCameraKitHubMonitor`](../objc/USBCameraKitHubMonitor_IOKit.md), [`USBFaultMonitor`](../objc/USBFaultMonitor_IOKit.md)

### Classes

`ACCPlatformPluginIOKit`, `ACCUserDefaults`, `IAPUIDManager`, `PowerMonitor`, `SleepAssertionManager`, `USBCableTypeMonitor`, `USBCameraKitHubMonitor`, `USBFaultMonitor`

### Protocols

`ACCPlatformIOKitPowerPluginProtocol`, `ACCPlatformPluginProtocol`, `ACCPlatformSleepAssertionPluginProtocol`, `ACCPlatformUSBCableTypePluginProtocol`, `ACCPlatformUSBCameraKitHubPluginProtocol`, `ACCPlatformUSBFaultPluginProtocol`, `ACCPluginProtocol`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) pluginName;
@property (TB,R,N) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,V_isRunning) isRunning;
@property (T@"USBFaultMonitor",&,N,V_monitor) monitor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_systemPowerQueue) systemPowerQueue;
@property (TI,N,V_systemPowerPort) systemPowerPort;
@property (T^{IONotificationPort=},N,V_systemPowerNotifyPortRef) systemPowerNotifyPortRef;
@property (TI,N,V_systemPowerIterator) systemPowerIterator;
@property (TB,N,V_sleepNotificationsEnabled) sleepNotificationsEnabled;
@property (T@"NSMutableArray",&,N,V_sleepNotificationClients) sleepNotificationClients;
@property (T@"NSMutableArray",&,N,V_clientsPreventingSleep) clientsPreventingSleep;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_sleepSemaphore) sleepSemaphore;
@property (TB,N,V_systemIsAsleep) systemIsAsleep;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_clientsPreventingSleepLock) clientsPreventingSleepLock;
@property (TB,N,V_isExtChargerConnected) isExtChargerConnected;
@property (Ti,N,V_batteryCapacity) batteryCapacity;
@property (Ti,N,V_batteryCapacityOverride) batteryCapacityOverride;
@property (Ti,N,V_batteryCapacityMax) batteryCapacityMax;
@property (TB,N,V_isBatteryCharging) isBatteryCharging;
@property (TC,N,V_batteryChargeLevelPercent) batteryChargeLevelPercent;
@property (T^{IONotificationPort=},N,V_batteryNotifyPortRef) batteryNotifyPortRef;
@property (TI,N,V_battery_iter) battery_iter;
@property (T@"NSMutableArray",&,N,V_batteryNotificationClients) batteryNotificationClients;
@property (T@"NSLock",&,N,V_batteryNotificationClientsLock) batteryNotificationClientsLock;
@property (Ti,N,V_batteryChargingType) batteryChargingType;
@property (Ti,N,V_batteryChargingTypeExternal) batteryChargingTypeExternal;
@property (T@"NSMutableDictionary",&,N,V_assertions) assertions;
@property (TB,N,V_sleepAssertionHeld) sleepAssertionHeld;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_sleepAssertionsLock) sleepAssertionsLock;
@property (TB,N,V_eaSleepAssertionHeld) eaSleepAssertionHeld;
@property (TI,N,V_eaSleepAssertionID) eaSleepAssertionID;
@property (TB,N,V_applePencilSleepAssertionHeld) applePencilSleepAssertionHeld;
@property (TI,N,V_applePencilSleepAssertionID) applePencilSleepAssertionID;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_applePencilSleepAssertionTimer) applePencilSleepAssertionTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_applePencilSleepAssertionTimerQueue) applePencilSleepAssertionTimerQueue;
@property (TB,N,V_mfi4SleepAssertionHeld) mfi4SleepAssertionHeld;
@property (TI,N,V_mfi4SleepAssertionID) mfi4SleepAssertionID;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_mfi4SleepAssertionTimer) mfi4SleepAssertionTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_mfi4SleepAssertionTimerQueue) mfi4SleepAssertionTimerQueue;
@property (T^{IONotificationPort=},V_ioUSB20CameraKitHubNotifyPort) ioUSB20CameraKitHubNotifyPort;
@property (TI,V_ioUSB20CameraKitHubNotification) ioUSB20CameraKitHubNotification;
@property (TI,V_ioUSB20CameraKitHubService) ioUSB20CameraKitHubService;
@property (TI,V_ioUSB20CameraKitHubMatchIterator) ioUSB20CameraKitHubMatchIterator;
@property (TI,V_ioUSB20CameraKitHubTerminateIterator) ioUSB20CameraKitHubTerminateIterator;
@property (TI,V_ioUSB20CameraKitHubCurrentNeeded) ioUSB20CameraKitHubCurrentNeeded;
@property (TI,V_ioUSB20CameraKitHubPortCurrentAllocation) ioUSB20CameraKitHubPortCurrentAllocation;
@property (TI,V_ioUSB20CameraKitHubPortFailedRequestedPower) ioUSB20CameraKitHubPortFailedRequestedPower;
@property (TI,V_ioUSB20CameraKitHubExtraRequestedPower) ioUSB20CameraKitHubExtraRequestedPower;
@property (T^{IONotificationPort=},V_ioUSB20CameraKitHubPortNotifyPort) ioUSB20CameraKitHubPortNotifyPort;
@property (TI,V_ioUSB20CameraKitHubPortNotification) ioUSB20CameraKitHubPortNotification;
@property (TI,V_ioUSB20CameraKitHubPortService) ioUSB20CameraKitHubPortService;
@property (TI,V_ioUSB20CameraKitHubPortMatchIterator) ioUSB20CameraKitHubPortMatchIterator;
@property (TI,V_ioUSB20CameraKitHubPortTerminateIterator) ioUSB20CameraKitHubPortTerminateIterator;
@property (T^{IONotificationPort=},V_ioUSB30CameraKitHubNotifyPort) ioUSB30CameraKitHubNotifyPort;
@property (TI,V_ioUSB30CameraKitHubNotification) ioUSB30CameraKitHubNotification;
@property (TI,V_ioUSB30CameraKitHubService) ioUSB30CameraKitHubService;
@property (TI,V_ioUSB30CameraKitHubMatchIterator) ioUSB30CameraKitHubMatchIterator;
@property (TI,V_ioUSB30CameraKitHubTerminateIterator) ioUSB30CameraKitHubTerminateIterator;
@property (TI,V_ioUSB30CameraKitHubCurrentNeeded) ioUSB30CameraKitHubCurrentNeeded;
@property (TI,V_ioUSB30CameraKitHubPortCurrentAllocation) ioUSB30CameraKitHubPortCurrentAllocation;
@property (TI,V_ioUSB30CameraKitHubPortFailedRequestedPower) ioUSB30CameraKitHubPortFailedRequestedPower;
@property (T^{IONotificationPort=},V_ioUSB30CameraKitHubPortNotifyPort) ioUSB30CameraKitHubPortNotifyPort;
@property (TI,V_ioUSB30CameraKitHubPortNotification) ioUSB30CameraKitHubPortNotification;
@property (TI,V_ioUSB30CameraKitHubPortService) ioUSB30CameraKitHubPortService;
@property (TI,V_ioUSB30CameraKitHubPortMatchIterator) ioUSB30CameraKitHubPortMatchIterator;
@property (TI,V_ioUSB30CameraKitHubPortTerminateIterator) ioUSB30CameraKitHubPortTerminateIterator;
@property (TI,V_ioUSBCameraKitHubTotalCurrent) ioUSBCameraKitHubTotalCurrent;
@property (TB,V_ioUSBCameraKitHubCurrentNeedUpdate) ioUSBCameraKitHubCurrentNeedUpdate;
@property (TB,V_ioUSBCameraKitHubOverCurrentDetected) ioUSBCameraKitHubOverCurrentDetected;
@property (Tq,V_once) once;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
```

## Strings (316)

```
com.apple.iapd.PreferencesDidChangeNotification
IOServicePublish
ACCPlatformCableTypePlugin_ConnectionUUIDKey
PretendAccessoryType
com.apple.CoreAccessories.PreferencesDidChangeNotification
USB3Device
EnableWrongOrientationMessage
ACCAuthProtocolMaxMessageSize
AppleUSB20CameraKitHub
AppleUSBCableType
FamilyCode
com.apple.CoreAccessories
EnableIndonesiaInductiveTx
DeviceIdentityPreArmDateOverride
DisableSNOnly
com.apple.accessories.signposts
clientsPreventingSleepLock
IdentityCertUseIndex
ForceMFi4AuthOverNFC
MPPAuthEnablePretendAuth
ChargingPowerOverride
OverrideCanReceiveInductivePowerOID
AllowMFi4DevCertsOnProdDevice
AssertName
USBFaultNotification_FaultTypeKey
BypassTrustDialog
MFi4ECDSAOnly
IgnoreAuthReset
com.apple.accessoryd.platform-iokit.applePencilSleepAssertionTimerQ
TreatAuthCPDEVNAsV3
IgnorePowerSourceUpdateForAvailableCurrent
MPPAuthPreferredSlot
ChargingPowerBehavior
NoIdleSleepAssertion
ACCPlatformCableTypePlugin_CableTypeKey
AllowACCAuthProtocolOnAllTransport
PretendBatteryLevel
DownstreamAdapterFamily
ACCAuthProtocolPretendAuth
DisableWirelessCTA
SkipNFCAuth
Disable1WayNFCForInductive
OverrideMPPAuthSupported
RejectionOfMultipleLocation
ACCPlatformSystemPower_SystemHasPoweredOnNotification
com.apple.logging
EnableAuthTimeoutTTR
BLEPairingDontEarlyInfoAsDeviceUID
IOServiceTerminate
NEEDS_ACCESSORY_RESET
IOService
IOPMPowerSource
ProductVersion
BLEPairingConfigRequestDelayMs
DisableMFi4CertSupport
Endpoint
com_apple_driver_AppleUSBCardReaderUMC
\xf01
ACCPlatformCableTypePlugin_USBCableTypeDidChange
EnableACCAuthProtocolOnNFC
SysdiagnoseOnInductiveCTAFailure
TransportSignpost
MaxOutboundiAP2PacketSize
com.apple.accessoryd.cameraKitHubQ
IOServiceFirstMatch
DisableAuthFailureTTRForXR
IdentityCertRefreshState
DisablePowerUpdateForCurrentDraw
DontSkipInductiveAuthOnCTA
ForceT56RelaySupport
com.apple.iap.iapuidmanager.queue
USBDevice
com.apple.accessoryd.platform-iokit.sleepAssertionQ
ShowHiddenAccessories
EnableTrustDialog
DisableIAPHVCFixForAuth
PretendWirelessCTAMatch
MPPAuthGetLeafCertFirst
kUSBCameraKitHubTotalCurrent
com.apple.iapd.LoggingPreferencesChangedNotification
IsCharging
ACCAuthProtocolAllowMutualAuth
DisableT56Support
Connection
void __powerBatteryMatch(void *, io_iterator_t)
ForceAuthTimeout
DisableAMSHookUp
KeepAACPAuthData
PretendNFCAuthTimeout
ACCPlatformCableTypePlugin_BatteryChargeLevelKey
USB3DeviceNeedsAuthentication
EnableDEVNCertSupport
SkipGaugeSignatureCheck
BLEPairingDisableOOBPPlusFlow
DisableACCAuthProtocolOnInductive
PretendNoNFCResponse
kUSBBusCurrentAllocation
com.apple.accessories.platform-plugins
MFi4ECDSADisallow
com.apple.accessoryd.mfi4Assertion
UseCertDataPropertyForAuth
TestCreateBLEPairingOnInductive
DisableAuthTimeoutTTRForXR
NFCAnalyticsDate
AppleUSB30CameraKitHub
ACCPlatformUSBCameraKitHubPlugin_ConnectionUUID
USBHost
USB3HostAltConfig
Power
IdentityCertRefreshInterval
DisableCertVerification
com.apple.accessoryd.ea-session-open
kUSBFailedRequestedPower
Detached
WiFiSharing
ExternalConnected
EnableChinaInductiveTx
BLEPairingAuthTimeoutValueS
NFCSecondaryColorOverride
ACCPlatformCableTypePlugin_BatteryChargingStateKey
USBDeviceNeedsAuthentication
Transport
i
KnownAccessories
AssertLevel
USB3Host
AuthTTRForAllTransports
NFCColorOverride
AllowNFCColorOverride
PretendNFCAuthFailed
MFi4SigmaIRequired
DisableNFCAuthTimer
v8@?0
com.apple.accessoryd.powerMonitor.systemPower.queue
IgnoreAACPAuthStatus
PretendNoDeviceIdentityCerts
MPPAuthChallengeFirst
USBHiAPEnable
GenericMFiIgnoreCertCaps
AuthenticationOverride
AppleUSB30XHCIRemovablePort
USBFaultNotification_ConnectionUUIDKey
ForceAuthFail
DisableInductiveAuthTTR
BLEPairingIgnoreZeroEarlyInfo
MFi4AuthTimeoutValueS
General
DisableAACPAuth
ACCAuthProtocolRoleSupport
ForceAccInfoUpdateRelaySupport
kUSBDesiredChargingCurrent
ACCPlatformCableTypePlugin_IsExternalChargerConnectedKey
MaxCapacity
com.apple.accessoryd
AssertType
ACCPlatformUSBCameraKitHubPlugin_HubChange
DisableCertSupport
IgnoreIsOnAC
PacketLoggingPlainTextOnly
LiveVoicemailFakeRinging
AdapterDetails
com.apple.iapd
PlatformIDOverride
InductiveAuthPretendMatchRxID
IgnoreAccInfoUpdateRelaySupport
ACCPlatformCableTypePlugin_BatteryChargingTypeChanged
IOGeneralInterest
com.apple.accessoryd.acc-connected.
com.apple.accessoryd.applePencilAssertion
&
-[PowerMonitor createBatteryNotificationClient]
CurrentCapacity
UARPActivityTimerS
<Undefined>
AllowsDeviceRestart
IdentityCertIsClassD
MFi4RelayReadRetryDelayMs
EnableManager2ForTransport
Use +[%@ %@] instead of -%@.
com.apple.accessoryd.platform-iokit.mfi4SleepAssertionTimerQ
ACCPlatformSystemPower_SystemCanSleepNotification
ACCPlatformSystemPower_SystemWillSleepNotification
USBFaultNotification
SysdiagnoseInsteadOfAuthTTR
IdentityCertUseTime
AuthCPStartDelayMs
PowerSourceUpdateBehavior
USBHostAltConfig
WaitForiAPTrafficDelayMS
0 clients, unregistering battery notifications
Apple Pencil assertion timer expired!!
createApplePencilSleepAssertion starting assertion timer
ERROR: Class instance pUSBMonitor = nil !\n
getUSBHubSiphoningCurrentRequirement: CameraKitHubPortCurrentAllocation=%d/%d CameraKitHubPortFailedRequestedPower=%d/%d CameraKitHubExtraRequestedPower=%d
_InitUSB30CameraKitHubNotifications: IOServiceAddMatchingNotification terminate fail status:%02X, ioIter:%04X
getBatteryChargingState: Disabled
createBatteryNotificationClient registered clientUUID: %@ batteryNotificationClients: %@
Apple Pencil sleep assertion taken
createMFi4SleepAssertion stopping assertion timer
ERROR: Class instance pUSBMonitor = NULL !\n
__USBCameraKitHubPortInterest: ERROR: service is NULL
__USBCameraKitHubGetPortFailedRequestedPower: failed to get kUSBFailedRequestedPower, service=%d(%d) child=%d usbFailedRequestedPowerRef=%x, expected for normal condition
__USBCameraKitHubGetPortExtraRequestedPower: failed to get %s, service=%d(%d) child=%d usbExtraRequestedPowerRef=%x, expected for normal condition
__USBCameraKitHubGetPortExtraRequestedPower: failed to get child kIOUSBPlane, service=%d(%d) child=%d, result=%d
__USBCameraKitHubPortInterest: received kIOMessageServiceIsAttemptingOpen, pRefCon=%d msgArg=%d
cableType=%d bCableTypeUSBDevice=%d bCableTypeUSBHost=%d
pUSBMonitor=%@
initUSBCameraKitHubNotifications: _ioUSB20CameraKitHubNotifyPort=%d _ioUSB30CameraKitHubNotifyPort=%d
ERROR - IORegistryGetRootEntry() failed
getExternalBatteryChargingTypeIsInductive = %d
ERROR - service is NULL
getUSBHubSiphoningCurrentRequirementInmA: ERROR: Unexpected extra power request on both CameraKitHub %d %d
_InitUSB20CameraKitHubNotifications: monitor=%@
ea session sleep assertion taken
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
__USBCameraKitHubGetPortCurAllocation: failed to get kUSBBusCurrentAllocation, service=%d(%d) child=%d usbCurAllocRef=%x
destroySleepNotificationsForClient clientUUID: %@ sleepNotificationClients: %@
No longer waiting on clients, signaling semaphore
handle battery state update: adapterFamily = %@, adapterDetails = %@
Received kIOMessageSystemWillSleep
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
__CameraKitHubClassHandleMatch: ERROR: IONotificationPortGetRunLoopSource(ioUSB20CameraKitHubNotifyPort) returned NULL!
destroyBatteryNotificationClient clientUUID: %@ remaining batteryNotificationClients: %@
0 clients, unregistering sleep notifications
_checkAndSendNotificationForOldConnected: overrideChanged %d, isExtChargerConnected %d -> %d, isBatteryCharging %d -> %d, batteryChargeLevelPercent(%d) %d -> %d, batteryChargingType %d -> %d, batteryChargingTypeExternal %d -> %d
MFi4 sleep assertion taken
__CameraKitHubClassSetupPortNotificationHandler: pRefCon=%x ioUSB20CameraKitHubService=%d
ERROR - IOPMAssertionCreateWithProperties returned error: 0x%08x!!
__CameraKitHubClassHandleMatch: ERROR: Invalid pRefCon(%d)
Received kIOMessageSystemHasPoweredOn
UUID: %@ has already taken a sleep assertion!!
MFi4 sleep assertion released
__CameraKitHubClassMatch: ERROR: invalid pRefCon(%x) !
__USBCameraKitHubGetPortCurAllocation: failed to get child kIOUSBPlane, service=%d(%d) child=%d, result=%d
__CameraKitHubClassSetupPortNotificationHandler: ERROR: couldn't get CameraKitHubService(%d) %#x
[WARNING] sleep notification handling timed out
ACCPlatformPluginIOKit: removeMFi4SleepAssertion: MFi4 sleep assertion removed
__CameraKitHubClassSetupPortNotificationHandler: ERROR: couldn't add interest notification %#x
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Created log object %s: %s
ERROR - couldn't take ea sleep assertion
__CameraKitHubClassHandleMatch: pRefCon=%x ioUSB20CameraKitHubService=%d
__CameraKitHubClassSetupPortNotificationHandler: couldn't get CameraKitHubService(%d) %#x
_InitUSB30CameraKitHubNotifications: IOServiceAddMatchingNotification publish fail status:%02X, ioIter:%04X
createSleepNotificationClient successfully registered for sleep notifications
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
ERROR -  couldn't release Apple Pencil sleep assertion
_InitUSB20CameraKitHubNotifications: IOServiceAddMatchingNotification terminate fail status:%02X, ioIter:%04X
__CameraKitHubClassHandleMatch: ERROR: couldn't add interest notification %#x
getBatteryChargeLevel: batteryChargeLevelPercent: %d -> %d
IORegisterForSystemPower failed!!  No system power notifications
uidForNotification = %lu
getBatteryChargingState: Charging
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Apple Pencil sleep assertion released
__USBCameraKitHubGetPortFailedRequestedPower: failed to get child kIOUSBPlane, service=%d(%d) child=%d, result=%d
ERROR - couldn't take MFi4 sleep assertion
IOServiceAddMatchingNotification terminate fail status:%02X, ioIter:%04X\n
ERROR - IOObjectRetain failed %#x
_updateSiphoningValuesFromDrivers: ResetOvercurrentSiphoning(), PortCurrentAllocation=%d/%d PortFailedRequestedPower=%d/%d ExtraRequestedPower=%d OverCurrentDetected=%d
ERROR - IONotificationPortGetRunLoopSource(pUSBMonitor->_ioUSB30XHCIRemovablePortNotifyPort) returned NULL!
Created %d log object(s)!
ERROR -  couldn't release MFi4 sleep assertion
__CameraKitHubClassMatch: ERROR: IOObjectRetain failed %#x
__CameraKitHubClassMatch: ERROR: already registered, service=%x
__CameraKitHubClassSetupPortNotificationHandler: pRefCon=%x ioUSB30CameraKitHubService=%d
getBatteryChargingState: Charged
UUID:%@ has taken a sleep assertion!!
removeApplePencilSleepAssertion stopping assertion timer
__CameraKitHubClassSetupPortNotificationHandler: ERROR: Invalid pRefCon(%d)
Failed to create os_log_t object %s: %s!
cableType=%d RemovablePortActive=%d
__USBCameraKitHubInterest: ERROR: service is NULL
%s IOServiceAddInterestNotification failed: %08x
ea session sleep assertion released
__USBCameraKitHubInterest: received kUSBHostMessageOvercurrentCondition! pRefCon=%d msgArg=%d
__USBCameraKitHubPortInterest: ERROR: Invalid pRefCon(%d)
Logging preferences changed! (pretendBatteryLevel): %d -> %d
ERROR - couldn't take Apple Pencil sleep assertion
ERROR - Couldn't add interest notification %#x
__CameraKitHubClassSetupPortNotificationHandler: ERROR: IONotificationPortGetRunLoopSource(ioUSB20CameraKitHubNotifyPort) returned NULL!
pUSBMonitor=%@ msgType=%xh msgArg=%hhx
getBatteryChargeLevel: isBatteryCharging %d, batteryCapacityOverride %d, isExtChargerConnected %d, batteryChargeLevelPercent %d
createSleepNotificationClient registered clientUUID: %@ sleepNotificationClients: %@
ERROR - IORegistryEntrySearchCFProperty() for AppleUSBCableType failed
familyCode to charging type: %llx -> %d
MFi4 assertion timer expired!!
createMFi4SleepAssertion starting assertion timer
type=%d flag=%d
Could not get property dictionary for service=%x
__USBCameraKitHubInterest: received kTotalCamKitCurrentMessage! pRefCon=%d msgArg=%d
__USBCameraKitHubPortInterest: received kUSBHostMessageOvercurrentCondition! pRefCon=%d msgArg=%d
ERROR: Class instance pUSBMonitor == NULL or _ioUSB30XHCIRemovablePortService(0x%x) = NULL !\n
getBatteryChargingTypeIsInductive = %d
IOServiceAddMatchingNotification publish fail status:%02X, ioIter:%04X\n
ERROR - already registered, service=%x
ERROR - IONotificationPortGetRunLoopSource(pUSBMonitor->_ioUSBCardReaderNotifyPort) returned NULL!
__CameraKitHubClassReset: pRefcon=%x monitor=%@
%s IOServiceAddMatchingNotification failed: %08x
clientHandledSleepNotification removed client: %@: clientsPreventingSleep: %@
handle battery state update: isExtChg=%u->%u, isBChg%u->%u, bCap=%u->%u, bCapMax=%u->%u, bCLP=%u->%u, chgType=%d->%d, chgTypeExt=%d->%d
UUID: %@ released sleep assertion!!
__CameraKitHubClassSetupPortNotificationHandler: ERROR: IONotificationPortGetRunLoopSource(ioUSB30CameraKitHubNotifyPort) returned NULL!
__CameraKitHubClassTerminate: pRefcon=%d
Received kIOMessageCanSystemSleep
ERROR -  couldn't release ea sleep assertion
ACCPlatformPluginIOKit: createMFi4SleepAssertion: MFi4 sleep assertion taken
_updateSiphoningValuesFromDrivers: %f TotalCurrent=%d PortCurrentAllocation=%d/%d PortFailedRequestedPower=%d/%d ExtraRequestedPower=%d OverCurrentDetected=%d
prop='%@' __usbCableType=%d
__CameraKitHubClassReset: ERROR: Invalid pRefCon(%d)
__CameraKitHubClassTerminate: ERROR: Invalid pRefCon!
ERROR: Class instance == NULL or _ioUSBCardReaderService(0x%x) = NULL !\n
_InitUSB20CameraKitHubNotifications: IOServiceAddMatchingNotification publish fail status:%02X, ioIter:%04X
__USBCameraKitHubInterest: ERROR: Invalid pRefCon(%d)
ERROR - IOMasterPort() failed
Already registered, service=%x
```
