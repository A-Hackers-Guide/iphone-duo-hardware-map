# `SBWiFiManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSRecursiveLock" _lock;
^{__CFRunLoop=} _callbackRunLoop;
^{__WiFiManagerClient=} _manager;
^{__WiFiDeviceClient=} _device;
@"NSString" _deviceInterfaceName;
B _mainThread_devicePresent;
^{__WiFiNetwork=} _currentNetwork;
^{__WiFiNetwork=} _previousNetwork;
B _currentNetworkHasBeenSet;
B _currentNetworkIsIOSHotspot;
B _currentNetworkIsIOSHotspotHasBeenSet;
B _powered;
B _poweredHasBeenSet;
i _mainThread_signalStrengthBars;
i _mainThread_signalStrengthRSSI;
B _mainThread_signalStrengthHasBeenSet;
@"NWSystemPathMonitor" _systemPathMonitor;
@"NSObject<OS_dispatch_source>" _primaryInterfaceUpdateTimeoutSource;
^{__WiFiNetwork=} _primaryInterface;
B _primaryInterfaceHasBeenSet;
B _isPrimaryInterface;
B _isPrimaryInterfaceChanging;
```

## Instance methods

```
-[SBWiFiManager setPowered:];
-[SBWiFiManager observeValueForKeyPath:ofObject:change:context:];
-[SBWiFiManager isAssociated];
-[SBWiFiManager init];
-[SBWiFiManager _updateSignalStrength];
-[SBWiFiManager isAssociatedToIOSHotspot];
-[SBWiFiManager _linkDidChange];
-[SBWiFiManager _lock_spawnManagerCallbackThread];
-[SBWiFiManager wifiRunLoopRef];
-[SBWiFiManager _updateDevicePresence];
-[SBWiFiManager wiFiEnabled];
-[SBWiFiManager isPrimaryInterface];
-[SBWiFiManager isPowered];
-[SBWiFiManager _updateWiFiDevice];
-[SBWiFiManager _updateCurrentNetwork];
-[SBWiFiManager _updateSignalStrengthFromRawRSSI:andScaledRSSI:];
-[SBWiFiManager _lock_setWiFiDevice:];
-[SBWiFiManager currentNetworkName];
-[SBWiFiManager _runManagerCallbackThread];
-[SBWiFiManager signalStrengthRSSI];
-[SBWiFiManager _updateWiFiState];
-[SBWiFiManager signalStrengthBars];
-[SBWiFiManager _powerStateDidChange];
-[SBWiFiManager _wifiInterface];
-[SBWiFiManager setWiFiEnabled:];
-[SBWiFiManager _lock_manager];
-[SBWiFiManager _cachedIsAssociated];
-[SBWiFiManager _primaryInterfaceChanged:];
```
