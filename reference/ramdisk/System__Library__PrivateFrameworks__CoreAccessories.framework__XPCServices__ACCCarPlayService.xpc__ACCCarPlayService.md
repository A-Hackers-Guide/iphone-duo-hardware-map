# `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCCarPlayService.xpc/ACCCarPlayService`

From the upgrade restore ramdisk (141-29011-104.dmg). 120,688 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 3208)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>application-identifier</key>
	<string>com.apple.internal.CoreAccessories.ACCCarPlayService</string>
	<key>com.apple.internal.seserviced.all.endpoints.and.cas</key>
	<true/>
	<key>com.apple.private.CarPlayServices.icon-layout</key>
	<true/>
	<key>com.apple.private.carkit</key>
	<true/>
	<key>com.apple.private.carkit.carconnectiontime</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.carkit.reconnectiontime.service</string>
	</array>
</dict>
</plist>
```

## Objective-C (3 classes, 3 protocols)

Classes: `ACCCarPlay`, `ACCCarPlayService`, `ServiceDelegate`

Protocols: `ACCCarPlayServiceProtocol`, `NSObject`, `NSXPCListenerDelegate`

## Strings (186)

```
v36@0:8I16@20@?28
v48@0:8Q16Q24@32@?40
v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray\">32
Vv16@0:8
B24@0:8@\"Protocol\"16
v32@0:8@16@?24
v32@0:8@\"NSData\"16@?<v@?B>24
v32@0:8@\"NSData\"16@?<v@?Q>24
v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32
v28@0:8I16@20
B24@0:8@16
@24@0:8:16
@\"NSString\"16@0:8
v40@0:8@16Q24@?32
v40@0:8q16q24@32
v16@0:8
B16@0:8
B32@0:8@16@24
@40@0:8:16@24@32
B24@0:8#16
v36@0:8I16@\"NSDictionary\"20@?<v@?B@\"NSError\">28
v48@0:8Q16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40
@\"NSXPCConnection\"
#16@0:8
@32@0:8:16@24
@16@0:8
Q16@0:8
v40@0:8@16@24@?32
v24@0:8@16
B24@0:8:16
^{_NSZone=}16@0:8
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
HW Component Auth
-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke
/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
Failed to link CARConnectionTimeStore
Transport Client
ConnectionInfo
iAP Auth Start
iAP Auth Complete
iAP2 Endpoint Created
CRIsEnhancedIntegrationEnabledWithCertificateSerialNumber
CARConnectionEvent
/System/Library/PrivateFrameworks/CarKit.framework/CarKit
/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
com.apple.coreaccessories.ACCCarPlayService
-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke
success
CarPlay Service
v24@?0Q8@\"NSError\"16
SESEndPointFilterDigitalCarKeys
/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
iAP NCM Start
CRAllowsConnectionsForCertificateSerialNumber
CRHandleCarPlayConnectionRequest
Could not load source: %ld
iAP CarPlay Start Session Received
CRIsPairedWithCertificateSerialNumber
Bluetooth Service
iAP2 Bytes Received
General
/System/Library/Frameworks/UIKit.framework/UIKit
/System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices
com.apple.accessories.frameworks.core-accessories
v12@?0B8
CRSIconLayoutController
Connection
Transport
v16@?0Q8
v24@?0@\"NSArray\"8@\"NSError\"16
External Accessory
iAP Connection Start
CARConnection Time Store timed out!
com.apple.accessories.signposts
/System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
v8@?0
v16@?0@\"NSArray\"8
TimeSync
<Undefined>
-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke
v20@?0B8@\"NSError\"12
Endpoint
/System/Library/PrivateFrameworks/SEService.framework/SEService
Transport Plugins
App Links
v16@?0@\"NSError\"8
-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke
CARConnectionTimeStore
failed
[#ACCCarPlayService] handleCarPlayAppLinksStateChanged() timed out after %lldms!
[#ACCCarPlayService] matched keys: %@
Failed to create os_log_t object %s: %s!
call to ACCCarPlayService failed: %@
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
[#ACCCarPlayService] carPlayAppLinksStateForCertSerial() timed out after %lldms!
[#ACCCarPlayService] _CRIsEnhancedIntegrationEnabledWithCertificateSerialNumber soft link failed
[#ACCCarPlayService] CarPlay Connection Event: preparing to send event: %@, %ld, %@
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
CarPlay Connection Event: %ld, %ld, %f, %@
[#ACCCarPlayService] CRSIconLayoutControllerClass soft link failed
[#ACCCarPlayService] failed to load SESEndPointFilterDigitalCarKeys
[#ACCCarPlayService] CARConnectionTimeStore soft link failed
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
failed to call ACCCarPlayService %@
[#ACCCarPlayService] failed to call SESEndPointFilterDigitalCarKeys: %@
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
[#ACCCarPlayService] isWirelessCarPlayAllowedForCertSerial() timed out after %lldms!
[#ACCCarPlayService] carPlayStartSessionForConnectionID: startSessionProperties %@
[#ACCCarPlayService] CarPlay Connection Event: %s -- %@ at %@, error: %@
[#ACCCarPlayService] sendConnectionEvent() timed out after %lldms!
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
can't invoke remote object %@
failed to send CarPlay Connect event %@
[#ACCCarPlayService] isCarPlayPairedWithCertSerial() timed out after %lldms!
Created log object %s: %s
[#ACCCarPlayService] accessoryUUID: %@ filterMatchingDigitalCarKeys: %@
Created %d log object(s)!
%s no reply handler!
[#ACCCarPlayService] _CRIsPairedWithCertificateSerialNumber soft link failed
[#ACCCarPlayService] _CRAllowsConnectionsForCertificateSerialNumber soft link failed
T#,R
conformsToProtocol:
isWirelessCarPlayAllowedForCertSerial:withReply:
retain
retainCount
setXpcConnection:
isCarPlayPairedWithCertSerial:withReply:
class
performSelector:withObject:
self
release
carPlayStartSessionForConnectionID:properties:withReply:
filterMatchingDigitalCarKeys:forAccessory:withReply:
isMemberOfClass:
setRemoteObjectInterface:
initForSystemDaemon
setExportedInterface:
setExportedObject:
zone
sendConnectionEvent:completion:
T@\"NSString\",R,C
debugDescription
init
remoteObjectProxyWithErrorHandler:
timeIntervalSinceReferenceDate
filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:
resume
T@\"NSString\",?,R,C
_init
carPlaySendConnectionTimeEvent:connectionType:eventTime:
isEqual:
xpcConnection
_xpcConnection
serviceListener
eventWithName:type:date:payload:
interfaceWithProtocol:
isKindOfClass:
setDelegate:
isProxy
carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:
dictionaryWithObjects:forKeys:count:
.cxx_destruct
initWithServiceName:
superclass
TQ,R
autorelease
carPlayAppLinksStateForCertSerial:withReply:
carPlayIconStateForCertSerial:andAppCategories:withReply:
performSelector:
sharedManager
errorWithDomain:code:userInfo:
T@\"NSXPCConnection\",&,N,V_xpcConnection
carPlayStartSessionForConnectionID:properties:
listener:shouldAcceptNewConnection:
respondsToSelector:
exportIconStateForCertificateSerial:categories:completion:
UTF8String
description
hash
performSelector:withObject:withObject:
NSXPCListenerDelegate
NSObject
ACCCarPlayService
ACCCarPlayServiceProtocol
ACCCarPlay
ServiceDelegate
```
