# `UIAsyncTextInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIWKTextInteractionAssistantDelegate`, `UIInteraction`
- 3 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"UIWKTextInteractionAssistant" _textInteractionAssistant;
@"UIView" _view;
@"<UIAsyncTextInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIAsyncTextInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"UITextSelectionDisplayInteraction",R,N) textSelectionDisplayInteraction;
@property (T@"<UIContextMenuInteractionDelegate>",W,N) contextMenuInteractionDelegate;
@property (T@"UIContextMenuInteraction",R,N) contextMenuInteraction;
@property (T@"UIView",R,W,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIAsyncTextInteraction contextMenuInteractionDelegate];
-[UIAsyncTextInteraction showTextServiceFor:fromRect:];
-[UIAsyncTextInteraction setContextMenuInteractionDelegate:];
-[UIAsyncTextInteraction lookup:withRange:fromRect:];
-[UIAsyncTextInteraction selectionChanged];
-[UIAsyncTextInteraction dealloc];
-[UIAsyncTextInteraction selectionWillChange:];
-[UIAsyncTextInteraction presentEditMenuForSelection];
-[UIAsyncTextInteraction editabilityChanged];
-[UIAsyncTextInteraction showShareSheetFor:fromRect:];
-[UIAsyncTextInteraction showDictionaryFor:fromRect:];
-[UIAsyncTextInteraction view];
-[UIAsyncTextInteraction translate:fromRect:];
-[UIAsyncTextInteraction setDelegate:];
-[UIAsyncTextInteraction contextMenuInteraction];
-[UIAsyncTextInteraction willMoveToView:];
-[UIAsyncTextInteraction dismissEditMenuForSelection];
-[UIAsyncTextInteraction scheduleReplacementsForText:];
-[UIAsyncTextInteraction delegate];
-[UIAsyncTextInteraction selectionChangedWithTouchAt:withSelectionTouch:withFlags:];
-[UIAsyncTextInteraction selectionChangedWithGestureAt:withGesture:withState:withFlags:];
-[UIAsyncTextInteraction asyncTextInput];
-[UIAsyncTextInteraction selectionDidChange:];
-[UIAsyncTextInteraction scheduleChineseTransliterationForText:];
-[UIAsyncTextInteraction textSelectionDisplayInteraction];
-[UIAsyncTextInteraction didMoveToView:];
```
