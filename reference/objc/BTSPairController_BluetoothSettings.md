# `BTSPairController`

- Image: [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](../userland/System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `UITextFieldDelegate`
- 4 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"BluetoothDevice" _device;
@"NSString" _promptFormat;
B _dismissed;
@"NSString" _pin;
```

## Properties

```
@property (T@"NSString",&,N,V_pin) pin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BTSPairController tableView:cellForRowAtIndexPath:];
-[BTSPairController init];
-[BTSPairController cancelButtonClicked:];
-[BTSPairController textDidChange:];
-[BTSPairController dealloc];
-[BTSPairController viewWillAppear:];
-[BTSPairController textFieldShouldReturn:];
-[BTSPairController loadView];
-[BTSPairController keyboardWillShow:];
-[BTSPairController deviceUpdated:];
-[BTSPairController specifiers];
-[BTSPairController pin];
-[BTSPairController setPin:];
-[BTSPairController doneButtonClicked:];
-[BTSPairController emptySetter:specifier:];
-[BTSPairController updatePrompt:];
```
