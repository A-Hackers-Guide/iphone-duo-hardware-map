# `DSCompletedController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `CLFindMyAccessoryManagerDelegate`, `DSController`
- 8 instance variables, 12 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _walletSharing;
B _UTAlertsEnabled;
@"<DSNavigationDelegate>" _delegate;
@"FAFamilyMember" _familyMember;
@"UIActivityIndicatorView" _spinner;
@"NSLayoutConstraint" _heightConstraint;
@"NSObject<OS_dispatch_group>" _fetchingGroup;
@"CLFindMyAccessoryManager" _accessoryManager;
```

## Properties

```
@property (T@"FAFamilyMember",&,V_familyMember) familyMember;
@property (TB,N,V_walletSharing) walletSharing;
@property (TB,N,V_UTAlertsEnabled) UTAlertsEnabled;
@property (T@"UIActivityIndicatorView",&,N,V_spinner) spinner;
@property (T@"NSLayoutConstraint",&,N,V_heightConstraint) heightConstraint;
@property (T@"NSObject<OS_dispatch_group>",&,N,V_fetchingGroup) fetchingGroup;
@property (T@"CLFindMyAccessoryManager",&,N,V_accessoryManager) accessoryManager;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSCompletedController initialize];
```

## Instance methods

```
-[DSCompletedController setHeightConstraint:];
-[DSCompletedController heightConstraint];
-[DSCompletedController init];
-[DSCompletedController viewDidLoad];
-[DSCompletedController accessoryManager];
-[DSCompletedController setDelegate:];
-[DSCompletedController setSpinner:];
-[DSCompletedController delegate];
-[DSCompletedController setAccessoryManager:];
-[DSCompletedController spinner];
-[DSCompletedController familyMember];
-[DSCompletedController setFamilyMember:];
-[DSCompletedController findMyAccessoryManager:didFailWithError:forDevice:];
-[DSCompletedController findMyAccessoryManager:didFetchStatusOfUTEnablementRequirementsWithStatus:withError:];
-[DSCompletedController fetchCompleted];
-[DSCompletedController UTAlertsEnabled];
-[DSCompletedController addFamilyBullet];
-[DSCompletedController addWalletBullet];
-[DSCompletedController addHomeBullet];
-[DSCompletedController addUTAlerts];
-[DSCompletedController fetchAdditionalSharingWithCompletion:];
-[DSCompletedController fetchingGroup];
-[DSCompletedController learnMorePressed];
-[DSCompletedController setFetchingGroup:];
-[DSCompletedController setUTAlertsEnabled:];
-[DSCompletedController setWalletSharing:];
-[DSCompletedController startContentSpinner];
-[DSCompletedController stopContentSpinner];
-[DSCompletedController walletSharing];
```
