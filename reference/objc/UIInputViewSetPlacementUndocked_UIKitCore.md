# `UIInputViewSetPlacementUndocked`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewSetPlacement`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 17 instance methods, 4 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _normalizedOffset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _chromeBuffer;
```

## Properties

```
@property (T{CGPoint=dd},N,V_normalizedOffset) normalizedOffset;
@property (T{UIEdgeInsets=dddd},N,V_chromeBuffer) chromeBuffer;
```

## Class methods

```
+[UIInputViewSetPlacementUndocked supportsSecureCoding];
+[UIInputViewSetPlacementUndocked infoWithPoint:];
+[UIInputViewSetPlacementUndocked placementWithUndockedOffset:chromeBuffer:];
+[UIInputViewSetPlacementUndocked computeOffsetForOffset:withSize:chromeBuffer:onScreenSize:];
```

## Instance methods

```
-[UIInputViewSetPlacementUndocked isUndocked];
-[UIInputViewSetPlacementUndocked remoteIntrinsicContentSizeForInputViewInSet:includingIAV:];
-[UIInputViewSetPlacementUndocked inputViewWillAppear];
-[UIInputViewSetPlacementUndocked applicatorClassForKeyboard:];
-[UIInputViewSetPlacementUndocked verticalConstraintForInputViewSet:hostView:containerView:];
-[UIInputViewSetPlacementUndocked encodeWithCoder:];
-[UIInputViewSetPlacementUndocked applicatorInfoForOwner:];
-[UIInputViewSetPlacementUndocked showsInputOrAssistantViewsForTracking];
-[UIInputViewSetPlacementUndocked initWithCoder:];
-[UIInputViewSetPlacementUndocked setOffset:];
-[UIInputViewSetPlacementUndocked isEqual:];
-[UIInputViewSetPlacementUndocked chromeBuffer];
-[UIInputViewSetPlacementUndocked heightOfInputViews:];
-[UIInputViewSetPlacementUndocked normalizedOffset];
-[UIInputViewSetPlacementUndocked setChromeBuffer:];
-[UIInputViewSetPlacementUndocked setNormalizedOffset:];
-[UIInputViewSetPlacementUndocked updateChromeBuffer];
```
