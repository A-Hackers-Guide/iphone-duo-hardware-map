# `DSDeveloperModeController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSPairedComputerDelegate`, `DSController`
- 6 instance variables, 10 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"NSError" _fetchError;
@"<DSDeveloperModeManagerProtocol>" _developerModeStore;
@"<DSPairedComputerStoreProtocol>" _pairedComputersStore;
@"<DSDevicesAppSessionManagerProtocol>" _sessionStore;
@"NSArray" _pairedComputers;
```

## Properties

```
@property (T@"NSError",&,N,V_fetchError) fetchError;
@property (T@"<DSDeveloperModeManagerProtocol>",&,N,V_developerModeStore) developerModeStore;
@property (T@"<DSPairedComputerStoreProtocol>",&,N,V_pairedComputersStore) pairedComputersStore;
@property (T@"<DSDevicesAppSessionManagerProtocol>",&,N,V_sessionStore) sessionStore;
@property (T@"NSArray",&,N,V_pairedComputers) pairedComputers;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSDeveloperModeController tableView:numberOfRowsInSection:];
-[DSDeveloperModeController tableView:accessoryButtonTappedForRowWithIndexPath:];
-[DSDeveloperModeController tableView:cellForRowAtIndexPath:];
-[DSDeveloperModeController init];
-[DSDeveloperModeController viewDidLoad];
-[DSDeveloperModeController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSDeveloperModeController setDelegate:];
-[DSDeveloperModeController viewDidAppear:];
-[DSDeveloperModeController fetchError];
-[DSDeveloperModeController setSessionStore:];
-[DSDeveloperModeController delegate];
-[DSDeveloperModeController setFetchError:];
-[DSDeveloperModeController sessionStore];
-[DSDeveloperModeController pairedComputers];
-[DSDeveloperModeController developerModeStore];
-[DSDeveloperModeController disableDeveloperMode];
-[DSDeveloperModeController pairedComputerAtIndexPath:];
-[DSDeveloperModeController pairedComputersStore];
-[DSDeveloperModeController prepareViewDataWithCompletion:];
-[DSDeveloperModeController presentFetchedErrorAlert];
-[DSDeveloperModeController removeDetailViewControllerFromStack];
-[DSDeveloperModeController returnFromDetailAndRemoveComputer:];
-[DSDeveloperModeController setDeveloperModeStore:];
-[DSDeveloperModeController setPairedComputers:];
-[DSDeveloperModeController setPairedComputersStore:];
-[DSDeveloperModeController shouldShowWithCompletion:];
-[DSDeveloperModeController updateHeaderDetailText];
```
