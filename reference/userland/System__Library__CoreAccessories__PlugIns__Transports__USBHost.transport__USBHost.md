# `/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (8)

- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 13 classes, 6 protocols, 347 methods, 108 properties

### Class pages

Every class and protocol, with its methods: [`ACCPlatformPluginProtocol`](../objc/ACCPlatformPluginProtocol_USBHost.protocol.md), [`ACCPlatformUSBBillboardDevicePluginProtocol`](../objc/ACCPlatformUSBBillboardDevicePluginProtocol_USBHost.protocol.md), [`ACCPlatformUSBHostPluginProtocol`](../objc/ACCPlatformUSBHostPluginProtocol_USBHost.protocol.md), [`ACCPluginProtocol`](../objc/ACCPluginProtocol_USBHost.protocol.md), [`ACCTransportPluginProtocol`](../objc/ACCTransportPluginProtocol_USBHost.protocol.md), [`ACCUserDefaults`](../objc/ACCUserDefaults_USBHost.md), [`ACCUserNotification`](../objc/ACCUserNotification_USBHost.md), [`ACCUserNotificationManager`](../objc/ACCUserNotificationManager_USBHost.md), [`AccessoryEAInterface`](../objc/AccessoryEAInterface_USBHost.md), [`AccessoryIAPInterface`](../objc/AccessoryIAPInterface_USBHost.md), [`AccessoryTransportPluginUSBHost`](../objc/AccessoryTransportPluginUSBHost_USBHost.md), [`AccessoryUSBBillboardDevice`](../objc/AccessoryUSBBillboardDevice_USBHost.md), [`AccessoryUSBBillboardDeviceListener`](../objc/AccessoryUSBBillboardDeviceListener_USBHost.md), [`AccessoryUSBBillboardDeviceManager`](../objc/AccessoryUSBBillboardDeviceManager_USBHost.md), [`AccessoryUSBCDCInterface`](../objc/AccessoryUSBCDCInterface_USBHost.md), [`EAUSBBuffer`](../objc/EAUSBBuffer_USBHost.md), [`IAPDataBuffer`](../objc/IAPDataBuffer_USBHost.md), [`NSObject`](../objc/NSObject_USBHost.protocol.md), [`iAP2EASession`](../objc/iAP2EASession_USBHost.md)

### Classes

`ACCUserDefaults`, `ACCUserNotification`, `ACCUserNotificationManager`, `AccessoryEAInterface`, `AccessoryIAPInterface`, `AccessoryTransportPluginUSBHost`, `AccessoryUSBBillboardDevice`, `AccessoryUSBBillboardDeviceListener`, `AccessoryUSBBillboardDeviceManager`, `AccessoryUSBCDCInterface`, `EAUSBBuffer`, `IAPDataBuffer`, `iAP2EASession`

### Protocols

`ACCPlatformPluginProtocol`, `ACCPlatformUSBBillboardDevicePluginProtocol`, `ACCPlatformUSBHostPluginProtocol`, `ACCPluginProtocol`, `ACCTransportPluginProtocol`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) pluginName;
@property (TB,R,N) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",&,N,V_userNotificationCFDict) userNotificationCFDict;
@property (T^{__CFUserNotification=},N,V_userNotificationCF) userNotificationCF;
@property (T@"NSString",R,N,V_uuid) uuid;
@property (Ti,N,V_type) type;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_message) message;
@property (T@"NSString",C,N,V_lockScreenTitle) lockScreenTitle;
@property (T@"NSString",C,N,V_lockScreenMessage) lockScreenMessage;
@property (T@"NSString",C,N,V_defaultButtonName) defaultButtonName;
@property (T@"NSString",C,N,V_alternateButtonName) alternateButtonName;
@property (T@"NSString",C,N,V_otherButtonName) otherButtonName;
@property (T@"NSDictionary",C,N,V_iconConfiguration) iconConfiguration;
@property (T@"NSURL",C,N,V_iconURL) iconURL;
@property (TB,N,V_allowLockScreenDismissal) allowLockScreenDismissal;
@property (TB,N,V_isModal) isModal;
@property (TB,N,V_dismissOnUnlock) dismissOnUnlock;
@property (TB,N,V_ignoreQuietMode) ignoreQuietMode;
@property (TB,N,V_presentViaSystemAperture) presentViaSystemAperture;
@property (T@"NSNumber",&,N,V_systemSoundID) systemSoundID;
@property (Td,N,V_timeout) timeout;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_groupIdentifier) groupIdentifier;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableSet",&,N,V_userNotifications) userNotifications;
@property (T@"NSMutableDictionary",&,N,V_completionHandlers) completionHandlers;
@property (T@"NSRecursiveLock",&,N,V_lock) lock;
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (T@?,C,N,V_dataInHandler) dataInHandler;
@property (TS,R,N,V_vid) vid;
@property (TS,R,N,V_pid) pid;
@property (TI,R,N,V_vidpid) vidpid;
@property (T^^{IOUSBInterfaceStruct942},N,V_interface) interface;
@property (TC,N,V_bulkOutPipeRef) bulkOutPipeRef;
@property (TS,N,V_bulkOutPipeMaxPacketSize) bulkOutPipeMaxPacketSize;
@property (TC,N,V_bulkInPipeRef) bulkInPipeRef;
@property (TS,N,V_bulkInPipeMaxPacketSize) bulkInPipeMaxPacketSize;
@property (TC,N,V_interruptInPipeRef) interruptInPipeRef;
@property (TS,N,V_interruptInPipeMaxPacketSize) interruptInPipeMaxPacketSize;
@property (T*,N,V_interruptInPipeBuffer) interruptInPipeBuffer;
@property (T@"NSMutableArray",&,N,V_interfacePropertiesArray) interfacePropertiesArray;
@property (T@"NSMutableArray",&,N,V_inUseDataBufArray) inUseDataBufArray;
@property (T@"NSLock",&,N,V_dataBufLock) dataBufLock;
@property (TB,N,V_hasReadInterruptPipe) hasReadInterruptPipe;
@property (T@"NSMutableArray",&,N,V_interruptBulkReadList) interruptBulkReadList;
@property (TI,N,V_interruptBulkReadAllocCount) interruptBulkReadAllocCount;
@property (TI,N,V_interruptBulkReadReleaseCount) interruptBulkReadReleaseCount;
@property (TB,N,V_interfaceConfigured) interfaceConfigured;
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (TI,R,N,V_locationID) locationID;
@property (TQ,R,N,V_parentDeviceRegistryEntryID) parentDeviceRegistryEntryID;
@property (T@"NSDictionary",R,N,V_ioregProperties) ioregProperties;
@property (T@?,C,N,V_dataInHandler) dataInHandler;
@property (TB,N,V_needOutZLP) needOutZLP;
@property (TI,N,V_maxOutLength) maxOutLength;
@property (TS,R,N,V_vid) vid;
@property (TS,R,N,V_pid) pid;
@property (TI,R,N,V_vidpid) vidpid;
@property (Td,R,N,V_creationTime) creationTime;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSDictionary",&,N,V_aidInfo) aidInfo;
@property (TB,N,V_isRunning) isRunning;
@property (T@"NSMutableDictionary",&,N,V_accessoryConnections) accessoryConnections;
@property (T@"NSMutableDictionary",&,N,V_accessoryNativeUSBEndpoints) accessoryNativeUSBEndpoints;
@property (T@"NSMutableDictionary",&,N,V_activeEAInterfaces) activeEAInterfaces;
@property (T@"NSMutableDictionary",&,N,V_activeUSBCDCInterfaces) activeUSBCDCInterfaces;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessoryConnectionsLock) accessoryConnectionsLock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_activeEAInterfacesLock) activeEAInterfacesLock;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessoryNativeUSBEndpointsLock) accessoryNativeUSBEndpointsLock;
@property (Tq,N,V_accessoryiAPIntefaceTrafficWaitListCount) accessoryiAPIntefaceTrafficWaitListCount;
@property (T@"NSMutableDictionary",&,N,V_accessoryiAPIntefaceTrafficWaitList) accessoryiAPIntefaceTrafficWaitList;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_accessoryiAPIntefaceTrafficTimer) accessoryiAPIntefaceTrafficTimer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (TS,R,N,V_vid) vid;
@property (TS,R,N,V_pid) pid;
@property (T@"NSDictionary",R,N,V_ioregProperties) ioregProperties;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T^{IONotificationPort=},N,V_appleUSBHostBillboardDeviceNotify) appleUSBHostBillboardDeviceNotify;
@property (TI,N,V_billboardAddedIterator) billboardAddedIterator;
@property (TI,N,V_billboardRemovedIterator) billboardRemovedIterator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessoryUSBBillboardDeviceListenerQueue) accessoryUSBBillboardDeviceListenerQueue;
@property (TI,N,V_accessoryUSBBillboardDeviceVIDPID) accessoryUSBBillboardDeviceVIDPID;
@property (TB,N,V_started) started;
@property (T@"NSMutableSet",&,N,V_accessoryUSBBillboardDeviceRegistryIDs) accessoryUSBBillboardDeviceRegistryIDs;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_accessoryUSBBillboardDeviceListenerQueue) accessoryUSBBillboardDeviceListenerQueue;
@property (TQ,R,N,V_registryEntryID) registryEntryID;
@property (TI,R,N,V_locationID) locationID;
@property (TQ,R,N,V_parentDeviceRegistryEntryID) parentDeviceRegistryEntryID;
@property (T@"NSDictionary",R,N,V_ioregProperties) ioregProperties;
@property (T@?,C,N,V_dataInHandler) dataInHandler;
@property (T@"AccessoryEAInterface",W,N,V_eaInterface) eaInterface;
@property (Ti,V_usbError) usbError;
@property (T*,R,N,V_readPtr) readPtr;
@property (T*,R,N,V_writePtr) writePtr;
@property (TQ,R,N,V_writeAttempts) writeAttempts;
@property (TQ,R,N) dataLength;
@property (TQ,R,N) writeSpaceRemaining;
@property (T@"AccessoryIAPInterface",W,N,V_parentiAPInterface) parentiAPInterface;
```

## Strings (501)

```
EA Native USB:  created USB interface from USBID 0x%llX
%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, override managerParent, newProperties = %@
IOUSBDevice Busy: %d
EA Native USB: read bytes from app, TOO Many Bytes!!! numberOfBytesRead %zd vs %lu
Setting bulk in reads to _dataBufferInLen = %zu
%s: IORegistryEntryGetName failed: %08x
USB Pipe stalled, clear and retry!
openCDCInterface kIOSerialMemoryRxBuf kr = 0x%X
openCDCInterface kIOSerialMemoryTxBuf kr = 0x%X
openCDCInterface IOConnectCallMethod kr = 0x%X
Registered for USB Host notifications
Setting USBHost HID interface: %d with HIDFunctionType: %d
Shutting down session for NativeEA protocol %@
EA Native USB: Couldn't GetPipeProperties on endpoint=%d, ioreturn 0x%x
OpenSocket From Accessory To App Native EA USB Session Notification, userInfo %@
Error getting usb device ID: %u
Unable to perform asynchronous interrupt read (%08x)
Created first EA Native Session, post notification
Failed to GetMatchingNotification, vidpid = 0x%X (0x%x,0x%x), vs 0X%X, matchingDictionary %@
Failed to AddMatchingNotification for Termination, ret 0x%x, vidpid = 0x%X (0x%x,0x%x), vs 0x%X
%s: service %d, registryID 0x%llx, vidpid 0x%X, Not in registryID list!
IORegistryEntryCreateCFProperties failed: %08x
USBInterfaceClose returned: %08x
Asynchronous event source added to run loop
No more EA Native Sessions, post notification
%s: vidpid 0x%X, start listener, %@
interfacePropertiesArray %@...
Shutting down session for USB CDC protocol %@
closeCDCInterface kIOSerialMemoryTxBuf kr = 0x%X
_handleReadDataCallback
POLLHUP
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
EA Native USB:  read %zd bytes from app
%s: vid/pid 0x%X/0x%X, registryID 0x%llx, groupidentifer %@
%s: Terminated BillboardDevice service with service %d
accInfoDictionary = %@
Endpoint SEND
failed to create async port 0x%08x
notificationPort = %p
Read %u bytes from interrupt in endpoint
Found interfaceNameString %@
%s: vidpid 0x%X, Failed to create device for registryID 0x%llx
Wait for iAP timer fired!
%s:%d connectionUUID %@, iapInterface %@, timeSinceCreationMs %llu
IOService Added Callback!
hard-code dataBufferInLen to 1024, change to calculate similarly to old project
Unable to get parent USB device ID
Error from async bulk read (%08x)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
%s: vidpid 0x%X, stop listener, %@
Registry entry ID: %llu 0x%llX
Closing EA USB CDC Session
Failed to create CDC interface
%s:%d Looking for match for %s in plane %s
%s: service %d (0x%x), vidpid 0x%X
EA Native USB: error releasing plugin interface
receivedData %@
Already started detecting billboard device, vidpid = 0x%X (0x%x,0x%x), vs 0x%X
Start configuring IOKit
txBuf[arena->txqoffset + ((pi++) & mask)] = 0x%X, dataBuf[%d] = 0x%X
%s:%d registryEntryID %llu, vid / pid = 0x%x / 0x%x, iapInterface %@
Trigger start of reading on dispatch_queue
Read %u bytes from bulk endpoint
EA Native USB:  wrote 0 bytes to app
EA Native USB: writing %zd bytes to app
%s: vidpid 0x%X, listener already started, %@
%s: vidpid 0x%X, Failed to create listener!!!
%s:%d trafficWaitList %@
unlockOtherInterfaces nativeEAProtocolString '%@', vid / pid = (0x%x / 0x%x), useEAService %d, protocol %{coreacc:ACCEndpoint_Protocol_t}d, transportType %{coreacc:ACCEndpoint_TransportType_t}d
Error getting kUSBIn kUSBBulk pipe properties (%08x)
Bulk out pipe: %d maxPacketSize: %d, Bulk in pipe: %d, maxPacketSize: %d, Interrupt in pipe: %d, maxPacketSize: %d
EA Native USB: Couldn't set socket recv buffer size
%s: error calling ControlRequest on interface, 0x%x
Opening EA USB Session Notification for endpoint %@
%s: service %d, registryID 0x%llx, vidpid 0x%X, Already in registryID list!
Unable to perform asynchronous bulk read (%08x)
EA Native USB: Couldn't GetNumEndpoints: 0x%x
%s: service %d (0x%x), registryID 0x%llx, vidpid 0x%X
%s: vidpid 0x%X, Already seen device for registryID 0x%llx
%s: EXIT listener(0x%X) = %@
OpenSocket From App To Accessory Native EA USB Session Notification, userInfo %@
VIDPIDServiceAdded Callback!
Setting NCM interface number to %u...
Post notification %s with state 1!
%s:%d received data for %@ - %@, timeSinceCreation %llu, vid / pid = 0x%x / 0x%x, trafficWaitList %@
EA Native USB:  FAILED TO CREATE USB INTERFACE
%s: vidpid 0x%X, remove listener, %@
Unlocking USB interfaces for connection %@...
configureIOKitVIDPID: IOServiceMatching() failed
_parentDeviceRegistryEntryID = 0x%llX
EA Native USB: send %lu bytes to dataInHandler
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Closing EA USB Session Notification for endpoint %@
Wrote %lu bytes to USB!
no bytes read!
%s:%d interface %d, stringIndex %d, pData[end] %p [%02x %02x], Adjust wLenDone %d -> %d
%s:%d service %d, aidInfo %@
VIDPIDServiceRemoved Callback!
EA Native USB: error creating interface iterator
Looking for Native USB EA interfaces with parent registry ID 0x%llX
Opening EA USB CDC Session
Failed to get childServiceProperties error: %08x
io_service_t: %u
Received incoming data! %@, %lu bytes
Unable to create iapInterface, destroying USB Host connection
CDC Data to write = %@
No iAP traffic for %llu msec!!!
closeCDCInterface kIOSerialMemoryArena kr = 0x%X
%s: vidpid 0x%X, add listener, %@
InterruptReadCompletion: result=%d numBytesRead=%u, counts %d : %d
writeData kr = 0x%X
%s: listener(0x%X) = %@
EAInterface: endpointUUID %@, received %lu bytes, %@
Native EA endpoint protocols found: %@
%s: error releasing plugin interface
%s: service %d, registryID 0x%llx, 0x%X
Stopped USB Host transport plugin!
GetPipeProperties failed with error: %08x for currentPipeRef: %d
%s: interface %d, stringIndex %d, name '%@'
%s: service %d, registryID 0x%llx, vidpid 0x%X
%s:%d can't create socket
serviceProperties: %@
Interface class %d, subclass %d
Unable to clear USB pipe stall! (%08x)
unlockOtherInterfaces succeeded? %@. Ignoring result anyways
Configuring IOKit for special-case vid pid
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Unable to find bulk out endpoint!
Error setting USB Host interface properties: 0x%x
%s: Connected BillboardDevice service with service %d
%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, _mb %d, _uart %d, _bd %d
Error, USB Host interface not found!
Unable to queue asynchronous bulk read (%08x)
EA Native USB: error releasing USB Interface
_attachiAPInterfaceUSBDevices: IOServiceMatching() failed
%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, override transportType %{coreacc:ACCEndpoint_TransportType_t}d -> %{coreacc:ACCEndpoint_TransportType_t}d
matching dictionary for vid pid is %@
Error getting kUSBOut kUSBBulk pipe properties (%08x)
Casting to IOUSBInterfaceInterface400
%s: service %d, registryID 0x%llx, vidpid 0x%X vs 0x%X
%s:%d add to trafficWaitList for %@ - %@, vid / pid = 0x%x / 0x%x, trafficWaitList %@
%s: Registry entry name: '%s'
Unable to open interface (%08x)
Set property for interface number %u: %@\ninterfacePropertiesArray: %@
EA Native USB: dataInHandler %p -> %p, vidpid 0x%x
Could not create parentPropertyDictionary, vidpid = 0x%X (0x%x,0x%x), vs 0x%X
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
findParentOfClass returned IO_OBJECT_NULL
Unable to perform bulk write (%08x)
openCDCInterface kIOSerialMemoryArena kr = 0x%X
%s: interface %d, device %d, out provided %d
%s:%d service %d, name '%s', digitalID %@
Creating EA Native USB Session
Created %d log object(s)!
Error from async interrupt read (%08x)
Configuring IOKit for host mode iAP.
Unable to create cdc Interface, destroying USB Host connection
Could not create matchingDictionary, vidpid = 0x%X (0x%x,0x%x), vs 0x%X
_ioregProperties = %@
_cdcDataService = %u, cdcService = %u
Set USB Host interface properties:\n%@
childServiceProperties = %@
openCDCInterface IOServiceOpen kr = 0x%X
_asyncReadCallback %p %x %llx %llx\n
%s: vidpid = 0x%X (0x%x,0x%x), vs 0x%X, matchingDictionary = %@
EA Native USB: failed to close USB Interface
Failed to register for %s notification!
%s:%d Found match for %s!
InterruptReadCompletion: mismatched interrupt and read? counts %d : %d   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
endpointUUID: %@
EA Native USB: Couldn't set socket to non-blocking mode
closeCDCInterface kIOSerialMemoryRxBuf kr = 0x%X
_poll kr = 0x%X
Found matching service!
Registry entry name: %s
EA Native USB:  read 0 bytes from app
EA Native USB: error releasing device interface
Could not create parentMatchingDictionary, vidpid = 0x%X (0x%x,0x%x), vs 0x%X
IORegistryEntryGetName failed: %08x
%s: vidpid 0x%X, aidInfo %@
Unable to get number of endpoints (%08x)
%s: Empty interfaceNameString
Failed to create os_log_t object %s: %s!
%s: vidpid 0x%X, Failed to find device for registryID 0x%llx
%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, override adapterVID/PID, newProperties = %@
Error getting USB Host interface: 0x%x
Make sure you have called init_logging_signposts() / init_logging()!\n module %d, gLogSignpostObjects: %p, gNumLogSignpostObjects: %d
Found IOSerialStreamSync
%s: vidpid 0x%X, listener already stopped, %@
%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, _mb %x, _uart %x, _bd %x
EA Native USB:  about to _createInterfaceFromUSBID from USBID 0x%llX
_cdcDataService = %d
%lu more pending iAPInterfaceTrafficWait!!!
%s:%d service %d, mikeyBusInfo %@
ReadCompletion: result=%d numBytesRead=%u, counts %d : %d
interruptInPipeRef = %d, dataBufferInLen = %s, numBytesRead = %d
EA Native USB: failed to open USB Interface: 0x%x
Post initial notification %s with state 0!
EA Native USB: Couldn't create event source for USB Interface: 0x%x
%s handling Received incoming data! %@, %lu bytes
_cancelThread: _usbInterface %p, _listenSockRls %p, _listenSockRef %p, _sockRls %p, _sockRef %@
POLLIN
Starting USB Host transport plugin...
EA sessionUUID is %@
Failed to get serviceProperties error: %08x
openCDCInterface IOConnectCallMethod 1 kr = 0x%X
Couldn't find parent matching class: %s
%s: service(%d) parent(%d) not available. (%d)
InterruptReadCompletion: queue read for interruptInPipe
EA Native USB: failed to release USB Interface
Could not create notification port
%s:%d parent %d after Looking for match for %s in plane %s
%s: vid/pid 0x%X/0x%X, registryID 0x%llx, groupidentifer %@, pAccErrorNotification %@
found USB pipe successfully for direction %d and type %d
Couldn’t create a device interface for the interface (%08x)
Unable to find bulk in endpoint!
Found interrupt in endpoint!
EA Native USB: error releasing USB Device
Created log object %s: %s
EA Native USB: Couldn't set socket send buffer size
Error getting interrupt pipe properties (%08x), but ignoring
No USB Host Data In Handler, numBytesRead: %d!
Endpoint RECV
%s: Found parent (%d) of iAP Interface (%d)
EA Native USB: read bytes from app, No Write Buffer available!!!
EA Native USB: failed to set alt USB Interface: 0x%x
Failed startDetectUSBBillboardDevice, cleanup, vidpid = 0x%X
%s: service %d, vidpid 0x%X
%s:%d service %d, name '%s', regEntryID %llu, vid / pid = %@ / %@ (0x%x / 0x%x), serviceProperties: %@
IOService Removed Callback!
Unable to retrieve asynchronous port
%s:%d can't listen to socket
Post notification %s with state 0!
%s: vidpid = 0x%X (0x%x,0x%x), vs 0x%X
%s: service(%d) parent(%d - %@) vid/pid(%@/%@) vidpid 0X%X
%s: vidpid 0x%X, Failed to find listener!!!
IORegistryEntryGetRegistryEntryID failed: %08x
Send outgoing data! %@, %lu bytes
%s: service %d, skipPipeSetup %d
Unable to create a plug-in (%08x)
%s:%d can't bind to ea address
EA Native USB: failed to set alt USB Interface
openCDCInterface IOConnectCallMethod 2 kr = 0x%X
PlatformIDOverride
Authenticated
SysdiagnoseOnInductiveCTAFailure
\"
DisableAACPAuth
IOServiceTerminate
DisableMFi4CertSupport
PretendNoDeviceIdentityCerts
RejectionOfMultipleLocation
bInterfaceProtocol
ACCTransportIOAccessory_USBHostPluginArrivedNotification
%s::%u %x
BluetoothAddress
WaitForiAPTrafficDelayMS
DeviceSupports9Pin
Charging Not Supported
Accessory Connected
AuthTTRForAllTransports
IOUSBInterface
BLEPairingIgnoreZeroEarlyInfo
AID Info
iPad13,20
IdentityCertUseTime
IgnoreAuthReset
MPPAuthPreferredSlot
USBHiAPEnable
Connection
InterfaceProperties
IOService
USB Serial Number
must call initWithConnectionID:protocolID:sessionID:
GetNumEndpoints failed 0x%08X (%u)
ShowHiddenAccessories
BLEPairingDontEarlyInfoAsDeviceUID
EnableManager2ForTransport
-[AccessoryIAPInterface dismissNotSupportNotification]
There are known compatibility issues with the 'serial' boot-arg and Smart Connector accessories, even for those not using HSAID. Please disable the 'serial' boot-arg when using Smart Connector accessories.
AllowACCAuthProtocolOnAllTransport
AuthenticationOverride
com.apple.accessories.signposts
iap-interface-registry
-[AccessoryTransportPluginUSBHost serviceAdded:]
-[AccessoryIAPInterface initWithInterface:vid:pid:aidInfo:andDataInHandler:]
<USBInfo: %p, regEntryID: %llu>
%s/ea.%lu
D6/BMDrlb8V3WSiqL8gL+w
AccessoryUSBCDCInterface
IdentityCertUseIndex
DisableACCAuthProtocolOnInductive
IgnoreAccInfoUpdateRelaySupport
Transport
PretendNFCAuthFailed
MPPAuthGetLeafCertFirst
BLEPairingConfigRequestDelayMs
MFi4SigmaIRequired
-[AccessoryUSBBillboardDevice presentNotSupportNotification]
-[AccessoryUSBBillboardDeviceManager AppleUSBHostBillboardDeviceServiceTerminated:vidpid:]
bInterfaceClass
Write timedout
IdentityCertRefreshInterval
v8@?0
UserAssignedDeviceName
Watch
-[AccessoryUSBBillboardDeviceListener startDetectUSBBillboardDevice]
Digital ID
iPad13,19
MFi4ECDSAOnly
MPPAuthChallengeFirst
TestCreateBLEPairingOnInductive
PacketLoggingPlainTextOnly
DeviceDescription
AllowNFCColorOverride
ACCAuthProtocolAllowMutualAuth
billboard-registry
General
UseCertDataPropertyForAuth
DisableWirelessCTA
+[AccessoryUSBBillboardDevice parentServiceVidPid:]
__AppleUSBHostBillboardDeviceTerminated
iFPGA
ACCAuthProtocolRoleSupport
com.medtronic.cdc.protocol
KnownAccessories
Use +[%@ %@] instead of -%@.
NFCColorOverride
__AppleUSBHostBillboardDeviceAdded
B24@?0@\"AccessoryUSBCDCInterface\"8@\"NSData\"16
DisableIAPHVCFixForAuth
IOAccessoryManager
SkipGaugeSignatureCheck
PretendBatteryLevel
-[AccessoryUSBBillboardDeviceManager AppleUSBHostBillboardDeviceServiceArrived:vidpid:]
ACCTransportIOAccessory_IOAccessoryManagerArrivedNotification
PretendAccessoryType
TransportSignpost
SUCCESS
iPad13,18
EnableTrustDialog
DisableAuthTimeoutTTRForXR
USBHostTransportPluginConnectionsLock
IOServicePublish
CarPlay
NFCAnalyticsDate
PretendNoNFCResponse
wapi
!
iPad15,8
IOSerialStreamSync
DeviceClass
%@ endpointUUID: %@
DisableCertVerification
InductiveAuthPretendMatchRxID
ForceAccInfoUpdateRelaySupport
OverrideMPPAuthSupported
%s-%x
Couldn’t release raw device object: %08x\n
Dismiss
SysdiagnoseInsteadOfAuthTTR
EnableACCAuthProtocolOnNFC
SkipNFCAuth
-[AccessoryUSBBillboardDeviceListener AppleUSBHostBillboardDeviceServiceArrived:]
-[AccessoryUSBBillboardDeviceManager stopDetectUSBBillboardDeviceWithVID:PID:]
1
DeviceSupportsUSBTypeC
ForceAuthTimeout
NFCSecondaryColorOverride
BLEPairingAuthTimeoutValueS
USBHostTransportPluginNativeUSBEndpointsLock
IOUSBHostDevice
B24@?0@\"AccessoryIAPInterface\"8@\"NSData\"16
-[AccessoryIAPInterface presentNotSupportNotification]
iPad
usbUtil_copyInterfaceAndNameString
ACCAuthProtocolPretendAuth
DisableNFCAuthTimer
0x%x,0x%x
RegionCode
DeviceIdentityPreArmDateOverride
DisableCertSupport
ERROR
USB Product Name
InternalBuild
i
com.apple.iapd
BypassTrustDialog
DisableSNOnly
GenericMFiIgnoreCertCaps
-[AccessoryTransportPluginUSBHost startPlugin]_block_invoke
DisableInductiveAuthTTR
ProductVersion
com.apple.CoreAccessories.PreferencesDidChangeNotification
AppleTV
PowerSourceUpdateBehavior
usbUtil_findParentOfClass
IgnoreAACPAuthStatus
OverrideCanReceiveInductivePowerOID
%x
USB Vendor Name
UARPActivityTimerS
GetPipeProperties failed with status 0x%08X (%u)
must call initWithInterface:protocol:endpointUUID:andDataInHandler:
IgnoreIsOnAC
ForceT56RelaySupport
-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke
ReleaseType
AuthCPStartDelayMs
ACCAuthProtocolMaxMessageSize
MFi4AuthTimeoutValueS
LiveVoicemailFakeRinging
AppleUSBHostBillboardDevice
idProduct
2
PearlIDCapability
EnableWrongOrientationMessage
IOUSBDeviceController
TreatAuthCPDEVNAsV3
KeepAACPAuthData
IOUSBHostInterface
DisableT56Support
NetworkInterfaceFlags
Unlock %@ to use accessories
idVendor
Endpoint
Charging with this accessory is not supported by Apple Device.
DisablePowerUpdateForCurrentDraw
ForceMFi4AuthOverNFC
MFi4RelayReadRetryDelayMs
-[iAP2EASession _createListenSocket]
-[AccessoryEAInterface _readSessionDataFromUSB]
EnableAuthTimeoutTTR
DisableAuthFailureTTRForXR
EnableDEVNCertSupport
-[AccessoryUSBBillboardDevice dismissNotSupportNotification]
USB Host Transport PlugIn
USBHostTransportPluginActiveEAInterfacesLock
AudioAccessory
com.apple.accessories.ea.native.sessionStatusChanged
ForceAuthFail
BLEPairingDisableOOBPPlusFlow
ChargingPowerOverride
IOParentMatch
DeviceSupportsApplePencil
DisableAMSHookUp
IOPropertyMatch
-[AccessoryUSBBillboardDeviceListener AppleUSBHostBillboardDeviceServiceTerminated:]
-[AccessoryUSBBillboardDeviceManager startDetectUSBBillboardDeviceWithVID:PID:]
IOPort
B24@?0@\"AccessoryEAInterface\"8@\"NSData\"16
ProductType
com.apple.accessoryd
PretendWirelessCTAMatch
com.apple.iapd.PreferencesDidChangeNotification
IdentityCertRefreshState
IAPSession
BluetoothAddressData
This accessory is not supported by this device.
Disable1WayNFCForInductive
Unknown
Beta
InterfaceRole
%@_%@
EnableChinaInductiveTx
IOProviderClass
locationID
com.apple.accessories.transport-plugins
MaxOutboundiAP2PacketSize
com.apple.CoreAccessories
Accessory Not Supported
MikeyBus Info
-[AccessoryIAPInterface configureInterface:skipPipeSetup:]
IAPHIDAccessoryCategoryKey
iPod
Serial Boot-Arg Detected
DontSkipInductiveAuthOnCTA
no
iPhone
iPad13,21
ChargingPowerBehavior
In Close, ClearPipeStallBothEnds for pipe = %d (direction = %u) failed 0x%08X (%u)
IgnorePowerSourceUpdateForAvailableCurrent
v48@?0@\"NSString\"8@\"NSString\"16@24@32@\"NSString\"40
Description
iPad15,7
PretendNFCAuthTimeout
serialNumber
yes
EnableIndonesiaInductiveTx
IdentityCertIsClassD
com.apple.coreaccessories.USBBillboardListener
bInterfaceSubClass
IOUSBDevice
<Undefined>
AllowMFi4DevCertsOnProdDevice
MFi4ECDSADisallow
IOServiceFirstMatch
MPPAuthEnablePretendAuth
com.apple.logging
com.apple.accessoryd.usbhost.notificationQueue
```
