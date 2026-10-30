# `SBFTouchPassThroughClippingView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- 5 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _contentClippingEnabled;
B _hitTestsSubviewsOutsideBounds;
@"_SBFActualClippingView" _contentClippingView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentClippingFrame;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _contentCornerRadii;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentClippingFrame) contentClippingFrame;
@property (T{UIRectCornerRadii=dddd},N,V_contentCornerRadii) contentCornerRadii;
@property (T@"_SBFActualClippingView",&,N,V_contentClippingView) contentClippingView;
@property (TB,N,GisContentClippingEnabled,V_contentClippingEnabled) contentClippingEnabled;
@property (TB,N,V_hitTestsSubviewsOutsideBounds) hitTestsSubviewsOutsideBounds;
```

## Instance methods

```
-[SBFTouchPassThroughClippingView contentCornerRadii];
-[SBFTouchPassThroughClippingView setHitTestsSubviewsOutsideBounds:];
-[SBFTouchPassThroughClippingView hitTestsSubviewsOutsideBounds];
-[SBFTouchPassThroughClippingView insertSubview:atIndex:];
-[SBFTouchPassThroughClippingView insertSubview:belowSubview:];
-[SBFTouchPassThroughClippingView isContentClippingEnabled];
-[SBFTouchPassThroughClippingView addSubview:];
-[SBFTouchPassThroughClippingView insertSubview:aboveSubview:];
-[SBFTouchPassThroughClippingView setContentCornerRadii:];
-[SBFTouchPassThroughClippingView setOpaque:];
-[SBFTouchPassThroughClippingView layoutSubviews];
-[SBFTouchPassThroughClippingView setBackgroundColor:];
-[SBFTouchPassThroughClippingView _setContinuousCornerRadius:];
-[SBFTouchPassThroughClippingView setContentClippingFrame:];
-[SBFTouchPassThroughClippingView contentClippingFrame];
-[SBFTouchPassThroughClippingView initWithFrame:];
-[SBFTouchPassThroughClippingView sendSubviewToBack:];
-[SBFTouchPassThroughClippingView bringSubviewToFront:];
-[SBFTouchPassThroughClippingView setContentClippingEnabled:];
-[SBFTouchPassThroughClippingView _layoutContentClippingView];
-[SBFTouchPassThroughClippingView contentClippingView];
-[SBFTouchPassThroughClippingView setContentClippingFrame:cornerRadii:];
-[SBFTouchPassThroughClippingView setContentClippingView:];
```
