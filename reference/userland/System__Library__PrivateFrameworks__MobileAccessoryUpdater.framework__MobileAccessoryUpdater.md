# `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`

iOS 27.2 dyld shared cache image. Version `1587.40.33.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 11 classes, 13 protocols, 236 methods, 52 properties

### Class pages

Every class and protocol, with its methods: [`AUDAccessory`](../objc/AUDAccessory_MobileAccessoryUpdater.md), [`AUDaemonProtocol`](../objc/AUDaemonProtocol_MobileAccessoryUpdater.protocol.md), [`AUNotificationRequest`](../objc/AUNotificationRequest_MobileAccessoryUpdater.md), [`AUServiceAdapter`](../objc/AUServiceAdapter_MobileAccessoryUpdater.md), [`AUServiceManager`](../objc/AUServiceManager_MobileAccessoryUpdater.md), [`AUServiceProtocol`](../objc/AUServiceProtocol_MobileAccessoryUpdater.protocol.md), [`FudConnection`](../objc/FudConnection_MobileAccessoryUpdater.protocol.md), [`FudInternalConnection`](../objc/FudInternalConnection_MobileAccessoryUpdater.md), [`FudPersonalizationObjectInfo`](../objc/FudPersonalizationObjectInfo_MobileAccessoryUpdater.md), [`FudPersonalizationPlugin`](../objc/FudPersonalizationPlugin_MobileAccessoryUpdater.protocol.md), [`FudPersonalizationRequest`](../objc/FudPersonalizationRequest_MobileAccessoryUpdater.md), [`FudPlugin`](../objc/FudPlugin_MobileAccessoryUpdater.protocol.md), [`FudPluginDelegate`](../objc/FudPluginDelegate_MobileAccessoryUpdater.protocol.md), [`FudProgressWeights`](../objc/FudProgressWeights_MobileAccessoryUpdater.md), [`FudQueryPlugin`](../objc/FudQueryPlugin_MobileAccessoryUpdater.protocol.md), [`FudXPCConnection`](../objc/FudXPCConnection_MobileAccessoryUpdater.md), [`MobileAccessoryUpdater`](../objc/MobileAccessoryUpdater_MobileAccessoryUpdater.md), [`MobileAccessoryUpdaterDelegate`](../objc/MobileAccessoryUpdaterDelegate_MobileAccessoryUpdater.protocol.md), [`NSCoding`](../objc/NSCoding_MobileAccessoryUpdater.protocol.md), [`NSCopying`](../objc/NSCopying_MobileAccessoryUpdater.protocol.md), [`NSObject`](../objc/NSObject_MobileAccessoryUpdater.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_MobileAccessoryUpdater.protocol.md), [`NSXPCListenerDelegate`](../objc/NSXPCListenerDelegate_MobileAccessoryUpdater.protocol.md), [`ServiceDelegate`](../objc/ServiceDelegate_MobileAccessoryUpdater.md)

### Classes

`AUDAccessory`, `AUNotificationRequest`, `AUServiceAdapter`, `AUServiceManager`, `FudInternalConnection`, `FudPersonalizationObjectInfo`, `FudPersonalizationRequest`, `FudProgressWeights`, `FudXPCConnection`, `MobileAccessoryUpdater`, `ServiceDelegate`

### Protocols

`AUDaemonProtocol`, `AUServiceProtocol`, `FudConnection`, `FudPersonalizationPlugin`, `FudPlugin`, `FudPluginDelegate`, `FudQueryPlugin`, `MobileAccessoryUpdaterDelegate`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSString",R,C,N,V_uid) uid;
@property (T@"NSString",&,N,V_fwVersion) fwVersion;
@property (Tq,N,V_type) type;
@property (T@"NSString",&,N,V_accessoryName) accessoryName;
@property (T@"<FudPlugin>",R,N,V_updater) updater;
@property (T@"NSXPCConnection",N,V_activeConnection) activeConnection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_objectTag) objectTag;
@property (T@"NSData",&,N,V_digest) digest;
@property (TB,N,V_trusted) trusted;
@property (TB,N,V_effectiveProductionMode) effectiveProductionMode;
@property (TB,N,V_effectiveSecurityMode) effectiveSecurityMode;
@property (T@"NSString",R,C,N,V_requestName) requestName;
@property (T@"NSString",&,N,V_requestPrefix) requestPrefix;
@property (Ti,N,V_responseFormat) responseFormat;
@property (TI,N,V_boardID) boardID;
@property (TI,N,V_chipID) chipID;
@property (TQ,N,V_ecID) ecID;
@property (T@"NSData",&,N,V_extEcID) extEcID;
@property (TB,N,V_globalSigning) globalSigning;
@property (TI,N,V_securityDomain) securityDomain;
@property (TB,N,V_productionMode) productionMode;
@property (TB,N,V_securityMode) securityMode;
@property (T@"NSData",&,N,V_nonceHash) nonceHash;
@property (TI,N,V_chipEpoch) chipEpoch;
@property (TB,N,V_enableMixMatch) enableMixMatch;
@property (T@"NSArray",&,N,V_objectList) objectList;
@property (T@"NSData",&,N,V_payload) payload;
@property (TS,N,V_responseAlignment) responseAlignment;
@property (Tf,VprepareWeight) prepareWeight;
@property (Tf,VapplyWeight) applyWeight;
@property (Tf,VfinishWeight) finishWeight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (202)

```
default
-[AUServiceAdapter prepareFirmwareWithOptions:]
requestPayload
Failed to register for BSD notifications
Delegate %@ does not conform to protocol
com.apple.MobileAccessoryUpdater.client.sessionQueue
SORRY... NO LONGER SUPPORTED\n
NULL reply from getPluginsList request
Internal connections no longer support notifications
XPC connection invalidated
-[AUServiceAdapter didFinish:info:error:]_block_invoke
requestRspAlign
Failed to create pending requests dict
No handler found for msg ID
requestExtECID
requestSecMode
Done
Caught exception while trying to archive key %s. error:%@
Releasing xpc context:%@
type
requestRspFormat
v8@?0
-[AUServiceAdapter personalizationRequest:]_block_invoke
%s(): super init error\n
Status
Prepare
Failed to create connection to fud
-[MobileAccessoryUpdater unregister]
-[AUServiceAdapter queryDeviceList:]
-[AUServiceAdapter issueNotification:]_block_invoke
requestEffectiveSecMode
Can't send message without connection
-[MobileAccessoryUpdater setLastRemoteFindDate:]
\tPayloadHeader\n\t\tTag     = %c%c%c%c\n\t\tVersion = %d.%d.%d\n\t\tFlags   = %08x\n\t\tOff     = %08x\n\t\tLen     = %d\n
Failed to copy value for entitlement %@: Error: %@
Can't create progress weights if total doesn't equal 1
requestPrefix
requestBoardID
requestProdModeSet
Can't create xpc connection without client name
Response
Error
SuperBinaryHeader\n\tVersion = %d.%d.%d\n\tHdrOff  = %08x\n\tHdrLen  = %d\n\tLength  = %d\n\tPloads  = %d\n\n
Failed to get task for audit token
-[AUServiceAdapter _init]
requestSecModeSet
Can't send a NULL message
Failed to create msg id mutex
Failed to copy block handler
AUDAccessory_UID
%s: Plugin does support personalization
requestTrusted
Invalid response operation to session request!
Failed to create session: %@
MessageID
-[AUServiceAdapter findFirmwareWithOptions:remote:]
-[AUServiceAdapter didFind:info:updateAvailable:needsDownload:error:]_block_invoke
ClientIdentifier
Failed to copy client cstring identifier
Failed to register for plugins with fud
-[MobileAccessoryUpdater bundleIdentifier]
%s: Error could not instantiate the ServiceAdapter
%s: Plugin not loaded
%s: Plugin does support queryDeviceList
-[AUServiceAdapter reportAnalytics:info:]_block_invoke
requestChipEpochSet
Find
Failed to create unarchiver object
Failed to create progress weights with input weights
-[AUServiceAdapter didBootstrap:info:error:]_block_invoke
requestNonceHash
Lost connection to fud...
Download
Can't set filter name to nil value
-[MobileAccessoryUpdater doneWithOptions:]
Accessory Attached
Can't calculate overall progress with negative step progress
requestChipID
%s: Error 'Principal class' does not conform to plugin protocol
-[AUServiceAdapter finishWithOptions:]
requestEffectiveSecModeSet
Continue
Apply
ApplyWeight
Checking isEntitled
%s: Could not report status to daemon
-[AUServiceAdapter didDownload:info:error:]_block_invoke
com.apple.MobileAccessoryUpdater.FudXPCConnection.session
Delegate does not conform require protocol MobileAccessoryUpdaterDelegate, can't initiate now!
-[MobileAccessoryUpdater clientIdentifier]
prepare:%f apply:%f finish:%f
Can't create connection without handler
-[AUServiceAdapter bootstrapWithOptions:]
%s(): requestName=nil\n
-[FudPersonalizationRequest initWithName:]
Can't send message with NULL reply handler
Can't convert XPC msg to Dictionary
requestECID
Connecting to fud...
Failed to create xpc dictionary for session
Command
%s: No longer supported
PrepareWeight
Unknown operation: %d
-[AUServiceAdapter applyFirmwareWithOptions:]
-[AUServiceAdapter personalizationResponse:response:status:]
-[FudPersonalizationObjectInfo initWithTag:]
Failed to get xpc connection from replyTo dict
Could not create a valid connection to daemon
Can't send command since filter is not set, command:%@
XPC connection interrupted
-[AUServiceAdapter deviceClassAttached:options:withReply:]
-[AUServiceAdapter didPrepare:info:error:]_block_invoke
requestChipEpoch
Dumping xpc object: %s
Session
%s: Denying incoming connection, connection status=%d
-[AUServiceAdapter didApply:info:error:]_block_invoke
%s(): objectTag=nil\n
requestObjectTag
requestGlobalSign
requestSecDomain
-[MobileAccessoryUpdater performNextStepWithOptions:]
Internal client messaging no longer supported
requestTrustedSet
No operation status in response
Failed to init super class
-[MobileAccessoryUpdater performStep:withOptions:]
-[MobileAccessoryUpdater activeFilter]
com.apple.private.accessoryupdater.client
v16@?0@\"NSError\"8
com.apple.MobileAccessoryUpdater
Can't perform operation without valid connection to fud
NULL reply from session request
Dropping message, no longer handling internal messages
Can't create xpc connection without reply handler
Finish
com.apple.MobileAccessoryUpdater.client.pid.%d
com.apple.MobileAccessoryUpdater.fud
Can't send NULL xpc message
accessoryName
requestEffectiveProdMode
Failed to convert client identifier to cstring
com.apple.MobileAccessoryUpdater.client.callbackQueue
Can't register for plugin events without delegate
FinishWeight
-[ServiceDelegate listener:shouldAcceptNewConnection:]
requestEnableMixMatch
Failed to get plugin list
Plugin list = %@
Checking for entitlement %@
Got SecTaskRef task, copying entitlementValue
-[AUServiceAdapter progress:]_block_invoke
requestName
requestProdMode
requestObjects
Registering for BSD notifications with identifier: %@
Options
-[MobileAccessoryUpdater queryNextStep:]
Caught exception while trying to unarchive key %s. error:%@
Bootstrap
PluginIdentifier
Can't send message to NULL connection
This is not an operation that supports weighted progress.
com.apple.mobileaccessoryupdater
-[AUServiceAdapter downloadFirmwareWithOptions:]
com.apple.MobileAccessoryUpdater.FudXPCConnection.connection
Can't create connection after it was explicitly stopped
AU Notification
Can't register for plugin with nil identifier
FUD replied error %@
FilterIdentifier
Can't create connection without handler queue
NextStep
-[AUServiceAdapter accessoryDisconnected:]_block_invoke
requestEffectiveProdModeSet
Failed to create queue for xpc connection
Failed to get c string identifier
Can't create session with out c identifier
LOADING PLUGIN: _bundleIdentifier = %@, _clientIdentifier = %@ 
Can't send NULL message
Can't create xpc connection without reply queue
PluginsList
Can't reply to NULL message
isEntitled = %d
Failed to convert client identifier to string
%s: %s\n
AUDAccessory_FWVersion
End
requestDigest
Fuds requesting a reconnection, initiating session...
v12@?0i8
Invalid error class %@
ClientRegistrationName
Accessory Detached
Client messaging no longer supported
v16@?0@\"NSObject<OS_xpc_object>\"8
Can't create connection without client identifier
Can't handle NULL msg in notification
failed to set temporary directory suffix: %d
failed to initialize temporary directory: %d
%s
```
