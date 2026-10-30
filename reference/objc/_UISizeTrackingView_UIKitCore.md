# `_UISizeTrackingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIScrollToTopView`, `_UIRemoteViewFocusProxy`, `_UIViewBoundingPathChangeObserver`
- 10 instance variables, 5 properties, 34 instance methods, 2 class methods

## Instance variables

```
@"_UIRemoteViewController" _remoteViewController;
@"_UIRemoteViewControllerLegacyImpl" _rvcImpl;
@ _viewControllerOperatorProxy;
@ _textEffectsOperatorProxy;
{CGSize="width"d"height"d} _intrinsicContentSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _formerTextEffectsContentFrame;
B _observingTextEffectsWindowRotation;
q _interfaceOrientation;
@"UIView" _viewForRemoteTextEffectsWindowMatchAnimation;
{?="hasIntrinsicContentSize"b1"observingBoundingPathChanges"b1"needsRemoteViewServiceBoundingPathUpdate"b1"remoteViewServiceBoundingPathUpdateScheduled"b1} _sizeTrackingViewFlags;
```

## Properties

```
@property (T@"_UIRemoteViewController",R,N) remoteViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISizeTrackingView _supportsInvalidatingFocusCache];
+[_UISizeTrackingView viewWithRemoteViewController:viewControllerOperatorProxy:textEffectsOperatorProxy:remoteViewControllerImpl:];
```

## Instance methods

```
-[_UISizeTrackingView focusItemsInRect:];
-[_UISizeTrackingView _intrinsicSizeWithinSize:];
-[_UISizeTrackingView isScrollEnabled];
-[_UISizeTrackingView dealloc];
-[_UISizeTrackingView remoteViewController];
-[_UISizeTrackingView _didMoveFromWindow:toWindow:];
-[_UISizeTrackingView _viewDidMoveFromScreen:toScreen:];
-[_UISizeTrackingView setBounds:];
-[_UISizeTrackingView canBecomeFocused];
-[_UISizeTrackingView _geometryChanged:forAncestor:];
-[_UISizeTrackingView _scrollToTopFromTouchAtScreenLocation:resultHandler:];
-[_UISizeTrackingView _boundingPathMayHaveChangedForView:relativeToBoundsOriginOnly:];
-[_UISizeTrackingView setFrame:];
-[_UISizeTrackingView _willMoveToWindow:];
-[_UISizeTrackingView nextResponder];
-[_UISizeTrackingView _needsTextEffectsUpdateToFrame:];
-[_UISizeTrackingView _boundingPathForRemoteViewService];
-[_UISizeTrackingView _boundsForRemoteViewService];
-[_UISizeTrackingView _clearNeedsRemoteViewServiceBoundingPathUpdate];
-[_UISizeTrackingView _fencingEffectsAreVisible];
-[_UISizeTrackingView _interfaceOrientationForScene:];
-[_UISizeTrackingView _prepareForWindowHostingSceneRemoval];
-[_UISizeTrackingView _remoteTextEffectsWindowSizeFromSize:];
-[_UISizeTrackingView _setNeedsRemoteViewServiceBoundingPathUpdate];
-[_UISizeTrackingView _sizeForRemoteViewService];
-[_UISizeTrackingView _textEffectsWindowDidRotate:];
-[_UISizeTrackingView _updateSceneGeometries:];
-[_UISizeTrackingView _updateSceneGeometries:forOrientation:];
-[_UISizeTrackingView _updateTextEffectsGeometries:];
-[_UISizeTrackingView _updateTextEffectsGeometries:textEffectsWindow:];
-[_UISizeTrackingView _updateTextEffectsGeometriesImmediately];
-[_UISizeTrackingView _updateTextEffectsWindowHostedViewSize];
-[_UISizeTrackingView _updateTextEffectsWindowSafeAreaInsets];
-[_UISizeTrackingView updateIntrinsicContentSize:];
```
