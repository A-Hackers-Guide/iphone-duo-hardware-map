# `TPSCloudCallingDeviceListController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSCloudCallingListController`
- Protocols: `TPSCloudCallingDeviceControllerDelegate`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"PSSpecifier" _devicesGroupSpecifier;
@"PSSpecifier" _mainGroupSpecifier;
@"PSSpecifier" _mainSwitchSpecifier;
@"TPSCloudCallingDeviceController" _deviceController;
@"NSArray" _deviceSwitchSpecifiers;
```

## Properties

```
@property (T@"NSArray",C,N,V_deviceSwitchSpecifiers) deviceSwitchSpecifiers;
@property (T@"TPSCloudCallingDeviceController",R,N,V_deviceController) deviceController;
@property (T@"PSSpecifier",R,N,V_devicesGroupSpecifier) devicesGroupSpecifier;
@property (T@"PSSpecifier",R,N,V_mainGroupSpecifier) mainGroupSpecifier;
@property (T@"PSSpecifier",R,N,V_mainSwitchSpecifier) mainSwitchSpecifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCloudCallingDeviceListController deviceController];
-[TPSCloudCallingDeviceListController init];
-[TPSCloudCallingDeviceListController specifiers];
-[TPSCloudCallingDeviceListController isMainSwitchOn:];
-[TPSCloudCallingDeviceListController cloudCallingDeviceController:didChangeDevices:];
-[TPSCloudCallingDeviceListController deviceSwitchSpecifiers];
-[TPSCloudCallingDeviceListController devicesGroupSpecifier];
-[TPSCloudCallingDeviceListController isDeviceSwitchOn:];
-[TPSCloudCallingDeviceListController mainGroupSpecifier];
-[TPSCloudCallingDeviceListController mainSwitchSpecifier];
-[TPSCloudCallingDeviceListController setDeviceSwitchOn:specifier:];
-[TPSCloudCallingDeviceListController setDeviceSwitchSpecifiers:];
-[TPSCloudCallingDeviceListController setMainSwitchOn:specifier:];
```
