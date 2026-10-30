# `JFXExportController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 38 instance methods, 5 class methods

## Instance variables

```
B _cancel;
Q _exportStartTime;
@"JFXComposition" _composition;
@"NSArray" _presets;
@"NSString" _currentPreset;
@"UIImage" _poster;
@"<JFXExportDelegate>" _delegate;
@"NSString" _exportPath;
@"NSTimer" _progressTimer;
Q _exportingIndexPresets;
q _status;
```

## Properties

```
@property (TQ,V_exportStartTime) exportStartTime;
@property (T@"JFXComposition",&,N,V_composition) composition;
@property (T@"NSArray",&,N,V_presets) presets;
@property (T@"NSString",&,N,V_currentPreset) currentPreset;
@property (T@"UIImage",&,N,V_poster) poster;
@property (T@"<JFXExportDelegate>",&,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_exportPath) exportPath;
@property (T@"NSTimer",&,N,V_progressTimer) progressTimer;
@property (TQ,N,V_exportingIndexPresets) exportingIndexPresets;
@property (Tq,N,V_status) status;
@property (TB,N,V_cancel) cancel;
```

## Class methods

```
+[JFXExportController audioDataRateForPreset:];
+[JFXExportController dataRateForPreset:size:];
+[JFXExportController estimatedFileSizeForDuration:frameRate:preset:size:];
+[JFXExportController presetNameForCGSize:];
+[JFXExportController videoDataRateForPreset:size:];
```

## Instance methods

```
-[JFXExportController setComposition:];
-[JFXExportController stopProgressTimer];
-[JFXExportController poster];
-[JFXExportController currentPreset];
-[JFXExportController startProgressTimer];
-[JFXExportController setPoster:];
-[JFXExportController setCurrentPreset:];
-[JFXExportController status];
-[JFXExportController composition];
-[JFXExportController progress];
-[JFXExportController setDelegate:];
-[JFXExportController delegate];
-[JFXExportController exportDuration];
-[JFXExportController setCancel:];
-[JFXExportController setStatus:];
-[JFXExportController cancel];
-[JFXExportController progressTimer];
-[JFXExportController setProgressTimer:];
-[JFXExportController presets];
-[JFXExportController exportStartTime];
-[JFXExportController analyticsForSessionBegin];
-[JFXExportController analyticsForSessionCompleteWithStatus:];
-[JFXExportController beginAsynchronousExport];
-[JFXExportController cancelExportWithStatus:];
-[JFXExportController closeSessionWithStatus:];
-[JFXExportController continueExportAfterDelay];
-[JFXExportController exportPath];
-[JFXExportController exportingIndexPresets];
-[JFXExportController informDelegateOfCompletion];
-[JFXExportController initWithWithComposition:presets:toFile:poster:delegate:];
-[JFXExportController metadataToAdd];
-[JFXExportController nextPreset];
-[JFXExportController serviceProgressTimer:];
-[JFXExportController setExportPath:];
-[JFXExportController setExportStartTime:];
-[JFXExportController setExportingIndexPresets:];
-[JFXExportController setPresets:];
-[JFXExportController updateProgressViewWithProgress:reduced:];
```
