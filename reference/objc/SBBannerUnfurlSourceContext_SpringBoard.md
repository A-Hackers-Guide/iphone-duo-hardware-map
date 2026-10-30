# `SBBannerUnfurlSourceContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
d _cornerRadius;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceCoordinateSpaceBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceFrame;
{CGPoint="x"d"y"d} _referenceVelocity;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceCoordinateSpaceBounds) referenceCoordinateSpaceBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceFrame) referenceFrame;
@property (Td,R,N,V_cornerRadius) cornerRadius;
@property (T{CGPoint=dd},R,N,V_referenceVelocity) referenceVelocity;
```

## Instance methods

```
-[SBBannerUnfurlSourceContext mutableCopyWithZone:];
-[SBBannerUnfurlSourceContext referenceFrame];
-[SBBannerUnfurlSourceContext cornerRadius];
-[SBBannerUnfurlSourceContext copyWithZone:];
-[SBBannerUnfurlSourceContext _copyWithClass:];
-[SBBannerUnfurlSourceContext referenceCoordinateSpaceBounds];
-[SBBannerUnfurlSourceContext referenceVelocity];
```
