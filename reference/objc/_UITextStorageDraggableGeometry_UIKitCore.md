# `_UITextStorageDraggableGeometry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextDraggableGeometry`, `UITextDraggableGeometryFastSameViewOperationsSupporting`
- 4 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _previousBackgroundColor;
q _geometryOptions;
@"UIView<UITextDragSupporting>" _view;
@"NSTextStorage" _textStorage;
```

## Properties

```
@property (T@"UIView<UITextDragSupporting>",R,W,N,V_view) view;
@property (T@"NSTextStorage",R,W,N,V_textStorage) textStorage;
@property (Tq,N,V_geometryOptions) geometryOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextStorageDraggableGeometry textStorage];
-[_UITextStorageDraggableGeometry targetedPreviewProviderForTextInRange:dismissing:];
-[_UITextStorageDraggableGeometry setGeometryOptions:];
-[_UITextStorageDraggableGeometry _previewProviderForTextInRange:];
-[_UITextStorageDraggableGeometry previewForDroppingTextInRange:toPosition:inContainerView:];
-[_UITextStorageDraggableGeometry _renderTextInRange:image:boundingRectangles:forLifting:];
-[_UITextStorageDraggableGeometry performSameViewDropOperation:];
-[_UITextStorageDraggableGeometry _draggableTextInRange:];
-[_UITextStorageDraggableGeometry draggableObjectsForTextRange:];
-[_UITextStorageDraggableGeometry geometryOptions];
-[_UITextStorageDraggableGeometry _targetedPreviewProviderForTextInRange:dismissing:overrideLifting:];
-[_UITextStorageDraggableGeometry _isActualLink:];
-[_UITextStorageDraggableGeometry attributedStringsForTextRanges:];
-[_UITextStorageDraggableGeometry view];
-[_UITextStorageDraggableGeometry _targetedPreviewProviderForTextInRange:];
-[_UITextStorageDraggableGeometry _targetedPreviewProviderForImage:inRange:];
-[_UITextStorageDraggableGeometry textRangesForAttachmentsInTextRange:];
-[_UITextStorageDraggableGeometry initWithView:textStorage:];
-[_UITextStorageDraggableGeometry textRangeForAttachmentInTextRange:atPoint:];
```
