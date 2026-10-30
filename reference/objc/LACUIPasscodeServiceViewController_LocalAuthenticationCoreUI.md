# `LACUIPasscodeServiceViewController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `LACUIPasscodeViewModelDelegate`, `LACUIPasscodeServiceViewControlling`
- 3 instance variables, 4 properties, 28 instance methods, 0 class methods

## Instance variables

```
? delegate;
viewModel;
@"LACUIPasscodeServiceViewConfiguration" configuration;
```

## Properties

```
@property (T@"<LACUIPasscodeServiceViewControllerDelegate>",N,W,Vdelegate) delegate;
@property (T@"LACUIPasscodeServiceViewConfiguration",N,R,Vconfiguration) configuration;
@property (T@"NSString",N,R) passcode;
@property (T@"UINavigationItem",N,R) navigationItem;
```

## Instance methods

```
-[LACUIPasscodeServiceViewController clear];
-[LACUIPasscodeServiceViewController passcode];
-[LACUIPasscodeServiceViewController setHeader:];
-[LACUIPasscodeServiceViewController setFooter:];
-[LACUIPasscodeServiceViewController hideSpinner];
-[LACUIPasscodeServiceViewController viewDidLoad];
-[LACUIPasscodeServiceViewController viewDidLayoutSubviews];
-[LACUIPasscodeServiceViewController initWithConfiguration:];
-[LACUIPasscodeServiceViewController initWithNibName:bundle:];
-[LACUIPasscodeServiceViewController viewWillAppear:];
-[LACUIPasscodeServiceViewController _canShowWhileLocked];
-[LACUIPasscodeServiceViewController setDelegate:];
-[LACUIPasscodeServiceViewController viewDidAppear:];
-[LACUIPasscodeServiceViewController configuration];
-[LACUIPasscodeServiceViewController delegate];
-[LACUIPasscodeServiceViewController navigationItem];
-[LACUIPasscodeServiceViewController initWithCoder:];
-[LACUIPasscodeServiceViewController showSpinner];
-[LACUIPasscodeServiceViewController _preferredContentSizeDidChangeForChildViewController:];
-[LACUIPasscodeServiceViewController focus];
-[LACUIPasscodeServiceViewController setErrorMessage:];
-[LACUIPasscodeServiceViewController setSubHeader:];
-[LACUIPasscodeServiceViewController unfocus];
-[LACUIPasscodeServiceViewController shakeWithCompletion:];
-[LACUIPasscodeServiceViewController passcodeViewModel:didSelectPasscodeType:];
-[LACUIPasscodeServiceViewController passcodeViewModelPasscodeCanceled:];
-[LACUIPasscodeServiceViewController passcodeViewModelPasscodeDidChange:];
-[LACUIPasscodeServiceViewController passcodeViewModelPasscodeEntered:];
```
