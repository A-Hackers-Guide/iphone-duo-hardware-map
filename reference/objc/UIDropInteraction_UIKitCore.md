# `UIDropInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragGestureRecognizerDelegate`, `UIInteraction_Internal`, `_UIDragSetDownAnimationTarget`, `_UIVisualStyleStylable`, `UIInteraction`
- 11 instance variables, 12 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _activeDragGestureRecognizers;
@"NSMapTable" _enteredDropSessionByDraggingSession;
Q _potentialDragOperation;
{?="canHandleSession"b1"sessionDidEnter"b1"sessionDidUpdate"b1"sessionDidExit"b1"performDrop"b1"concludeDrop"b1"sessionDidEnd"b1"previewForDroppingItem"b1"willAnimateDropWithAnimator"b1"dataOwnerForSession"b1"delayedPreviewProviderForDroppingItem"b1"customSpringAnimationBehaviorForDroppingItem"b1"shouldPlayDropFeedbackForSession"b1} _delegateImplements;
B _allowsSimultaneousDropSessions;
B _wantsDefaultVisualBehavior;
@"<UIDropInteractionDelegate>" _delegate;
@"<_UIDropInteractionOwning>" _owner;
@"UIDropInteractionContextImpl" _context;
@"UIPasteConfiguration" _pasteConfiguration;
@"<UIDropInteractionEffect>" _interactionEffect;
```

## Properties

```
@property (T@"<_UIDropInteractionOwning>",W,N,V_owner) owner;
@property (T@"UIDropInteractionContextImpl",&,N,V_context) context;
@property (T@"UIPasteConfiguration",R,C,N,G_pasteConfiguration,V_pasteConfiguration) pasteConfiguration;
@property (T@"<UIDropInteractionEffect>",&,N,V_interactionEffect) interactionEffect;
@property (TB,N,G_wantsDefaultVisualBehavior,S_setWantsDefaultVisualBehavior:,V_wantsDefaultVisualBehavior) wantsDefaultVisualBehavior;
@property (T@"<UIDropInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_allowsSimultaneousDropSessions) allowsSimultaneousDropSessions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N) view;
```

## Class methods

```
+[UIDropInteraction visualStyleRegistryIdentity];
```

## Instance methods

```
-[UIDropInteraction _gestureRecognizerFailed:];
-[UIDropInteraction owner];
-[UIDropInteraction _dynamicGestureRecognizersForEvent:];
-[UIDropInteraction initWithDelegate:];
-[UIDropInteraction interactionEffect];
-[UIDropInteraction _setDownAnimation:prepareForSetDownOfDragItem:visibleDroppedItem:];
-[UIDropInteraction _sendSessionDidEnd:];
-[UIDropInteraction _dropSessionEntered:withSessionDestination:];
-[UIDropInteraction setInteractionEffect:];
-[UIDropInteraction _setWantsDefaultVisualBehavior:];
-[UIDropInteraction _setDownAnimation:willAnimateSetDownOfDragItem:withAnimator:preview:];
-[UIDropInteraction _gestureRecognizer:shouldReceiveDragEvent:];
-[UIDropInteraction _canHandleDragEvent:];
-[UIDropInteraction setOwner:];
-[UIDropInteraction _validateDragOperation:forSelector:delegate:dropSession:onSession:forbidden:];
-[UIDropInteraction didMoveToOwner:];
-[UIDropInteraction _windowForSetDownOfDragItem:];
-[UIDropInteraction view];
-[UIDropInteraction _allowsSimultaneousDragWithEvent:];
-[UIDropInteraction setContext:];
-[UIDropInteraction willMoveToOwner:];
-[UIDropInteraction _pasteConfiguration];
-[UIDropInteraction willMoveToView:];
-[UIDropInteraction _initWithPasteConfiguration:];
-[UIDropInteraction delegate];
-[UIDropInteraction _prepareItemsInSessionForDrop:];
-[UIDropInteraction setAllowsSimultaneousDropSessions:];
-[UIDropInteraction _wantsDefaultVisualBehavior];
-[UIDropInteraction isActive];
-[UIDropInteraction _setDownAnimation:customSpringAnimationBehaviorForSetDownOfDragItem:];
-[UIDropInteraction context];
-[UIDropInteraction allowsSimultaneousDropSessions];
-[UIDropInteraction didMoveToView:];
-[UIDropInteraction _setDownAnimation:updatedSetDownOfDragItem:preview:];
-[UIDropInteraction _dragDestinationGestureStateChanged:];
-[UIDropInteraction _setLastDragOperation:forbidden:precise:prefersFullSizePreview:preferredBadgeStyle:onSession:];
```
