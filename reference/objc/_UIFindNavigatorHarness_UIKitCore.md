# `_UIFindNavigatorHarness`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGeometryChangeObserver`, `_UIFindNavigatorViewControllerDelegate`, `_UIFindNavigatorHosting`
- 6 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isHoistingFindNavigator;
B _interactionViewIsWebView;
@"UIView" _interactionView;
@"UIView" _hostView;
@"UIScrollView" _hostScrollView;
@"_UIFindNavigatorViewController" _findNavigatorViewController;
```

## Properties

```
@property (T@"_UIFindNavigatorViewController",&,N,V_findNavigatorViewController) findNavigatorViewController;
@property (T@"UIView",W,N,V_interactionView) interactionView;
@property (T@"UIView",W,N,V_hostView) hostView;
@property (T@"UIScrollView",W,N,V_hostScrollView) hostScrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisFindNavigatorVisible) findNavigatorVisible;
```

## Instance methods

```
-[_UIFindNavigatorHarness hostView];
-[_UIFindNavigatorHarness setHostView:];
-[_UIFindNavigatorHarness init];
-[_UIFindNavigatorHarness dealloc];
-[_UIFindNavigatorHarness _geometryChanged:forAncestor:];
-[_UIFindNavigatorHarness isFindNavigatorVisible];
-[_UIFindNavigatorHarness interactionView];
-[_UIFindNavigatorHarness setFindNavigatorViewController:];
-[_UIFindNavigatorHarness _adjustHostViewScrollOffsetToTopIfSupported];
-[_UIFindNavigatorHarness _findNavigatorView];
-[_UIFindNavigatorHarness _layoutFindNavigator];
-[_UIFindNavigatorHarness _sendPlacementUpdate];
-[_UIFindNavigatorHarness _shouldAdjustHostViewContentOffsets];
-[_UIFindNavigatorHarness beginHoistingFindNavigator:];
-[_UIFindNavigatorHarness dismissFindNavigatorEndingActiveSession:];
-[_UIFindNavigatorHarness endHoistingFindNavigator:];
-[_UIFindNavigatorHarness endHoistingFindNavigator:endingActiveSession:];
-[_UIFindNavigatorHarness findNavigatorShouldDismissOnResponderChange:];
-[_UIFindNavigatorHarness findNavigatorViewController];
-[_UIFindNavigatorHarness findNavigatorViewControllerDidRequestDismissal:];
-[_UIFindNavigatorHarness findNavigatorViewControllerViewDidChangeIntrinsicContentSize:];
-[_UIFindNavigatorHarness hostScrollView];
-[_UIFindNavigatorHarness presentFindNavigatorWithFindSession:showingReplace:idiom:];
-[_UIFindNavigatorHarness setHostScrollView:];
-[_UIFindNavigatorHarness setInteractionView:];
```
