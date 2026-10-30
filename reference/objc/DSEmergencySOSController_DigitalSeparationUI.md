# `DSEmergencySOSController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`, `HKMedicalIDEmergencyContactFlowDelegate`, `DSController`
- 10 instance variables, 14 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _hasRetriedEmergencyContactFetch;
@"<DSNavigationDelegate>" _delegate;
@"HKHealthStore" _healthStore;
@"HKMedicalIDStore" _medicalIDStore;
@"_HKMedicalIDData" _medicalIDData;
@"NSArray" _emergencyContacts;
@"_HKEmergencyContact" _selectedEmergencyContact;
@"HKMedicalIDEmergencyContactFlow" _contactFlow;
@"DSAppSharing" _appSharing;
@"NSString" _kappaApprovedAppID;
```

## Properties

```
@property (T@"HKHealthStore",&,N,V_healthStore) healthStore;
@property (T@"HKMedicalIDStore",&,N,V_medicalIDStore) medicalIDStore;
@property (T@"_HKMedicalIDData",&,N,V_medicalIDData) medicalIDData;
@property (T@"NSArray",&,N,V_emergencyContacts) emergencyContacts;
@property (T@"_HKEmergencyContact",&,N,V_selectedEmergencyContact) selectedEmergencyContact;
@property (T@"HKMedicalIDEmergencyContactFlow",&,N,V_contactFlow) contactFlow;
@property (TB,V_hasRetriedEmergencyContactFetch) hasRetriedEmergencyContactFetch;
@property (T@"DSAppSharing",&,N,V_appSharing) appSharing;
@property (T@"NSString",&,N,V_kappaApprovedAppID) kappaApprovedAppID;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSEmergencySOSController tableView:shouldHighlightRowAtIndexPath:];
-[DSEmergencySOSController tableView:titleForFooterInSection:];
-[DSEmergencySOSController healthStore];
-[DSEmergencySOSController tableView:numberOfRowsInSection:];
-[DSEmergencySOSController numberOfSectionsInTableView:];
-[DSEmergencySOSController setHealthStore:];
-[DSEmergencySOSController tableView:editingStyleForRowAtIndexPath:];
-[DSEmergencySOSController tableView:commitEditingStyle:forRowAtIndexPath:];
-[DSEmergencySOSController tableView:cellForRowAtIndexPath:];
-[DSEmergencySOSController init];
-[DSEmergencySOSController medicalIDStore];
-[DSEmergencySOSController tableView:titleForHeaderInSection:];
-[DSEmergencySOSController viewDidLoad];
-[DSEmergencySOSController setDelegate:];
-[DSEmergencySOSController setMedicalIDStore:];
-[DSEmergencySOSController tableView:didSelectRowAtIndexPath:];
-[DSEmergencySOSController delegate];
-[DSEmergencySOSController emergencyContacts];
-[DSEmergencySOSController setEmergencyContacts:];
-[DSEmergencySOSController medicalIDData];
-[DSEmergencySOSController setMedicalIDData:];
-[DSEmergencySOSController emergencyContactFlow:didSelectContact:];
-[DSEmergencySOSController emergencyContactFlowDidCancel:];
-[DSEmergencySOSController hasRetriedEmergencyContactFetch];
-[DSEmergencySOSController setContactFlow:];
-[DSEmergencySOSController _showMaxContactsAlert];
-[DSEmergencySOSController appSharing];
-[DSEmergencySOSController chooseNewEmergencyContact];
-[DSEmergencySOSController contactFlow];
-[DSEmergencySOSController gatherEmergencyContacts];
-[DSEmergencySOSController hasAppWithKappaApproved];
-[DSEmergencySOSController kappaApprovedAppID];
-[DSEmergencySOSController maybeRetryDueToError:withReason:];
-[DSEmergencySOSController removeEmergencyContact:];
-[DSEmergencySOSController revokeKappaPermission];
-[DSEmergencySOSController selectedEmergencyContact];
-[DSEmergencySOSController setAppSharing:];
-[DSEmergencySOSController setHasRetriedEmergencyContactFetch:];
-[DSEmergencySOSController setKappaApprovedAppID:];
-[DSEmergencySOSController setSelectedEmergencyContact:];
-[DSEmergencySOSController updateKappaBundleID];
```
