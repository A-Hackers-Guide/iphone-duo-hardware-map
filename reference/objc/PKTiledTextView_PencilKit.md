# `PKTiledTextView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKTiledView`
- Protocols: `UITextInteractionDelegate`, `UIPointerInteractionDelegate`
- 2 instance variables, 6 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"UIView<PKTextAttachmentDrawingViewProviderView>" _standInEndAttachmentView;
@"UIButton" _tapToRadarButton;
```

## Properties

```
@property (T@"UIView<PKTextAttachmentDrawingViewProviderView>",&,N,V_standInEndAttachmentView) standInEndAttachmentView;
@property (T@"UIButton",&,N,V_tapToRadarButton) tapToRadarButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTiledTextView _layoutSubviews];
-[PKTiledTextView observeValueForKeyPath:ofObject:change:context:];
-[PKTiledTextView textDidChange:];
-[PKTiledTextView dealloc];
-[PKTiledTextView layoutSubviews];
-[PKTiledTextView hitTest:withEvent:];
-[PKTiledTextView interactionShouldBegin:atPoint:];
-[PKTiledTextView pointerInteraction:regionForRequest:defaultRegion:];
-[PKTiledTextView _textView];
-[PKTiledTextView setLinedPaper:];
-[PKTiledTextView setTapToRadarButton:];
-[PKTiledTextView tapToRadarButton];
-[PKTiledTextView rulerHostWantsSharedRuler];
-[PKTiledTextView insertAttachmentIfInBlankSpace:];
-[PKTiledTextView _canvasViewWillCreateSnapshot];
-[PKTiledTextView _didHitNestedTiledView:];
-[PKTiledTextView _scrollViewDidScroll];
-[PKTiledTextView _setupTapToRadarButton];
-[PKTiledTextView _shouldExpandBottomAttachmentForDragAndDrop];
-[PKTiledTextView _shouldPreventScrollViewPanGestureWhilePreviewing];
-[PKTiledTextView _shouldUpdateHeightOfAttachments];
-[PKTiledTextView _tapToRadarButtonTapped:];
-[PKTiledTextView appendPath:attachmentString:];
-[PKTiledTextView canAddStroke];
-[PKTiledTextView canvasViewDidEndDrawing:];
-[PKTiledTextView canvasViewWillBeginNewStroke:withTouch:location:];
-[PKTiledTextView frameOfEndAttachment];
-[PKTiledTextView handwritingFeedback:];
-[PKTiledTextView hasEndAttachment];
-[PKTiledTextView initInScrollView:sixChannelBlending:defaultDrawingClass:];
-[PKTiledTextView saveTempData:name:];
-[PKTiledTextView setDefaultDrawingClass:];
-[PKTiledTextView setStandInEndAttachmentView:];
-[PKTiledTextView standInAttachmentView];
-[PKTiledTextView standInEndAttachmentView];
-[PKTiledTextView textDidBeginEditing:];
-[PKTiledTextView textDidEndEditing:];
-[PKTiledTextView updateEndAttachment];
-[PKTiledTextView viewForAttachmentAtBlankSpace];
-[PKTiledTextView viewToMakeFirstResponderWhenHoveringOverAttachment:];
```
