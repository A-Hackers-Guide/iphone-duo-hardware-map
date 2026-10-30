# `CAMFaceResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMMetadataObjectResult`
- 4 instance variables, 11 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _uniqueIdentifier;
d _rollAngle;
@"AVMetadataFaceObject" _underlyingFaceObject;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds) bounds;
@property (Td,R,N,V_rollAngle) rollAngle;
@property (T@"AVMetadataFaceObject",R,N,V_underlyingFaceObject) underlyingFaceObject;
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
-[CAMFaceResult metadataType];
-[CAMFaceResult syntheticFocusMode];
-[CAMFaceResult uniqueIdentifier];
-[CAMFaceResult rollAngle];
-[CAMFaceResult bounds];
-[CAMFaceResult description];
-[CAMFaceResult burstMetadataRepresentation];
-[CAMFaceResult initWithFaceObject:];
-[CAMFaceResult underlyingFaceObject];
-[CAMFaceResult underlyingMetadataObject];
```
