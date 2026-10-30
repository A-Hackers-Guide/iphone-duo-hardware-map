# `PKScribbleInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapperProvider`, `UIInteraction`
- 5 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<PKScribbleInteractionWrapper>" _cachedWrapper;
@"UIView" _view;
B _requestElementsShouldCallBackSynchronously;
@"<PKScribbleInteractionDelegate>" _delegate;
@"<PKScribbleInteractionElementSource>" _elementSource;
```

## Properties

```
@property (T@"<PKScribbleInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"<PKScribbleInteractionElementSource>",W,N,V_elementSource) elementSource;
@property (T@"UIView",R,W,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKScribbleInteraction scribbleInteractionWrapper];
-[PKScribbleInteraction view];
-[PKScribbleInteraction setDelegate:];
-[PKScribbleInteraction willMoveToView:];
-[PKScribbleInteraction elementSource];
-[PKScribbleInteraction delegate];
-[PKScribbleInteraction setElementSource:];
-[PKScribbleInteraction didMoveToView:];
```
