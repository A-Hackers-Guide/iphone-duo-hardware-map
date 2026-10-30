# `VTUIVoiceSelectionProximityView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- Protocols: `VTUIVoiceSelectionContaining`
- 13 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _orbImage;
@"VTUIProximityContainerView" _containerView;
@"UILabel" _titleLabel;
@"UIView" _footerView;
@"UIView" _contentView;
@"VTUIStyle" _vtStyle;
B _allowsRandomVoiceSelection;
q _selectionStyle;
B _isHidingCompactBackgroundCardView;
@"UIButton" _continueButton;
@"UIButton" _chooseRandomVoiceButton;
@"UIButton" _dismissButton;
@"NSArray" _constraints;
```

## Properties

```
@property (T@"NSArray",&,N,V_constraints) constraints;
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
-[VTUIVoiceSelectionProximityView setContentView:];
-[VTUIVoiceSelectionProximityView constraints];
-[VTUIVoiceSelectionProximityView intrinsicContentSize];
-[VTUIVoiceSelectionProximityView setConstraints:];
-[VTUIVoiceSelectionProximityView pointInside:withEvent:];
-[VTUIVoiceSelectionProximityView continueButton];
-[VTUIVoiceSelectionProximityView dismissButton];
-[VTUIVoiceSelectionProximityView setContinueButton:];
-[VTUIVoiceSelectionProximityView setDismissButton:];
-[VTUIVoiceSelectionProximityView viewConstraints];
-[VTUIVoiceSelectionProximityView _setupConstraintsToSize:];
-[VTUIVoiceSelectionProximityView _setupContentWithTitle:];
-[VTUIVoiceSelectionProximityView chooseRandomVoiceButton];
-[VTUIVoiceSelectionProximityView initWithTitle:allowsRandomVoiceSelection:forSelectionStyle:];
-[VTUIVoiceSelectionProximityView setChooseRandomVoiceButton:];
-[VTUIVoiceSelectionProximityView setShouldHideCompactBackgroundCardView:];
```
