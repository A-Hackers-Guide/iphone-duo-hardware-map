# `ASAccessoryResetWiFiViewController`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTableWelcomeController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`
- 5 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"DASession" _session;
@"NSArray" _wifiAwareDevices;
@"UIImage" _wifiIcon;
@"UIImage" _multiTechIcon;
@"OBBoldTrayButton" _confirmButton;
```

## Properties

```
@property (T@"DASession",&,N,V_session) session;
@property (T@"NSArray",&,N,V_wifiAwareDevices) wifiAwareDevices;
@property (T@"UIImage",&,N,V_wifiIcon) wifiIcon;
@property (T@"UIImage",&,N,V_multiTechIcon) multiTechIcon;
@property (T@"OBBoldTrayButton",&,N,V_confirmButton) confirmButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ASAccessoryResetWiFiViewController tableView:numberOfRowsInSection:];
-[ASAccessoryResetWiFiViewController numberOfSectionsInTableView:];
-[ASAccessoryResetWiFiViewController tableView:cellForRowAtIndexPath:];
-[ASAccessoryResetWiFiViewController setConfirmButton:];
-[ASAccessoryResetWiFiViewController viewDidLoad];
-[ASAccessoryResetWiFiViewController setSession:];
-[ASAccessoryResetWiFiViewController initWithDevices:];
-[ASAccessoryResetWiFiViewController viewDidDisappear:];
-[ASAccessoryResetWiFiViewController session];
-[ASAccessoryResetWiFiViewController didTapCancel:];
-[ASAccessoryResetWiFiViewController confirmButton];
-[ASAccessoryResetWiFiViewController didTapConfirm:];
-[ASAccessoryResetWiFiViewController handleDAEvent:];
-[ASAccessoryResetWiFiViewController imageWithTypeIdentifier:];
-[ASAccessoryResetWiFiViewController multiTechIcon];
-[ASAccessoryResetWiFiViewController setMultiTechIcon:];
-[ASAccessoryResetWiFiViewController setWifiAwareDevices:];
-[ASAccessoryResetWiFiViewController setWifiIcon:];
-[ASAccessoryResetWiFiViewController settingsIconImageDescriptor];
-[ASAccessoryResetWiFiViewController wifiAwareDevices];
-[ASAccessoryResetWiFiViewController wifiIcon];
```
