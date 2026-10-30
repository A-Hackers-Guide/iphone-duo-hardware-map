# `UIInputViewSetPlacementFloating`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewSetPlacementUndocked`
- Protocols: `_UIGeometryChangeObserver`, `NSSecureCoding`
- 6 instance variables, 2 properties, 29 instance methods, 4 class methods

## Instance variables

```
d _floatingWidth;
@"UIView" _responderToFollow;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _responderRect;
{CGSize="width"d"height"d} _lastSize;
@"UIInputViewSetPlacementOnScreen" _cachedSecondaryPlacement;
@"NSArray" _subPlacements;
```

## Properties

```
@property (Td,N,V_floatingWidth) floatingWidth;
@property (T@"UIResponder",W,N,V_responderToFollow) responderToFollow;
```

## Class methods

```
+[UIInputViewSetPlacementFloating supportsSecureCoding];
+[UIInputViewSetPlacementFloating placementWithUndockedOffset:chromeBuffer:floatingWidth:];
+[UIInputViewSetPlacementFloating infoWithPoint:forOwner:];
+[UIInputViewSetPlacementFloating frameAtOffset:keyboardSize:screenSize:];
```

## Instance methods

```
-[UIInputViewSetPlacementFloating isFloating];
-[UIInputViewSetPlacementFloating floatingWidth];
-[UIInputViewSetPlacementFloating dealloc];
-[UIInputViewSetPlacementFloating showsEditItems];
-[UIInputViewSetPlacementFloating assistantView];
-[UIInputViewSetPlacementFloating remoteIntrinsicContentSizeForInputViewInSet:includingIAV:];
-[UIInputViewSetPlacementFloating _geometryChanged:forAncestor:];
-[UIInputViewSetPlacementFloating applicatorClassForKeyboard:];
-[UIInputViewSetPlacementFloating setDelegate:];
-[UIInputViewSetPlacementFloating encodeWithCoder:];
-[UIInputViewSetPlacementFloating applicatorInfoForOwner:];
-[UIInputViewSetPlacementFloating showsInputOrAssistantViewsForTracking];
-[UIInputViewSetPlacementFloating accessoryViewWillAppear];
-[UIInputViewSetPlacementFloating initWithCoder:];
-[UIInputViewSetPlacementFloating isFloatingAssistantView];
-[UIInputViewSetPlacementFloating isEqual:];
-[UIInputViewSetPlacementFloating adjustBoundsForNotificationsWithOwner:];
-[UIInputViewSetPlacementFloating checkSizeForOwner:];
-[UIInputViewSetPlacementFloating currentResponderView];
-[UIInputViewSetPlacementFloating expiringPlacement];
-[UIInputViewSetPlacementFloating horizontalConstraintForInputViewSet:hostView:containerView:];
-[UIInputViewSetPlacementFloating indexForPurpose:];
-[UIInputViewSetPlacementFloating responderToFollow];
-[UIInputViewSetPlacementFloating setFloatingWidth:];
-[UIInputViewSetPlacementFloating setResponderToFollow:];
-[UIInputViewSetPlacementFloating setSubPlacements:];
-[UIInputViewSetPlacementFloating subPlacements];
-[UIInputViewSetPlacementFloating updateChromeBuffer];
-[UIInputViewSetPlacementFloating widthConstraintForInputViewSet:hostView:containerView:];
```
