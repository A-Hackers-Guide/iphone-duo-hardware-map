# `CABTMIDILocalPeripheralViewController`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`, `UITextFieldDelegate`
- 12 instance variables, 4 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"AMSBTLEAdvertisementManager" advertisingManager;
@"NSString" statusString;
@"UITextField" serviceNameField;
B advertising;
B isErrorMessage;
@"UIActivityIndicatorView" indicator;
@"NSString" theServiceName;
q advertiseTimeout;
q fullRefreshCounter;
@"NSTimer" advertiseTimer;
@"NSTimer" messageTimer;
B didCleanup;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CABTMIDILocalPeripheralViewController cleanup];
-[CABTMIDILocalPeripheralViewController tableView:numberOfRowsInSection:];
-[CABTMIDILocalPeripheralViewController numberOfSectionsInTableView:];
-[CABTMIDILocalPeripheralViewController tableView:cellForRowAtIndexPath:];
-[CABTMIDILocalPeripheralViewController observeValueForKeyPath:ofObject:change:context:];
-[CABTMIDILocalPeripheralViewController dealloc];
-[CABTMIDILocalPeripheralViewController statusString];
-[CABTMIDILocalPeripheralViewController textFieldDidBeginEditing:];
-[CABTMIDILocalPeripheralViewController tableView:titleForHeaderInSection:];
-[CABTMIDILocalPeripheralViewController viewDidLoad];
-[CABTMIDILocalPeripheralViewController initWithNibName:bundle:];
-[CABTMIDILocalPeripheralViewController textFieldDidEndEditing:];
-[CABTMIDILocalPeripheralViewController title];
-[CABTMIDILocalPeripheralViewController loadView];
-[CABTMIDILocalPeripheralViewController didReceiveMemoryWarning];
-[CABTMIDILocalPeripheralViewController viewDidDisappear:];
-[CABTMIDILocalPeripheralViewController activateController:];
-[CABTMIDILocalPeripheralViewController stopTimers];
-[CABTMIDILocalPeripheralViewController advertiseServiceSwitchToggled:];
-[CABTMIDILocalPeripheralViewController advertiseServiceWithName:completionBlock:error:];
-[CABTMIDILocalPeripheralViewController advertiseTimerFired:];
-[CABTMIDILocalPeripheralViewController advertisedServiceName];
-[CABTMIDILocalPeripheralViewController changeServiceNameTo:completionBlock:error:];
-[CABTMIDILocalPeripheralViewController deactivateController:];
-[CABTMIDILocalPeripheralViewController disconnectLocalPeripheral];
-[CABTMIDILocalPeripheralViewController messageTimerFired:];
-[CABTMIDILocalPeripheralViewController setStatusString:animateIndicator:isError:];
-[CABTMIDILocalPeripheralViewController stopAdvertisingServiceWithCompletionBlock:error:];
-[CABTMIDILocalPeripheralViewController textFieldDone:];
-[CABTMIDILocalPeripheralViewController updateAdvertiseUI];
```
