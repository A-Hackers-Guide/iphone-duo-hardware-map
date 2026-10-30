# `AVAssetVideoTrackPlan`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetTrackPlan`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _videoCodecType;
@"NSDictionary" _encoderSpecification;
```

## Properties

```
@property (T@"NSDictionary",R,V_encoderSpecification) encoderSpecification;
@property (T@"NSString",R,V_videoCodecType) videoCodecType;
```

## Instance methods

```
-[AVAssetVideoTrackPlan dealloc];
-[AVAssetVideoTrackPlan videoCodec];
-[AVAssetVideoTrackPlan hash];
-[AVAssetVideoTrackPlan description];
-[AVAssetVideoTrackPlan copyWithZone:];
-[AVAssetVideoTrackPlan isEqual:];
-[AVAssetVideoTrackPlan encoderSpecification];
-[AVAssetVideoTrackPlan initWithMediaType:segmentConfigurations:assemblyTrackID:];
-[AVAssetVideoTrackPlan initWithVideoCodecType:encoderSpecification:mediaType:segmentConfigurations:assemblyTrackID:];
-[AVAssetVideoTrackPlan requiresCompression];
-[AVAssetVideoTrackPlan videoCodecType];
```
