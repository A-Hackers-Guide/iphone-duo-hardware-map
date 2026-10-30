# `LACUIPasscodeViewController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `LACUIPasscodeViewModelDelegate`, `LACUIPasscodeViewType`
- 3 instance variables, 3 properties, 20 instance methods, 0 class methods

## Instance variables

```
? delegate;
@"LACUIPasscodeViewState" state;
viewModel;
```

## Properties

```
@property (T@"<LACUIPasscodeViewDelegate>",N,W,Vdelegate) delegate;
@property (T@"LACUIPasscodeViewState",N,&,Vstate) state;
@property (T@"NSString",N,R) passcode;
```

## Instance methods

```
-[LACUIPasscodeViewController initWithViewModel:];
-[LACUIPasscodeViewController setState:];
-[LACUIPasscodeViewController passcode];
-[LACUIPasscodeViewController pressesEnded:withEvent:];
-[LACUIPasscodeViewController viewDidLoad];
-[LACUIPasscodeViewController viewDidLayoutSubviews];
-[LACUIPasscodeViewController initWithConfiguration:];
-[LACUIPasscodeViewController initWithNibName:bundle:];
-[LACUIPasscodeViewController _canShowWhileLocked];
-[LACUIPasscodeViewController setDelegate:];
-[LACUIPasscodeViewController viewDidAppear:];
-[LACUIPasscodeViewController delegate];
-[LACUIPasscodeViewController initWithCoder:];
-[LACUIPasscodeViewController _preferredContentSizeDidChangeForChildViewController:];
-[LACUIPasscodeViewController state];
-[LACUIPasscodeViewController animateToFailureStateWithCompletion:];
-[LACUIPasscodeViewController animateToSuccessStateWithCompletion:];
-[LACUIPasscodeViewController passcodeViewModelPasscodeCanceled:];
-[LACUIPasscodeViewController passcodeViewModelPasscodeDidChange:];
-[LACUIPasscodeViewController passcodeViewModelPasscodeEntered:];
```
