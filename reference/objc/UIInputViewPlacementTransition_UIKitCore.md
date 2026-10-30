# `UIInputViewPlacementTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 20 instance methods, 2 class methods

## Instance variables

```
B cancelled;
i animationState;
@"UIInputViewSetPlacement" fromPlacement;
@"UIInputViewSetPlacement" toPlacement;
@"UIInputViewAnimationStyle" animationStyle;
@"UIInputViewSetNotificationInfo" notificationInfo;
Q notifications;
@"<NSObject>" animationContext;
@"<UIInputViewAnimationController>" animationController;
```

## Properties

```
@property (T@"UIInputViewSetPlacement",&,N,VfromPlacement) fromPlacement;
@property (T@"UIInputViewSetPlacement",&,N,VtoPlacement) toPlacement;
@property (T@"UIInputViewAnimationStyle",&,N,VanimationStyle) animationStyle;
@property (T@"UIInputViewSetNotificationInfo",&,N,VnotificationInfo) notificationInfo;
@property (TQ,N,Vnotifications) notifications;
@property (Ti,N,VanimationState) animationState;
@property (T@"<UIInputViewAnimationController>",&,N,VanimationController) animationController;
@property (T@"<NSObject>",&,N,VanimationContext) animationContext;
@property (TB,N,Vcancelled) cancelled;
```

## Class methods

```
+[UIInputViewPlacementTransition transitionForExistingPlacement:animationStyle:];
+[UIInputViewPlacementTransition transitionFromPlacement:toPlacement:withAnimationStyle:];
```

## Instance methods

```
-[UIInputViewPlacementTransition animationState];
-[UIInputViewPlacementTransition notifications];
-[UIInputViewPlacementTransition animationController];
-[UIInputViewPlacementTransition cancelled];
-[UIInputViewPlacementTransition setAnimationContext:];
-[UIInputViewPlacementTransition setNotificationInfo:];
-[UIInputViewPlacementTransition setCancelled:];
-[UIInputViewPlacementTransition notificationInfo];
-[UIInputViewPlacementTransition dealloc];
-[UIInputViewPlacementTransition fromPlacement];
-[UIInputViewPlacementTransition animationStyle];
-[UIInputViewPlacementTransition animationContext];
-[UIInputViewPlacementTransition setFromPlacement:];
-[UIInputViewPlacementTransition didAdvanceAnimationToState:];
-[UIInputViewPlacementTransition toPlacement];
-[UIInputViewPlacementTransition setToPlacement:];
-[UIInputViewPlacementTransition setAnimationState:];
-[UIInputViewPlacementTransition setAnimationStyle:];
-[UIInputViewPlacementTransition setNotifications:];
-[UIInputViewPlacementTransition setAnimationController:];
```
