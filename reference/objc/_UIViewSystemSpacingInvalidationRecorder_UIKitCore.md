# `_UIViewSystemSpacingInvalidationRecorder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGeometryChangeObserver`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _observingViewTable;
@"UIView" _topView;
@"UIView" _bottomView;
```

## Properties

```
@property (T@"UIView",R,W,N,V_topView) topView;
@property (T@"UIView",R,W,N,V_bottomView) bottomView;
@property (T@"NSArray",R,N) observingViews;
```

## Instance methods

```
-[_UIViewSystemSpacingInvalidationRecorder dealloc];
-[_UIViewSystemSpacingInvalidationRecorder _geometryChanged:forAncestor:];
-[_UIViewSystemSpacingInvalidationRecorder description];
-[_UIViewSystemSpacingInvalidationRecorder topView];
-[_UIViewSystemSpacingInvalidationRecorder _existingObservingViewTable];
-[_UIViewSystemSpacingInvalidationRecorder _observingViewTable];
-[_UIViewSystemSpacingInvalidationRecorder addObservingView:];
-[_UIViewSystemSpacingInvalidationRecorder bottomView];
-[_UIViewSystemSpacingInvalidationRecorder initWithTopView:bottomView:];
-[_UIViewSystemSpacingInvalidationRecorder observingViews];
-[_UIViewSystemSpacingInvalidationRecorder removeObservingView:];
```
