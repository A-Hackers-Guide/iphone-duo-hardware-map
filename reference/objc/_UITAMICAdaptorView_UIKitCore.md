# `_UITAMICAdaptorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIGeometryChangeObserver`
- 8 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"UIView" _view;
@"NSLayoutConstraint" _width;
@"NSLayoutConstraint" _height;
{CGSize="width"d"height"d} _layoutSize;
B _inLayout;
B _invalidatesIntrinsicContentSizeOnSizeChange;
f _sizingPriority;
@"<_UITAMICAdaptorViewDelegate>" _delegate;
```

## Properties

```
@property (T@"UIView",R,N,V_view) view;
@property (Tf,N,V_sizingPriority) sizingPriority;
@property (TB,N,V_invalidatesIntrinsicContentSizeOnSizeChange) invalidatesIntrinsicContentSizeOnSizeChange;
@property (T@"<_UITAMICAdaptorViewDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[_UITAMICAdaptorView shouldWrapView:];
```

## Instance methods

```
-[_UITAMICAdaptorView didMoveToWindow];
-[_UITAMICAdaptorView _updateTraitsAndLayoutSizeIfNecessary];
-[_UITAMICAdaptorView _intrinsicContentSizeInvalidatedForChildView:];
-[_UITAMICAdaptorView initWithView:];
-[_UITAMICAdaptorView setSizingPriority:];
-[_UITAMICAdaptorView layoutSubviews];
-[_UITAMICAdaptorView _geometryChanged:forAncestor:];
-[_UITAMICAdaptorView sizeThatFits:];
-[_UITAMICAdaptorView view];
-[_UITAMICAdaptorView invalidatesIntrinsicContentSizeOnSizeChange];
-[_UITAMICAdaptorView setDelegate:];
-[_UITAMICAdaptorView setInvalidatesIntrinsicContentSizeOnSizeChange:];
-[_UITAMICAdaptorView delegate];
-[_UITAMICAdaptorView _willMoveToWindow:];
-[_UITAMICAdaptorView updateForAvailableSize];
-[_UITAMICAdaptorView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[_UITAMICAdaptorView sizingPriority];
-[_UITAMICAdaptorView updateHasGeometryChangeObserver:];
```
