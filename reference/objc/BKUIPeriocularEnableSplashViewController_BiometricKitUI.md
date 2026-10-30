# `BKUIPeriocularEnableSplashViewController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTableWelcomeController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`
- 12 instance variables, 16 properties, 43 instance methods, 2 class methods

## Instance variables

```
B _inBuddy;
B _upsell;
@"BKUIPeriocularSelectionCell" _cellTop;
@"BKUIPeriocularSelectionCell" _cellBottom;
@"OBTrayButton" _skipButton;
@? _endEnrollActionPrimary;
@? _endEnrollActionSecondary;
@"OBTrayButton" _continueButton;
@"BKDevice" _device;
@"OBPrivacyLinkController" _linkController;
@"OBAnimationController" _animationController;
@? _userSkippedAction;
```

## Properties

```
@property (T@"BKUIPeriocularSelectionCell",&,N,V_cellTop) cellTop;
@property (T@"BKUIPeriocularSelectionCell",&,N,V_cellBottom) cellBottom;
@property (TB,N,V_inBuddy) inBuddy;
@property (T@"OBTrayButton",&,N,V_skipButton) skipButton;
@property (T@?,C,N,V_endEnrollActionPrimary) endEnrollActionPrimary;
@property (T@?,C,N,V_endEnrollActionSecondary) endEnrollActionSecondary;
@property (T@"OBTrayButton",&,N,V_continueButton) continueButton;
@property (T@"BKDevice",&,N,V_device) device;
@property (TB,N,V_upsell) upsell;
@property (T@"OBPrivacyLinkController",&,N,V_linkController) linkController;
@property (T@"OBAnimationController",&,N,V_animationController) animationController;
@property (T@?,C,N,V_userSkippedAction) userSkippedAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKUIPeriocularEnableSplashViewController setPeriocularFaceIDMatchEnabledForUserConfigurationWithDevice:credentialSet:authContext:enabled:completion:];
+[BKUIPeriocularEnableSplashViewController setPeriocularFaceIDMatchEnabledForUserConfigurationWithDevice:credentialSet:enabled:];
```

## Instance methods

```
-[BKUIPeriocularEnableSplashViewController tableView:heightForFooterInSection:];
-[BKUIPeriocularEnableSplashViewController animationController];
-[BKUIPeriocularEnableSplashViewController tableView:numberOfRowsInSection:];
-[BKUIPeriocularEnableSplashViewController numberOfSectionsInTableView:];
-[BKUIPeriocularEnableSplashViewController tableView:viewForFooterInSection:];
-[BKUIPeriocularEnableSplashViewController tableView:cellForRowAtIndexPath:];
-[BKUIPeriocularEnableSplashViewController setDevice:];
-[BKUIPeriocularEnableSplashViewController setSkipButton:];
-[BKUIPeriocularEnableSplashViewController device];
-[BKUIPeriocularEnableSplashViewController viewDidLoad];
-[BKUIPeriocularEnableSplashViewController viewWillAppear:];
-[BKUIPeriocularEnableSplashViewController tableView:heightForRowAtIndexPath:];
-[BKUIPeriocularEnableSplashViewController tableView:didSelectRowAtIndexPath:];
-[BKUIPeriocularEnableSplashViewController skipButton];
-[BKUIPeriocularEnableSplashViewController preferredStatusBarStyle];
-[BKUIPeriocularEnableSplashViewController tableView:estimatedHeightForRowAtIndexPath:];
-[BKUIPeriocularEnableSplashViewController setAnimationController:];
-[BKUIPeriocularEnableSplashViewController tableView:viewForHeaderInSection:];
-[BKUIPeriocularEnableSplashViewController tableView:heightForHeaderInSection:];
-[BKUIPeriocularEnableSplashViewController continueButton];
-[BKUIPeriocularEnableSplashViewController setContinueButton:];
-[BKUIPeriocularEnableSplashViewController inBuddy];
-[BKUIPeriocularEnableSplashViewController setInBuddy:];
-[BKUIPeriocularEnableSplashViewController headerViewBottomToTableViewTopPadding];
-[BKUIPeriocularEnableSplashViewController linkController];
-[BKUIPeriocularEnableSplashViewController _enrollSkipped:];
-[BKUIPeriocularEnableSplashViewController cellTop];
-[BKUIPeriocularEnableSplashViewController _continuePressed:];
-[BKUIPeriocularEnableSplashViewController _createCellForIndexPath:];
-[BKUIPeriocularEnableSplashViewController _showPrivacyLink];
-[BKUIPeriocularEnableSplashViewController cellBottom];
-[BKUIPeriocularEnableSplashViewController endEnrollActionPrimary];
-[BKUIPeriocularEnableSplashViewController endEnrollActionSecondary];
-[BKUIPeriocularEnableSplashViewController initInBuddy:bkDevice:upsell:withEndEnrollmentActionPrimary:enrollmentActionSecondary:];
-[BKUIPeriocularEnableSplashViewController setCellBottom:];
-[BKUIPeriocularEnableSplashViewController setCellTop:];
-[BKUIPeriocularEnableSplashViewController setEndEnrollActionPrimary:];
-[BKUIPeriocularEnableSplashViewController setEndEnrollActionSecondary:];
-[BKUIPeriocularEnableSplashViewController setLinkController:];
-[BKUIPeriocularEnableSplashViewController setUpsell:];
-[BKUIPeriocularEnableSplashViewController setUserSkippedAction:];
-[BKUIPeriocularEnableSplashViewController upsell];
-[BKUIPeriocularEnableSplashViewController userSkippedAction];
```
