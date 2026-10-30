# `CAMTextRegionResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMMetadataObjectResult`
- 4 instance variables, 12 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _uniqueIdentifier;
d _baselineAngle;
@"AVMetadataTextRegionObject" __metadataTextRegionObject;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"AVMetadataTextRegionObject",&,N,V__metadataTextRegionObject) _metadataTextRegionObject;
@property (Tf,R,N) confidence;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds) bounds;
@property (Td,R,N,V_baselineAngle) baselineAngle;
@property (T@"NSString",R,C,N) metadataType;
@property (T@"NSString",R,C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"AVMetadataObject",R,N) underlyingMetadataObject;
@property (TQ,?,R,N) syntheticFocusMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTextRegionResult metadataType];
-[CAMTextRegionResult uniqueIdentifier];
-[CAMTextRegionResult bounds];
-[CAMTextRegionResult description];
-[CAMTextRegionResult baselineAngle];
-[CAMTextRegionResult confidence];
-[CAMTextRegionResult _metadataTextRegionObject];
-[CAMTextRegionResult initWithTextRegionObject:];
-[CAMTextRegionResult set_metadataTextRegionObject:];
-[CAMTextRegionResult underlyingMetadataObject];
```
