# `SBVoiceControlViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SiriUISuggestionsViewDelegate`, `SUICFlamesViewDelegate`, `VSRecognitionSessionDelegate`
- 22 instance variables, 11 properties, 64 instance methods, 0 class methods

## Instance variables

```
@"NSString" _avAudioRouteName;
@"NSString" _avAudioRouteUID;
@"UIView" _contentView;
@"NSTimer" _delayedConfirmationActionTimer;
@"SUICFlamesView" _flamesView;
B _hasConfiguredRouting;
@"NSDictionary" _localizationKeys;
B _isHeadsetButtonPressedDown;
B _prefersProximityDetectionEnabled;
@"VSRecognitionSession" _session;
@"SBVoiceControlPresentationSource" _source;
q _startingKeywordIndex;
@"UILabel" _subtitleLabel;
@"SiriUISuggestionsView" _suggestionsView;
@"UILabel" _titleLabel;
B _wasRecognizing;
B _shouldAllowSensitiveActions;
B _shouldDisableHandlerActions;
B _shouldDisableVoiceControlForBluetoothRequests;
B _voiceControlLoggingEnabled;
@"NSArray" _nextRecognitionAudioInputPaths;
@"<SBVoiceControlViewControllerDelegate>" _voiceControlDelegate;
```

## Properties

```
@property (T@"NSArray",C,N,V_nextRecognitionAudioInputPaths) nextRecognitionAudioInputPaths;
@property (TB,R,N,V_prefersProximityDetectionEnabled) prefersProximityDetectionEnabled;
@property (TB,N,V_shouldAllowSensitiveActions) shouldAllowSensitiveActions;
@property (TB,N,V_shouldDisableHandlerActions) shouldDisableHandlerActions;
@property (TB,N,V_shouldDisableVoiceControlForBluetoothRequests) shouldDisableVoiceControlForBluetoothRequests;
@property (TB,N,GisVoiceControlLoggingEnabled,V_voiceControlLoggingEnabled) voiceControlLoggingEnabled;
@property (T@"<SBVoiceControlViewControllerDelegate>",W,N,V_voiceControlDelegate) voiceControlDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBVoiceControlViewController initWithSource:];
-[SBVoiceControlViewController viewWillDisappear:];
-[SBVoiceControlViewController dealloc];
-[SBVoiceControlViewController viewDidLoad];
-[SBVoiceControlViewController viewDidLayoutSubviews];
-[SBVoiceControlViewController viewWillAppear:];
-[SBVoiceControlViewController _canShowWhileLocked];
-[SBVoiceControlViewController _setSession:];
-[SBVoiceControlViewController handleHomeButtonPress];
-[SBVoiceControlViewController audioLevelForFlamesView:];
-[SBVoiceControlViewController _requestDismissal];
-[SBVoiceControlViewController _startSession];
-[SBVoiceControlViewController _setStatusText:];
-[SBVoiceControlViewController _localizedStringForKey:];
-[SBVoiceControlViewController _resetSession];
-[SBVoiceControlViewController _flamesViewFrame];
-[SBVoiceControlViewController nextSuggestionsForSuggestionsView:maxSuggestions:];
-[SBVoiceControlViewController recognitionSession:didCompleteActionWithError:];
-[SBVoiceControlViewController recognitionSession:didFinishSpeakingFeedbackStringWithError:];
-[SBVoiceControlViewController recognitionSession:openURL:completion:];
-[SBVoiceControlViewController recognitionSessionDidBeginAction:];
-[SBVoiceControlViewController recognitionSessionWillBeginAction:];
-[SBVoiceControlViewController setShouldAllowSensitiveActions:];
-[SBVoiceControlViewController setShouldDisableHandlerActions:];
-[SBVoiceControlViewController _avSystemControllerHeadphoneJackIsConnectedDidChangeNotification:];
-[SBVoiceControlViewController _avSystemControllerPickableRoutesDidChangeNotification:];
-[SBVoiceControlViewController _availableRouteDictionaries];
-[SBVoiceControlViewController _configureRoutingIfNeeded];
-[SBVoiceControlViewController _continueRecognitionAction];
-[SBVoiceControlViewController _continueWithRecognitionAction];
-[SBVoiceControlViewController _currentPreferredRouteDictionary];
-[SBVoiceControlViewController _deviceProximityStateDidChangeNotification:];
-[SBVoiceControlViewController _handleButtonUpCancel];
-[SBVoiceControlViewController _hasPickableBluetoothDevice];
-[SBVoiceControlViewController _newRecognitionSession];
-[SBVoiceControlViewController _performConfirmationAction];
-[SBVoiceControlViewController _performNoMatchFound];
-[SBVoiceControlViewController _popNextRecognitionAudioInputPath];
-[SBVoiceControlViewController _preferredRouteDictionaryWithAvailableRouteDictionaries:preferredAVAudioRouteName:preferredAVAudioRouteUID:shouldPreferBluetooth:];
-[SBVoiceControlViewController _recognitionSessionKeywordsDidChangeNotification:];
-[SBVoiceControlViewController _setAVAudioRouteUID:];
-[SBVoiceControlViewController _setFeedbackVisible:animated:];
-[SBVoiceControlViewController _setNeedsRoutingUpdate];
-[SBVoiceControlViewController _setPrefersProximityDetectionEnabled:];
-[SBVoiceControlViewController _setTitleText:];
-[SBVoiceControlViewController _speakFeedbackText];
-[SBVoiceControlViewController _speakText:];
-[SBVoiceControlViewController _subtitleBaseline];
-[SBVoiceControlViewController _titleBaseline];
-[SBVoiceControlViewController handleHeadsetButtonUpFromButtonDownSource:];
-[SBVoiceControlViewController isVoiceControlLoggingEnabled];
-[SBVoiceControlViewController nextRecognitionAudioInputPaths];
-[SBVoiceControlViewController performDismissalTransitionAnimated:completionHandler:];
-[SBVoiceControlViewController performPresentationTransitionAnimated:completionHandler:];
-[SBVoiceControlViewController prefersProximityDetectionEnabled];
-[SBVoiceControlViewController resetSessionWithSource:];
-[SBVoiceControlViewController setNextRecognitionAudioInputPaths:];
-[SBVoiceControlViewController setShouldDisableVoiceControlForBluetoothRequests:];
-[SBVoiceControlViewController setVoiceControlDelegate:];
-[SBVoiceControlViewController setVoiceControlLoggingEnabled:];
-[SBVoiceControlViewController shouldAllowSensitiveActions];
-[SBVoiceControlViewController shouldDisableHandlerActions];
-[SBVoiceControlViewController shouldDisableVoiceControlForBluetoothRequests];
-[SBVoiceControlViewController voiceControlDelegate];
```
