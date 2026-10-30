# `AVVideoCompositionInstruction`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `NSMutableCopying`, `AVVideoCompositionInstruction`
- 1 instance variables, 12 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"AVVideoCompositionInstructionInternal" _instruction;
```

## Properties

```
@property (T{?={?=qiIq}{?=qiIq}},R,N) timeRange;
@property (T^{CGColor=},R,&,N) backgroundColor;
@property (T@"NSArray",R,C,N) layerInstructions;
@property (TB,R,N) enablePostProcessing;
@property (T@"NSArray",R,N) requiredSourceTrackIDs;
@property (Ti,R,N) passthroughTrackID;
@property (T@"NSArray",R,N) requiredSourceSampleDataTrackIDs;
@property (TB,R,N) containsTweening;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVVideoCompositionInstruction supportsSecureCoding];
+[AVVideoCompositionInstruction initialize];
+[AVVideoCompositionInstruction videoCompositionInstructionWithInstruction:];
```

## Instance methods

```
-[AVVideoCompositionInstruction setTimeRange:];
-[AVVideoCompositionInstruction mutableCopyWithZone:];
-[AVVideoCompositionInstruction timeRange];
-[AVVideoCompositionInstruction init];
-[AVVideoCompositionInstruction dealloc];
-[AVVideoCompositionInstruction setBackgroundColor:];
-[AVVideoCompositionInstruction encodeWithCoder:];
-[AVVideoCompositionInstruction backgroundColor];
-[AVVideoCompositionInstruction description];
-[AVVideoCompositionInstruction initWithCoder:];
-[AVVideoCompositionInstruction copyWithZone:];
-[AVVideoCompositionInstruction isEqual:];
-[AVVideoCompositionInstruction dictionaryRepresentation];
-[AVVideoCompositionInstruction _deepCopy];
-[AVVideoCompositionInstruction _setValuesFromDictionary:];
-[AVVideoCompositionInstruction blendingTransferFunction];
-[AVVideoCompositionInstruction containsTweening];
-[AVVideoCompositionInstruction enablePostProcessing];
-[AVVideoCompositionInstruction layerInstructions];
-[AVVideoCompositionInstruction passthroughTrackID];
-[AVVideoCompositionInstruction requiredSourceSampleDataTrackIDs];
-[AVVideoCompositionInstruction requiredSourceTrackIDs];
-[AVVideoCompositionInstruction setBlendingTransferFunction:];
-[AVVideoCompositionInstruction setEnablePostProcessing:];
-[AVVideoCompositionInstruction setLayerInstructions:];
-[AVVideoCompositionInstruction setRequiredSourceSampleDataTrackIDs:];
```
