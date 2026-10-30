# `DSEmergencyResetController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `DSController`
- 15 instance variables, 19 properties, 50 instance methods, 1 class methods

## Instance variables

```
B _isFetching;
B _userDidPressReset;
@"<DSNavigationDelegate>" _delegate;
@"DSSharingPermissions" _permissions;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"DSAppSharing" _appSharing;
@"OBBoldTrayButton" _boldButton;
@"NSMutableArray" _resetErrors;
@"SPBeaconManager" _beaconManager;
@"UIStackView" _progressStackView;
@"UIProgressView" _progressView;
@"<DSPairedComputerStoreProtocol>" _pairedComputerStore;
@"DSContinuityStore" _continuityStore;
@"DSDeveloperModeManager" _developerModeManager;
@"NSArray" _emergencyResetSteps;
```

## Properties

```
@property (T@"DSSharingPermissions",&,N,V_permissions) permissions;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"DSAppSharing",&,N,V_appSharing) appSharing;
@property (T@"OBBoldTrayButton",&,N,V_boldButton) boldButton;
@property (T@"NSMutableArray",&,N,V_resetErrors) resetErrors;
@property (TB,N,V_isFetching) isFetching;
@property (T@"SPBeaconManager",&,N,V_beaconManager) beaconManager;
@property (T@"UIStackView",&,N,V_progressStackView) progressStackView;
@property (T@"UIProgressView",&,N,V_progressView) progressView;
@property (TB,N,V_userDidPressReset) userDidPressReset;
@property (T@"<DSPairedComputerStoreProtocol>",&,N,V_pairedComputerStore) pairedComputerStore;
@property (T@"DSContinuityStore",&,N,V_continuityStore) continuityStore;
@property (T@"DSDeveloperModeManager",&,N,V_developerModeManager) developerModeManager;
@property (T@"NSArray",&,N,V_emergencyResetSteps) emergencyResetSteps;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSEmergencyResetController initialize];
```

## Instance methods

```
-[DSEmergencyResetController setWorkQueue:];
-[DSEmergencyResetController setPermissions:];
-[DSEmergencyResetController init];
-[DSEmergencyResetController workQueue];
-[DSEmergencyResetController viewDidLoad];
-[DSEmergencyResetController progressView];
-[DSEmergencyResetController permissions];
-[DSEmergencyResetController beaconManager];
-[DSEmergencyResetController viewWillAppear:];
-[DSEmergencyResetController setDelegate:];
-[DSEmergencyResetController setBoldButton:];
-[DSEmergencyResetController delegate];
-[DSEmergencyResetController setBeaconManager:];
-[DSEmergencyResetController setProgressView:];
-[DSEmergencyResetController boldButton];
-[DSEmergencyResetController resetErrors];
-[DSEmergencyResetController isFetching];
-[DSEmergencyResetController setIsFetching:];
-[DSEmergencyResetController showProgressBar];
-[DSEmergencyResetController removeAllPairedDevicesOnQueue:completion:];
-[DSEmergencyResetController continuityStore];
-[DSEmergencyResetController hideProgressBar];
-[DSEmergencyResetController initializeEmergencyResetActions];
-[DSEmergencyResetController setResetErrors:];
-[DSEmergencyResetController appSharing];
-[DSEmergencyResetController developerModeManager];
-[DSEmergencyResetController disableDeveloperMode:];
-[DSEmergencyResetController emergencyResetSteps];
-[DSEmergencyResetController fetchSharingPermissions:];
-[DSEmergencyResetController handleErrorsAndMoveToNextPane];
-[DSEmergencyResetController pairedComputerStore];
-[DSEmergencyResetController progressStackView];
-[DSEmergencyResetController resetAllFirstPartySharing:];
-[DSEmergencyResetController resetAllThirdPartyTCCs:];
-[DSEmergencyResetController resetAppDistribution:];
-[DSEmergencyResetController resetIDFA:];
-[DSEmergencyResetController resetNecessaryFirstPartyPermissions:];
-[DSEmergencyResetController safetyResetAll];
-[DSEmergencyResetController safetyResetAllPressed];
-[DSEmergencyResetController setAppSharing:];
-[DSEmergencyResetController setContinuityStore:];
-[DSEmergencyResetController setDeveloperModeManager:];
-[DSEmergencyResetController setDigitalSeparationTipsFlag];
-[DSEmergencyResetController setEmergencyResetSteps:];
-[DSEmergencyResetController setPairedComputerStore:];
-[DSEmergencyResetController setProgressStackView:];
-[DSEmergencyResetController setUserDidPressReset:];
-[DSEmergencyResetController unpairContinuityDevices:];
-[DSEmergencyResetController updateProgressBar];
-[DSEmergencyResetController userDidPressReset];
```
