# `LAPSPasscodeChangeUICoordinator`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAPSFetchOldPasscodeCoordinatorDelegate`, `LAPSFetchNewPasscodeCoordinatorDelegate`, `LACUIContainerViewControllerDelegate`, `LAPSPasscodeChangeUI`
- 3 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"LAPSPasscodeChangeUIPresentationController" _presentationController;
@"LAPSPasscodeChangeUICoordinatorOptions" _options;
@"<LAPSPasscodeChangeUIDelegate>" delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LAPSPasscodeChangeUIDelegate>",W,N,Vdelegate) delegate;
```

## Instance methods

```
-[LAPSPasscodeChangeUICoordinator setDelegate:];
-[LAPSPasscodeChangeUICoordinator delegate];
-[LAPSPasscodeChangeUICoordinator _alertControllerWithTitle:message:];
-[LAPSPasscodeChangeUICoordinator deactivateWithCompletion:];
-[LAPSPasscodeChangeUICoordinator _localizedDescriptionFromError:];
-[LAPSPasscodeChangeUICoordinator _configurePasscodeSubPromptForConfig:request:];
-[LAPSPasscodeChangeUICoordinator _configureVerifySubPromptForConfig:request:];
-[LAPSPasscodeChangeUICoordinator _presentPasscodeDoesNotMeetRequirementsError:completion:];
-[LAPSPasscodeChangeUICoordinator _presentPasscodeIsTooSimpleErrorWithCompletion:];
-[LAPSPasscodeChangeUICoordinator _presentPasscodesDidNotMatchErrorWithCompletion:];
-[LAPSPasscodeChangeUICoordinator _shouldUseFooterMessages];
-[LAPSPasscodeChangeUICoordinator _subPromptForRequest:];
-[LAPSPasscodeChangeUICoordinator containerViewControllerViewDidDisappear:];
-[LAPSPasscodeChangeUICoordinator fetchNewPasscode:completion:];
-[LAPSPasscodeChangeUICoordinator fetchNewPasscodeCoordinator:verifyPasscode:];
-[LAPSPasscodeChangeUICoordinator fetchNewPasscodeCoordinator:verifyPasscode:matchesPasscode:];
-[LAPSPasscodeChangeUICoordinator fetchOldPasscode:completion:];
-[LAPSPasscodeChangeUICoordinator fetchOldPasscodeCoordinator:backoffMessageForTimeout:];
-[LAPSPasscodeChangeUICoordinator fetchOldPasscodeCoordinator:verifyPasscode:];
-[LAPSPasscodeChangeUICoordinator initWithParentVC:];
-[LAPSPasscodeChangeUICoordinator initWithParentVC:options:];
-[LAPSPasscodeChangeUICoordinator presentAlertWithTitle:message:button:completion:];
```
