# `VTUITurnOnSiriView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIEnrollmentBaseView`
- Protocols: `UITextViewDelegate`
- 6 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _siriLanguages;
@"UIView" _footerView;
@"<VTUITurnOnSiriViewDelegate>" _stateViewDelegate;
@"UIButton" _laterButton;
@"UIButton" _continueButton;
@"NSArray" _continueButtons;
```

## Properties

```
@property (T@"<VTUITurnOnSiriViewDelegate>",W,N,V_stateViewDelegate) stateViewDelegate;
@property (T@"UIButton",R,N,V_laterButton) laterButton;
@property (T@"UIButton",R,N,V_continueButton) continueButton;
@property (T@"NSArray",R,N,V_continueButtons) continueButtons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUITurnOnSiriView footerView];
-[VTUITurnOnSiriView layoutSubviews];
-[VTUITurnOnSiriView initWithFrame:];
-[VTUITurnOnSiriView continueButton];
-[VTUITurnOnSiriView textView:shouldInteractWithURL:inRange:interaction:];
-[VTUITurnOnSiriView laterButton];
-[VTUITurnOnSiriView continueButtons];
-[VTUITurnOnSiriView languageSelectionOfContinueButton:];
-[VTUITurnOnSiriView prepareForLastTimeShown];
-[VTUITurnOnSiriView setStateViewDelegate:];
-[VTUITurnOnSiriView _setupContent];
-[VTUITurnOnSiriView _setupTurnOnSiriUI];
-[VTUITurnOnSiriView imageOffsetFromTop];
-[VTUITurnOnSiriView showPrivacyTextView];
-[VTUITurnOnSiriView stateViewDelegate];
```
