# `VTUIProximityEnrollTrainingView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTUIProximityView`
- 14 instance variables, 12 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SUICOrbView" _orbView;
@"VTUIStyle" _vtStyle;
@"VTPreferences" _vtPrefs;
@"UIButton" _skipButton;
@"UIButton" _dismissButton;
@"VTUICheckMarkView" _checkMark;
@"VTUIPagedLabel" _instructionPagedLabel;
@"UIView" _containerView;
@"UILabel" _statusLabel;
@"UILabel" _pageLabel;
@"UILabel" _instructionPreludeLabel;
@"UIStackView" _instructionStackView;
q _enrollmentStyle;
@"NSArray" _viewConstraints;
```

## Properties

```
@property (T@"NSArray",&,N,V_viewConstraints) viewConstraints;
@property (T@"UIButton",&,N,V_skipButton) skipButton;
@property (T@"UIButton",&,N,V_dismissButton) dismissButton;
@property (T@"VTUICheckMarkView",&,N,V_checkMark) checkMark;
@property (T@"VTUIPagedLabel",&,N,V_instructionPagedLabel) instructionPagedLabel;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UILabel",&,N,V_statusLabel) statusLabel;
@property (T@"UILabel",&,N,V_pageLabel) pageLabel;
@property (T@"SUICOrbView",&,N,V_orbView) orbView;
@property (T@"UILabel",&,N,V_instructionPreludeLabel) instructionPreludeLabel;
@property (T@"UIStackView",&,N,V_instructionStackView) instructionStackView;
@property (Tq,N,V_enrollmentStyle) enrollmentStyle;
```

## Instance methods

```
-[VTUIProximityEnrollTrainingView setContainerView:];
-[VTUIProximityEnrollTrainingView didMoveToWindow];
-[VTUIProximityEnrollTrainingView setSkipButton:];
-[VTUIProximityEnrollTrainingView dealloc];
-[VTUIProximityEnrollTrainingView containerView];
-[VTUIProximityEnrollTrainingView skipButton];
-[VTUIProximityEnrollTrainingView initWithFrame:];
-[VTUIProximityEnrollTrainingView dismissButton];
-[VTUIProximityEnrollTrainingView setDismissButton:];
-[VTUIProximityEnrollTrainingView setStatusLabel:];
-[VTUIProximityEnrollTrainingView statusLabel];
-[VTUIProximityEnrollTrainingView checkMark];
-[VTUIProximityEnrollTrainingView _setupContent];
-[VTUIProximityEnrollTrainingView viewConstraints];
-[VTUIProximityEnrollTrainingView setViewConstraints:];
-[VTUIProximityEnrollTrainingView pageLabel];
-[VTUIProximityEnrollTrainingView setPageLabel:];
-[VTUIProximityEnrollTrainingView enrollmentStyle];
-[VTUIProximityEnrollTrainingView orbView];
-[VTUIProximityEnrollTrainingView _setupConstraintsToSize:];
-[VTUIProximityEnrollTrainingView initWithFrame:forEnrollmentStyle:];
-[VTUIProximityEnrollTrainingView instructionPagedLabel];
-[VTUIProximityEnrollTrainingView instructionPreludeLabel];
-[VTUIProximityEnrollTrainingView instructionStackView];
-[VTUIProximityEnrollTrainingView setCheckMark:];
-[VTUIProximityEnrollTrainingView setEnrollmentStyle:];
-[VTUIProximityEnrollTrainingView setInstructionPagedLabel:];
-[VTUIProximityEnrollTrainingView setInstructionPreludeLabel:];
-[VTUIProximityEnrollTrainingView setInstructionStackView:];
-[VTUIProximityEnrollTrainingView setOrbView:];
```
