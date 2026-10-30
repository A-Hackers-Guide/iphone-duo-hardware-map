# `_UITextCanvasContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"_UITextLayoutControllerBase<_UITextLayoutController>",R,N) textLayoutController;
@property (T@"NSTextContainer",R,N) textContainer;
@property (T{CGPoint=dd},R,N) textContainerOrigin;
@property (T@"UIColor",R,N) textColor;
@property (T@"UIScrollView",R,N) enclosingScrollView;
@property (TB,R,N) hasOverriddenEnclosingScrollView;
@property (TB,R,N,GisEditable) editable;
@property (TB,R,N,GisEditing) editing;
@property (T{CGPoint=dd},R,N) drawingScale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _clipRectForFadedEdges;
@property (T@"<NSCustomTextRendering>",?,R,N) customRenderController;
```

## Instance methods

```
-[_UITextCanvasContext isEditable];
-[_UITextCanvasContext _clipRectForFadedEdges];
-[_UITextCanvasContext textContainer];
-[_UITextCanvasContext textContainerUsageDidChangeToSize:];
-[_UITextCanvasContext textColor];
-[_UITextCanvasContext enclosingScrollView];
-[_UITextCanvasContext drawTextInRectIfNeeded:];
-[_UITextCanvasContext textLayoutController];
-[_UITextCanvasContext drawingScale];
-[_UITextCanvasContext textContainerOrigin];
-[_UITextCanvasContext didAddTextAttachmentViews:];
-[_UITextCanvasContext didLayoutTextAttachmentView:inFragmentRect:];
-[_UITextCanvasContext hasOverriddenEnclosingScrollView];
-[_UITextCanvasContext didRemoveTextAttachmentViews:];
-[_UITextCanvasContext isEditing];
-[_UITextCanvasContext _updateInteractionGeometry];
-[_UITextCanvasContext _textKit2CanvasDidLayout];
-[_UITextCanvasContext customRenderController];
```
