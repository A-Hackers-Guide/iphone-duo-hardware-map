# `UIScribbleInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapperProvider`, `UIInteraction`
- 4 instance variables, 8 properties, 11 instance methods, 4 class methods

## Instance variables

```
B _handlingWriting;
B __defaultSystemInteraction;
@"<UIScribbleInteractionDelegate>" _delegate;
@"UIView" _view;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (TB,R,N,G_isDefaultSystemInteraction,V__defaultSystemInteraction) _defaultSystemInteraction;
@property (T@"<UIScribbleInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TB,R,N,GisHandlingWriting,V_handlingWriting) handlingWriting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIScribbleInteraction _lastEventSourceChanged:];
+[UIScribbleInteraction _recommendedBlankSpaceHeight];
+[UIScribbleInteraction isScribbleEnabled];
+[UIScribbleInteraction isPencilInputExpected];
```

## Instance methods

```
-[UIScribbleInteraction initWithDelegate:];
-[UIScribbleInteraction _setDefaultSystemInteraction:];
-[UIScribbleInteraction scribbleInteractionWrapper];
-[UIScribbleInteraction setView:];
-[UIScribbleInteraction isHandlingWriting];
-[UIScribbleInteraction view];
-[UIScribbleInteraction willMoveToView:];
-[UIScribbleInteraction delegate];
-[UIScribbleInteraction _setHandlingWriting:];
-[UIScribbleInteraction _isDefaultSystemInteraction];
-[UIScribbleInteraction didMoveToView:];
```
