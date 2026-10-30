# `SBActivationInfoViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `STTelephonyStateObserver`, `UITableViewDataSource`, `UITableViewDelegate`
- 14 instance variables, 10 properties, 38 instance methods, 1 class methods

## Instance variables

```
@"NSString" _serial;
@"NSString" _meid;
@"NSString" _eid;
@"NSArray" _mobileEquipmentInfo;
@"UIView" _containerView;
@"UITableView" _activationInfoTableView;
@"NSLayoutConstraint" _activationInfoTableViewHeight;
@"UIButton" _activateForESIMSetupButton;
@"UIButton" _regulatoryInfoButton;
@"UIButton" _secureIntentButton;
@"UIButton" _simConfigButton;
B _isReadyToShip;
B _isShipChargeLimitSupported;
@"_UILegibilitySettings" _legibilitySettings;
```

## Properties

```
@property (T@"NSArray",&,N,V_mobileEquipmentInfo) mobileEquipmentInfo;
@property (T@"UIButton",R,N,V_activateForESIMSetupButton) activateForESIMSetupButton;
@property (T@"UIButton",R,N,V_regulatoryInfoButton) regulatoryInfoButton;
@property (T@"UIButton",R,N,V_secureIntentButton) secureIntentButton;
@property (T@"UIButton",R,N,V_simConfigButton) simConfigButton;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBActivationInfoViewController _queue_readShipModeComplianceSupported:readyToShip:];
```

## Instance methods

```
-[SBActivationInfoViewController tableView:heightForFooterInSection:];
-[SBActivationInfoViewController tableView:numberOfRowsInSection:];
-[SBActivationInfoViewController numberOfSectionsInTableView:];
-[SBActivationInfoViewController tableView:cellForRowAtIndexPath:];
-[SBActivationInfoViewController mobileEquipmentInfo];
-[SBActivationInfoViewController dealloc];
-[SBActivationInfoViewController viewDidLayoutSubviews];
-[SBActivationInfoViewController initWithNibName:bundle:];
-[SBActivationInfoViewController subscriptionInfoDidChangeForStateProvider:slot:];
-[SBActivationInfoViewController viewWillAppear:];
-[SBActivationInfoViewController tableView:heightForRowAtIndexPath:];
-[SBActivationInfoViewController _canShowWhileLocked];
-[SBActivationInfoViewController setMobileEquipmentInfo:];
-[SBActivationInfoViewController loadView];
-[SBActivationInfoViewController legibilitySettings];
-[SBActivationInfoViewController setLegibilitySettings:];
-[SBActivationInfoViewController tableView:viewForHeaderInSection:];
-[SBActivationInfoViewController _formattedIMEI:];
-[SBActivationInfoViewController simConfigButton];
-[SBActivationInfoViewController _activationInfoCell];
-[SBActivationInfoViewController _adjustMobileEquipmentLayout:];
-[SBActivationInfoViewController _appendMobileEquipmentInfoForSlot:mobileEquipmentInfoList:];
-[SBActivationInfoViewController _backgroundViewForHeaderView:];
-[SBActivationInfoViewController _deviceIsChinaSKU];
-[SBActivationInfoViewController _displayLabelForKey:];
-[SBActivationInfoViewController _formattedEID:];
-[SBActivationInfoViewController _formattedICCID:];
-[SBActivationInfoViewController _formattedString:withSpaceAfterDigits:];
-[SBActivationInfoViewController _processDeviceInfo];
-[SBActivationInfoViewController _repinActivationTableHeight];
-[SBActivationInfoViewController _shouldGroupIMEIsForPrimary:secondary:];
-[SBActivationInfoViewController _telephonyStateChanged];
-[SBActivationInfoViewController _updateMobileEquipmentInfo];
-[SBActivationInfoViewController _updateShipModeCompliance];
-[SBActivationInfoViewController activateForESIMSetupButton];
-[SBActivationInfoViewController mobileEquipmentInfoDidChangeForStateProvider:slot:];
-[SBActivationInfoViewController regulatoryInfoButton];
-[SBActivationInfoViewController secureIntentButton];
```
