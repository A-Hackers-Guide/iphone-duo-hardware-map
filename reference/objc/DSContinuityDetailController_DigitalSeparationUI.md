# `DSContinuityDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- 3 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<DSContinuityDelegate>" _delegate;
@"DSContinuityDevice" _continuityDevice;
@"NSMutableArray" _orderedCells;
```

## Properties

```
@property (T@"DSContinuityDevice",&,N,V_continuityDevice) continuityDevice;
@property (T@"NSMutableArray",&,N,V_orderedCells) orderedCells;
@property (T@"<DSContinuityDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[DSContinuityDetailController tableView:numberOfRowsInSection:];
-[DSContinuityDetailController stringFromDate:];
-[DSContinuityDetailController tableView:editingStyleForRowAtIndexPath:];
-[DSContinuityDetailController tableView:cellForRowAtIndexPath:];
-[DSContinuityDetailController viewDidLoad];
-[DSContinuityDetailController setDelegate:];
-[DSContinuityDetailController delegate];
-[DSContinuityDetailController orderedCells];
-[DSContinuityDetailController setOrderedCells:];
-[DSContinuityDetailController localizedDetailText];
-[DSContinuityDetailController back];
-[DSContinuityDetailController cellWithText:secondaryText:];
-[DSContinuityDetailController continuityDevice];
-[DSContinuityDetailController initWithContinuityDevice:];
-[DSContinuityDetailController marketingNameForDevice:];
-[DSContinuityDetailController presentRemoveDeviceAlert];
-[DSContinuityDetailController returnFromDetailAndRemoveComputer];
-[DSContinuityDetailController setContinuityDevice:];
```
