# `BKSHitTestRegion`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`
- 3 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _exclusiveTouchNormalizedSubRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _exclusiveTouchNormalizedSubRectInReferenceSpace;
```

## Properties

```
@property (TB,R,N,GisEmpty) empty;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,G_exclusiveTouchNormalizedSubRectInReferenceSpace,V_exclusiveTouchNormalizedSubRectInReferenceSpace) exclusiveTouchNormalizedSubRectInReferenceSpace;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rect) rect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_exclusiveTouchNormalizedSubRect) exclusiveTouchNormalizedSubRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHitTestRegion supportsSecureCoding];
```

## Instance methods

```
-[BKSHitTestRegion initWithRect:];
-[BKSHitTestRegion exclusiveTouchNormalizedSubRect];
-[BKSHitTestRegion _exclusiveTouchNormalizedSubRectInReferenceSpace];
-[BKSHitTestRegion setExclusiveTouchNormalizedSubRect:];
-[BKSHitTestRegion initWithRect:exclusiveTouchSubRect:];
-[BKSHitTestRegion hitTestRegionLocationForPoint:];
-[BKSHitTestRegion rect];
-[BKSHitTestRegion isEmpty];
-[BKSHitTestRegion _initWithRect:exclusiveTouchNormalizedSubRect:];
-[BKSHitTestRegion encodeWithCoder:];
-[BKSHitTestRegion hash];
-[BKSHitTestRegion description];
-[BKSHitTestRegion initWithCoder:];
-[BKSHitTestRegion appendDescriptionToStream:];
-[BKSHitTestRegion isEqual:];
```
