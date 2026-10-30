# `VTUIEnrollTrainingIntelligentLightView`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 13 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _skipButtonHidden;
B _radarButtonHidden;
@"SUICIntelligentLightLayer" _lightLayer;
@"UILabel" _statusLabel;
@"UIButton" _radarExitButton;
@"<VTUIEnrollTrainingViewDelegate>" _delegate;
@"UIButton" _skipButton;
@"SiriUIContentButton" _radarButton;
@"VTUIPagedLabel" _instructionPagedLabel;
@"AVCaptureSession" _captureSession;
@"_TtC14VoiceTriggerUI27GMEnrollmentTextViewManager" _enrollmentTextViewManager;
@"_TtC14VoiceTriggerUI21GMEnrollmentViewModel" _enrollmentViewModel;
@"BSUICAPackageView" _lightView;
```

## Properties

```
@property (T@"UIButton",&,N,V_skipButton) skipButton;
@property (T@"SiriUIContentButton",&,N,V_radarButton) radarButton;
@property (T@"VTUIPagedLabel",&,N,V_instructionPagedLabel) instructionPagedLabel;
@property (T@"AVCaptureSession",&,N,V_captureSession) captureSession;
@property (T@"_TtC14VoiceTriggerUI27GMEnrollmentTextViewManager",&,N,V_enrollmentTextViewManager) enrollmentTextViewManager;
@property (T@"_TtC14VoiceTriggerUI21GMEnrollmentViewModel",&,N,V_enrollmentViewModel) enrollmentViewModel;
@property (T@"BSUICAPackageView",&,N,V_lightView) lightView;
@property (TB,N,V_skipButtonHidden) skipButtonHidden;
@property (TB,N,V_radarButtonHidden) radarButtonHidden;
@property (T@"SUICIntelligentLightLayer",&,N,V_lightLayer) lightLayer;
@property (T@"UILabel",R,N,V_statusLabel) statusLabel;
@property (T@"UIButton",R,N,V_radarExitButton) radarExitButton;
@property (T@"<VTUIEnrollTrainingViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[VTUIEnrollTrainingIntelligentLightView setSkipButton:];
-[VTUIEnrollTrainingIntelligentLightView dealloc];
-[VTUIEnrollTrainingIntelligentLightView setDelegate:];
-[VTUIEnrollTrainingIntelligentLightView delegate];
-[VTUIEnrollTrainingIntelligentLightView skipButton];
-[VTUIEnrollTrainingIntelligentLightView initWithFrame:];
-[VTUIEnrollTrainingIntelligentLightView _setupUI];
-[VTUIEnrollTrainingIntelligentLightView captureSession];
-[VTUIEnrollTrainingIntelligentLightView setCaptureSession:];
-[VTUIEnrollTrainingIntelligentLightView statusLabel];
-[VTUIEnrollTrainingIntelligentLightView setRadarButton:];
-[VTUIEnrollTrainingIntelligentLightView radarButton];
-[VTUIEnrollTrainingIntelligentLightView radarExitButton];
-[VTUIEnrollTrainingIntelligentLightView animateSuccessfulStepWithCompletion:];
-[VTUIEnrollTrainingIntelligentLightView clearInstructionLabel];
-[VTUIEnrollTrainingIntelligentLightView enrollmentTextViewManager];
-[VTUIEnrollTrainingIntelligentLightView enrollmentViewModel];
-[VTUIEnrollTrainingIntelligentLightView instructionPagedLabel];
-[VTUIEnrollTrainingIntelligentLightView lightLayer];
-[VTUIEnrollTrainingIntelligentLightView lightView];
-[VTUIEnrollTrainingIntelligentLightView radarButtonHidden];
-[VTUIEnrollTrainingIntelligentLightView setContinuationAndPreludeLabelHidden:];
-[VTUIEnrollTrainingIntelligentLightView setContinuationLabel:];
-[VTUIEnrollTrainingIntelligentLightView setContinuationLabelHidden:animated:];
-[VTUIEnrollTrainingIntelligentLightView setEnrollmentTextViewManager:];
-[VTUIEnrollTrainingIntelligentLightView setEnrollmentViewModel:];
-[VTUIEnrollTrainingIntelligentLightView setInstructionPagedLabel:];
-[VTUIEnrollTrainingIntelligentLightView setLightLayer:];
-[VTUIEnrollTrainingIntelligentLightView setLightView:];
-[VTUIEnrollTrainingIntelligentLightView setPreludeLabel:];
-[VTUIEnrollTrainingIntelligentLightView setPreludeLabelHidden:];
-[VTUIEnrollTrainingIntelligentLightView setRadarButtonHidden:];
-[VTUIEnrollTrainingIntelligentLightView setSkipButtonHidden:];
-[VTUIEnrollTrainingIntelligentLightView showRadarExitButton:];
-[VTUIEnrollTrainingIntelligentLightView skipButtonHidden];
-[VTUIEnrollTrainingIntelligentLightView slideInText:afterDelay:completion:];
```
