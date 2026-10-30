# `UITrackingElementPlacementTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 22 instance methods, 2 class methods

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
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} lastKnownKeyboardFrame;
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
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,VlastKnownKeyboardFrame) lastKnownKeyboardFrame;
```

## Class methods

```
+[UITrackingElementPlacementTransition transitionForExistingPlacement:animationStyle:];
+[UITrackingElementPlacementTransition transitionFromPlacement:toPlacement:withAnimationStyle:];
```

## Instance methods

```
-[UITrackingElementPlacementTransition animationState];
-[UITrackingElementPlacementTransition notifications];
-[UITrackingElementPlacementTransition animationController];
-[UITrackingElementPlacementTransition cancelled];
-[UITrackingElementPlacementTransition setAnimationContext:];
-[UITrackingElementPlacementTransition setNotificationInfo:];
-[UITrackingElementPlacementTransition setCancelled:];
-[UITrackingElementPlacementTransition setLastKnownKeyboardFrame:];
-[UITrackingElementPlacementTransition notificationInfo];
-[UITrackingElementPlacementTransition dealloc];
-[UITrackingElementPlacementTransition fromPlacement];
-[UITrackingElementPlacementTransition animationStyle];
-[UITrackingElementPlacementTransition animationContext];
-[UITrackingElementPlacementTransition setFromPlacement:];
-[UITrackingElementPlacementTransition didAdvanceAnimationToState:];
-[UITrackingElementPlacementTransition toPlacement];
-[UITrackingElementPlacementTransition setToPlacement:];
-[UITrackingElementPlacementTransition setAnimationState:];
-[UITrackingElementPlacementTransition setAnimationStyle:];
-[UITrackingElementPlacementTransition setNotifications:];
-[UITrackingElementPlacementTransition setAnimationController:];
-[UITrackingElementPlacementTransition lastKnownKeyboardFrame];
```
