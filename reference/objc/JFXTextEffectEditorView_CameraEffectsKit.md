# `JFXTextEffectEditorView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIIndirectScribbleInteractionDelegate`
- 6 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"JFXTextEffectEditorTextView" _editField;
@"UIView" _transformView;
@"JFXEffectTextEditingProperties" _textEditingProperties;
@"NSUUID" _pencilTextEditingElementID;
@"JFXOverlayEffectDebugViewOptions" _debugOptions;
@"UIView" _debugView;
```

## Properties

```
@property (T@"JFXTextEffectEditorTextView",&,N,V_editField) editField;
@property (T@"JFXEffectTextEditingProperties",&,N,V_textEditingProperties) textEditingProperties;
@property (T@"UIView",&,N,V_transformView) transformView;
@property (T@"NSUUID",&,N,V_pencilTextEditingElementID) pencilTextEditingElementID;
@property (T@"JFXOverlayEffectDebugViewOptions",&,N,V_debugOptions) debugOptions;
@property (T@"UIView",&,N,V_debugView) debugView;
@property (T@"NSString",R,N) text;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXTextEffectEditorView endEditing];
-[JFXTextEffectEditorView text];
-[JFXTextEffectEditorView debugView];
-[JFXTextEffectEditorView setDebugView:];
-[JFXTextEffectEditorView debugOptions];
-[JFXTextEffectEditorView setDebugOptions:];
-[JFXTextEffectEditorView selectAll];
-[JFXTextEffectEditorView indirectScribbleInteraction:focusElementIfNeeded:referencePoint:completion:];
-[JFXTextEffectEditorView indirectScribbleInteraction:frameForElement:];
-[JFXTextEffectEditorView indirectScribbleInteraction:isElementFocused:];
-[JFXTextEffectEditorView indirectScribbleInteraction:requestElementsInRect:completion:];
-[JFXTextEffectEditorView transformView];
-[JFXTextEffectEditorView applyTextEditingProperties:];
-[JFXTextEffectEditorView editField];
-[JFXTextEffectEditorView initWithFrame:textEditingProperties:];
-[JFXTextEffectEditorView initWithFrame:textEditingProperties:textContainer:];
-[JFXTextEffectEditorView pencilTextEditingElementID];
-[JFXTextEffectEditorView setEditField:];
-[JFXTextEffectEditorView setPencilTextEditingElementID:];
-[JFXTextEffectEditorView setTextEditingProperties:];
-[JFXTextEffectEditorView setTransformView:];
-[JFXTextEffectEditorView textEditingProperties];
```
