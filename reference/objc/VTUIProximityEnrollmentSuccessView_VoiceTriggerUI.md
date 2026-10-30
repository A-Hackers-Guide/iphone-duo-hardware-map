# `VTUIProximityEnrollmentSuccessView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- 9 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _languageCode;
@"UIImageView" _orbImage;
@"UILabel" _subtitleLabel;
@"UILabel" _titleLabel;
@"VTUIProximityContainerView" _containerView;
@"VTUIStyle" _vtStyle;
@"VTUIButton" _continueButton;
@"UIButton" _dismissButton;
@"NSArray" _viewConstraints;
```

## Properties

```
@property (T@"NSArray",&,N,V_viewConstraints) viewConstraints;
@property (T@"VTUIButton",R,N,V_continueButton) continueButton;
@property (T@"UIButton",&,N,V_dismissButton) dismissButton;
```

## Instance methods

```
-[VTUIProximityEnrollmentSuccessView initWithFrame:];
-[VTUIProximityEnrollmentSuccessView continueButton];
-[VTUIProximityEnrollmentSuccessView dismissButton];
-[VTUIProximityEnrollmentSuccessView setDismissButton:];
-[VTUIProximityEnrollmentSuccessView _setupContent];
-[VTUIProximityEnrollmentSuccessView viewConstraints];
-[VTUIProximityEnrollmentSuccessView setViewConstraints:];
-[VTUIProximityEnrollmentSuccessView _setupPhoneLandscapeConstraints];
-[VTUIProximityEnrollmentSuccessView _setupConstraintsToSize:];
-[VTUIProximityEnrollmentSuccessView _setupPortraitConstraints];
```
