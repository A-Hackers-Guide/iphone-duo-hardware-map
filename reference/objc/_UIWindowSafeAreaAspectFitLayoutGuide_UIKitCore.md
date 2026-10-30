# `_UIWindowSafeAreaAspectFitLayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILayoutGuide`
- Protocols: `_UIViewBoundingPathChangeObserver`, `UILayoutGuideAspectFitting`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _layoutFrameDirty;
@"NSLayoutConstraint" _leftConstraint;
@"NSLayoutConstraint" _topConstraint;
@"NSLayoutConstraint" _widthConstraint;
@"NSLayoutConstraint" _heightConstraint;
d _aspectRatio;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_aspectRatio) aspectRatio;
```

## Instance methods

```
-[_UIWindowSafeAreaAspectFitLayoutGuide _setOwningView:];
-[_UIWindowSafeAreaAspectFitLayoutGuide init];
-[_UIWindowSafeAreaAspectFitLayoutGuide aspectRatio];
-[_UIWindowSafeAreaAspectFitLayoutGuide dealloc];
-[_UIWindowSafeAreaAspectFitLayoutGuide setAspectRatio:];
-[_UIWindowSafeAreaAspectFitLayoutGuide encodeWithCoder:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _boundingPathMayHaveChangedForView:relativeToBoundsOriginOnly:];
-[_UIWindowSafeAreaAspectFitLayoutGuide initWithCoder:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _isSafeAreaAspectFitLayoutGuide];
-[_UIWindowSafeAreaAspectFitLayoutGuide _createOrUpdateHeightConstraintWithConstant:owningView:constraintsToActivate:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _createOrUpdateLeftConstraintWithConstant:owningView:constraintsToActivate:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _createOrUpdateTopConstraintWithConstant:owningView:constraintsToActivate:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _createOrUpdateWidthConstraintWithConstant:owningView:constraintsToActivate:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _updateLayoutFrameConstraintsIfNeededWithOwningView:];
-[_UIWindowSafeAreaAspectFitLayoutGuide _updateLayoutFrameInOwningView:fromEngine:];
```
