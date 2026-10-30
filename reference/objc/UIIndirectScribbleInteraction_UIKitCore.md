# `UIIndirectScribbleInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapperProvider`, `UIInteraction`
- 5 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
q __handlingWritingCount;
B _handlingWriting;
B __defaultSystemInteraction;
@"<UIIndirectScribbleInteractionDelegate>" _delegate;
@"UIView" _view;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (TB,N,GisHandlingWriting,S_setHandlingWriting:,V_handlingWriting) handlingWriting;
@property (TB,R,N,G_isDefaultSystemInteraction,V__defaultSystemInteraction) _defaultSystemInteraction;
@property (T@"<UIIndirectScribbleInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIIndirectScribbleInteraction initWithDelegate:];
-[UIIndirectScribbleInteraction _setDefaultSystemInteraction:];
-[UIIndirectScribbleInteraction scribbleInteractionWrapper];
-[UIIndirectScribbleInteraction setView:];
-[UIIndirectScribbleInteraction isHandlingWriting];
-[UIIndirectScribbleInteraction _setHandlingWritingCount:];
-[UIIndirectScribbleInteraction view];
-[UIIndirectScribbleInteraction willMoveToView:];
-[UIIndirectScribbleInteraction delegate];
-[UIIndirectScribbleInteraction _handlingWritingCount];
-[UIIndirectScribbleInteraction _setHandlingWriting:];
-[UIIndirectScribbleInteraction _isDefaultSystemInteraction];
-[UIIndirectScribbleInteraction didMoveToView:];
```
