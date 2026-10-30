# `MLImageConstraint`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureValueConstraint`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 8 properties, 16 instance methods, 6 class methods

## Instance variables

```
q _pixelsHigh;
q _pixelsWide;
@"MLImageSizeConstraint" _sizeConstraint;
Q _pixelType;
```

## Properties

```
@property (TQ,R) imageHeight;
@property (TQ,R) imageWidth;
@property (TQ,R,V_pixelType) pixelType;
@property (TI,R) osType;
@property (Tq,R,N,V_pixelsHigh) pixelsHigh;
@property (Tq,R,N,V_pixelsWide) pixelsWide;
@property (TI,R,N) pixelFormatType;
@property (T@"MLImageSizeConstraint",R,N,V_sizeConstraint) sizeConstraint;
```

## Class methods

```
+[MLImageConstraint supportsSecureCoding];
+[MLImageConstraint constraintWithPixelsWide:pixelsHigh:pixelType:];
+[MLImageConstraint constraintWithPixelsWide:pixelsHigh:pixelType:sizeConstraint:];
+[MLImageConstraint imagePixelTypeFromOSType:];
+[MLImageConstraint stringForImagePixelType:];
+[MLImageConstraint stringForPixelFormatType:];
```

## Instance methods

```
-[MLImageConstraint imageHeight];
-[MLImageConstraint imageWidth];
-[MLImageConstraint encodeWithCoder:];
-[MLImageConstraint description];
-[MLImageConstraint initWithCoder:];
-[MLImageConstraint isAllowedValue:error:];
-[MLImageConstraint copyWithZone:];
-[MLImageConstraint pixelFormatType];
-[MLImageConstraint osType];
-[MLImageConstraint _stringForAllowedOSTypes];
-[MLImageConstraint allowsPixelBuffer:error:];
-[MLImageConstraint initWithPixelsWide:pixelsHigh:pixelType:sizeConstraint:];
-[MLImageConstraint pixelType];
-[MLImageConstraint pixelsHigh];
-[MLImageConstraint pixelsWide];
-[MLImageConstraint sizeConstraint];
```
