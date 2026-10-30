# `DSContinuityController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `UITableViewDelegate`, `DSContinuityDelegate`, `DSDeviceListDelegate`, `DSController`
- 4 instance variables, 8 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"NSMutableArray" _selectedDevices;
@"NSMutableArray" _continuityDevices;
@"DSContinuityStore" _continuityStore;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_selectedDevices) selectedDevices;
@property (T@"NSMutableArray",&,N,V_continuityDevices) continuityDevices;
@property (T@"DSContinuityStore",&,N,V_continuityStore) continuityStore;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSContinuityController clearRemoteWidgetBlocklist];
```

## Instance methods

```
-[DSContinuityController tableView:numberOfRowsInSection:];
-[DSContinuityController tableView:accessoryButtonTappedForRowWithIndexPath:];
-[DSContinuityController tableView:cellForRowAtIndexPath:];
-[DSContinuityController init];
-[DSContinuityController viewDidLoad];
-[DSContinuityController viewWillAppear:];
-[DSContinuityController setDelegate:];
-[DSContinuityController tableView:didSelectRowAtIndexPath:];
-[DSContinuityController delegate];
-[DSContinuityController _updateButtons];
-[DSContinuityController tableView:didDeselectRowAtIndexPath:];
-[DSContinuityController selectedDevices];
-[DSContinuityController setSelectedDevices:];
-[DSContinuityController continuityStore];
-[DSContinuityController allComputerNames];
-[DSContinuityController computerNameWithUUID:];
-[DSContinuityController continuityDevices];
-[DSContinuityController dateDescription:];
-[DSContinuityController getDevicesWithCompletion:];
-[DSContinuityController presentLearnMore];
-[DSContinuityController presentRemoveAllDevicesAlert];
-[DSContinuityController presentRemoveSelectedDevicesAlert];
-[DSContinuityController presentUnpairErrorAlert:];
-[DSContinuityController remoteDeviceListModified:];
-[DSContinuityController removeAllPairedDevicesAndPushNextPane];
-[DSContinuityController removeDetailViewControllerFromStack];
-[DSContinuityController removeSelectedPairedDevicesAndPushNextPane];
-[DSContinuityController returnFromDetailAndRemoveDevice:];
-[DSContinuityController selectedComputerNames];
-[DSContinuityController setContinuityDevices:];
-[DSContinuityController setContinuityStore:];
-[DSContinuityController shouldShowWithCompletion:];
```
