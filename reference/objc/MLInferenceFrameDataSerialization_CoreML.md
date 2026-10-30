# `MLInferenceFrameDataSerialization`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _shouldOverwrite;
B _modelIOFrameData;
B _segmentIOFrameData;
@"NSURL" _outputDirectoryURL;
@"NSString" _prefix;
```

## Properties

```
@property (T@"NSURL",C,N,V_outputDirectoryURL) outputDirectoryURL;
@property (T@"NSString",C,N,V_prefix) prefix;
@property (TB,N,V_shouldOverwrite) shouldOverwrite;
@property (TB,N,V_modelIOFrameData) modelIOFrameData;
@property (TB,N,V_segmentIOFrameData) segmentIOFrameData;
```

## Instance methods

```
-[MLInferenceFrameDataSerialization setPrefix:];
-[MLInferenceFrameDataSerialization prefix];
-[MLInferenceFrameDataSerialization copyWithZone:];
-[MLInferenceFrameDataSerialization shouldOverwrite];
-[MLInferenceFrameDataSerialization initWithOutputDirectory:prefix:];
-[MLInferenceFrameDataSerialization initWithOutputDirectory:prefix:shouldOverwrite:modelIOFrameData:segmentIOFrameData:];
-[MLInferenceFrameDataSerialization modelIOFrameData];
-[MLInferenceFrameDataSerialization outputDirectoryURL];
-[MLInferenceFrameDataSerialization segmentIOFrameData];
-[MLInferenceFrameDataSerialization setModelIOFrameData:];
-[MLInferenceFrameDataSerialization setOutputDirectoryURL:];
-[MLInferenceFrameDataSerialization setSegmentIOFrameData:];
-[MLInferenceFrameDataSerialization setShouldOverwrite:];
```
