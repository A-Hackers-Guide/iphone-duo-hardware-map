# `UIContextualAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _forcesFallbackBackgroundColor;
q _style;
@? _handler;
@"NSString" _title;
@"UIColor" _backgroundColor;
@"UIImage" _image;
@? _completionHandler;
@? _preHandler;
@"UIMenu" __menu;
@"UIVisualEffect" __backgroundEffect;
```

## Properties

```
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@?,C,N,V_handler) handler;
@property (TB,N,V_forcesFallbackBackgroundColor) forcesFallbackBackgroundColor;
@property (TB,R,N) isDestructive;
@property (T@?,C,N,V_preHandler) preHandler;
@property (T@"UIMenu",C,N,S_setMenu:,V__menu) _menu;
@property (T@"UIVisualEffect",C,N,S_setBackgroundEffect:,V__backgroundEffect) _backgroundEffect;
@property (Tq,R,N,V_style) style;
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
@property (T@"UIImage",C,N,V_image) image;
```

## Class methods

```
+[UIContextualAction contextualActionWithStyle:title:handler:];
```

## Instance methods

```
-[UIContextualAction _backgroundEffect];
-[UIContextualAction setCompletionHandler:];
-[UIContextualAction completionHandler];
-[UIContextualAction _setBackgroundEffect:];
-[UIContextualAction setHandler:];
-[UIContextualAction style];
-[UIContextualAction setBackgroundColor:];
-[UIContextualAction title];
-[UIContextualAction handler];
-[UIContextualAction isDestructive];
-[UIContextualAction backgroundColor];
-[UIContextualAction description];
-[UIContextualAction setTitle:];
-[UIContextualAction image];
-[UIContextualAction cancel];
-[UIContextualAction setImage:];
-[UIContextualAction _completeWithResult:];
-[UIContextualAction _menu];
-[UIContextualAction _setMenu:];
-[UIContextualAction executeHandlerWithView:completionHandler:];
-[UIContextualAction executePreHandlerWithView:];
-[UIContextualAction forcesFallbackBackgroundColor];
-[UIContextualAction preHandler];
-[UIContextualAction setForcesFallbackBackgroundColor:];
-[UIContextualAction setPreHandler:];
```
