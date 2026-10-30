# `MLImageSizeConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 5 properties, 12 instance methods, 4 class methods

## Instance variables

```
q _type;
@"NSOrderedSet" _imageSizeSet;
{_NSRange="location"Q"length"Q} _pixelsWideRange;
{_NSRange="location"Q"length"Q} _pixelsHighRange;
```

## Properties

```
@property (T@"NSOrderedSet",R,N,V_imageSizeSet) imageSizeSet;
@property (Tq,R,N,V_type) type;
@property (T{_NSRange=QQ},R,N,V_pixelsWideRange) pixelsWideRange;
@property (T{_NSRange=QQ},R,N,V_pixelsHighRange) pixelsHighRange;
@property (T@"NSArray",R,N) enumeratedImageSizes;
```

## Class methods

```
+[MLImageSizeConstraint supportsSecureCoding];
+[MLImageSizeConstraint closestImageSizeInArray:toImageSize:preferDownScaling:];
+[MLImageSizeConstraint closestImageSizeInPixelsWideRange:pixelsHighRange:toImageSize:preferInputAspectRatio:];
+[MLImageSizeConstraint locationClosestTo:inRange:];
```

## Instance methods

```
-[MLImageSizeConstraint initUnspecified];
-[MLImageSizeConstraint type];
-[MLImageSizeConstraint encodeWithCoder:];
-[MLImageSizeConstraint initWithCoder:];
-[MLImageSizeConstraint pixelsHighRange];
-[MLImageSizeConstraint pixelsWideRange];
-[MLImageSizeConstraint allowedImageSizeClosestToPixelsWide:pixelsHigh:preferDownScaling:preferInputAspectRatio:];
-[MLImageSizeConstraint enumeratedImageSizes];
-[MLImageSizeConstraint imageSizeSet];
-[MLImageSizeConstraint initWithEnumeratedImageSizes:];
-[MLImageSizeConstraint initWithPixelsWideRange:pixelsHighRange:];
-[MLImageSizeConstraint isAllowedImageSize:error:];
```
