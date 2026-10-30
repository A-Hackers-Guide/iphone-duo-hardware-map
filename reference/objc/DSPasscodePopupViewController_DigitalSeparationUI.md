# `DSPasscodePopupViewController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BFFPasscodeInputViewDelegate`
- 11 instance variables, 15 properties, 51 instance methods, 1 class methods

## Instance variables

```
B _numeric;
@"<DSNavigationDelegate>" _delegate;
q _passcodeState;
@"NSData" _passcodeContextOld;
@"NSData" _passcodeContextNew;
@"NSString" _passcodeNew;
Q _numericLength;
@"BFFPasscodeView" _passcodeView;
@"NSLayoutConstraint" _contentHeightConstraint;
@"UIAlertController" _passcodeOptionAlertController;
@"<DSPairedComputerStoreProtocol>" _pairedComputerStore;
```

## Properties

```
@property (Tq,N,V_passcodeState) passcodeState;
@property (T@"NSData",&,N,V_passcodeContextOld) passcodeContextOld;
@property (T@"NSData",&,N,V_passcodeContextNew) passcodeContextNew;
@property (T@"NSString",&,N,V_passcodeNew) passcodeNew;
@property (TB,N,GisNumeric,V_numeric) numeric;
@property (TQ,N,V_numericLength) numericLength;
@property (T@"BFFPasscodeView",&,N,V_passcodeView) passcodeView;
@property (T@"NSLayoutConstraint",&,N,V_contentHeightConstraint) contentHeightConstraint;
@property (T@"UIAlertController",&,N,V_passcodeOptionAlertController) passcodeOptionAlertController;
@property (T@"<DSPairedComputerStoreProtocol>",&,N,V_pairedComputerStore) pairedComputerStore;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSPasscodePopupViewController isPasscodeSet];
```

## Instance methods

```
-[DSPasscodePopupViewController init];
-[DSPasscodePopupViewController viewDidLoad];
-[DSPasscodePopupViewController reset];
-[DSPasscodePopupViewController setDelegate:];
-[DSPasscodePopupViewController delegate];
-[DSPasscodePopupViewController contentHeightConstraint];
-[DSPasscodePopupViewController keyboardDidShow:];
-[DSPasscodePopupViewController isNumeric];
-[DSPasscodePopupViewController setNumeric:];
-[DSPasscodePopupViewController passcodeView];
-[DSPasscodePopupViewController setPasscodeView:];
-[DSPasscodePopupViewController _createAndShowAnimatedNavBarSpinner];
-[DSPasscodePopupViewController setContentHeightConstraint:];
-[DSPasscodePopupViewController passcodeInput:enteredPasscode:];
-[DSPasscodePopupViewController passcodeInputView];
-[DSPasscodePopupViewController _applyPasscode];
-[DSPasscodePopupViewController nextButtonTapped];
-[DSPasscodePopupViewController passcodeInput:tappedFooterButton:];
-[DSPasscodePopupViewController setPasscodeNew:];
-[DSPasscodePopupViewController _animatePasscodeViewTransition];
-[DSPasscodePopupViewController _commitPasscodeEntryTypeChange];
-[DSPasscodePopupViewController _setupFirstEntry];
-[DSPasscodePopupViewController _showPasswordRequirementAlertWithText:];
-[DSPasscodePopupViewController _showWeakWarningAlert];
-[DSPasscodePopupViewController _transitionToPasscodePaneWithState:animationType:];
-[DSPasscodePopupViewController acceptWeakPasscode:];
-[DSPasscodePopupViewController configurePasscodeOptionsSheet];
-[DSPasscodePopupViewController configurePasscodeTypeUsingAnimations:];
-[DSPasscodePopupViewController handleCurrentPasscodeEntry:];
-[DSPasscodePopupViewController handleNewPasscodeEntry:];
-[DSPasscodePopupViewController handlePasscodeConfirmationEntry:];
-[DSPasscodePopupViewController handlePasscodeDoesNotMeetConstraints:];
-[DSPasscodePopupViewController makeContextForPasscode:completion:];
-[DSPasscodePopupViewController numericLength];
-[DSPasscodePopupViewController optionsSheetIsEmpty];
-[DSPasscodePopupViewController pairedComputerStore];
-[DSPasscodePopupViewController passcodeContextNew];
-[DSPasscodePopupViewController passcodeContextOld];
-[DSPasscodePopupViewController passcodeNew];
-[DSPasscodePopupViewController passcodeOptionAlertController];
-[DSPasscodePopupViewController passcodeState];
-[DSPasscodePopupViewController pushNextPane];
-[DSPasscodePopupViewController setNumericLength:];
-[DSPasscodePopupViewController setPairedComputerStore:];
-[DSPasscodePopupViewController setPasscodeContextNew:];
-[DSPasscodePopupViewController setPasscodeContextOld:];
-[DSPasscodePopupViewController setPasscodeOptionAlertController:];
-[DSPasscodePopupViewController setPasscodeState:];
-[DSPasscodePopupViewController userEnteredPasscode:];
-[DSPasscodePopupViewController usesSimplePasscodeEntry];
-[DSPasscodePopupViewController validatePIN:context:];
```
