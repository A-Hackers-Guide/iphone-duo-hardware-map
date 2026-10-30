# `_UIVectorTextLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _runs;
Q _numberOfLines;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _usedBoundingRect;
{_NSRange="location"Q"length"Q} _fitRange;
d _firstLineBaseline;
d _lastLineBaseline;
@"_UIVectorTextLayoutInfo" _layoutInfo;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _coordinateAdjustment;
```

## Properties

```
@property (T@"_UIVectorTextLayoutParameters",R,C,N) parameters;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) boundingRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) usedBoundingRect;
@property (T{CGSize=dd},R,N) size;
@property (T{_NSRange=QQ},R,N) textRange;
@property (TQ,R,N) numberOfLines;
@property (TQ,R,N) numberOfRuns;
@property (Td,R,N) firstLineBaseline;
@property (Td,R,N) lastLineBaseline;
@property (T{CGAffineTransform=dddddd},R,N,V_coordinateAdjustment) coordinateAdjustment;
```

## Instance methods

```
-[_UIVectorTextLayout boundingRect];
-[_UIVectorTextLayout layoutDescription];
-[_UIVectorTextLayout parameters];
-[_UIVectorTextLayout _layoutIfNeeded];
-[_UIVectorTextLayout numberOfLines];
-[_UIVectorTextLayout textRange];
-[_UIVectorTextLayout size];
-[_UIVectorTextLayout lastLineBaseline];
-[_UIVectorTextLayout description];
-[_UIVectorTextLayout firstLineBaseline];
-[_UIVectorTextLayout coordinateAdjustment];
-[_UIVectorTextLayout enumerateRunsUsingBlock:];
-[_UIVectorTextLayout hasLayout];
-[_UIVectorTextLayout initWithTextParameters:];
-[_UIVectorTextLayout numberOfRuns];
-[_UIVectorTextLayout resetLayout];
-[_UIVectorTextLayout usedBoundingRect];
```
