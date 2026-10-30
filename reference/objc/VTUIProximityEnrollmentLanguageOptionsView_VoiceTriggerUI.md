# `VTUIProximityEnrollmentLanguageOptionsView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- Protocols: `UIPickerViewDataSource`, `UIPickerViewDelegate`
- 11 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _continueButtonsLanguages;
@"VTUIProximityContainerView" _containerView;
@"UILabel" _titleLabel;
@"UILabel" _settingsLabel;
@"UIView" _footerView;
@"UIView" _languagesView;
@"VTUIStyle" _vtStyle;
@"UIPickerView" _languagesPickerView;
@"VTUIButton" _continueButton;
@"UIButton" _dismissButton;
@"NSArray" _viewConstraints;
```

## Properties

```
@property (T@"NSArray",&,N,V_viewConstraints) viewConstraints;
@property (T@"UIPickerView",R,N,V_languagesPickerView) languagesPickerView;
@property (T@"VTUIButton",R,N,V_continueButton) continueButton;
@property (T@"UIButton",&,N,V_dismissButton) dismissButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUIProximityEnrollmentLanguageOptionsView numberOfComponentsInPickerView:];
-[VTUIProximityEnrollmentLanguageOptionsView pickerView:numberOfRowsInComponent:];
-[VTUIProximityEnrollmentLanguageOptionsView continueButton];
-[VTUIProximityEnrollmentLanguageOptionsView dismissButton];
-[VTUIProximityEnrollmentLanguageOptionsView pickerView:titleForRow:forComponent:];
-[VTUIProximityEnrollmentLanguageOptionsView setDismissButton:];
-[VTUIProximityEnrollmentLanguageOptionsView _setupContent];
-[VTUIProximityEnrollmentLanguageOptionsView viewConstraints];
-[VTUIProximityEnrollmentLanguageOptionsView setViewConstraints:];
-[VTUIProximityEnrollmentLanguageOptionsView _setupConstraintsToSize:];
-[VTUIProximityEnrollmentLanguageOptionsView initWithFrame:languageOptions:];
-[VTUIProximityEnrollmentLanguageOptionsView languagesPickerView];
```
