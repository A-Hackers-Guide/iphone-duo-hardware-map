# `AVCaptionRegion`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 1 instance variables, 11 properties, 35 instance methods, 11 class methods

## Instance variables

```
@"AVCaptionRegionInternal" _internal;
```

## Properties

```
@property (T^{OpaqueFigCaptionRegion=},R,N) _figCaptionRegion;
@property (TB,N,S_setPredefinedRegionPositionShouldBeNil:) _predefinedRegionPositionShouldBeNil;
@property (T@"AVCaptionPosition",R,N) position;
@property (T@"AVCaptionPosition",R,N) endPosition;
@property (T@"AVCaptionLength",R,N) height;
@property (T@"NSString",R,N) identifier;
@property (T{AVCaptionPoint={AVCaptionDimension=dq}{AVCaptionDimension=dq}},R,N) origin;
@property (T{AVCaptionSize={AVCaptionDimension=dq}{AVCaptionDimension=dq}},R,N) size;
@property (Tq,R,N) scroll;
@property (Tq,R,N) displayAlignment;
@property (Tq,R,N) writingMode;
```

## Class methods

```
+[AVCaptionRegion supportsSecureCoding];
+[AVCaptionRegion appleITTBottomRegion];
+[AVCaptionRegion appleITTLeftRegion];
+[AVCaptionRegion appleITTRightRegion];
+[AVCaptionRegion appleITTTopRegion];
+[AVCaptionRegion appleiTTBottom];
+[AVCaptionRegion appleiTTLeft];
+[AVCaptionRegion appleiTTRight];
+[AVCaptionRegion appleiTTTop];
+[AVCaptionRegion subRipTextBottom];
+[AVCaptionRegion subRipTextBottomRegion];
```

## Instance methods

```
-[AVCaptionRegion position];
-[AVCaptionRegion mutableCopyWithZone:];
-[AVCaptionRegion origin];
-[AVCaptionRegion identifier];
-[AVCaptionRegion init];
-[AVCaptionRegion scroll];
-[AVCaptionRegion dealloc];
-[AVCaptionRegion size];
-[AVCaptionRegion _setPosition:];
-[AVCaptionRegion encodeWithCoder:];
-[AVCaptionRegion hash];
-[AVCaptionRegion initWithCoder:];
-[AVCaptionRegion copyWithZone:];
-[AVCaptionRegion isEqual:];
-[AVCaptionRegion height];
-[AVCaptionRegion initWithIdentifier:];
-[AVCaptionRegion _position];
-[AVCaptionRegion _setSize:];
-[AVCaptionRegion endPosition];
-[AVCaptionRegion _endPosition];
-[AVCaptionRegion _figCaptionRegion];
-[AVCaptionRegion _predefinedRegionPositionShouldBeNil];
-[AVCaptionRegion _setDisplayAlignment:];
-[AVCaptionRegion _setEndPosition:];
-[AVCaptionRegion _setHeight:];
-[AVCaptionRegion _setOrigin:];
-[AVCaptionRegion _setPredefinedRegionPositionShouldBeNil:];
-[AVCaptionRegion _setScroll:];
-[AVCaptionRegion _setWritingMode:];
-[AVCaptionRegion _updateExtentPropertiesOfFigCaptionRegionWithPosition:endPosition:];
-[AVCaptionRegion _updateFigCaptionRegion];
-[AVCaptionRegion _updatePositionPropertyOfFigCaptionRegionWithPosition:];
-[AVCaptionRegion displayAlignment];
-[AVCaptionRegion initWithFigCaptionRegion:];
-[AVCaptionRegion writingMode];
```
