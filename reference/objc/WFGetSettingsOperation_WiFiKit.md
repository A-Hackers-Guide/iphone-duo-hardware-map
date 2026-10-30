# `WFGetSettingsOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"NSArray" _settings;
@"NSString" _ssid;
@"NSString" _interfaceName;
^{__SCPreferences=} _prefs;
@"NSOperationQueue" _keychainQueue;
```

## Properties

```
@property (T@"NSString",C,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T^{__SCPreferences=},N,V_prefs) prefs;
@property (T@"NSArray",&,N,V_settings) settings;
@property (T@"NSOperationQueue",&,N,V_keychainQueue) keychainQueue;
```

## Instance methods

```
-[WFGetSettingsOperation ssid];
-[WFGetSettingsOperation setSsid:];
-[WFGetSettingsOperation setSettings:];
-[WFGetSettingsOperation settings];
-[WFGetSettingsOperation setInterfaceName:];
-[WFGetSettingsOperation dealloc];
-[WFGetSettingsOperation start];
-[WFGetSettingsOperation interfaceName];
-[WFGetSettingsOperation setName:];
-[WFGetSettingsOperation name];
-[WFGetSettingsOperation keychainQueue];
-[WFGetSettingsOperation setKeychainQueue:];
-[WFGetSettingsOperation initWithSSID:interfaceName:];
-[WFGetSettingsOperation prefs];
-[WFGetSettingsOperation setPrefs:];
```
