# `LAPSPasscodeOptionsAlertViewController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAlertController`
- Protocols: `LAPSPasscodeOptionsViewController`
- 2 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"LACUIPasscodeServiceOptionsViewConfiguration" _config;
@"<LAPSPasscodeOptionsViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<LAPSPasscodeOptionsViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LAPSPasscodeOptionsAlertViewController _dismiss];
-[LAPSPasscodeOptionsAlertViewController _setup];
-[LAPSPasscodeOptionsAlertViewController viewWillDisappear:];
-[LAPSPasscodeOptionsAlertViewController supportedInterfaceOrientations];
-[LAPSPasscodeOptionsAlertViewController viewDidLoad];
-[LAPSPasscodeOptionsAlertViewController initWithConfiguration:];
-[LAPSPasscodeOptionsAlertViewController _canShowWhileLocked];
-[LAPSPasscodeOptionsAlertViewController setDelegate:];
-[LAPSPasscodeOptionsAlertViewController delegate];
-[LAPSPasscodeOptionsAlertViewController viewDidDisappear:];
-[LAPSPasscodeOptionsAlertViewController _addActionForPasscodeType:];
-[LAPSPasscodeOptionsAlertViewController _addActionForRecoveryEnabled:restricted:];
-[LAPSPasscodeOptionsAlertViewController _addActionWithTitle:style:completion:];
-[LAPSPasscodeOptionsAlertViewController _setActionWithTitle:enabled:];
```
