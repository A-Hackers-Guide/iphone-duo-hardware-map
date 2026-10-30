# `CAMPanoramaPaintingStatus`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 0 class methods

## Instance variables

```
d _speed;
d _normalizedBaselineOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropRectangle;
```

## Properties

```
@property (Td,R,N,V_speed) speed;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cropRectangle) cropRectangle;
@property (Td,R,N,V_normalizedBaselineOffset) normalizedBaselineOffset;
```

## Instance methods

```
-[CAMPanoramaPaintingStatus speed];
-[CAMPanoramaPaintingStatus cropRectangle];
-[CAMPanoramaPaintingStatus initWithSpeed:cropRectangle:normalizedBaselineOffset:];
-[CAMPanoramaPaintingStatus normalizedBaselineOffset];
```
