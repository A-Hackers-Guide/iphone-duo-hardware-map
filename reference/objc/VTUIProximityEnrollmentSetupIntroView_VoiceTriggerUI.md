# `VTUIProximityEnrollmentSetupIntroView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- Protocols: `UITextViewDelegate`
- 14 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _orbImage;
@"VTUIProximityContainerView" _containerView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
@"UITextView" _termsAndConds;
@"VTUIStyle" _vtStyle;
@"SSRVoiceProfileManager" _voiceProfileMgr;
@"NSString" _languageCode;
B _supportsCompactTrigger;
@"<VTUIEnrollmentDelegate>" _enrollmentDelegate;
@"VTUIButton" _setupButton;
@"VTUIButton" _notNowButton;
@"UIButton" _dismissButton;
@"NSArray" _viewConstraints;
```

## Properties

```
@property (T@"NSArray",&,N,V_viewConstraints) viewConstraints;
@property (T@"<VTUIEnrollmentDelegate>",W,N,V_enrollmentDelegate) enrollmentDelegate;
@property (T@"VTUIButton",R,N,V_setupButton) setupButton;
@property (T@"VTUIButton",R,N,V_notNowButton) notNowButton;
@property (T@"UIButton",&,N,V_dismissButton) dismissButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUIProximityEnrollmentSetupIntroView initWithFrame:];
-[VTUIProximityEnrollmentSetupIntroView dismissButton];
-[VTUIProximityEnrollmentSetupIntroView setDismissButton:];
-[VTUIProximityEnrollmentSetupIntroView textView:shouldInteractWithURL:inRange:interaction:];
-[VTUIProximityEnrollmentSetupIntroView setupButton];
-[VTUIProximityEnrollmentSetupIntroView notNowButton];
-[VTUIProximityEnrollmentSetupIntroView _setupContent];
-[VTUIProximityEnrollmentSetupIntroView viewConstraints];
-[VTUIProximityEnrollmentSetupIntroView setViewConstraints:];
-[VTUIProximityEnrollmentSetupIntroView _setupPhoneLandscapeConstraints];
-[VTUIProximityEnrollmentSetupIntroView _setupConstraintsToSize:];
-[VTUIProximityEnrollmentSetupIntroView _setupPortraitConstraints];
-[VTUIProximityEnrollmentSetupIntroView _setupTermsAndConditions];
-[VTUIProximityEnrollmentSetupIntroView enrollmentDelegate];
-[VTUIProximityEnrollmentSetupIntroView setEnrollmentDelegate:];
```
