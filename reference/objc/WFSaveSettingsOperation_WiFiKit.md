# `WFSaveSettingsOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- 7 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _currentNetwork;
@"NSString" _name;
@"NSString" _interfaceName;
@"NSString" _ssid;
^{__SCPreferences=} _prefs;
@"NSArray" _settings;
@"NSOperationQueue" _keychainQueue;
```

## Properties

```
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSString",C,N,V_ssid) ssid;
@property (T^{__SCPreferences=},N,V_prefs) prefs;
@property (T@"NSArray",&,N,V_settings) settings;
@property (T@"NSOperationQueue",&,N,V_keychainQueue) keychainQueue;
@property (TB,N,GisCurrentNetwork,V_currentNetwork) currentNetwork;
```

## Instance methods

```
-[WFSaveSettingsOperation setCurrentNetwork:];
-[WFSaveSettingsOperation ssid];
-[WFSaveSettingsOperation setSsid:];
-[WFSaveSettingsOperation setSettings:];
-[WFSaveSettingsOperation settings];
-[WFSaveSettingsOperation setInterfaceName:];
-[WFSaveSettingsOperation dealloc];
-[WFSaveSettingsOperation start];
-[WFSaveSettingsOperation interfaceName];
-[WFSaveSettingsOperation setName:];
-[WFSaveSettingsOperation name];
-[WFSaveSettingsOperation keychainQueue];
-[WFSaveSettingsOperation setKeychainQueue:];
-[WFSaveSettingsOperation _applyProxySettings:service:];
-[WFSaveSettingsOperation _createNewSetForNetworkNamed:interfaceName:];
-[WFSaveSettingsOperation _defaultSetRetained];
-[WFSaveSettingsOperation initWithSSID:interfaceName:settings:];
-[WFSaveSettingsOperation isCurrentNetwork];
-[WFSaveSettingsOperation prefs];
-[WFSaveSettingsOperation setPrefs:];
```
