# `FBSDisplayPixelDensity`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCCoding`, `BSDescriptionStreaming`
- 2 instance variables, 6 properties, 12 instance methods, 2 class methods

## Instance variables

```
d _horizontalPixelsPerInch;
d _verticalPixelsPerInch;
```

## Properties

```
@property (Td,R,N,V_horizontalPixelsPerInch) horizontalPixelsPerInch;
@property (Td,R,N,V_verticalPixelsPerInch) verticalPixelsPerInch;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSDisplayPixelDensity supportsSecureCoding];
+[FBSDisplayPixelDensity _densityForPixelsPerInch:];
```

## Instance methods

```
-[FBSDisplayPixelDensity supportsBSXPCSecureCoding];
-[FBSDisplayPixelDensity initWithXPCDictionary:];
-[FBSDisplayPixelDensity initWithHorizontalPixelsPerInch:verticalPixelsPerInch:];
-[FBSDisplayPixelDensity verticalPixelsPerInch];
-[FBSDisplayPixelDensity encodeWithXPCDictionary:];
-[FBSDisplayPixelDensity encodeWithCoder:];
-[FBSDisplayPixelDensity horizontalPixelsPerInch];
-[FBSDisplayPixelDensity description];
-[FBSDisplayPixelDensity initWithCoder:];
-[FBSDisplayPixelDensity appendDescriptionToStream:];
-[FBSDisplayPixelDensity copyWithZone:];
-[FBSDisplayPixelDensity isEqual:];
```
