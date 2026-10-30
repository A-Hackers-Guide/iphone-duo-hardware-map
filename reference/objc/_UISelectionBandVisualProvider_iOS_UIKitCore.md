# `_UISelectionBandVisualProvider_iOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPointerInteractionDelegate`, `_UISelectionBandVisualProviding`
- 3 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"UIPointerInteraction" _ptrInteraction;
{CGPoint="x"d"y"d} _initialPoint;
```

## Properties

```
@property (T@"UIPointerInteraction",&,N,V_ptrInteraction) ptrInteraction;
@property (T{CGPoint=dd},N,V_initialPoint) initialPoint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",W,N,V_view) view;
@property (TB,N) enabled;
```

## Instance methods

```
-[_UISelectionBandVisualProvider_iOS initialPoint];
-[_UISelectionBandVisualProvider_iOS _isActive];
-[_UISelectionBandVisualProvider_iOS enabled];
-[_UISelectionBandVisualProvider_iOS pointerInteraction:styleForRegion:];
-[_UISelectionBandVisualProvider_iOS setView:];
-[_UISelectionBandVisualProvider_iOS beginAtPoint:];
-[_UISelectionBandVisualProvider_iOS setInitialPoint:];
-[_UISelectionBandVisualProvider_iOS view];
-[_UISelectionBandVisualProvider_iOS setEnabled:];
-[_UISelectionBandVisualProvider_iOS setPtrInteraction:];
-[_UISelectionBandVisualProvider_iOS pointerInteraction:regionForRequest:defaultRegion:];
-[_UISelectionBandVisualProvider_iOS endAtPoint:];
-[_UISelectionBandVisualProvider_iOS ptrInteraction];
-[_UISelectionBandVisualProvider_iOS updateWithPoint:];
```
