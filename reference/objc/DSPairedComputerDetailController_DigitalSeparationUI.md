# `DSPairedComputerDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- 3 instance variables, 3 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"<DSPairedComputerDelegate>" _delegate;
@"DSPairedComputer" _pairedComputer;
@"NSMutableArray" _orderedCells;
```

## Properties

```
@property (T@"DSPairedComputer",&,N,V_pairedComputer) pairedComputer;
@property (T@"NSMutableArray",&,N,V_orderedCells) orderedCells;
@property (T@"<DSPairedComputerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[DSPairedComputerDetailController initialize];
```

## Instance methods

```
-[DSPairedComputerDetailController tableView:numberOfRowsInSection:];
-[DSPairedComputerDetailController tableView:editingStyleForRowAtIndexPath:];
-[DSPairedComputerDetailController tableView:cellForRowAtIndexPath:];
-[DSPairedComputerDetailController viewDidLoad];
-[DSPairedComputerDetailController setDelegate:];
-[DSPairedComputerDetailController delegate];
-[DSPairedComputerDetailController orderedCells];
-[DSPairedComputerDetailController setOrderedCells:];
-[DSPairedComputerDetailController dateDescription];
-[DSPairedComputerDetailController back];
-[DSPairedComputerDetailController cellWithText:secondaryText:];
-[DSPairedComputerDetailController initWithPairedComputer:];
-[DSPairedComputerDetailController pairedComputer];
-[DSPairedComputerDetailController presentRemoveDeviceAlert];
-[DSPairedComputerDetailController returnFromDetailAndRemoveComputer];
-[DSPairedComputerDetailController setPairedComputer:];
```
