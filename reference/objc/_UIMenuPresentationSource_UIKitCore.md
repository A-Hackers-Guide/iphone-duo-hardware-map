# `_UIMenuPresentationSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UITargetedPreview" _targetedPreview;
@"UIView" _sourceView;
@"_UIDragSessionIntelligenceBridge" _dragSessionBridge;
{CGPoint="x"d"y"d} _touchLocation;
```

## Properties

```
@property (T@"UITargetedPreview",R,N,V_targetedPreview) targetedPreview;
@property (T@"UIView",R,N,V_sourceView) sourceView;
@property (T{CGPoint=dd},R,N,V_touchLocation) touchLocation;
@property (T@"_UIDragSessionIntelligenceBridge",&,N,V_dragSessionBridge) dragSessionBridge;
```

## Instance methods

```
-[_UIMenuPresentationSource sourceView];
-[_UIMenuPresentationSource targetedPreview];
-[_UIMenuPresentationSource dragSessionBridge];
-[_UIMenuPresentationSource initWithTargetedPreview:sourceView:touchLocation:];
-[_UIMenuPresentationSource setDragSessionBridge:];
-[_UIMenuPresentationSource touchLocation];
```
