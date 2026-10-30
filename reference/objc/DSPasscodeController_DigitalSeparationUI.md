# `DSPasscodeController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSOBWelcomeController`
- Protocols: `LARatchetViewControllerDelegate`, `DSController`
- 4 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"LARatchetViewController" _ratchetVC;
@"<DSNavigationDelegate>" _delegate;
@"OBBoldTrayButton" _boldButton;
@"OBLinkTrayButton" _linkButton;
```

## Properties

```
@property (T@"OBBoldTrayButton",&,N,V_boldButton) boldButton;
@property (T@"OBLinkTrayButton",&,N,V_linkButton) linkButton;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSPasscodeController isPasscodeSet];
```

## Instance methods

```
-[DSPasscodeController detailText];
-[DSPasscodeController init];
-[DSPasscodeController viewWillAppear:];
-[DSPasscodeController setDelegate:];
-[DSPasscodeController setBoldButton:];
-[DSPasscodeController delegate];
-[DSPasscodeController boldButton];
-[DSPasscodeController linkButton];
-[DSPasscodeController configureViews];
-[DSPasscodeController setLinkButton:];
-[DSPasscodeController ratchetViewController:didFinishWithResult:error:];
-[DSPasscodeController displayPasscodeChangeSheet];
-[DSPasscodeController passcodeChangePressed];
-[DSPasscodeController shouldShowWithCompletion:];
-[DSPasscodeController startRatchetEvalInPresentationContext:];
-[DSPasscodeController userDidTapCancelButton:];
```
