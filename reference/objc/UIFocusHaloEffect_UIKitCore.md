# `UIFocusHaloEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFocusEffect`
- 6 instance variables, 5 properties, 11 instance methods, 4 class methods

## Instance variables

```
{?="isResolved"b1} _flags;
@"UIView" _containerView;
@"UIView" _referenceView;
q _position;
@"_UIShape" __shape;
@"<UICoordinateSpace>" __shapeCoordinateSpace;
```

## Properties

```
@property (T@"_UIShape",R,N,V__shape) _shape;
@property (T@"<UICoordinateSpace>",R,N,V__shapeCoordinateSpace) _shapeCoordinateSpace;
@property (T@"UIView",W,N,V_containerView) containerView;
@property (T@"UIView",W,N,V_referenceView) referenceView;
@property (Tq,N,V_position) position;
```

## Class methods

```
+[UIFocusHaloEffect effectWithPath:];
+[UIFocusHaloEffect effectWithRect:];
+[UIFocusHaloEffect _effectWithUIShape:];
+[UIFocusHaloEffect effectWithRoundedRect:cornerRadius:curve:];
```

## Instance methods

```
-[UIFocusHaloEffect setContainerView:];
-[UIFocusHaloEffect position];
-[UIFocusHaloEffect containerView];
-[UIFocusHaloEffect setReferenceView:];
-[UIFocusHaloEffect setPosition:];
-[UIFocusHaloEffect copyWithZone:];
-[UIFocusHaloEffect isEqual:];
-[UIFocusHaloEffect referenceView];
-[UIFocusHaloEffect _resolvedEffectForItem:];
-[UIFocusHaloEffect _shape];
-[UIFocusHaloEffect _shapeCoordinateSpace];
```
