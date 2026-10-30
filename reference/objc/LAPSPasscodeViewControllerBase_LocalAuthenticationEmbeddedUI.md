# `LAPSPasscodeViewControllerBase`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `LAPSPasscodeOptionsViewControllerDelegate`, `LACUIPasscodeServiceViewControlling`
- 5 instance variables, 5 properties, 54 instance methods, 0 class methods

## Instance variables

```
B _isPasscodeRecoveryEnabled;
@"LACUIPasscodeServiceViewConfiguration" _config;
@"LACPasscode" _passcodeType;
@"<LACUIPasscodeServiceViewControllerDelegate>" _delegate;
@"LAPSPasscodeViewControllerManagedViews" _managedViews;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACUIPasscodeServiceViewControllerDelegate>",W,N) delegate;
```

## Instance methods

```
-[LAPSPasscodeViewControllerBase _scrollView];
-[LAPSPasscodeViewControllerBase setup];
-[LAPSPasscodeViewControllerBase clear];
-[LAPSPasscodeViewControllerBase layoutIfNeeded];
-[LAPSPasscodeViewControllerBase config];
-[LAPSPasscodeViewControllerBase setHeader:];
-[LAPSPasscodeViewControllerBase setFooter:];
-[LAPSPasscodeViewControllerBase hideSpinner];
-[LAPSPasscodeViewControllerBase submit];
-[LAPSPasscodeViewControllerBase _finishWithError:];
-[LAPSPasscodeViewControllerBase becomeFirstResponder];
-[LAPSPasscodeViewControllerBase willMoveToParentViewController:];
-[LAPSPasscodeViewControllerBase viewDidLoad];
-[LAPSPasscodeViewControllerBase viewDidLayoutSubviews];
-[LAPSPasscodeViewControllerBase initWithConfiguration:];
-[LAPSPasscodeViewControllerBase resignFirstResponder];
-[LAPSPasscodeViewControllerBase viewWillAppear:];
-[LAPSPasscodeViewControllerBase _canShowWhileLocked];
-[LAPSPasscodeViewControllerBase setDelegate:];
-[LAPSPasscodeViewControllerBase viewDidAppear:];
-[LAPSPasscodeViewControllerBase delegate];
-[LAPSPasscodeViewControllerBase navigationItem];
-[LAPSPasscodeViewControllerBase cancel];
-[LAPSPasscodeViewControllerBase showSpinner];
-[LAPSPasscodeViewControllerBase canBecomeFirstResponder];
-[LAPSPasscodeViewControllerBase passcodeType];
-[LAPSPasscodeViewControllerBase focus];
-[LAPSPasscodeViewControllerBase setErrorMessage:];
-[LAPSPasscodeViewControllerBase _footerLabel];
-[LAPSPasscodeViewControllerBase setupNavigationItem];
-[LAPSPasscodeViewControllerBase setSubHeader:];
-[LAPSPasscodeViewControllerBase unfocus];
-[LAPSPasscodeViewControllerBase _subHeaderLabel];
-[LAPSPasscodeViewControllerBase shouldShowPasscodeOptionsButton];
-[LAPSPasscodeViewControllerBase _errorCapsule];
-[LAPSPasscodeViewControllerBase _errorCapsuleContainer];
-[LAPSPasscodeViewControllerBase _headerLabel];
-[LAPSPasscodeViewControllerBase _passcodeFieldVC];
-[LAPSPasscodeViewControllerBase _setPasscodeType:];
-[LAPSPasscodeViewControllerBase _showPasscodeOptionsSourceWithView:sourceItem:presentationStyle:shouldResignFirstResponder:];
-[LAPSPasscodeViewControllerBase _submitPasscode:];
-[LAPSPasscodeViewControllerBase isAccessibilityTextEnabled];
-[LAPSPasscodeViewControllerBase passcodeField:didChangePasscodeLength:];
-[LAPSPasscodeViewControllerBase passcodeField:didSubmitPasscode:];
-[LAPSPasscodeViewControllerBase passcodeOptionsViewController:didSelectPasscodeType:];
-[LAPSPasscodeViewControllerBase passcodeOptionsViewController:didSetPasscodeRecoveryEnabled:];
-[LAPSPasscodeViewControllerBase passcodeOptionsViewControllerDidDisappear:];
-[LAPSPasscodeViewControllerBase passcodeOptionsViewControllerWillDisappear:];
-[LAPSPasscodeViewControllerBase shakeWithCompletion:];
-[LAPSPasscodeViewControllerBase showPasscodeOptionsSourceItem:presentationStyle:shouldResignFirstResponder:];
-[LAPSPasscodeViewControllerBase showPasscodeOptionsSourceWithView:presentationStyle:shouldResignFirstResponder:];
-[LAPSPasscodeViewControllerBase styleWithPasscodeType:];
-[LAPSPasscodeViewControllerBase updateLayoutAfterPasscodeLengthChangeIfNeeded:];
-[LAPSPasscodeViewControllerBase updateLayoutAfterPasscodeTypeChangeIfNeeded];
```
