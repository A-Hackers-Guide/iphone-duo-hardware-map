# `UIInputViewSetPlacement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 18 properties, 46 instance methods, 4 class methods

## Instance variables

```
B _dirty;
@"<UIInputViewSetPlacementDelegate>" delegate;
d _extendedHeight;
@"NSArray" _subPlacements;
```

## Properties

```
@property (TB,R,N) showsInputViews;
@property (TB,R,N) showsKeyboard;
@property (TB,R,N) showsInputOrAssistantViews;
@property (TB,R,N) showsInputOrAssistantViewsForTracking;
@property (TB,R,N) showsEditItems;
@property (TB,R,N) isUndocked;
@property (TB,R,N) requiresWindowBasedSafeAreaInsets;
@property (TB,R,N) isFloating;
@property (T@"UIInputViewSetPlacement",R,N) assistantView;
@property (TB,R,N) isFloatingAssistantView;
@property (TB,R,N) isCompactAssistantView;
@property (TB,R,N) isVisible;
@property (TB,R,N) isHiddenForFloatingTransition;
@property (TB,R,N) isInteractive;
@property (Td,N,V_extendedHeight) extendedHeight;
@property (Td,R,N) alpha;
@property (T@"NSArray",&,N,V_subPlacements) subPlacements;
@property (T@"<UIInputViewSetPlacementDelegate>",W,N,Vdelegate) delegate;
```

## Class methods

```
+[UIInputViewSetPlacement supportsSecureCoding];
+[UIInputViewSetPlacement placement];
+[UIInputViewSetPlacement deactivatedKeyboardPlacementWithCurrentPlacement:];
+[UIInputViewSetPlacement encodablePlacementsForXPC];
```

## Instance methods

```
-[UIInputViewSetPlacement extendedHeight];
-[UIInputViewSetPlacement isUndocked];
-[UIInputViewSetPlacement isFloating];
-[UIInputViewSetPlacement isInteractive];
-[UIInputViewSetPlacement showsEditItems];
-[UIInputViewSetPlacement isVisible];
-[UIInputViewSetPlacement transform];
-[UIInputViewSetPlacement assistantView];
-[UIInputViewSetPlacement keyboardState];
-[UIInputViewSetPlacement remoteIntrinsicContentSizeForInputViewInSet:includingIAV:];
-[UIInputViewSetPlacement inputViewWillAppear];
-[UIInputViewSetPlacement applicatorClassForKeyboard:];
-[UIInputViewSetPlacement setDelegate:];
-[UIInputViewSetPlacement verticalConstraintForInputViewSet:hostView:containerView:];
-[UIInputViewSetPlacement encodeWithCoder:];
-[UIInputViewSetPlacement applicatorInfoForOwner:];
-[UIInputViewSetPlacement showsInputOrAssistantViews];
-[UIInputViewSetPlacement delegate];
-[UIInputViewSetPlacement showsInputOrAssistantViewsForTracking];
-[UIInputViewSetPlacement showsInputViews];
-[UIInputViewSetPlacement description];
-[UIInputViewSetPlacement accessoryViewWillAppear];
-[UIInputViewSetPlacement initWithCoder:];
-[UIInputViewSetPlacement showsKeyboard];
-[UIInputViewSetPlacement alpha];
-[UIInputViewSetPlacement isFloatingAssistantView];
-[UIInputViewSetPlacement isEqual:];
-[UIInputViewSetPlacement setExtendedHeight:];
-[UIInputViewSetPlacement adjustBoundsForNotificationsWithOwner:];
-[UIInputViewSetPlacement checkSizeForOwner:];
-[UIInputViewSetPlacement computeComparisonMask];
-[UIInputViewSetPlacement expiringPlacement];
-[UIInputViewSetPlacement horizontalConstraintForInputViewSet:hostView:containerView:];
-[UIInputViewSetPlacement indexForPurpose:];
-[UIInputViewSetPlacement inputAccessoryViewPadding];
-[UIInputViewSetPlacement inputAssistantViewHeightForInputViewSet:];
-[UIInputViewSetPlacement isCompactAssistantView];
-[UIInputViewSetPlacement isHiddenForFloatingTransition];
-[UIInputViewSetPlacement notificationsForTransitionToPlacement:];
-[UIInputViewSetPlacement requiresWindowBasedSafeAreaInsets];
-[UIInputViewSetPlacement setDirty];
-[UIInputViewSetPlacement setOtherPlacement:];
-[UIInputViewSetPlacement setSubPlacements:];
-[UIInputViewSetPlacement subPlacements];
-[UIInputViewSetPlacement subPlacementsForInputViewSet:];
-[UIInputViewSetPlacement widthConstraintForInputViewSet:hostView:containerView:];
```
