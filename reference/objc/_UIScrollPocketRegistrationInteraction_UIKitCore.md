# `_UIScrollPocketRegistrationInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `UIInteraction_Private`, `UIInteraction`, `_UIGeometryChangeObserver`, `BSDescriptionStreaming`
- 5 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
receiver;
? delegate;
? _view;
isEnabled;
parentScrollPocketCollectorModel;
```

## Properties

```
@property (T@"<_UIScrollPocketRegistrationInteractionDelegate>",N,W,Vdelegate) delegate;
@property (T@"UIView",N,W,V_view) _view;
@property (T@"UIView",N,R) view;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_UIScrollPocketRegistrationInteraction _view];
-[_UIScrollPocketRegistrationInteraction init];
-[_UIScrollPocketRegistrationInteraction _updateProperties];
-[_UIScrollPocketRegistrationInteraction updatePocketCollectorModel];
-[_UIScrollPocketRegistrationInteraction _geometryChanged:forAncestor:];
-[_UIScrollPocketRegistrationInteraction view];
-[_UIScrollPocketRegistrationInteraction setDelegate:];
-[_UIScrollPocketRegistrationInteraction willMoveToView:];
-[_UIScrollPocketRegistrationInteraction set_view:];
-[_UIScrollPocketRegistrationInteraction delegate];
-[_UIScrollPocketRegistrationInteraction description];
-[_UIScrollPocketRegistrationInteraction appendDescriptionToStream:];
-[_UIScrollPocketRegistrationInteraction didMoveToView:];
```
