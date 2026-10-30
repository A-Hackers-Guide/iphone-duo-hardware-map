# `JFXReaderWriterExportController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXExportController`
- 2 instance variables, 2 properties, 18 instance methods, 0 class methods

## Instance variables

```
f _progress;
@"PVVideoCompositing" _customCompositor;
```

## Properties

```
@property (Tf,N,V_progress) progress;
@property (T@"PVVideoCompositing",&,N,V_customCompositor) customCompositor;
```

## Instance methods

```
-[JFXReaderWriterExportController setProgress:];
-[JFXReaderWriterExportController progress];
-[JFXReaderWriterExportController JFX_continueExportForNextPreset];
-[JFXReaderWriterExportController JFX_videoCompressionSettingsFromAssistant:];
-[JFXReaderWriterExportController applyCompositionAspectRatioToAVPresetSize:compositionSize:];
-[JFXReaderWriterExportController audioCompressionSettings];
-[JFXReaderWriterExportController cancelExportWithStatus:];
-[JFXReaderWriterExportController continueExportAfterDelay];
-[JFXReaderWriterExportController customCompositor];
-[JFXReaderWriterExportController fileTypeFromExtension];
-[JFXReaderWriterExportController mapAssetReaderStatusToExportStatus:];
-[JFXReaderWriterExportController mapAssetWriterStatusToExportStatus:];
-[JFXReaderWriterExportController setCustomCompositor:];
-[JFXReaderWriterExportController transferSampleBuffers:assetReader:assetWriterInput:assetWriter:timeRangeToExport:queue:pass:completionBlock:];
-[JFXReaderWriterExportController updateSessionProgress:];
-[JFXReaderWriterExportController updateStatusAndErrorFromReader:andWriter:];
-[JFXReaderWriterExportController videoCompressionSettings:];
-[JFXReaderWriterExportController videoDecompressionSettingsForVideoCompressionSettings:];
```
