# `ASAccessoryNameEditingController`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `UITextFieldDelegate`
- 4 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"DASession" _session;
@"DADevice" _currentDevice;
@"NSString" _deviceName;
B _keyboardShownOnce;
```

## Properties

```
@property (TB,N,V_keyboardShownOnce) keyboardShownOnce;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ASAccessoryNameEditingController tableView:cellForRowAtIndexPath:];
-[ASAccessoryNameEditingController suspend];
-[ASAccessoryNameEditingController init];
-[ASAccessoryNameEditingController viewWillDisappear:];
-[ASAccessoryNameEditingController textDidChange:];
-[ASAccessoryNameEditingController dealloc];
-[ASAccessoryNameEditingController viewDidLoad];
-[ASAccessoryNameEditingController textFieldShouldReturn:];
-[ASAccessoryNameEditingController keyboardWillShow:];
-[ASAccessoryNameEditingController specifiers];
-[ASAccessoryNameEditingController shouldSelectResponderOnAppearance];
-[ASAccessoryNameEditingController getDeviceName:];
-[ASAccessoryNameEditingController keyboardShownOnce];
-[ASAccessoryNameEditingController saveEditedName:specifier:];
-[ASAccessoryNameEditingController setKeyboardShownOnce:];
```
