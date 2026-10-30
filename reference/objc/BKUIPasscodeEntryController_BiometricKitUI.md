# `BKUIPasscodeEntryController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBPasscodeViewController`
- Protocols: `OBPasscodeViewControllerDelegate`
- 1 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@? _passcodeEntryAction;
```

## Properties

```
@property (T@?,C,N,V_passcodeEntryAction) passcodeEntryAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKUIPasscodeEntryController isDevicePasscodeSet];
```

## Instance methods

```
-[BKUIPasscodeEntryController isModalInPresentation];
-[BKUIPasscodeEntryController viewDidLoad];
-[BKUIPasscodeEntryController passcodeViewController:shouldEnableCompletionButtonForPasscode:];
-[BKUIPasscodeEntryController completionButtonTitleForPasscodeViewController:];
-[BKUIPasscodeEntryController passcodeViewController:didEnterPasscode:];
-[BKUIPasscodeEntryController verifyPasscode:];
-[BKUIPasscodeEntryController initWithVerifiedPasscodeAction:];
-[BKUIPasscodeEntryController cancelPasscodeEntry];
-[BKUIPasscodeEntryController passcodeEntryAction];
-[BKUIPasscodeEntryController setPasscodeEntryAction:];
-[BKUIPasscodeEntryController setUnlockScreenType:simplePasscodeType:];
-[BKUIPasscodeEntryController simplePasscodeType];
-[BKUIPasscodeEntryController unlockType];
```
