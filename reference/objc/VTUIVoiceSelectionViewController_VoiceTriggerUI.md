# `VTUIVoiceSelectionViewController`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SUICVoiceSelectionPresenterDelegate`
- 10 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SUICVoiceSelectionPresenter" _voiceSelectionPresenter;
@"VTUIVoiceSelectionOptionsView" _voiceOptionsView;
@"NSLayoutConstraint" _voiceOptionsViewHeightConstraint;
@"VTUIStyle" _style;
@"<VTUIVoiceSelectionContaining>" _voiceSelectionContainer;
@"AFVoiceInfo" _currentVoiceSelection;
B _allowsRandomSelection;
@"UIBarButtonItem" _continueBarButton;
B shouldReportSelectionOnRandomVoicePlayBackCompletion;
@"<VTUIVoiceSelectionViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<VTUIVoiceSelectionViewControllerDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTUIVoiceSelectionViewController viewWillDisappear:];
-[VTUIVoiceSelectionViewController viewWillAppear:];
-[VTUIVoiceSelectionViewController delegate];
-[VTUIVoiceSelectionViewController viewWillLayoutSubviews];
-[VTUIVoiceSelectionViewController continueButton];
-[VTUIVoiceSelectionViewController _setupButtons];
-[VTUIVoiceSelectionViewController presenter:didChangeVoiceSelection:];
-[VTUIVoiceSelectionViewController initWithRecognitionLanguage:allowsRandomSelection:barButtonItemForContinue:customVoicePreviewer:delegate:];
-[VTUIVoiceSelectionViewController _chooseForMeButtonClicked];
-[VTUIVoiceSelectionViewController _continueButtonClicked];
-[VTUIVoiceSelectionViewController _dismissButtonClicked];
-[VTUIVoiceSelectionViewController _getDetailedText];
-[VTUIVoiceSelectionViewController _getTitle];
-[VTUIVoiceSelectionViewController _informDelegateVoiceWasSelected:randomlySelected:];
-[VTUIVoiceSelectionViewController _initWithTitle:detailText:recognitionLanguage:compact:allowsRandomSelection:forSelectionStyle:barButtonItemForContinue:dataManager:customVoicePreviewer:delegate:];
-[VTUIVoiceSelectionViewController _setupContentForRecognitionLanguage:dataManager:customVoicePreviewer:];
-[VTUIVoiceSelectionViewController _setupWithTitle:detailText:allowsRandomSelection:compact:forSelectionStyle:];
-[VTUIVoiceSelectionViewController chooseForMeButton];
-[VTUIVoiceSelectionViewController initCompactWithRecognitionLanguage:allowsRandomSelection:customVoicePreviewer:delegate:];
-[VTUIVoiceSelectionViewController initCompactWithRecognitionLanguage:allowsRandomSelection:dataManager:customVoicePreviewer:delegate:];
-[VTUIVoiceSelectionViewController initCompactWithRecognitionLanguage:allowsRandomSelection:dataManager:customVoicePreviewer:forSelectionStyle:delegate:];
-[VTUIVoiceSelectionViewController initWithRecognitionLanguage:allowsRandomSelection:barButtonItemForContinue:dataManager:customVoicePreviewer:delegate:];
-[VTUIVoiceSelectionViewController setShouldHideCompactBackgroundCardView:];
-[VTUIVoiceSelectionViewController updateContainerConstraintsForOrientationChangeToSize:];
```
