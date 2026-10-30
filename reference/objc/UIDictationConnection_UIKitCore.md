# `UIDictationConnection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AFDictationDelegate`
- 15 instance variables, 19 properties, 92 instance methods, 9 class methods

## Instance variables

```
B _receivedMultilingualResultsCommand;
B _offlineOnly;
B _ignoreSpeechRecognitionResults;
B _lowConfidenceAboutLanguageDetection;
I _charBeforeInsertionPointOnDictationStart;
I _charAfterInsertionPointOnDictationStart;
@"<UIDictationConnectionDelegate>" _delegate;
@"<UIDictationConnectionTokenFilterProtocol>" _tokenFilter;
@"AFDictationOptions" _dictationOptions;
@"AFDictationConnection" _connection;
@"NSObject<OS_dispatch_queue>" _analyticsQueue;
@"NSString" _lastUsedPrimaryLanguage;
@"NSString" _lastUsedDetectedLanguage;
@"NSMutableArray" _lastUsedTopLanguages;
@"NSMutableDictionary" _lastReceivedPartials;
```

## Properties

```
@property (T@"AFDictationOptions",&,N,V_dictationOptions) dictationOptions;
@property (T@"AFDictationConnection",&,N,V_connection) connection;
@property (TB,N,V_offlineOnly) offlineOnly;
@property (TB,N,V_ignoreSpeechRecognitionResults) ignoreSpeechRecognitionResults;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_analyticsQueue) analyticsQueue;
@property (T@"NSString",C,N,V_lastUsedPrimaryLanguage) lastUsedPrimaryLanguage;
@property (T@"NSString",C,N,V_lastUsedDetectedLanguage) lastUsedDetectedLanguage;
@property (T@"NSMutableArray",&,N,V_lastUsedTopLanguages) lastUsedTopLanguages;
@property (TB,N,V_lowConfidenceAboutLanguageDetection) lowConfidenceAboutLanguageDetection;
@property (TI,N,V_charBeforeInsertionPointOnDictationStart) charBeforeInsertionPointOnDictationStart;
@property (TI,N,V_charAfterInsertionPointOnDictationStart) charAfterInsertionPointOnDictationStart;
@property (T@"NSMutableDictionary",&,N,V_lastReceivedPartials) lastReceivedPartials;
@property (T@"<UIDictationConnectionDelegate>",W,N,V_delegate) delegate;
@property (T@"<UIDictationConnectionTokenFilterProtocol>",W,N,V_tokenFilter) tokenFilter;
@property (TB,N,V_receivedMultilingualResultsCommand) receivedMultilingualResultsCommand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDictationConnection analytics];
+[UIDictationConnection dictationIsSupportedForLanguageCode:error:];
+[UIDictationConnection _updateFromGlobalOptions:];
+[UIDictationConnection interpretationFromSpeechTokens:startIndex:filterBlock:];
+[UIDictationConnection cacheSupportedDictationLanguages];
+[UIDictationConnection isDictationAvailable];
+[UIDictationConnection dictationRestricted];
+[UIDictationConnection hasSpeechRecognitionPauseAckPhrases:];
+[UIDictationConnection afDelegate:didReceiveSearchResults:recognizedText:stable:final:];
```

## Instance methods

```
-[UIDictationConnection preheat];
-[UIDictationConnection pauseSpeechRecognition];
-[UIDictationConnection synthesizeDidRecognizePhrases:languageModel:correctionIdentifier:];
-[UIDictationConnection requestOfflineDictationSupportForLanguage:completion:];
-[UIDictationConnection dictationConnection:speechRecordingDidFail:];
-[UIDictationConnection offlineOnly];
-[UIDictationConnection receivedMultilingualResultsCommand];
-[UIDictationConnection _createConnectionOptions];
-[UIDictationConnection dictationConnection:didRecognizeVoiceCommandCandidatePackage:nluResult:];
-[UIDictationConnection dictationConnection:didRecognizePhrases:languageModel:correctionIdentifier:];
-[UIDictationConnection setCharBeforeInsertionPointOnDictationStart:];
-[UIDictationConnection resumeSpeechRecognitionWithPrefixText:postfixText:selectedText:];
-[UIDictationConnection getRemoteContentForLayerContextWithId:slotStyle:dictationButtonTag:completionBlock:];
-[UIDictationConnection updateVoiceCommandContextWithPrefixText:postfixText:selectedText:disambiguationActive:cursorInVisibleText:favorCommandSuppression:abortCommandSuppression:undoEvent:];
-[UIDictationConnection suppressLowStorageNotificationForLanguage:suppress:];
-[UIDictationConnection dictationConnection:didRecognizeFinalResultCandidatePackage:];
-[UIDictationConnection preheatEuclidModelWithLanguageCode:clientID:];
-[UIDictationConnection dictationOptions];
-[UIDictationConnection dictationConnnectionDidChangeAvailability:];
-[UIDictationConnection languageDetectionUserContext];
-[UIDictationConnection lastUsedDetectedLanguage];
-[UIDictationConnection setCharAfterInsertionPointOnDictationStart:];
-[UIDictationConnection sendVisualContextAndCorrectionsInfo:interactionIdentifier:];
-[UIDictationConnection dictationSerializedResultWithPhrases:languageModel:];
-[UIDictationConnection setTokenFilter:];
-[UIDictationConnection setOfflineOnly:];
-[UIDictationConnection speechEventTypeForDictationActivationType:];
-[UIDictationConnection setReceivedMultilingualResultsCommand:];
-[UIDictationConnection start];
-[UIDictationConnection logDidAcceptReplacement:replacementLanguageCode:originalText:correctionIdentifier:interactionIdentifier:];
-[UIDictationConnection dictationConnectionSpeechRecognitionDidSucceed:];
-[UIDictationConnection dictationConnection:didRecognizeTokens:languageModel:];
-[UIDictationConnection dictationConnection:didRecognizePartialPackage:nluResult:languageModel:];
-[UIDictationConnection setDictationOptions:];
-[UIDictationConnection setLastReceivedPartials:];
-[UIDictationConnection endSession];
-[UIDictationConnection logDidAcceptDictationResult:reason:result:correctionIdentifier:];
-[UIDictationConnection lowConfidenceAboutLanguageDetection];
-[UIDictationConnection sendSpeechCorrection:interactionIdentifier:];
-[UIDictationConnection analyticsQueue];
-[UIDictationConnection lastUsedPrimaryLanguage];
-[UIDictationConnection prepareSecureTouchWithAuthenticationMessage:];
-[UIDictationConnection setAnalyticsQueue:];
-[UIDictationConnection setDelegate:];
-[UIDictationConnection _startWithOptions:];
-[UIDictationConnection supportNewVoiceEditingCommandSPI];
-[UIDictationConnection dictationConnectionSpeechRecordingDidBegin:];
-[UIDictationConnection setLowConfidenceAboutLanguageDetection:];
-[UIDictationConnection speechMessageContexts];
-[UIDictationConnection startForFileAtURL:forLanguage:];
-[UIDictationConnection dictationConnection:didRecognizePartialResult:];
-[UIDictationConnection dictationConnectionDidPauseRecognition:];
-[UIDictationConnection setIgnoreSpeechRecognitionResults:];
-[UIDictationConnection connection];
-[UIDictationConnection dictationConnection:languageDetectorFailedWithError:];
-[UIDictationConnection delegate];
-[UIDictationConnection dictationConnectionSpeechRecordingWillBegin:];
-[UIDictationConnection logDidShowAlternatives:correctionIdentifier:interactionIdentifier:];
-[UIDictationConnection tokenFilter];
-[UIDictationConnection updateVoiceCommandContextWithPrefixText:postfixText:selectedText:disambiguationActive:cursorInVisibleText:favorCommandSuppression:abortCommandSuppression:];
-[UIDictationConnection beginAvailabilityMonitoring];
-[UIDictationConnection setConnection:];
-[UIDictationConnection dictationConnection:speechRecordingDidBeginWithOptions:];
-[UIDictationConnection cancelSpeech];
-[UIDictationConnection dictationConnection:didRecognizeMultilingualSpeech:];
-[UIDictationConnection dictationConnection:didReceiveSearchResults:recognizedText:stable:final:];
-[UIDictationConnection logDidSelectAlternative:correctionIdentifier:interactionIdentifier:];
-[UIDictationConnection dictationConnection:didDetectLanguage:confidenceScores:isConfident:];
-[UIDictationConnection charAfterInsertionPointOnDictationStart];
-[UIDictationConnection dictationConnectionSpeechRecordingDidEnd:];
-[UIDictationConnection averagePower];
-[UIDictationConnection euclidPhoneticString:maxResultsCount:completion:];
-[UIDictationConnection _speechOptions:];
-[UIDictationConnection lastUsedTopLanguages];
-[UIDictationConnection dictationIsAvailableForLanguage:];
-[UIDictationConnection cancelAvailabilityMonitoring];
-[UIDictationConnection charBeforeInsertionPointOnDictationStart];
-[UIDictationConnection _dictationOptions:];
-[UIDictationConnection setLastUsedDetectedLanguage:];
-[UIDictationConnection synthesizeDidRecognizeTokens:languageModel:];
-[UIDictationConnection setLastUsedTopLanguages:];
-[UIDictationConnection sendSpeechCorrection:forIdentifier:];
-[UIDictationConnection ignoreSpeechRecognitionResults];
-[UIDictationConnection dictationConnectionSpeechRecordingDidCancel:];
-[UIDictationConnection stopSpeech:activationType:result:suppressAlert:];
-[UIDictationConnection dictationConnection:speechRecognitionDidFail:];
-[UIDictationConnection dictationConnection:didBeginLocalRecognitionWithModelInfo:];
-[UIDictationConnection setLastUsedPrimaryLanguage:];
-[UIDictationConnection isSecureInput];
-[UIDictationConnection _initializeWithOptions:];
-[UIDictationConnection lastReceivedPartials];
-[UIDictationConnection prepareSecureTouchWithProvenance:];
```
