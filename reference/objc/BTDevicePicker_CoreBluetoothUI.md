# `BTDevicePicker`

- Image: [`/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI`](../userland/System__Library__PrivateFrameworks__CoreBluetoothUI.framework__CoreBluetoothUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BTDevicePickerRemoteViewControllerHost`
- 8 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIWindow_Custom" _alertWindow;
@"NSString" _title;
I _service;
@"NSPredicate" _predicate;
@"<BTDevicePickerDelegate>" _delegate;
@"NSExtension" _extension;
@"<NSCopying>" _extensionRequestIdentifier;
@"BTDevicePickerRemoteViewController" _devicePickerRemoteViewController;
```

## Properties

```
@property (T@"NSExtension",&,N,V_extension) extension;
@property (T@"<NSCopying>",C,N,V_extensionRequestIdentifier) extensionRequestIdentifier;
@property (T@"BTDevicePickerRemoteViewController",&,N,V_devicePickerRemoteViewController) devicePickerRemoteViewController;
@property (T@"<BTDevicePickerDelegate>",N,V_delegate) delegate;
```

## Instance methods

```
-[BTDevicePicker dismissAnimated:];
-[BTDevicePicker applicationWillResignActive:];
-[BTDevicePicker dealloc];
-[BTDevicePicker setDelegate:];
-[BTDevicePicker delegate];
-[BTDevicePicker show];
-[BTDevicePicker extension];
-[BTDevicePicker setExtension:];
-[BTDevicePicker extensionRequestIdentifier];
-[BTDevicePicker setExtensionRequestIdentifier:];
-[BTDevicePicker initWithTitle:service:discoveryNameFilter:];
-[BTDevicePicker discoveredDevice:deviceAddress:];
-[BTDevicePicker createAlertWindowForRootViewController:];
-[BTDevicePicker devicePickerRemoteViewController];
-[BTDevicePicker didDismissWithResult:deviceAddress:];
-[BTDevicePicker setDevicePickerRemoteViewController:];
```
