# `/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`

iOS 27.2 dyld shared cache image. Version `41.7.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`
- `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 15 classes, 9 protocols, 525 methods, 139 properties

### Class pages

Every class and protocol, with its methods: [`BTAirPodsControlRequest`](../objc/BTAirPodsControlRequest_BluetoothServices.md), [`BTAirPodsControlServiceClient`](../objc/BTAirPodsControlServiceClient_BluetoothServices.md), [`BTAudioRoutingRequest`](../objc/BTAudioRoutingRequest_BluetoothServices.md), [`BTAudioRoutingResponse`](../objc/BTAudioRoutingResponse_BluetoothServices.md), [`BTAudioSession`](../objc/BTAudioSession_BluetoothServices.md), [`BTBannerUISession`](../objc/BTBannerUISession_BluetoothServices.md), [`BTBluetoothPairingSession`](../objc/BTBluetoothPairingSession_BluetoothServices.md), [`BTCloudAccountInfo`](../objc/BTCloudAccountInfo_BluetoothServices.md), [`BTCloudDevice`](../objc/BTCloudDevice_BluetoothServices.md), [`BTCloudDeviceSupportInformation`](../objc/BTCloudDeviceSupportInformation_BluetoothServices.md), [`BTCloudServicesClient`](../objc/BTCloudServicesClient_BluetoothServices.md), [`BTCloudServicesXPCClientInterface`](../objc/BTCloudServicesXPCClientInterface_BluetoothServices.protocol.md), [`BTCloudServicesXPCDaemonInterface`](../objc/BTCloudServicesXPCDaemonInterface_BluetoothServices.protocol.md), [`BTCloudSoundProfileRecord`](../objc/BTCloudSoundProfileRecord_BluetoothServices.md), [`BTMagicPairingSettings`](../objc/BTMagicPairingSettings_BluetoothServices.md), [`BTServicesClient`](../objc/BTServicesClient_BluetoothServices.md), [`BTServicesXPCClientInterface`](../objc/BTServicesXPCClientInterface_BluetoothServices.protocol.md), [`BTServicesXPCDaemonInterface`](../objc/BTServicesXPCDaemonInterface_BluetoothServices.protocol.md), [`BTShareAudioSessionClient`](../objc/BTShareAudioSessionClient_BluetoothServices.md), [`CBCentralManagerDelegate`](../objc/CBCentralManagerDelegate_BluetoothServices.protocol.md), [`CBPeripheralDelegate`](../objc/CBPeripheralDelegate_BluetoothServices.protocol.md), [`NSCoding`](../objc/NSCoding_BluetoothServices.protocol.md), [`NSObject`](../objc/NSObject_BluetoothServices.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_BluetoothServices.protocol.md)

### Classes

`BTAirPodsControlRequest`, `BTAirPodsControlServiceClient`, `BTAudioRoutingRequest`, `BTAudioRoutingResponse`, `BTAudioSession`, `BTBannerUISession`, `BTBluetoothPairingSession`, `BTCloudAccountInfo`, `BTCloudDevice`, `BTCloudDeviceSupportInformation`, `BTCloudServicesClient`, `BTCloudSoundProfileRecord`, `BTMagicPairingSettings`, `BTServicesClient`, `BTShareAudioSessionClient`

### Protocols

`BTCloudServicesXPCClientInterface`, `BTCloudServicesXPCDaemonInterface`, `BTServicesXPCClientInterface`, `BTServicesXPCDaemonInterface`, `CBCentralManagerDelegate`, `CBPeripheralDelegate`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"BTAirPodsControlServiceClient",&,N,V_client) client;
@property (TB,N,V_enabled) enabled;
@property (T@?,C,N,V_getHandler) getHandler;
@property (T@?,C,N,V_setHandler) setHandler;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_timeoutTimer) timeoutTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"CBDevice",&,N,V_peerDevice) peerDevice;
@property (T@"NSString",&,N,V_deviceSN) deviceSN;
@property (T@"NSString",&,N,V_deviceUUID) deviceUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (Ti,N,V_audioScore) audioScore;
@property (T@"NSString",C,N,V_appBundleID) appBundleID;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (TI,N,V_flags) flags;
@property (T@"NSDictionary",&,N,V_options) options;
@property (T@"NSString",C,N,V_reason) reason;
@property (T@?,C,N,V_responseHandler) responseHandler;
@property (Ti,N,V_action) action;
@property (TI,N,V_clientID) clientID;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (T@"NSError",C,N,V_error) error;
@property (T@"NSString",C,N,V_reason) reason;
@property (T@"NSDictionary",C,N,V_wxInfo) wxInfo;
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (Ti,N,V_audioArbitrationResult) audioArbitrationResult;
@property (Ti,N,V_category) category;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (TI,N,V_flags) flags;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (TB,N,V_inAppRouting) inAppRouting;
@property (T@"NSString",C,N,V_label) label;
@property (Td,N,V_timeoutSeconds) timeoutSeconds;
@property (Ti,N,V_mode) mode;
@property (T@?,C,N,V_actionHandler) actionHandler;
@property (Ti,N,V_backgroundColor) backgroundColor;
@property (T@"NSString",C,N,V_bannerAppID) bannerAppID;
@property (TI,N,V_bannerType) bannerType;
@property (T@"NSString",C,N,V_centerContentText) centerContentText;
@property (T@"NSString",C,N,V_centerContentItemsIcon) centerContentItemsIcon;
@property (T@"NSString",C,N,V_centerContentItemsText) centerContentItemsText;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_label) label;
@property (T@"NSString",C,N,V_leadingAccessoryImageName) leadingAccessoryImageName;
@property (T@"NSString",C,N,V_leadingAccessoryImagePath) leadingAccessoryImagePath;
@property (TI,N,V_leadingAccessoryImagePID) leadingAccessoryImagePID;
@property (Td,N,V_timeoutSeconds) timeoutSeconds;
@property (T@"NSString",C,N,V_trailingAccessoryImageName) trailingAccessoryImageName;
@property (T@"NSString",C,N,V_trailingAccessoryImagePath) trailingAccessoryImagePath;
@property (T@"NSString",C,N,V_trailingAccessoryText) trailingAccessoryText;
@property (Td,N,V_lowBatteryLevel) lowBatteryLevel;
@property (Td,N,V_batteryLevelInfo) batteryLevelInfo;
@property (T@"NSString",C,N,V_feedbackDeviceContext) feedbackDeviceContext;
@property (T@"NSString",C,N,V_feedbackFormIdentifier) feedbackFormIdentifier;
@property (T@"NSString",C,N,V_subformType) subformType;
@property (TB,N,V_aggregate) aggregate;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TB,N,V_connectOnly) connectOnly;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (TI,R,N,V_deviceVersion) deviceVersion;
@property (TB,N,V_disconnectOnly) disconnectOnly;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"NSString",C,N,V_guestAddress) guestAddress;
@property (T@"NSData",C,N,V_guestKey) guestKey;
@property (TB,N,V_guestMode) guestMode;
@property (TB,N,V_guestPermanent) guestPermanent;
@property (T@"NSString",R,C,N,V_name) name;
@property (TB,R,N,V_softwareVolume) softwareVolume;
@property (TB,N,V_userNotInContacts) userNotInContacts;
@property (TB,N,V_isSignedIn) isSignedIn;
@property (TB,N,V_manateeAvailable) manateeAvailable;
@property (T@"NSString",&,N,V_accountIdentifier) accountIdentifier;
@property (T@"NSString",&,N,V_loginID) loginID;
@property (T@"NSString",&,N,V_bluetoothAddress) bluetoothAddress;
@property (T@"NSString",&,N,V_manufacturer) manufacturer;
@property (T@"NSString",&,N,V_modelNumber) modelNumber;
@property (T@"NSString",&,N,V_nickname) nickname;
@property (T@"NSString",&,N,V_productID) productID;
@property (T@"NSString",&,N,V_vendorID) vendorID;
@property (T@"NSString",&,N,V_bluetoothAddress) bluetoothAddress;
@property (T@"NSString",&,N,V_budsFirmwareVersion) budsFirmwareVersion;
@property (T@"NSString",&,N,V_caseName) caseName;
@property (T@"NSString",&,N,V_caseFirmwareVersion) caseFirmwareVersion;
@property (T@"NSString",&,N,V_caseSerialNumber) caseSerialNumber;
@property (T@"NSString",&,N,V_hardwareVersion) hardwareVersion;
@property (T@"NSString",&,N,V_leftBudSerialNumber) leftBudSerialNumber;
@property (T@"NSString",&,N,V_rightBudSerialNumber) rightBudSerialNumber;
@property (T@"NSString",&,N,V_ancAssetVersion) ancAssetVersion;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@"NSData",&,N,V_soundProfileData) soundProfileData;
@property (T@"NSURL",&,N,V_soundProfileFileURL) soundProfileFileURL;
@property (T@"NSString",&,N,V_bluetoothAddress) bluetoothAddress;
@property (T@"NSData",&,N,V_masterKey) masterKey;
@property (T@"NSData",&,N,V_masterHint) masterHint;
@property (T@"NSData",&,N,V_accessoryKey) accessoryKey;
@property (T@"NSData",&,N,V_accessoryHint) accessoryHint;
@property (T@"NSData",&,N,V_encryptionKey) encryptionKey;
@property (T@"NSData",&,N,V_irk) irk;
@property (T@"NSData",&,N,V_crownRotationDirection) crownRotationDirection;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_productID) productID;
@property (T@"NSString",&,N,V_vendorID) vendorID;
@property (T@"NSString",&,N,V_buttonModes) buttonModes;
@property (T@"NSString",&,N,V_color) color;
@property (T@"NSString",&,N,V_deviceIDFeatureBitsV1) deviceIDFeatureBitsV1;
@property (T@"NSString",&,N,V_deviceIDFeatureBitsV2) deviceIDFeatureBitsV2;
@property (T@"NSString",&,N,V_listeningServices) listeningServices;
@property (T@"NSString",&,N,V_listeningServicesV2) listeningServicesV2;
@property (T@"NSString",&,N,V_spatialAudio) spatialAudio;
@property (T@"NSString",&,N,V_optimizedBatteryCharging) optimizedBatteryCharging;
@property (T@"NSString",&,N,V_optimizedBatteryFullChargeDeadline) optimizedBatteryFullChargeDeadline;
@property (T@"NSString",&,N,V_ratchet) ratchet;
@property (T@"NSString",&,N,V_reserved) reserved;
@property (T@"NSString",&,N,V_settingsMask) settingsMask;
@property (T@"NSString",&,N,V_supportedServices) supportedServices;
@property (T@"NSString",&,N,V_version) version;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (Ti,N,V_mode) mode;
@property (T@?,C,N,V_progressHandler) progressHandler;
```

## Strings (555)

```
DontRoute
### BTDeviceDisconnect failed: %d, %#m\n
BT_SERVICE_HANDSFREE_START_VOICE_COMMAND
PoweredOn
Create Device Record: %@
### BTDevice lookup %@ failed: %#m\n
### BTAccessoryManagerGetFeatureCapability software volume failed: %#m\n
BT_SERVICE_DISCONNECTION_RESULT
BUISKeyLowBatteryLevel
, MainKey: %@
-[BTBluetoothPairingSession _completed:]
Retry after BTSession finishes tearing down\n
BTPairingAgentDeletePairedDevice
BTPairingAgent started: %#m\n
BT_SERVICE_LMP_NAME_CHANGED
Ready
-[BTCloudServicesClient modifyDeviceSupportInformationRecord:completion:]_block_invoke_2
-[BTCloudServicesClient deleteMagicSettingsRecord:completion:]_block_invoke_2
Nil Sound Profile Record or Data
PlayAndRecord
BTPairingAgentCancelPairing\n
BT_SERVICE_DISCONNECTION_ATTEMPT
BUISKeyLAProductID
, LSv2: %@
BTSession attached: %#m\n
Unable to create sound profile with file handle
### BTSesson add service callbacks failed: %#m\n
BTServiceRemoveCallbacks\n
BUISKeyBannerTimeout
BTSession retrying after detach\n
BUISKeyFeedbackDeviceContext
### SetSilentMode failed: peer %@, enabled %s, %@
BTBannerUISession
, LS: %@
No peripheral: %@
Bad set opcode: 0x%04X, value <%@>
DiscoverCharacteristicsWait
Delete device with BluetoothAddress: %@
-[BTCloudServicesClient deviceSupportInformationRecord:completion:]_block_invoke_2
### BTCloudDeviceSupportInformation Fetch failed: %{error}
BTBluetoothPairingSession
BTPairingAgentStart
BT_SERVICE_REMOTE_PLAY
-[BTAudioSession _activate]
### Create timeout timer failed\n
BTService disconnect: %#{flags}, %d %s, %#m\n
XPC connection interrupted
-[BTBannerUISession _xpcSendReplyError:request:]
SetSilentMode start: peer %@, enable %s, value <%@>
BUISKeyBackgroundColor
v8@?0
Invalidating
-[BTAudioSession _interrupted]
-[BTAudioSession invalidate]_block_invoke
BTService connect: %#{flags}, %d %s, %#m\n
BTService connect, ignoring device: %s vs %s\n
BUISKeyType
### BTDeviceConnectServicesWithParameters aggregate failed: %#m\n
BTSessionAttachWithQueue
No peripheral
-[BTCloudServicesClient createDeviceRecord:completion:]_block_invoke_2
-[BTCloudServicesClient fetchSoundProfileRecordWithCompletion:]_block_invoke_2
-[BTAudioRoutingRequest _activateSync]_block_invoke
BTSession still active during dealloc
BTPairingAgentDestroy
-[BTShareAudioSessionClient _invalidated]
BTCloudDevice
Resetting
BTCloudDeviceSupportInformation: %@
BT_SERVICE_SENSOR_RSSI
-[BTServicesClient _invalidated]
### GetSilentMode failed: peer %@, %@
DidDiscoverServices: peer %@, services %@
### Bad BTDevice address: '%@'\n
BT_SERVICE_CONNECTION_ATTEMPT
BUISKeyBannerType
### Failed to write sound profile, %{error}
Playback
-[BTAirPodsControlServiceClient getSilentModeWithCompletionHandler:]_block_invoke
-[BTAirPodsControlServiceClient setSilentMode:completionHandler:]_block_invoke
-[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:]
-[BTAudioSession _invalidated]
BTDeviceGetPairingStatus
%s completed
DidUpdateNotificationStateForCharacteristic: peer %@, characteristic %@, error %@
BTRootCloudServicesClient
BTAudioRoutingRequest
already paired
BTDeviceFromAddress
No characteristic
DidUpdateValueForCharacteristic: peer %@, characteristic %@, value <%@>
BTMagicPairingSettings: %@
Invalid
Activate: DA %@, GA %@, GM %s, DO %s, UNIC %s\n
### Device get pairing status failed: %#m\n
BTCloudServicesSoundProfileChangedNotification
Failed
errC
### Can't get the peer device for SN %@
GuestiOSAuthenticated
Stop
yes
### User confirmed without XPC cnx
-[BTBannerUISession activate]_block_invoke
Banner was dismissed by user
Bluetooth powered off
-[BTCloudServicesClient modifyDeviceRecord:completion:]_block_invoke
-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke
no
BT_SERVICE_REMOTE_REWIND_STOP
### DidFailToConnectPeripheral %@, error %@
Bad get opcode: 0x%04X, value <%@>
BTErrorDomain
SetSilentMode enqueued: peer %@, enable %s
DiscoverCharacteristicsStart
Please add sound profile data
Banner timed out
### DidDiscoverServices wrong peripheral: %@ (not %@)
Activated: %@
### Create retry timer failed\n
BTService event: %#{flags}, %d %s, %#m\n
BTDeviceGetName
-[BTShareAudioSessionClient invalidate]_block_invoke
No peer ID
DiscoverServicesStart
reas
Invalidate called
### DidDiscoverCharacteristics wrong service: %@ (not %@)
-[BTCloudServicesClient createMagicSettingsRecord:completion:]_block_invoke
Dealloc without invalidation
No BTSession for retry?\n
BT_SERVICE_REMOTE_STOP
BTCloudDeviceInformation: %@, %@, %@, %@, %@, %@, %@, %@, %@
DidDiscoverCharacteristicsForService: %@, service %@, characteristics %@
-[BTAudioRoutingRequest _activate]_block_invoke
BTPairingAgent attempt complete: %#m\n
### BTAccessoryManagerGetDefault failed: %#m\n
BT_SERVICE_REMOTE_VOL_DOWN
Activate already called
### BTDeviceGetAddressString start %@ failed: %#m\n
### BTPairingAgentCreate failed: %#m\n
void _btPairingAgentStatusHandler(BTPairingAgent, BTPairingEvent, BTDevice, BTResult, void *)
-[BTShareAudioSessionClient _ensureXPCStarted]
com.apple.BluetoothServices
actn
### BTDeviceConnectServices failed: %#m\n
BTPairingAgent attempt started: %#m\n
BTPairingAgent user confirmation handler\n
Bad set status 0x%04X, value <%@>
### Failed to create sound profile: %@, %{error}
### BTDeviceConfigureLinkKey failed: %#m\n
void _btPairingAgentUserConfirmationHandler(BTPairingAgent, BTDevice, uint32_t, BTBool, void *)
Re-activated
GuestiOSConnecting
No service UUID
-[BTAirPodsControlServiceClient peripheral:didUpdateNotificationStateForCharacteristic:error:]
-[BTAirPodsControlServiceClient peripheral:didWriteValueForCharacteristic:error:]
Ambient
BTDeviceConfigureLinkKey
BTPairingAgentCancelPairing
com.apple.BluetoothUIService
, VID: %@
, CR: %@
, DID2: %@
State: %s -> %s
-[BTCloudServicesClient cloudPairingIdentifierForPeripheral:completion:]_block_invoke_2
BT_SERVICE_REMOTE_MUTE
Succeeded
71060001-413A-41EA-AF86-8CECFA21D057
No characteristic UUID
Bluetooth state changed: %s
### DidDiscoverCharacteristics wrong peripheral: %@ (not %@)
-[BTCloudServicesClient deviceRecord:completion:]_block_invoke_2
### Create transaction failed\n
-[BTBluetoothPairingSession _btDeletePairingAndRetry]
BT_SERVICE_HANDSFREE_AUDIO_CONNECTED
-[BTShareAudioSessionClient _activate:]
Invalidate
BTMagicPairingSettings[%@]: Name(%lu): %@
Connected
-[BTAudioRoutingRequest invalidate]_block_invoke
Connecting
Pairing completed (%.2f seconds): %#m\n
BTPairingAgentCreate\n
-[BTShareAudioSessionClient _activate:]_block_invoke
Nil BTMagicPairingSettings deviceBluetoothAddress
BUISKeyTAImagePath
, MainHint: %@
, C: %@
-[BTAudioSession activateWithCompletion:]_block_invoke
-[BTBluetoothPairingSession _btEnsureStopped]
-[BTCloudServicesClient deviceRecordsWithCompletion:]_block_invoke_2
BUISKeyCCItemsIcon
-[BTBannerUISession _xpcSendMessage]
### BTCloudDevice failed: %@, %{error}
Delete Magic Settings for device with BluetoothAddress: %@
-[BTCloudServicesClient magicSettingsRecord:completion:]_block_invoke_2
BUISKeyLabel
-[BTMagicPairingSettings initWithCoder:]
WaitPoweredOn
-[BTCloudServicesClient createSoundProfileRecord:completion:]_block_invoke_4
com.apple.bluetoothcloud
### XPC error: %{error}, %{xpc}
errO
, AccKey: %@
, V: %@
-[BTAirPodsControlServiceClient centralManager:didFailToConnectPeripheral:error:]
com.apple.BluetoothCloudServices
### UpdateAudioState no XPC
BTPairingAgent stopped: %#m\n
DidUpdateFindMyPeripherals: peers %@
-[BTCloudServicesClient createMagicSettingsRecord:completion:]_block_invoke_2
GuestiOSWaitingForAccept
-[BTCloudDeviceSupportInformation initWithCoder:]
### BTDeviceConnectServicesWithParameters failed: %#m\n
-[BTCloudServicesClient cloudPairingIdentifierForPeripheral:completion:]_block_invoke
### Failed to fetch sound profile, %{error}
auSc
BTSession attach\n
-[BTServicesClient invalidate]_block_invoke
BTShareAudioSessionClient
No peer Device or Serial Number is specified
BTCloudServicesClient
v24@?0@\"NSFileHandle\"8@\"NSError\"16
wxif
mode
Activate
### DidWriteValueForCharacteristic wrong peripheral: %@ (not %@)
PoweredOff
### BTSession terminated (bluetoothd crash)...re-attaching\n
### UpdateAudioState failed to start XPC: %{error}
### BTPairingAgentStart failed: %#m\n
-[BTCloudServicesClient modifyDeviceRecord:completion:]_block_invoke_2
Nil record provided
BUISKeyFeedbackFormIdentifier
-[BTCloudServicesClient deviceRecord:completion:]_block_invoke
-[BTCloudServicesClient createDeviceSupportInformationRecord:completion:]_block_invoke_2
com.apple.bluetooth
BTSession still attaching during dealloc
BTDeviceDisconnect\n
Tearing down BTSession to retry later\n
-[BTCloudServicesClient deleteMagicSettingsRecord:completion:]_block_invoke
### Error: %{error}
BTDeviceConfigureLinkKey: %@, key %d bytes\n
-[BTCloudDevice initWithCoder:]
### DidUpdateValueForCharacteristic wrong characteristic: %@ (not %@)
-[BTBluetoothPairingSession _btDeletePairingAndRetry]_block_invoke
-[BTAirPodsControlServiceClient peripheral:didDiscoverServices:]
Magic deviceBluetoothAddress: %@
aid
BT_SERVICE_HANDSFREE_END_VOICE_COMMAND
BTDeviceGetDeviceId
-[BTAirPodsControlServiceClient isFindmyManaged]_block_invoke
Create CBCentralManager failed
Fetching Sound Profile Record
flgs
BTService connected: '%s', version 0x%X\n
-[BTCloudServicesClient _invalidated]
### BTPairingAgentDeletePairedDevice failed: %#m\n
BUISKeyLAImageName
\t
cid
-[BTAudioRoutingRequest updateAudioState:withState:]_block_invoke_2
### BTDeviceGetAddressString event %@ failed: %#m\n
GuestHeadphonesConnecting
, Enc: %@
No deviceBluetoothAddress to delete
BTSessionDetachWithQueue
### DidUpdateValueForCharacteristic wrong peripheral: %@ (not %@)
-[BTCloudServicesClient deviceSupportInformationRecordsWithCompletion:]_block_invoke_2
-[BTAudioRoutingRequest _activate]_block_invoke_2
BTDeviceConnectServices: aggregate\n
-[BTAirPodsControlServiceClient _runConnectStart]
-[BTAirPodsControlServiceClient _runConnectStart]_block_invoke
BUISKeyTAImageName
### Failed to modify sound profile: %@, %{error}
BT_SERVICE_REMOTE_FASTFORWARD_START
XPC started
Bluetooth reset
-[BTCloudServicesClient deleteDeviceSupportInformationRecord:completion:]_block_invoke
-[BTCloudServicesClient deleteSoundProfileRecordWithCompletion:]_block_invoke_2
-[BTAudioSession _activate]_block_invoke_2
BT_SERVICE_PHONE_BOOK_SEND_COMPLETE
BT_SERVICE_REMOTE_PAUSE
BT_SERVICE_REMOTE_NEXT
BUISKeyFeedbackSubformType
No params
-[BTCloudServicesClient deleteDeviceSupportInformationRecord:completion:]_block_invoke_2
v16@?0@\"NSArray\"8
ConnectStart
BUISKeyIdentifier
BUISKeyLAImagePath
, OBC: %@-%@
-[BTAirPodsControlServiceClient invalidate]_block_invoke
DiscoverServicesWait
Nil BTCloudDeviceSupportInformation
### BTSesson attach failed: %#m\n
Confirm
Bad peer ID: '%@'
Discover characteristics start: peer %@, service %@, characteristics %@
-[BTCloudServicesClient modifyMagicSettingsRecord:completion:]_block_invoke
### deviceBluetoothAddress failed: %@, %{error}
Route
Pushing out timer another %d seconds\n
DidWriteValueForCharacteristic: peer %@, characteristic %@
-[BTCloudServicesClient forceCloudPairingForIdentifiers:completion:]_block_invoke_2
### BT setup failed: %#m\n
void _btServiceEventHandler(BTDevice, BTServiceID, BTServiceEventType, BTServiceSpecificEvent, BTResult, void *)
-[BTAirPodsControlServiceClient _completeRequest:error:]
CentralManager retrieved FindMy peripherals with serial numbers count %lu
### DidWriteValueForCharacteristic wrong characteristic: %@ (not %@)
Nil BTCloudDeviceSupportInformation deviceBluetoothAddress
-[BTCloudServicesClient magicSettingsRecord:completion:]_block_invoke
-[BTCloudServicesClient accountInfoWithCompletion:]_block_invoke_2
-[BTCloudServicesClient createSoundProfileRecord:completion:]_block_invoke_5
Deleting Sound Profile Record
dAdr
### Send error create reply failed
### XPC connection unexpectedly invalidated
### Account Info failed: %{error}
-[BTAudioRoutingRequest _activateSync]
HijackBackOff
BTServiceAddCallbacks
### BTService connect failed: %#m\n
-[BTBannerUISession _xpcConnectionMessage:]
-[BTAirPodsControlServiceClient _reportError:]
BTAudioRoutingRequest, CID 0x%X, auSc %d, dAdr %@, flags %#{flags}
-[BTAudioRoutingRequest _interrupted]
### Too many retries (%u)\n
BTPairingAgent unknown event: %d, %#m\n
### XPC no message type
, DID1: %@
-[BTCloudServicesClient createSoundProfileRecord:completion:]_block_invoke_2
label
-[BTShareAudioSessionClient shareAudioProgressEvent:info:]
errD
### DidDiscoverCharacteristics not found: peer %@, service %@, characteristic %@ vs %@
-[BTCloudServicesClient _interrupted]
-[BTCloudServicesClient deleteSoundProfileRecordWithCompletion:]_block_invoke
BTAudioSession
-[BTBluetoothPairingSession _activate]
WPClient
/System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
BUISKeyCCItemsText
Error: %@
/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity
BT_SERVICE_PHONE_BOOK_SEND_INITIATED
BUISKeyBannerAppID
deviceBluetoothAddress: %@
opts
XPC interrupted
### Bad guest address: '%@'\n
-[BTShareAudioSessionClient userConfirmed:]_block_invoke
Invalid BTMagicPairingSettings with no bluetooth adress
Timed out
v16@?0@\"NSError\"8
Nil MagicSettings deviceBluetoothAddress
BT_SERVICE_A2DP_AUDIO_DISCONNECTED
CentralManager retrieved FindMy peripherals with serial numbers count %lu, managed by findmy %s
Discover services start: peer %@, services %@
Init
UpdateAudioState CID 0x%X audioState %s apps %@ 
BUISKeyBatteryLevel
### Info deviceBluetoothAddress failed: %@, %{error}
Info deviceBluetoothAddress: %@
Nil Peripheral Identifier
AudioAccessorydDiedNotification
BT_SERVICE_REMOTE_VOL_UP
-[BTShareAudioSessionClient _interrupted]
No opcode: value <%@>
-[BTCloudServicesClient createSoundProfileRecord:completion:]_block_invoke
### audioaccessoryd died
%s-%s
BTSession add callbacks\n
BTDeviceConnectServicesWithParameters: guest, permanent %s, key %d bytes\n
BTAccessoryManagerGetDefault
void _btSessionEventHandler(BTSession, BTSessionEvent, BTResult, void *)
Invalid BTCloudDeviceInformation with no bluetooth adress
### Activate failed: %{error}
errM
Unauthorized
### Interrupted
### BTDevice address not specified\n
BTServicesClient
BTDeviceConnectServices
BTAccessoryManagerGetFeatureCapability
, S: %@
No deviceBluetoothAddress
BTAudioRoutingResponse, CID 0x%X, actn %s, dAdr %@, err %{error}, reason %@, wxInfo %@
Unexpectedly invalidated
Default
Invalidate\n
BTDeviceAddressFromString
BTPairingAgentStop
### BTDeviceGetAddressString confirm %@ failed: %#m\n
Modify Device Record: %@
Invaliated
BTDeviceConnectServicesWithParameters
BTPairingAgentStop\n
BT_SERVICE_REMOTE_PREVIOUS
Re-activate
### No valid XPC connection
-[BTCloudServicesClient fetchSoundProfileRecordWithCompletion:]_block_invoke
BTDeviceGetAddressString
BTAirPodsControlServiceClient
### Peripheral Identifier failed: %@, %{error}
-[BTAudioRoutingRequest _handleServerDied]_block_invoke
-[BTBluetoothPairingSession _activate]_block_invoke
BTDeviceDisconnect
ShowPairInstructions
-[BTCloudServicesClient forceCloudPairingForIdentifiers:completion:]_block_invoke
Timeout
BTPairingAgentDestroy\n
BTCloudDevice: %@, %@, %@, %@, %@, %@
-[BTAirPodsControlServiceClient _invalidate]
v16@?0@\"BTAudioRoutingResponse\"8
-[BTAudioRoutingRequest _activateSync]_block_invoke_2
Activate, %@
Deleting stale BTDevice pairing and retrying (%u)\n
### Re-activate failed: %{error}
Cloud Identifiers: %@
Create Sound Profile Record: %@
BTSession device lookup\n
-[BTBannerUISession _xpcCompleted:]
### XPC unknown message type: %lld
### Send error with no cnx
, R: %@
-[BTAirPodsControlServiceClient centralManager:didConnectPeripheral:]
### Timeout\n
Unknown message type: %lld
-[BTAirPodsControlServiceClient _runDiscoverServicesStart]
-[BTAirPodsControlServiceClient _runDiscoverCharacteristicsStart]
No get result: value <%@>
Unknown
### Force Cloud Pairing failed for identifier: %@, %{error}
### Activate XPC error: %{error}
Start
### %s failed: %@
Unsupported
-[BTCloudServicesClient deviceSupportInformationRecord:completion:]_block_invoke
Activated
BTDeviceConnectServices\n
User confirmed: permanent %s
-[BTAirPodsControlServiceClient peripheral:didDiscoverCharacteristicsForService:error:]
### Magic deviceBluetoothAddress failed: %@, %{error}
-[BTCloudServicesClient deleteDeviceRecord:completion:]_block_invoke_2
, BM: %@
Connecting to peer %@
### DidConnectPeripheral wrong peripheral: %@ (not %@)
Create characteristic UUID failed: %@
Bad device SN: %@
-[BTAirPodsControlServiceClient centralManagerDidUpdateState:]
No set status: value <%@>
Unmanaged
Activating XPC Banner request
BUISKeyCCText
### BTCloudDeviceSupportInformation failed: %@, %{error}
err
-[BTBluetoothPairingSession _invalidate]
BT_SERVICE_REMOTE_REWIND_START
-[BTServicesClient _interrupted]
BTCloudAccountInfo - Account(%@): %@, signedIn: %d, manatee: %d
Progress: %s %##@
v16@?0@\"NSObject<OS_xpc_object>\"8
GetSilentMode enqueued: peer %@
-[BTAirPodsControlServiceClient centralManager:didUpdateFindMyPeripherals:]
cat
Record
, IRK: %@
-[BTAirPodsControlServiceClient _runProcessRequest:]
-[BTCloudServicesClient modifyDeviceSupportInformationRecord:completion:]_block_invoke
### Failed to delete sound profile: %@, %{error}
BT_SERVICE_A2DP_AUDIO_CONNECTED
No error, no response
Unable to establish connection to Bluetooth Cloud Services
-[BTBannerUISession _xpcEvent:]
-[BTCloudServicesClient invalidate]_block_invoke
-[BTCloudServicesClient deleteDeviceRecord:completion:]_block_invoke
BT_SERVICE_SDP
GuestHeadphonesConnected
Starting timer to retry pairing later %d seconds\n
BTSession detached: %#m\n
BTMagicPairingSettings[%@]: Name(%lu), PID: %@, VID: %@
Request after invalidate
GetSilentMode start: peer %@, value <%@>
-[BTAudioRoutingRequest _activate]
BTSession configure device %@, guest %@\n
BT_SERVICE_REMOTE_FASTFORWARD_STOP
-[BTAudioRoutingRequest _invalidated]
-[BTAudioRoutingRequest _reportError:]
GuestHeadphonesWaitForRoute
### BTMagicPairingSettings failed: %@, %{error}
?
BT_SERVICE_CONNECTION_RESULT
No service
-[BTCloudServicesClient createDeviceSupportInformationRecord:completion:]_block_invoke
BTSessionDetachWithQueue\n
XPC connection invalidated
XPC error %@
-[BTAudioSession _reportError:]
Banner was accepted by user
SetSilentMode
BTSession device %@ pairing status: %s\n
BTCloudAccountInfo - AccountID: %@, signedIn: %d, manatee: %d
-[BTCloudServicesClient modifyMagicSettingsRecord:completion:]_block_invoke_2
### DidDiscoverServices not found: peer %@, service %@ vs %@
DidUpdateValueForCharacteristic ignored without request: peer %@, characteristic %@
Invalidated
PhoneCall
Retry pairing\n
BT_SERVICE_PHONE_BOOK_SYNC_SUPPORTED
Interrupted
XPC event error
Writing Sound Profile Record to handle
, PID: %@
Wrote Sound Profile Record to handle
BTAudioSession, CID 0x%X, Category %s, Timeout %.3f seconds
BTPairingAgent user confirmation handler, ignoring device: %s vs %s\n
-[BTCloudServicesClient modifySoundProfileRecord:completion:]_block_invoke
BTPairingAgentStart\n
GetSilentMode
-[BTAirPodsControlServiceClient _run]
-[BTCloudServicesClient createDeviceRecord:completion:]_block_invoke
Peripheral Identifier: %@
BTServiceRemoveCallbacks
### BTSession failed: %#m\n
BUISKeyTAText
Nil Device Record
Activate, CID 0x%X
-[BTBluetoothPairingSession _btEnsureStarted]
, AccHint: %@
-[BTCloudServicesClient modifySoundProfileRecord:completion:]_block_invoke_2
BTService unknown event type: %#{flags}, %d, %d %s, %#m\n
BT_SERVICE_HANDSFREE_AUDIO_DISCONNECTED
-[BTShareAudioSessionClient _activate:]_block_invoke_2
DidConnectPeripheral peer %@
Modify Sound Profile Record: %@
### UpdateAudioState XPC error: %{error}
-[BTAudioSession _activate]_block_invoke_3
BTPairingAgentCreate
BTSession unknown event %d, result %#m\n
### Re-activate XPC error: %{error}
BTCloudSoundProfileRecord: %@
Create service UUID failed: %@
Delete Info device with BluetoothAddress: %@
2EE26CD4-C04E-41CE-905A-B4054F5D1770
### DidFailToConnectPeripheral wrong peripheral: %@ (not %@)
Restricted
BTPairingAgentAcceptSSP
Invalid BTCloudDevice with no bluetooth address
, SS: %@
### BTCloudDevice Fetch failed: %{error}
not paired
BUISKeyArgType
Connect failed without error
```
