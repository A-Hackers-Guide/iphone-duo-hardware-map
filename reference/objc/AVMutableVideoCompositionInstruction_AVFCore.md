# `AVMutableVideoCompositionInstruction`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVVideoCompositionInstruction`
- 1 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVMutableVideoCompositionInstructionInternal" _mutableInstruction;
```

## Properties

```
@property (T{?={?=qiIq}{?=qiIq}},N) timeRange;
@property (T^{CGColor=},&,N) backgroundColor;
@property (T@"NSArray",C,N) layerInstructions;
@property (TB,N) enablePostProcessing;
@property (T@"NSArray",C,N) requiredSourceSampleDataTrackIDs;
```

## Class methods

```
+[AVMutableVideoCompositionInstruction videoCompositionInstruction];
```

## Instance methods

```
-[AVMutableVideoCompositionInstruction setTimeRange:];
-[AVMutableVideoCompositionInstruction timeRange];
-[AVMutableVideoCompositionInstruction setBackgroundColor:];
-[AVMutableVideoCompositionInstruction backgroundColor];
-[AVMutableVideoCompositionInstruction enablePostProcessing];
-[AVMutableVideoCompositionInstruction layerInstructions];
-[AVMutableVideoCompositionInstruction requiredSourceSampleDataTrackIDs];
-[AVMutableVideoCompositionInstruction setEnablePostProcessing:];
-[AVMutableVideoCompositionInstruction setLayerInstructions:];
-[AVMutableVideoCompositionInstruction setRequiredSourceSampleDataTrackIDs:];
```
