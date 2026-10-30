# `UIToolTipInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIToolTipProvider`, `_UIVisualStyleStylable`, `UIInteraction`
- 7 instance variables, 8 properties, 14 instance methods, 3 class methods

## Instance variables

```
B _delegateImplementsToolTipAtPoint;
B _isDefaultInteraction;
@"NSString" _defaultToolTip;
@"_UIToolTipInteractionStyle" _style;
B _enabled;
@"UIView" _view;
@"<UIToolTipInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIToolTipInteractionDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSString",C,N) defaultToolTip;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIToolTipInteraction visualStyleRegistryIdentity];
+[UIToolTipInteraction _defaultToolTipInteractionFromInteractions:];
+[UIToolTipInteraction _newDefaultToolTipInteraction];
```

## Instance methods

```
-[UIToolTipInteraction _refreshStyle];
-[UIToolTipInteraction init];
-[UIToolTipInteraction toolTipAtPoint:boundingRect:];
-[UIToolTipInteraction defaultToolTip];
-[UIToolTipInteraction isEnabled];
-[UIToolTipInteraction view];
-[UIToolTipInteraction setDefaultToolTip:];
-[UIToolTipInteraction setDelegate:];
-[UIToolTipInteraction _updateStyleForInteractionProperties];
-[UIToolTipInteraction setEnabled:];
-[UIToolTipInteraction willMoveToView:];
-[UIToolTipInteraction delegate];
-[UIToolTipInteraction initWithDefaultToolTip:];
-[UIToolTipInteraction didMoveToView:];
```
