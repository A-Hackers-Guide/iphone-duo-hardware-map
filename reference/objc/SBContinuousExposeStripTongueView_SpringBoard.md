# `SBContinuousExposeStripTongueView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIView" _tongueContainerView;
@"UIImageView" _chevronImageView;
@"UIView" _tongueMaskView;
@"_UIBackdropView" _backdropView;
@"UITapGestureRecognizer" _tapGestureRecognizer;
{CGSize="width"d"height"d} _bitmapMaskSize;
B _animating;
@"<SBContinuousExposeStripTongueViewDelegate>" _delegate;
{SBSwitcherContinuousExposeStripTongueAttributes="state"Q"direction"Q} _attributes;
```

## Properties

```
@property (T@"<SBContinuousExposeStripTongueViewDelegate>",W,N,V_delegate) delegate;
@property (T{SBSwitcherContinuousExposeStripTongueAttributes=QQ},R,N,V_attributes) attributes;
@property (TB,R,N,GisAnimating,V_animating) animating;
```

## Instance methods

```
-[SBContinuousExposeStripTongueView _handleTap:];
-[SBContinuousExposeStripTongueView layoutSubviews];
-[SBContinuousExposeStripTongueView setDelegate:];
-[SBContinuousExposeStripTongueView delegate];
-[SBContinuousExposeStripTongueView attributes];
-[SBContinuousExposeStripTongueView pointInside:withEvent:];
-[SBContinuousExposeStripTongueView isAnimating];
-[SBContinuousExposeStripTongueView initWithFrame:];
-[SBContinuousExposeStripTongueView _updateContainerPosition];
-[SBContinuousExposeStripTongueView _updateContainerTransform];
-[SBContinuousExposeStripTongueView _updateSubviewLayoutForCollapsedOrExpandedState];
-[SBContinuousExposeStripTongueView _updateSubviewOpacityForCollapsedOrExpandedState];
-[SBContinuousExposeStripTongueView setAttributes:animated:];
```
