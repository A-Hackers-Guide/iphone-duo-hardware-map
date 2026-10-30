# `TPSetPINViewController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `TPSimpleNumberPadDelegate`
- 16 instance variables, 16 properties, 50 instance methods, 0 class methods

## Instance variables

```
B _confirmPIN;
i _initialState;
i _state;
I _minPINLength;
I _maxPINLength;
@"<TPSetPINViewControllerDelegate>" _delegate;
@"NSString" _promptTextForOldPIN;
@"NSString" _promptTextForNewPIN;
@"NSString" _promptTextForConfirmingNewPIN;
@"NSString" _promptTextForSavingPIN;
@"UIView" _customBackgroundView;
@"UILabel" _statusLabel;
@"TPPasscodeView" _passcodeView;
@"TPSimpleNumberPad" _numberPad;
@"NSString" _oldPIN;
@"NSString" _unconfirmedPIN;
```

## Properties

```
@property (Ti,V_initialState) initialState;
@property (Ti,N,V_state) state;
@property (TI,V_minPINLength) minPINLength;
@property (TI,V_maxPINLength) maxPINLength;
@property (TB,V_confirmPIN) confirmPIN;
@property (T@"UILabel",&,V_statusLabel) statusLabel;
@property (T@"TPPasscodeView",&,V_passcodeView) passcodeView;
@property (T@"TPSimpleNumberPad",&,V_numberPad) numberPad;
@property (T@"NSString",&,V_oldPIN) oldPIN;
@property (T@"NSString",&,V_unconfirmedPIN) unconfirmedPIN;
@property (T@"<TPSetPINViewControllerDelegate>",V_delegate) delegate;
@property (T@"NSString",&,N,V_promptTextForOldPIN) promptTextForOldPIN;
@property (T@"NSString",&,N,V_promptTextForNewPIN) promptTextForNewPIN;
@property (T@"NSString",&,N,V_promptTextForConfirmingNewPIN) promptTextForConfirmingNewPIN;
@property (T@"NSString",&,N,V_promptTextForSavingPIN) promptTextForSavingPIN;
@property (T@"UIView",&,V_customBackgroundView) customBackgroundView;
```

## Instance methods

```
-[TPSetPINViewController setCustomBackgroundView:];
-[TPSetPINViewController setState:];
-[TPSetPINViewController init];
-[TPSetPINViewController dealloc];
-[TPSetPINViewController setDelegate:];
-[TPSetPINViewController customBackgroundView];
-[TPSetPINViewController loadView];
-[TPSetPINViewController delegate];
-[TPSetPINViewController setInitialState:];
-[TPSetPINViewController initialState];
-[TPSetPINViewController state];
-[TPSetPINViewController wantsFullScreenLayout];
-[TPSetPINViewController _doneButtonTapped];
-[TPSetPINViewController _cancelButtonTapped];
-[TPSetPINViewController setStatusLabel:];
-[TPSetPINViewController _initForMinLength:maxLength:confirmPIN:];
-[TPSetPINViewController _updateDeleteAllowed];
-[TPSetPINViewController _updateNavBarButtons];
-[TPSetPINViewController _updateStatusLabel];
-[TPSetPINViewController _updateUIForStateChange];
-[TPSetPINViewController confirmPIN];
-[TPSetPINViewController initForChangePINWithMinLength:maxLength:confirmPIN:];
-[TPSetPINViewController initForNewPINWithMinLength:maxLength:confirmPIN:];
-[TPSetPINViewController maxPINLength];
-[TPSetPINViewController minPINLength];
-[TPSetPINViewController numberPad];
-[TPSetPINViewController numberPadTopConstraintConstant];
-[TPSetPINViewController oldPIN];
-[TPSetPINViewController passcodeView];
-[TPSetPINViewController promptTextForConfirmingNewPIN];
-[TPSetPINViewController promptTextForNewPIN];
-[TPSetPINViewController promptTextForOldPIN];
-[TPSetPINViewController promptTextForSavingPIN];
-[TPSetPINViewController resetWithErrorPrompt:];
-[TPSetPINViewController resetWithErrorPrompt:title:];
-[TPSetPINViewController setConfirmPIN:];
-[TPSetPINViewController setMaxPINLength:];
-[TPSetPINViewController setMinPINLength:];
-[TPSetPINViewController setNumberPad:];
-[TPSetPINViewController setOldPIN:];
-[TPSetPINViewController setPasscodeView:];
-[TPSetPINViewController setPromptTextForConfirmingNewPIN:];
-[TPSetPINViewController setPromptTextForNewPIN:];
-[TPSetPINViewController setPromptTextForOldPIN:];
-[TPSetPINViewController setPromptTextForSavingPIN:];
-[TPSetPINViewController setUnconfirmedPIN:];
-[TPSetPINViewController simpleNumberPad:buttonPressedWithCharacter:];
-[TPSetPINViewController simpleNumberPadDeletePressed:];
-[TPSetPINViewController statusLabel];
-[TPSetPINViewController unconfirmedPIN];
```
