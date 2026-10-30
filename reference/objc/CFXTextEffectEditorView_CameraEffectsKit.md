# `CFXTextEffectEditorView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UITextDragDelegate`, `UITextPasteDelegate`, `UITextViewDelegate`, `JFXTextEffectEditorTextViewDelegate`
- 2 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"<CFXTextEffectEditorViewDelegate>" _delegate;
@"JFXTextEffectEditorView" _editorView;
```

## Properties

```
@property (T@"JFXTextEffectEditorView",&,N,V_editorView) editorView;
@property (T@"NSString",R,N) text;
@property (T@"<CFXTextEffectEditorViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXTextEffectEditorView viewWithFrame:textEditingProperties:];
```

## Instance methods

```
-[CFXTextEffectEditorView text];
-[CFXTextEffectEditorView applicationDidEnterBackground:];
-[CFXTextEffectEditorView textViewDidChange:];
-[CFXTextEffectEditorView setDelegate:];
-[CFXTextEffectEditorView delegate];
-[CFXTextEffectEditorView textView:shouldChangeTextInRange:replacementText:];
-[CFXTextEffectEditorView selectAll];
-[CFXTextEffectEditorView textDraggableView:itemsForDrag:];
-[CFXTextEffectEditorView textPasteConfigurationSupporting:shouldAnimatePasteOfAttributedString:toRange:];
-[CFXTextEffectEditorView CFX_setupTextField:];
-[CFXTextEffectEditorView textEditingFrameRelativeToView:];
-[CFXTextEffectEditorView applyTextEditingProperties:];
-[CFXTextEffectEditorView editorView];
-[CFXTextEffectEditorView endTextEditing];
-[CFXTextEffectEditorView initWithFrame:textEditingProperties:];
-[CFXTextEffectEditorView selectAtEnd];
-[CFXTextEffectEditorView setEditorView:];
-[CFXTextEffectEditorView textEffectEditorTextViewDidUnmarkText:];
```
