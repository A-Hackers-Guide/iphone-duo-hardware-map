# `_UIViewGeometryObserverInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `_UIGeometryChangeObserver`
- 4 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q options;
? changeHandler;
$__lazy_storage_$_geometryChangeFlags;
? _view;
```

## Properties

```
@property (TQ,N,R,Voptions) options;
@property (T@?,N,R) changeHandler;
@property (TQ,N) geometryChangeFlags;
@property (T@"UIView",N,W,V_view) _view;
@property (T@"UIView",N,R) view;
```

## Instance methods

```
-[_UIViewGeometryObserverInteraction _view];
-[_UIViewGeometryObserverInteraction init];
-[_UIViewGeometryObserverInteraction _geometryChanged:forAncestor:];
-[_UIViewGeometryObserverInteraction view];
-[_UIViewGeometryObserverInteraction willMoveToView:];
-[_UIViewGeometryObserverInteraction set_view:];
-[_UIViewGeometryObserverInteraction options];
-[_UIViewGeometryObserverInteraction changeHandler];
-[_UIViewGeometryObserverInteraction didMoveToView:];
-[_UIViewGeometryObserverInteraction geometryChangeFlags];
-[_UIViewGeometryObserverInteraction initWithOptions:changeHandler:];
-[_UIViewGeometryObserverInteraction setGeometryChangeFlags:];
```
