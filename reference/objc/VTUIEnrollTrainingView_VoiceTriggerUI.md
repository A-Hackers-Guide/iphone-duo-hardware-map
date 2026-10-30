# `VTUIEnrollTrainingView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _skipButtonHidden;
B _checkMarkViewHidden;
B _radarButtonHidden;
@"SUICOrbView" _orbView;
@"UILabel" _statusLabel;
@"UILabel" _instructionPreludeLabel;
@"UILabel" _instructionContinuationLabel;
@"UIButton" _radarExitButton;
@"<VTUIEnrollTrainingViewDelegate>" _delegate;
@"UIButton" _skipButton;
@"VTUICheckMarkView" _checkMark;
@"VTUIPagedLabel" _instructionPagedLabel;
@"SiriUIContentButton" _radarButton;
```

## Properties

```
@property (T@"UIButton",&,N,V_skipButton) skipButton;
@property (T@"VTUICheckMarkView",&,N,V_checkMark) checkMark;
@property (T@"VTUIPagedLabel",&,N,V_instructionPagedLabel) instructionPagedLabel;
@property (T@"SiriUIContentButton",&,N,V_radarButton) radarButton;
@property (TB,N,V_skipButtonHidden) skipButtonHidden;
@property (TB,N,V_checkMarkViewHidden) checkMarkViewHidden;
@property (TB,N,V_radarButtonHidden) radarButtonHidden;
@property (T@"SUICOrbView",R,N,V_orbView) orbView;
@property (T@"UILabel",R,N,V_statusLabel) statusLabel;
@property (T@"UILabel",R,N,V_instructionPreludeLabel) instructionPreludeLabel;
@property (T@"UILabel",R,N,V_instructionContinuationLabel) instructionContinuationLabel;
@property (T@"UIButton",R,N,V_radarExitButton) radarExitButton;
@property (T@"<VTUIEnrollTrainingViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[VTUIEnrollTrainingView setSkipButton:];
-[VTUIEnrollTrainingView dealloc];
-[VTUIEnrollTrainingView setDelegate:];
-[VTUIEnrollTrainingView delegate];
-[VTUIEnrollTrainingView skipButton];
-[VTUIEnrollTrainingView initWithFrame:];
-[VTUIEnrollTrainingView _setupUI];
-[VTUIEnrollTrainingView statusLabel];
-[VTUIEnrollTrainingView checkMark];
-[VTUIEnrollTrainingView setRadarButton:];
-[VTUIEnrollTrainingView radarButton];
-[VTUIEnrollTrainingView orbView];
-[VTUIEnrollTrainingView radarExitButton];
-[VTUIEnrollTrainingView checkMarkViewHidden];
-[VTUIEnrollTrainingView clearInstructionLabel];
-[VTUIEnrollTrainingView instructionContinuationLabel];
-[VTUIEnrollTrainingView instructionPagedLabel];
-[VTUIEnrollTrainingView instructionPreludeLabel];
-[VTUIEnrollTrainingView radarButtonHidden];
-[VTUIEnrollTrainingView setCheckMark:];
-[VTUIEnrollTrainingView setCheckMarkViewHidden:];
-[VTUIEnrollTrainingView setContinuationAndPreludeLabelHidden:];
-[VTUIEnrollTrainingView setContinuationLabelHidden:animated:];
-[VTUIEnrollTrainingView setInstructionPagedLabel:];
-[VTUIEnrollTrainingView setPreludeLabelHidden:];
-[VTUIEnrollTrainingView setRadarButtonHidden:];
-[VTUIEnrollTrainingView setSkipButtonHidden:];
-[VTUIEnrollTrainingView showRadarExitButton:];
-[VTUIEnrollTrainingView skipButtonHidden];
-[VTUIEnrollTrainingView slideInText:afterDelay:completion:];
-[VTUIEnrollTrainingView startCheckMarkAnimation:completion:];
```
