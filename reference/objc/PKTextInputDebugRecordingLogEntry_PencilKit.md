# `PKTextInputDebugRecordingLogEntry`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKTextInputDebugLogEntry`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"CHTextInputQueryItem" __resultQueryItem;
@"PKDrawing" __originalDrawing;
```

## Properties

```
@property (T@"CHTextInputQueryItem",&,N,V__resultQueryItem) _resultQueryItem;
@property (T@"PKDrawing",&,N,V__originalDrawing) _originalDrawing;
```

## Class methods

```
+[PKTextInputDebugRecordingLogEntry _dictionaryRepresentationForDrawing:detailLevel:containsInProgress:];
+[PKTextInputDebugRecordingLogEntry _dictionaryRepresentationForTarget:];
+[PKTextInputDebugRecordingLogEntry _dictionaryRepresentationForTargetContentInfo:elementType:detailLevel:contentLevel:resultAffectedRange:localeIdentifiers:];
```

## Instance methods

```
-[PKTextInputDebugRecordingLogEntry inputDrawing];
-[PKTextInputDebugRecordingLogEntry _extractDataFromResultCommand:];
-[PKTextInputDebugRecordingLogEntry _originalDrawing];
-[PKTextInputDebugRecordingLogEntry _resultQueryItem];
-[PKTextInputDebugRecordingLogEntry dictionaryRepresentationWithDetailLevel:targetContentLevel:];
-[PKTextInputDebugRecordingLogEntry initWithResultCommand:];
-[PKTextInputDebugRecordingLogEntry set_originalDrawing:];
-[PKTextInputDebugRecordingLogEntry set_resultQueryItem:];
```
