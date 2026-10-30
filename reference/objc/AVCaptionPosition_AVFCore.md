# `AVCaptionPosition`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"AVCaptionPositionInternal" _internal;
```

## Properties

```
@property (Tq,R,N) cellX;
@property (Tq,R,N) cellY;
@property (Tf,R,N) relativeToEnclosingRegionX;
@property (Tf,R,N) relativeToEnclosingRegionY;
@property (Tq,R,N) unitType;
```

## Class methods

```
+[AVCaptionPosition supportsSecureCoding];
```

## Instance methods

```
-[AVCaptionPosition init];
-[AVCaptionPosition dealloc];
-[AVCaptionPosition unitType];
-[AVCaptionPosition encodeWithCoder:];
-[AVCaptionPosition hash];
-[AVCaptionPosition description];
-[AVCaptionPosition initWithCoder:];
-[AVCaptionPosition copyWithZone:];
-[AVCaptionPosition isEqual:];
-[AVCaptionPosition cellX];
-[AVCaptionPosition cellY];
-[AVCaptionPosition initWithCellPositionX:andY:];
-[AVCaptionPosition initWithCellPositionX:y:];
-[AVCaptionPosition initWithPositionRelativeToEnclosingRegionX:relativeToEnclosingRegionY:];
-[AVCaptionPosition initWithRelativeToEnclosingRegionX:andY:];
-[AVCaptionPosition relativeToEnclosingRegionX];
-[AVCaptionPosition relativeToEnclosingRegionY];
```
