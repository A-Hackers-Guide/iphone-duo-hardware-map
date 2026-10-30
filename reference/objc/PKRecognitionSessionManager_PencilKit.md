# `PKRecognitionSessionManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHRecognitionSessionDataSource`, `CHRecognitionSessionObserver`, `PKDataDetectorQueryDelegate`, `PKHashtagQueryDelegate`, `PKMentionQueryDelegate`, `PKGroupQueryDelegate`, `PKProofreadingQueryDelegate`, `PKAutoRefineQueryDelegate`
- 34 instance variables, 5 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _shouldLoadAndSaveSession;
Aq _stateAtomic;
@"NSObject<OS_dispatch_queue>" _recognitionSessionQueue;
@"PKDrawing" _drawingForGetter;
@"PKDrawing" q_drawing;
@"CHRecognitionSession" q_session;
@"<CHSynthesizingTextWithLocaleFallback>" q_textSynthesizerWithLocaleFallback;
@"<CHSynthesizingText>" q_textSynthesizer;
@"NSDate" q_previousTime;
@"<CHCalculateDocumentProvider>" q_calculateDocumentProvider;
@"<CHCanvasAttachmentProvider>" q_canvasAttachmentProvider;
@"PKHandwritingTranscriptionCache" q_transcriptionCache;
@"PKHandwritingTranscriptionCache" q_stagingTranscriptionCache;
@"NSArray" q_visibleOnscreenStrokes;
B q_wantsGrouping;
B q_wantsDataDetection;
B q_wantsHashtagDetection;
B q_wantsMentionDetection;
B q_wantsProofreadingDetection;
B q_wantsTranscription;
B q_wantsAutoRefine;
@"PKRecognitionQueryController" q_queryController;
@"PKRecognitionSessionObserverWrapper" _observerWrapper;
@"PKAutoRefineQuery" q_autoRefineQuery;
@"PKAutoRefineTaskManager" q_autoRefineManager;
@"NSHashTable" q_listeners;
B _isTearingDown;
@"NSTimer" _proofreadingTimer;
{?="delegateSupportsFoundDataDetectorItems"b1"delegateSupportsFoundHashtagItems"b1"delegateSupportsFoundMentionItems"b1"delegateSupportsFoundProofreadingItems"b1"delegateSupportsFoundGroupItems"b1} _delegateFlags;
@"NSUUID" _sessionCacheIdentifier;
@"NSArray" _preferredLocales;
@"<PKRecognitionSessionManagerDelegate>" _delegate;
@"<PKAutoRefineViewDelegate>" _autoRefineViewDelegate;
@"NSSet" _mentionSuffixes;
```

## Properties

```
@property (Tq,N) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKRecognitionSessionManager _localesForPreferredLanguages:];
+[PKRecognitionSessionManager enabledLocales];
+[PKRecognitionSessionManager hasAutoRefineLocaleEnabled];
```

## Instance methods

```
-[PKRecognitionSessionManager listeners];
-[PKRecognitionSessionManager setState:];
-[PKRecognitionSessionManager init];
-[PKRecognitionSessionManager dealloc];
-[PKRecognitionSessionManager textInputDidChange:];
-[PKRecognitionSessionManager state];
-[PKRecognitionSessionManager calculateDocumentProviderSnapshot];
-[PKRecognitionSessionManager canvasAttachmentProviderSnapshot];
-[PKRecognitionSessionManager recognitionSessionDidUpdateRecognitionResult:];
-[PKRecognitionSessionManager strokeProviderSnapshot];
-[PKRecognitionSessionManager autoRefineQuery:didUpdateWithQueryItem:validProviderVersion:];
-[PKRecognitionSessionManager dataDetectorQuery:foundItems:];
-[PKRecognitionSessionManager groupQuery:foundItems:];
-[PKRecognitionSessionManager hashtagQuery:foundItems:];
-[PKRecognitionSessionManager mentionQuery:foundItems:];
-[PKRecognitionSessionManager proofreadingQuery:foundItems:];
-[PKRecognitionSessionManager saveRecognitionSessionIfNecessary];
```
