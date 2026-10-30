# `PKTranscriptionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKProgressAlertControllerDelegate`
- 10 instance variables, 10 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _shouldCancel;
B _didReceiveTranscription;
B _didShowHUD;
i _transcriptionType;
@"<PKAttachment>" _attachment;
@"PKStrokeSelection" _strokeSelection;
@"PKRecognitionSessionManager" _recognitionManager;
@"PKProgressAlertController" _progressAlertController;
@"NSProgress" _currentProgress;
@"NSString" _textTranscription;
```

## Properties

```
@property (T@"PKRecognitionSessionManager",W,N,V_recognitionManager) recognitionManager;
@property (T@"PKProgressAlertController",&,N,V_progressAlertController) progressAlertController;
@property (T@"NSProgress",&,N,V_currentProgress) currentProgress;
@property (TB,N,V_shouldCancel) shouldCancel;
@property (TB,N,V_didReceiveTranscription) didReceiveTranscription;
@property (TB,N,V_didShowHUD) didShowHUD;
@property (T@"NSString",C,N,V_textTranscription) textTranscription;
@property (T@"<PKAttachment>",W,N,V_attachment) attachment;
@property (T@"PKStrokeSelection",&,N,V_strokeSelection) strokeSelection;
@property (Ti,N,V_transcriptionType) transcriptionType;
```

## Instance methods

```
-[PKTranscriptionController attachment];
-[PKTranscriptionController observeValueForKeyPath:ofObject:change:context:];
-[PKTranscriptionController setCurrentProgress:];
-[PKTranscriptionController dealloc];
-[PKTranscriptionController setAttachment:];
-[PKTranscriptionController textInputDidChange:];
-[PKTranscriptionController currentProgress];
-[PKTranscriptionController setShouldCancel:];
-[PKTranscriptionController shouldCancel];
-[PKTranscriptionController _progressChanged];
-[PKTranscriptionController strokeSelection];
-[PKTranscriptionController _fetchTranscriptionWithCompletion:];
-[PKTranscriptionController _hideHUD];
-[PKTranscriptionController _receiveTranscription:];
-[PKTranscriptionController _showHUDWithProgress:];
-[PKTranscriptionController _unregisterProgressObserver];
-[PKTranscriptionController alertControllerDidCancel:];
-[PKTranscriptionController cancelAndTeardown];
-[PKTranscriptionController didReceiveTranscription];
-[PKTranscriptionController didShowHUD];
-[PKTranscriptionController findCompleteTranscriptionForNote:];
-[PKTranscriptionController findTranscriptionForType:withCompletion:];
-[PKTranscriptionController initWithRecognitionManager:strokeSelection:attachment:];
-[PKTranscriptionController progressAlertController];
-[PKTranscriptionController recognitionManager];
-[PKTranscriptionController setDidReceiveTranscription:];
-[PKTranscriptionController setDidShowHUD:];
-[PKTranscriptionController setProgressAlertController:];
-[PKTranscriptionController setRecognitionManager:];
-[PKTranscriptionController setStrokeSelection:];
-[PKTranscriptionController setTextTranscription:];
-[PKTranscriptionController setTranscriptionType:];
-[PKTranscriptionController textTranscription];
-[PKTranscriptionController transcriptionType];
```
