# `AVAssetWriterInputGroup`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMediaSelectionGroup`
- 1 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"AVAssetWriterInputGroupInternal" _internal;
```

## Properties

```
@property (T@"NSArray",R,N) provisionalInputs;
@property (T@"NSArray",R,N) inputs;
@property (T@"AVAssetWriterInput",R,N) defaultInput;
```

## Class methods

```
+[AVAssetWriterInputGroup assetWriterInputGroupWithInputs:provisionalInputs:defaultInput:];
+[AVAssetWriterInputGroup assetWriterInputGroupWithInputs:defaultInput:];
```

## Instance methods

```
-[AVAssetWriterInputGroup mediaSelectionOptionWithPropertyList:];
-[AVAssetWriterInputGroup observeValueForKeyPath:ofObject:change:context:];
-[AVAssetWriterInputGroup init];
-[AVAssetWriterInputGroup inputs];
-[AVAssetWriterInputGroup dealloc];
-[AVAssetWriterInputGroup options];
-[AVAssetWriterInputGroup copyWithZone:];
-[AVAssetWriterInputGroup _startObservingInputPropertiesThatMayChangeValueOfOptions];
-[AVAssetWriterInputGroup _stopObservingInputPropertiesThatMayChangeValueOfOptions];
-[AVAssetWriterInputGroup defaultInput];
-[AVAssetWriterInputGroup initWithInputs:defaultInput:];
-[AVAssetWriterInputGroup initWithInputs:provisionalInputs:defaultInput:];
-[AVAssetWriterInputGroup provisionalInputs];
```
