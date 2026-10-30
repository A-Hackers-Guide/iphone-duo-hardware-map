# `/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 4 protocols, 39 methods, 12 properties

### Class pages

Every class and protocol, with its methods: [`ACCPlatformPluginProtocol`](../objc/ACCPlatformPluginProtocol_WiFiSharing.protocol.md), [`ACCPlatformPluginWiFiSharing`](../objc/ACCPlatformPluginWiFiSharing_WiFiSharing.md), [`ACCPlatformWiFiSharingProtocol`](../objc/ACCPlatformWiFiSharingProtocol_WiFiSharing.protocol.md), [`ACCPluginProtocol`](../objc/ACCPluginProtocol_WiFiSharing.protocol.md), [`NSObject`](../objc/NSObject_WiFiSharing.protocol.md)

### Classes

`ACCPlatformPluginWiFiSharing`

### Protocols

`ACCPlatformPluginProtocol`, `ACCPlatformWiFiSharingProtocol`, `ACCPluginProtocol`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) pluginName;
@property (TB,R,N) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,V_isRunning) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Strings (42)

```
password
Power
SSID_STR
Connection
Endpoint
WPA_IE
i
WiFiBSSID
WiFiPassphrase
WiFiChannel
RSN_IE
securityType
LegacyAccessoryExternalAccessoryConnectionID
com.apple.accessories.platform-plugins
WiFiSharing
<Undefined>
com.apple.accessories.signposts
General
yes
BSSID
WiFiStatus
WiFiSecurityType
WiFiSSID
v8@?0
Transport
wapi
no
CHANNEL
Failed to create os_log_t object %s: %s!
_hasWAPICapability = %@
Returning deviceWiFiNetworkInformation %@
accessory wifi info for CarPlay is %@
Invalid accessory security type %d
Saving dictionary %@ to carPlay for EA connectionID %lu (0x%lX)
Created log object %s: %s
Created %d log object(s)!
ERROR: either SSID is nil (it's %@), or passphrase is present but securityType is none, not setting CarPlay WiFi params
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
```
