# `AVVideoCompositionLayerInstruction`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `NSMutableCopying`
- 1 instance variables, 1 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"AVVideoCompositionLayerInstructionInternal" _layerInstruction;
```

## Properties

```
@property (Ti,R,N) trackID;
```

## Class methods

```
+[AVVideoCompositionLayerInstruction supportsSecureCoding];
+[AVVideoCompositionLayerInstruction initialize];
+[AVVideoCompositionLayerInstruction videoCompositionLayerInstructionWithLayerInstruction:];
```

## Instance methods

```
-[AVVideoCompositionLayerInstruction mutableCopyWithZone:];
-[AVVideoCompositionLayerInstruction init];
-[AVVideoCompositionLayerInstruction trackID];
-[AVVideoCompositionLayerInstruction dealloc];
-[AVVideoCompositionLayerInstruction encodeWithCoder:];
-[AVVideoCompositionLayerInstruction initWithCoder:];
-[AVVideoCompositionLayerInstruction copyWithZone:];
-[AVVideoCompositionLayerInstruction isEqual:];
-[AVVideoCompositionLayerInstruction _setCropRectangleRampFromStartCropRectangle:toEndCropRectangle:timeRange:selector:];
-[AVVideoCompositionLayerInstruction _setCropRectangleRamps:];
-[AVVideoCompositionLayerInstruction _setOpacityRampFromStartOpacity:toEndOpacity:timeRange:selector:];
-[AVVideoCompositionLayerInstruction _setOpacityRamps:];
-[AVVideoCompositionLayerInstruction _setTransformRampFromStartTransform:toEndTransform:timeRange:selector:];
-[AVVideoCompositionLayerInstruction _setTransformRamps:];
-[AVVideoCompositionLayerInstruction _setValuesFromDictionary:timeRange:];
-[AVVideoCompositionLayerInstruction dictionaryRepresentationWithTimeRange:];
-[AVVideoCompositionLayerInstruction getCropRectangleRampForTime:startCropRectangle:endCropRectangle:timeRange:];
-[AVVideoCompositionLayerInstruction getOpacityRampForTime:startOpacity:endOpacity:timeRange:];
-[AVVideoCompositionLayerInstruction getTransformRampForTime:startTransform:endTransform:timeRange:];
-[AVVideoCompositionLayerInstruction setCropRectangle:atTime:];
-[AVVideoCompositionLayerInstruction setCropRectangleRampFromStartCropRectangle:toEndCropRectangle:timeRange:];
-[AVVideoCompositionLayerInstruction setOpacity:atTime:];
-[AVVideoCompositionLayerInstruction setOpacityRampFromStartOpacity:toEndOpacity:timeRange:];
-[AVVideoCompositionLayerInstruction setTrackID:];
-[AVVideoCompositionLayerInstruction setTransform:atTime:];
-[AVVideoCompositionLayerInstruction setTransformRampFromStartTransform:toEndTransform:timeRange:];
```
