# `DSPairedComputerController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `UITableViewDelegate`, `DSPairedComputerDelegate`, `DSController`
- 5 instance variables, 9 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"NSError" _fetchError;
@"NSMutableArray" _pairedComputers;
@"NSMutableArray" _selectedPairedComputers;
@"<DSPairedComputerStoreProtocol>" _pairedComputerStore;
```

## Properties

```
@property (T@"NSError",&,N,V_fetchError) fetchError;
@property (T@"NSMutableArray",&,N,V_pairedComputers) pairedComputers;
@property (T@"NSMutableArray",&,N,V_selectedPairedComputers) selectedPairedComputers;
@property (T@"<DSPairedComputerStoreProtocol>",&,N,V_pairedComputerStore) pairedComputerStore;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSPairedComputerController tableView:numberOfRowsInSection:];
-[DSPairedComputerController tableView:accessoryButtonTappedForRowWithIndexPath:];
-[DSPairedComputerController tableView:cellForRowAtIndexPath:];
-[DSPairedComputerController init];
-[DSPairedComputerController viewDidLoad];
-[DSPairedComputerController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSPairedComputerController viewWillAppear:];
-[DSPairedComputerController setDelegate:];
-[DSPairedComputerController fetchError];
-[DSPairedComputerController tableView:didSelectRowAtIndexPath:];
-[DSPairedComputerController delegate];
-[DSPairedComputerController setFetchError:];
-[DSPairedComputerController _updateButtons];
-[DSPairedComputerController tableView:didDeselectRowAtIndexPath:];
-[DSPairedComputerController localizedDetailText];
-[DSPairedComputerController pairedComputers];
-[DSPairedComputerController addPairedDevices:];
-[DSPairedComputerController dateDescription:];
-[DSPairedComputerController finalizeComputerReviewAndPushNextPane];
-[DSPairedComputerController finalizePairingReviewReport];
-[DSPairedComputerController learnMoreWifiSyncPressed];
-[DSPairedComputerController pairedComputerStore];
-[DSPairedComputerController presentFetchedErrorAlert];
-[DSPairedComputerController presentRemoveAllDevicesAlert];
-[DSPairedComputerController presentRemoveErrorAlert:];
-[DSPairedComputerController presentRemoveSelectedDevicesAlert];
-[DSPairedComputerController reloadDetailText];
-[DSPairedComputerController removeAllPairedDevicesAndPushNextPane];
-[DSPairedComputerController removeDetailViewControllerFromStack];
-[DSPairedComputerController removeSelectedPairedDevicesAndPushNextPane];
-[DSPairedComputerController reportReviewedComputers:];
-[DSPairedComputerController reportUnpairedComputers:];
-[DSPairedComputerController returnFromDetailAndRemoveComputer:];
-[DSPairedComputerController selectedPairedComputers];
-[DSPairedComputerController setPairedComputerStore:];
-[DSPairedComputerController setPairedComputers:];
-[DSPairedComputerController setSelectedPairedComputers:];
-[DSPairedComputerController shouldShowWithCompletion:];
-[DSPairedComputerController titleForPairedComputer:];
```
