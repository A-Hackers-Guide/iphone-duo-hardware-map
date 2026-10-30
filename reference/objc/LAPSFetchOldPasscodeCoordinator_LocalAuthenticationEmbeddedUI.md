# `LAPSFetchOldPasscodeCoordinator`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUIPasscodeServiceViewControllerDelegate`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"LAPSFetchOldPasscodeCoordinatorInput" _input;
@? _handler;
@"LAPSPasscodeChangeUIPresentationController" _presentationController;
@"LAPSPasscodeBackoffTimerController" _timer;
@"UIViewController<LACUIPasscodeServiceViewControlling>" _passcodeVC;
@"<LAPSFetchOldPasscodeCoordinatorDelegate>" _delegate;
```

## Properties

```
@property (T@"<LAPSFetchOldPasscodeCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LAPSFetchOldPasscodeCoordinator _deactivate];
-[LAPSFetchOldPasscodeCoordinator finishWithError:];
-[LAPSFetchOldPasscodeCoordinator setDelegate:];
-[LAPSFetchOldPasscodeCoordinator delegate];
-[LAPSFetchOldPasscodeCoordinator _invokeHandlerWithOutput:error:];
-[LAPSFetchOldPasscodeCoordinator _invokeHandlerWithError:];
-[LAPSFetchOldPasscodeCoordinator _invokeHandlerWithOutput:];
-[LAPSFetchOldPasscodeCoordinator _presentPasscodeVC];
-[LAPSFetchOldPasscodeCoordinator _presentViewController:transitionStyle:];
-[LAPSFetchOldPasscodeCoordinator finishWithPasscode:];
-[LAPSFetchOldPasscodeCoordinator passcodeViewController:didCancelWithError:];
-[LAPSFetchOldPasscodeCoordinator passcodeViewController:verifyPasscode:passcodeType:];
-[LAPSFetchOldPasscodeCoordinator showPasscodeValidationError:completion:];
-[LAPSFetchOldPasscodeCoordinator startBackoffWithTimeout:];
-[LAPSFetchOldPasscodeCoordinator startWithInput:presentationController:completion:];
```
