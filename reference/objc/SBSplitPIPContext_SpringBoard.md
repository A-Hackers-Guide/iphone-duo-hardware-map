# `SBSplitPIPContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 3 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _edgeInsets;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _applicationCornerRadii;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (T{UIEdgeInsets=dddd},R,N,V_edgeInsets) edgeInsets;
@property (T{UIRectCornerRadii=dddd},R,N,V_applicationCornerRadii) applicationCornerRadii;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSplitPIPContext edgeInsets];
-[SBSplitPIPContext appendDescriptionToStream:];
-[SBSplitPIPContext copyWithZone:];
-[SBSplitPIPContext frame];
-[SBSplitPIPContext applicationCornerRadii];
-[SBSplitPIPContext initWithFrame:edgeInsets:applicationCornerRadii:];
```
