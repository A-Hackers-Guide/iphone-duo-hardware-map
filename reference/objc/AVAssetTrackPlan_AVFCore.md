# `AVAssetTrackPlan`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
i _assemblyTrackID;
@"NSString" _mediaType;
@"NSArray" _segmentConfigurations;
```

## Properties

```
@property (Ti,R,V_assemblyTrackID) assemblyTrackID;
@property (T@"NSString",R,V_mediaType) mediaType;
@property (T@"NSArray",R,C,V_segmentConfigurations) segmentConfigurations;
```

## Instance methods

```
-[AVAssetTrackPlan dealloc];
-[AVAssetTrackPlan hash];
-[AVAssetTrackPlan description];
-[AVAssetTrackPlan copyWithZone:];
-[AVAssetTrackPlan mediaType];
-[AVAssetTrackPlan isEqual:];
-[AVAssetTrackPlan assemblyTrackID];
-[AVAssetTrackPlan initWithMediaType:segmentConfigurations:assemblyTrackID:];
-[AVAssetTrackPlan requiresCompression];
-[AVAssetTrackPlan segmentConfigurations];
```
