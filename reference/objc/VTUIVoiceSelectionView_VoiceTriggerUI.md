# `VTUIVoiceSelectionView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIEnrollmentBaseView`
- Protocols: `VTUIVoiceSelectionContaining`
- 6 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIView" _footerView;
B _allowsRandomSelection;
B _shouldShowContinueButton;
@"UIButton" _continueButton;
@"UIButton" _chooseRandomVoiceButton;
@"UIButton" _dismissButton;
```

## Properties

```
@property (T@"UIButton",&,N,V_continueButton) continueButton;
@property (T@"UIButton",&,N,V_chooseRandomVoiceButton) chooseRandomVoiceButton;
@property (T@"UIButton",&,N,V_dismissButton) dismissButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUIVoiceSelectionView footerView];
-[VTUIVoiceSelectionView tintColorDidChange];
-[VTUIVoiceSelectionView continueButton];
-[VTUIVoiceSelectionView dismissButton];
-[VTUIVoiceSelectionView setContinueButton:];
-[VTUIVoiceSelectionView setDismissButton:];
-[VTUIVoiceSelectionView _setupButtons];
-[VTUIVoiceSelectionView chooseRandomVoiceButton];
-[VTUIVoiceSelectionView initWithAllowsRandomVoiceSelection:showContinueButton:];
-[VTUIVoiceSelectionView setChooseRandomVoiceButton:];
```
