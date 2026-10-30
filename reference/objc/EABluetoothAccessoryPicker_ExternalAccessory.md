# `EABluetoothAccessoryPicker`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BTDevicePickerDelegate`
- 2 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BTDevicePicker" _picker;
@"<EABluetoothAccessoryPickerDelegate>" _delegate;
```

## Properties

```
@property (T@"<EABluetoothAccessoryPickerDelegate>",N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EABluetoothAccessoryPicker wakeSelectedBluetoothAccessories:];
```

## Instance methods

```
-[EABluetoothAccessoryPicker dealloc];
-[EABluetoothAccessoryPicker setDelegate:];
-[EABluetoothAccessoryPicker delegate];
-[EABluetoothAccessoryPicker show];
-[EABluetoothAccessoryPicker initWithPredicate:];
-[EABluetoothAccessoryPicker devicePicker:didDismissWithResult:deviceAddress:];
-[EABluetoothAccessoryPicker dismissPicker];
```
