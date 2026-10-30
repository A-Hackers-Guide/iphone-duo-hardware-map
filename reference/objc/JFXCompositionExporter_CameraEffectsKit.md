# `JFXCompositionExporter`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXExportDelegate`
- 6 instance variables, 11 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"<JFXExportDelegate>" _delegate;
@"<JFXCompositionPlayableElementsDataSource>" _clipsDataSource;
@"JFXComposition" _composition;
@"JFXReaderWriterExportController" _exportController;
@"NSDate" _exportStartTime;
@"NSDate" _exportEndTime;
```

## Properties

```
@property (T@"JFXComposition",&,N,V_composition) composition;
@property (T@"JFXReaderWriterExportController",&,N,V_exportController) exportController;
@property (T@"NSDate",&,V_exportStartTime) exportStartTime;
@property (T@"NSDate",&,V_exportEndTime) exportEndTime;
@property (T@"<JFXExportDelegate>",&,N,V_delegate) delegate;
@property (TI,N) parentCode;
@property (T@"<JFXCompositionPlayableElementsDataSource>",R,N,V_clipsDataSource) clipsDataSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[JFXCompositionExporter compositionClass];
```

## Instance methods

```
-[JFXCompositionExporter setComposition:];
-[JFXCompositionExporter tearDown];
-[JFXCompositionExporter dealloc];
-[JFXCompositionExporter composition];
-[JFXCompositionExporter setDelegate:];
-[JFXCompositionExporter delegate];
-[JFXCompositionExporter exportStartTime];
-[JFXCompositionExporter clipsDataSource];
-[JFXCompositionExporter exportAnalyticsForSessionCompleteWithStatus:exportMachDuration:];
-[JFXCompositionExporter cancelWithStatus:];
-[JFXCompositionExporter didFinishExport:];
-[JFXCompositionExporter estimatedFileSizeForDuration:frameRate:preset:];
-[JFXCompositionExporter exportAnalyticsForSessionBegin];
-[JFXCompositionExporter exportController];
-[JFXCompositionExporter exportEndTime];
-[JFXCompositionExporter exportProgressedTo:];
-[JFXCompositionExporter initWithClipsDataSource:];
-[JFXCompositionExporter parentCode];
-[JFXCompositionExporter setExportController:];
-[JFXCompositionExporter setExportEndTime:];
-[JFXCompositionExporter setExportStartTime:];
-[JFXCompositionExporter setParentCode:];
-[JFXCompositionExporter startWithPresets:toFilePath:poster:];
-[JFXCompositionExporter timeElapsedDuringExport];
```
