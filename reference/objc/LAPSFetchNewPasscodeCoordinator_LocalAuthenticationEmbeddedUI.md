# `LAPSFetchNewPasscodeCoordinator`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUIPasscodeServiceViewControllerDelegate`
- 8 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"LAPSFetchNewPasscodeCoordinatorInput" _input;
@? _handler;
@"LAPSPasscodeChangeUIPresentationController" _presentationController;
@"LACPasscode" _passcodeType;
B _isPasscodeRecoveryEnabled;
@"LAPSPasscode" _passcode;
@"UIViewController<LACUIPasscodeServiceViewControlling>" _passcodeVC;
@"<LAPSFetchNewPasscodeCoordinatorDelegate>" _delegate;
```

## Properties

```
@property (T@"<LAPSFetchNewPasscodeCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LAPSFetchNewPasscodeCoordinator clear];
-[LAPSFetchNewPasscodeCoordinator _deactivate];
-[LAPSFetchNewPasscodeCoordinator finishWithError:];
-[LAPSFetchNewPasscodeCoordinator setDelegate:];
-[LAPSFetchNewPasscodeCoordinator restart];
-[LAPSFetchNewPasscodeCoordinator delegate];
-[LAPSFetchNewPasscodeCoordinator _footerText];
-[LAPSFetchNewPasscodeCoordinator _invokeHandlerWithOutput:error:];
-[LAPSFetchNewPasscodeCoordinator _invokeHandlerWithError:];
-[LAPSFetchNewPasscodeCoordinator _invokeHandlerWithOutput:];
-[LAPSFetchNewPasscodeCoordinator _presentNewPasscodeVCWithTransitionStyle:];
-[LAPSFetchNewPasscodeCoordinator _presentNewPasscodeVCWithTransitionStyle:errorMessage:];
-[LAPSFetchNewPasscodeCoordinator _presentVerifyPasscodeVCWithTransitionStyle:];
-[LAPSFetchNewPasscodeCoordinator _presentViewController:transitionStyle:];
-[LAPSFetchNewPasscodeCoordinator clearWithErrorMessage:];
-[LAPSFetchNewPasscodeCoordinator continueWithPasscode:];
-[LAPSFetchNewPasscodeCoordinator finishWithPasscode:];
-[LAPSFetchNewPasscodeCoordinator passcodeViewController:didCancelWithError:];
-[LAPSFetchNewPasscodeCoordinator passcodeViewController:didSelectPasscodeType:];
-[LAPSFetchNewPasscodeCoordinator passcodeViewController:didSetPasscodeRecoveryEnabled:];
-[LAPSFetchNewPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:];
-[LAPSFetchNewPasscodeCoordinator restartWithErrorMessage:];
-[LAPSFetchNewPasscodeCoordinator startWithInput:presentationController:completion:];
```
