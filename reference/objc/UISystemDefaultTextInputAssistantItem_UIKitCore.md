# `UISystemDefaultTextInputAssistantItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInputAssistantItem`
- 5 instance variables, 5 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _systemItem;
B _isKeyboardCameraItem;
@"<UISystemDefaultTextInputAssistantItemDelegate>" _delegate;
@"NSArray" _defaultSystemLeadingBarButtonGroups;
@"NSArray" _defaultSystemTrailingBarButtonGroups;
```

## Properties

```
@property (TB,N,G_isSystemItem,V_systemItem) systemItem;
@property (T@"NSArray",&,N,V_defaultSystemLeadingBarButtonGroups) defaultSystemLeadingBarButtonGroups;
@property (T@"NSArray",&,N,V_defaultSystemTrailingBarButtonGroups) defaultSystemTrailingBarButtonGroups;
@property (T@"<UISystemDefaultTextInputAssistantItemDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,V_isKeyboardCameraItem) isKeyboardCameraItem;
```

## Instance methods

```
-[UISystemDefaultTextInputAssistantItem assistantTextFormatting];
-[UISystemDefaultTextInputAssistantItem performSystemButtonActionForStyle:];
-[UISystemDefaultTextInputAssistantItem assistantPaste:forEvent:];
-[UISystemDefaultTextInputAssistantItem init];
-[UISystemDefaultTextInputAssistantItem assistantCut];
-[UISystemDefaultTextInputAssistantItem setSystemItem:];
-[UISystemDefaultTextInputAssistantItem analyticsDispatchWithActionStyle:];
-[UISystemDefaultTextInputAssistantItem assistantDictation];
-[UISystemDefaultTextInputAssistantItem assistantShowKeyboard];
-[UISystemDefaultTextInputAssistantItem isKeyboardCameraItem];
-[UISystemDefaultTextInputAssistantItem canPerformSystemButtonActionForStyle:];
-[UISystemDefaultTextInputAssistantItem assistantUndo];
-[UISystemDefaultTextInputAssistantItem _responderSelectorForSystemButtonStyle:];
-[UISystemDefaultTextInputAssistantItem assistantExpand];
-[UISystemDefaultTextInputAssistantItem assistantReturnKey];
-[UISystemDefaultTextInputAssistantItem assistantBold];
-[UISystemDefaultTextInputAssistantItem _updateIsSystemItem];
-[UISystemDefaultTextInputAssistantItem setDelegate:];
-[UISystemDefaultTextInputAssistantItem _isSystemItem];
-[UISystemDefaultTextInputAssistantItem assistantEmoji];
-[UISystemDefaultTextInputAssistantItem assistantDismiss];
-[UISystemDefaultTextInputAssistantItem delegate];
-[UISystemDefaultTextInputAssistantItem setTrailingBarButtonGroups:];
-[UISystemDefaultTextInputAssistantItem defaultSystemTrailingBarButtonGroups];
-[UISystemDefaultTextInputAssistantItem assistantTextAnimation];
-[UISystemDefaultTextInputAssistantItem setLeadingBarButtonGroups:];
-[UISystemDefaultTextInputAssistantItem defaultSystemLeadingBarButtonGroups];
-[UISystemDefaultTextInputAssistantItem assistantUnderline];
-[UISystemDefaultTextInputAssistantItem assistantDictationMicOn];
-[UISystemDefaultTextInputAssistantItem assistantCopy];
-[UISystemDefaultTextInputAssistantItem assistantRedo];
-[UISystemDefaultTextInputAssistantItem setDefaultSystemTrailingBarButtonGroups:];
-[UISystemDefaultTextInputAssistantItem setDefaultSystemLeadingBarButtonGroups:];
-[UISystemDefaultTextInputAssistantItem assistantItalic];
-[UISystemDefaultTextInputAssistantItem assistantWriteboard];
```
