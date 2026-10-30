# `PKTextInputDebugLogEntryRerun`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputRecognitionManagerDataSource`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"PKTextInputRecognitionManager" _recognitionManager;
@? _completionBlock;
@"PKTextInputLanguageSpec" _languageSpec;
@"PKTextInputStrokeProvider" _strokeProvider;
@"PKTextInputDebugArchivedLogEntry" _logEntry;
```

## Properties

```
@property (T@"PKTextInputDebugArchivedLogEntry",R,N,V_logEntry) logEntry;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputDebugLogEntryRerun runWithCompletion:];
-[PKTextInputDebugLogEntryRerun logEntry];
-[PKTextInputDebugLogEntryRerun recognitionManager:recognitionDidFinishWithQueryItems:duration:];
-[PKTextInputDebugLogEntryRerun _finishRerunWithQueryItems:error:];
-[PKTextInputDebugLogEntryRerun initWithLogEntry:];
-[PKTextInputDebugLogEntryRerun recognitionManager:fetchContentInfoForTextInputTarget:strokeIdentifiers:completion:];
-[PKTextInputDebugLogEntryRerun recognitionManager:textInputTargetForItemStableIdentifier:strokeIdentifiers:simultaneousItemStableIdentifiers:];
-[PKTextInputDebugLogEntryRerun recognitionManagerStrokeProvider:];
-[PKTextInputDebugLogEntryRerun recognitionManagerTextInputTargets:];
```
