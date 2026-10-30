# `ALActivitySettingsDetailExtension`

- Image: [`/System/Library/PrivateFrameworks/AccessoryLiveActivitiesUI.framework/AccessoryLiveActivitiesUI`](../userland/System__Library__PrivateFrameworks__AccessoryLiveActivitiesUI.framework__AccessoryLiveActivitiesUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"AccessorySettingsDataProvider" _dataProvider;
B _forwardingEnabled;
@"NSString" _bundleIdentifier;
@? _reloadBlock;
@"NSArray" _devices;
```

## Properties

```
@property (T@"NSArray",&,N,V_devices) devices;
```

## Instance methods

```
-[ALActivitySettingsDetailExtension setDevices:];
-[ALActivitySettingsDetailExtension devices];
-[ALActivitySettingsDetailExtension initWithBundleIdentifier:];
-[ALActivitySettingsDetailExtension setReloadBlock:];
-[ALActivitySettingsDetailExtension _loadDevices];
-[ALActivitySettingsDetailExtension forwardingSpecifiers];
-[ALActivitySettingsDetailExtension isDeviceEnabled:];
-[ALActivitySettingsDetailExtension setDeviceEnabled:forSpecifier:];
```
