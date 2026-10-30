# `ACCPlatformPluginWiFiSharing`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing`](../userland/System__Library__CoreAccessories__PlugIns__Platform__WiFiSharing.platform__WiFiSharing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCPlatformWiFiSharingProtocol`, `ACCPlatformPluginProtocol`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _hasWAPICapability;
B _isRunning;
```

## Properties

```
@property (TB,N,V_isRunning) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Instance methods

```
-[ACCPlatformPluginWiFiSharing isRunning];
-[ACCPlatformPluginWiFiSharing stopPlugin];
-[ACCPlatformPluginWiFiSharing pluginName];
-[ACCPlatformPluginWiFiSharing startPlugin];
-[ACCPlatformPluginWiFiSharing initPlugin];
-[ACCPlatformPluginWiFiSharing hasWAPICapability];
-[ACCPlatformPluginWiFiSharing setIsRunning:];
-[ACCPlatformPluginWiFiSharing copyDeviceWiFiNetworkInformation];
-[ACCPlatformPluginWiFiSharing handleAccessoryWiFiInformationForWirelessCarPlay:];
-[ACCPlatformPluginWiFiSharing isDeviceConnectedToWiFi];
```
