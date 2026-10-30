# `_UIMorphingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _useOpacityPairFilter;
d _progress;
@"NSMutableOrderedSet" _contentViews;
@"UIView" _opacityPairSourceView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialBounds;
```

## Properties

```
@property (T@"NSMutableOrderedSet",&,N,V_contentViews) contentViews;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_initialBounds) initialBounds;
@property (T@"UIView",W,N,V_opacityPairSourceView) opacityPairSourceView;
@property (Td,N,V_progress) progress;
@property (TB,N,V_useOpacityPairFilter) useOpacityPairFilter;
```

## Instance methods

```
-[_UIMorphingView contentViews];
-[_UIMorphingView initialBounds];
-[_UIMorphingView setProgress:];
-[_UIMorphingView addContentView:];
-[_UIMorphingView useOpacityPairFilter];
-[_UIMorphingView progress];
-[_UIMorphingView setInitialBounds:];
-[_UIMorphingView setOpacityPairSourceView:];
-[_UIMorphingView setContentViews:];
-[_UIMorphingView opacityPairSourceView];
-[_UIMorphingView _updateMorphProgress];
-[_UIMorphingView _currentDestinationView];
-[_UIMorphingView setUseOpacityPairFilter:];
```
