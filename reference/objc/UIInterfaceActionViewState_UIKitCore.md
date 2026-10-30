# `UIInterfaceActionViewState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInterfaceActionVisualStyleViewState`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 15 instance methods, 6 class methods

## Instance variables

```
B _isHighlighted;
B _isPressed;
B _isFocused;
B _isPreferred;
@"UIInterfaceAction" _action;
@ _actionViewStateContext;
Q _visualCornerPosition;
```

## Properties

```
@property (T@"UIInterfaceAction",R,N,V_action) action;
@property (TB,R,N,V_isHighlighted) isHighlighted;
@property (TB,R,N,V_isPressed) isPressed;
@property (TB,R,N,V_isFocused) isFocused;
@property (TB,R,N,V_isPreferred) isPreferred;
@property (T@,R,N,V_actionViewStateContext) actionViewStateContext;
@property (TQ,R,N,V_visualCornerPosition) visualCornerPosition;
```

## Class methods

```
+[UIInterfaceActionViewState _nullViewStateForActionType:];
+[UIInterfaceActionViewState viewStateForActionRepresentationView:action:];
+[UIInterfaceActionViewState viewStateForActionRepresentationViewDescendantView:action:];
+[UIInterfaceActionViewState viewStateForAlertControllerActionView:];
+[UIInterfaceActionViewState viewStateRepresentingDefaultAction];
+[UIInterfaceActionViewState viewStateRepresentingPreferredAction];
```

## Instance methods

```
-[UIInterfaceActionViewState _collectStateForDefaultState];
-[UIInterfaceActionViewState isPreferred];
-[UIInterfaceActionViewState visualCornerPosition];
-[UIInterfaceActionViewState isHighlighted];
-[UIInterfaceActionViewState _collectStateFromAction:];
-[UIInterfaceActionViewState action];
-[UIInterfaceActionViewState isFocused];
-[UIInterfaceActionViewState isPressed];
-[UIInterfaceActionViewState _collectStateFromActionViewState:];
-[UIInterfaceActionViewState _collectStateFromActionRepresentationView:];
-[UIInterfaceActionViewState initWithPropertiesFromActionRepresentationView:groupView:action:];
-[UIInterfaceActionViewState copyWithZone:];
-[UIInterfaceActionViewState isEqual:];
-[UIInterfaceActionViewState actionViewStateContext];
-[UIInterfaceActionViewState _stateEqualToActionViewState:];
```
