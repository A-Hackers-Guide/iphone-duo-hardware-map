# `SBSlideOverTongueView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIView" _contentView;
@"SBSlideOverGlassMaterialView" _glassView;
@"UIView" _sdfElementContainerView;
@"SBSDFElementView" _sourceSDFElementView;
@"SBSDFElementView" _destinationSDFElementView;
@"UIImageView" _chevronImageView;
@"UITapGestureRecognizer" _tapGestureRecognizer;
{CGSize="width"d"height"d} _tongueSize;
d _continuousCornerRadius;
@"<SBSlideOverTongueViewDelegate>" _delegate;
Q _direction;
Q _state;
```

## Properties

```
@property (T@"<SBSlideOverTongueViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_direction) direction;
@property (TQ,R,N,V_state) state;
```

## Instance methods

```
-[SBSlideOverTongueView _updateCornerRadius];
-[SBSlideOverTongueView _handleTap:];
-[SBSlideOverTongueView layoutSubviews];
-[SBSlideOverTongueView _continuousCornerRadius];
-[SBSlideOverTongueView direction];
-[SBSlideOverTongueView setDelegate:];
-[SBSlideOverTongueView _setContinuousCornerRadius:];
-[SBSlideOverTongueView delegate];
-[SBSlideOverTongueView pointInside:withEvent:];
-[SBSlideOverTongueView initWithFrame:];
-[SBSlideOverTongueView state];
-[SBSlideOverTongueView _updateContainerTransform];
-[SBSlideOverTongueView _updateSubviewCollapsedExpandedState];
-[SBSlideOverTongueView setDirection:state:animated:];
```
