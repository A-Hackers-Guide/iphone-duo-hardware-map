# `LACUIPasscodeField`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITextFieldDelegate`
- 14 instance variables, 12 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"UIStackView" _mainContainer;
@"UIView" _passcodeFieldContainer;
@"UIImpactFeedbackGenerator" _hapticGenerator;
@"UIButton" _submitButton;
@"<LACUIPasscodeFieldConfiguring>" _configurator;
@"NSMutableArray" _fieldLayouts;
@"LACUIPasscodeFieldLayout" _currentFieldLayout;
B _canShowInLockScreen;
B _ignoreInputs;
B _hasAlphanumericPasscode;
@"NSString" _placeholderText;
@"<LACUIPasscodeFieldDelegate>" _delegate;
q _style;
Q _passcodeLength;
```

## Properties

```
@property (TB,N,V_ignoreInputs) ignoreInputs;
@property (T@"LAUITextField",R,W,N) passcodeField;
@property (TQ,R,N,V_passcodeLength) passcodeLength;
@property (TB,R,N,V_hasAlphanumericPasscode) hasAlphanumericPasscode;
@property (T@"NSString",&,N,V_placeholderText) placeholderText;
@property (T@"<LACUIPasscodeFieldDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_style) style;
@property (TB,N,V_canShowInLockScreen) canShowInLockScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUIPasscodeField _setup];
-[LACUIPasscodeField textField:editMenuForCharactersInRange:suggestedActions:];
-[LACUIPasscodeField clear];
-[LACUIPasscodeField viewWillDisappear:];
-[LACUIPasscodeField pressesEnded:withEvent:];
-[LACUIPasscodeField submit];
-[LACUIPasscodeField becomeFirstResponder];
-[LACUIPasscodeField viewDidLoad];
-[LACUIPasscodeField initWithStyle:];
-[LACUIPasscodeField resignFirstResponder];
-[LACUIPasscodeField style];
-[LACUIPasscodeField setStyle:];
-[LACUIPasscodeField textFieldShouldBeginEditing:];
-[LACUIPasscodeField textFieldShouldReturn:];
-[LACUIPasscodeField _canShowWhileLocked];
-[LACUIPasscodeField setDelegate:];
-[LACUIPasscodeField textField:shouldChangeCharactersInRange:replacementString:];
-[LACUIPasscodeField delegate];
-[LACUIPasscodeField canBecomeFirstResponder];
-[LACUIPasscodeField textFieldDidChange:];
-[LACUIPasscodeField placeholderText];
-[LACUIPasscodeField setPlaceholderText:];
-[LACUIPasscodeField passcodeLength];
-[LACUIPasscodeField passcodeField];
-[LACUIPasscodeField setAcceptInputs:];
-[LACUIPasscodeField setCanShowInLockScreen:];
-[LACUIPasscodeField shakeWithCompletion:];
-[LACUIPasscodeField _passcodeLength];
-[LACUIPasscodeField _activateFieldLayoutForSelectedPasscodeStyle];
-[LACUIPasscodeField _alphanumericFieldPlaceholder];
-[LACUIPasscodeField _applyStyleToFieldLayout];
-[LACUIPasscodeField _handleTraitChanges];
-[LACUIPasscodeField _notifyPasscodeFieldLengthChange];
-[LACUIPasscodeField _passcodeFieldColor];
-[LACUIPasscodeField _passcodeLengthForStyle:];
-[LACUIPasscodeField _selectPasscodeField:];
-[LACUIPasscodeField _shouldShowSubmitButtonForStyle:];
-[LACUIPasscodeField _shouldUseAlphanumericKeyboard];
-[LACUIPasscodeField _shouldUseAlphanumericKeyboardForStyle:];
-[LACUIPasscodeField _shouldUseDotPattern];
-[LACUIPasscodeField _shouldUseDotPatternForStyle:];
-[LACUIPasscodeField _textAlignment];
-[LACUIPasscodeField _updateDotPattern];
-[LACUIPasscodeField _verifyTextField:];
-[LACUIPasscodeField canShowInLockScreen];
-[LACUIPasscodeField hasAlphanumericPasscode];
-[LACUIPasscodeField ignoreInputs];
-[LACUIPasscodeField setIgnoreInputs:];
```
