# `_UIPreviewInteractionSystemHighlighter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPreviewInteractionHighlighting`
- 4 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _blinderViewEnabled;
@"UIView" _initialSnapshotView;
@"UIView" _updatedSnapshotView;
@"UIView" _blinderView;
```

## Properties

```
@property (T@"UIView",&,N,V_initialSnapshotView) initialSnapshotView;
@property (T@"UIView",&,N,V_updatedSnapshotView) updatedSnapshotView;
@property (TB,N,V_blinderViewEnabled) blinderViewEnabled;
@property (T@"UIView",&,N,V_blinderView) blinderView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionSystemHighlighter setBlinderView:];
-[_UIPreviewInteractionSystemHighlighter _newSnapshotViewForPreviewingContext:afterScreenUpdates:];
-[_UIPreviewInteractionSystemHighlighter blinderView];
-[_UIPreviewInteractionSystemHighlighter blinderViewEnabled];
-[_UIPreviewInteractionSystemHighlighter finalizeHighlightForPreviewingContext:];
-[_UIPreviewInteractionSystemHighlighter highlightShouldBeginInContainerView:presentationContainerView:previewingContext:];
-[_UIPreviewInteractionSystemHighlighter initialSnapshotView];
-[_UIPreviewInteractionSystemHighlighter prepareHighlightWithPreviewingContext:];
-[_UIPreviewInteractionSystemHighlighter setBlinderViewEnabled:];
-[_UIPreviewInteractionSystemHighlighter setInitialSnapshotView:];
-[_UIPreviewInteractionSystemHighlighter setUpdatedSnapshotView:];
-[_UIPreviewInteractionSystemHighlighter updatedSnapshotView];
```
