# `_UITextKit1LayoutController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextLayoutControllerBase`
- Protocols: `_UITextLayoutController`
- 3 instance variables, 19 properties, 79 instance methods, 0 class methods

## Instance variables

```
@"UITextView" _textView;
@"NSLayoutManager" _originalLayoutManager;
@"_UITextCanvasView" _canvasView;
```

## Properties

```
@property (T@"NSTextStorage",R,N) textStorage;
@property (T@"UITextPosition",R,N) beginningOfDocument;
@property (T@"UITextPosition",R,N) endOfDocument;
@property (T@"UITextRange",R,N) documentRange;
@property (T@"CUIStyleEffectConfiguration",C,N) styleEffectConfiguration;
@property (T@"NSArray",R,C,N) textContainers;
@property (T@"NSTextContainer",R,N) firstTextContainer;
@property (TB,R,N) canAccessLayoutManager;
@property (TB,N) usesTiledViews;
@property (Td,N) maxTileHeight;
@property (TB,N) drawsDebugBaselines;
@property (T@"NSLayoutManager",R,N) layoutManager;
@property (T@"<NSLayoutManagerDelegate>",W,N) layoutManagerDelegate;
@property (TB,?,GisEditable) editable;
@property (TB,?,R,N) includesTextListMarkers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextKit1LayoutController textContainers];
-[_UITextKit1LayoutController offsetFromPosition:toPosition:];
-[_UITextKit1LayoutController endOfDocument];
-[_UITextKit1LayoutController comparePosition:toPosition:];
-[_UITextKit1LayoutController isEditable];
-[_UITextKit1LayoutController textStorage];
-[_UITextKit1LayoutController textRangeFromPosition:toPosition:];
-[_UITextKit1LayoutController emptyTextRangeAtPosition:];
-[_UITextKit1LayoutController includesTextListMarkers];
-[_UITextKit1LayoutController unionRectForCharacterRange:bottomInset:];
-[_UITextKit1LayoutController ensureLayoutForTextContainer:];
-[_UITextKit1LayoutController beginningOfDocument];
-[_UITextKit1LayoutController invalidateLayoutForRange:];
-[_UITextKit1LayoutController setMaxTileHeight:];
-[_UITextKit1LayoutController ensureLayoutForBounds:inTextContainer:];
-[_UITextKit1LayoutController annotatedSubstringForRange:];
-[_UITextKit1LayoutController addRenderingAttributes:forRange:];
-[_UITextKit1LayoutController updateLayoutForSizeChangeOfTextContainer:];
-[_UITextKit1LayoutController insertionRectForPosition:typingAttributes:placeholderAttachment:textContainer:];
-[_UITextKit1LayoutController invalidateDisplayForCharacterRange:];
-[_UITextKit1LayoutController enumerateTextLineFragmentsInRange:usingBlock:];
-[_UITextKit1LayoutController enumerateTextSegmentsInRange:inTextContainer:usingBlock:];
-[_UITextKit1LayoutController drawsDebugBaselines];
-[_UITextKit1LayoutController layoutManager];
-[_UITextKit1LayoutController styleEffectConfiguration];
-[_UITextKit1LayoutController dequeueCanvasViewForTextContainer:];
-[_UITextKit1LayoutController _textStorageLength];
-[_UITextKit1LayoutController usedRectForTextContainer:];
-[_UITextKit1LayoutController usesTiledViews];
-[_UITextKit1LayoutController viewportRangeForTextContainer:];
-[_UITextKit1LayoutController textContainerForPosition:];
-[_UITextKit1LayoutController addInvisibleRange:];
-[_UITextKit1LayoutController annotationAttribute:atPosition:];
-[_UITextKit1LayoutController ensureLayoutForRange:];
-[_UITextKit1LayoutController setUsesTiledViews:];
-[_UITextKit1LayoutController textRangeForBounds:inTextContainer:layoutIfNeeded:];
-[_UITextKit1LayoutController resumeTiling];
-[_UITextKit1LayoutController addGhostedRange:];
-[_UITextKit1LayoutController boundingRectForCharacterRange:];
-[_UITextKit1LayoutController previewRendererForRange:unifyRects:];
-[_UITextKit1LayoutController _writingToolsMinimumContextualRangeForRange:];
-[_UITextKit1LayoutController baseWritingDirectionAtPosition:];
-[_UITextKit1LayoutController removeAllGhostedRanges];
-[_UITextKit1LayoutController setStyleEffectConfiguration:];
-[_UITextKit1LayoutController canAccessLayoutManager];
-[_UITextKit1LayoutController textRangeForCharacterRange:];
-[_UITextKit1LayoutController resetFontForExtraBulletRendering];
-[_UITextKit1LayoutController characterRangeForTextRange:];
-[_UITextKit1LayoutController characterRangesForTextRange:clippedToDocument:];
-[_UITextKit1LayoutController setDrawsDebugBaselines:];
-[_UITextKit1LayoutController addAnnotationAttribute:value:forRange:];
-[_UITextKit1LayoutController removeInvisibleRange:];
-[_UITextKit1LayoutController requestTextGeometryAtPosition:typingAttributes:resultBlock:];
-[_UITextKit1LayoutController rangeOfCharacterClusterAtIndex:type:];
-[_UITextKit1LayoutController setEditable:];
-[_UITextKit1LayoutController suspendTiling];
-[_UITextKit1LayoutController attributedTextInRange:];
-[_UITextKit1LayoutController characterRangeForTextRange:clippedToDocument:];
-[_UITextKit1LayoutController nearestPositionAtPoint:inContainer:];
-[_UITextKit1LayoutController removeRenderingAttributes:forRange:];
-[_UITextKit1LayoutController attributesAtPosition:inDirection:];
-[_UITextKit1LayoutController positionFromPosition:offset:affinity:];
-[_UITextKit1LayoutController boundingRectForRange:];
-[_UITextKit1LayoutController layoutManagerDelegate];
-[_UITextKit1LayoutController extraLineFragmentRect];
-[_UITextKit1LayoutController selectionRectsForRange:fromView:forContainerPassingTest:];
-[_UITextKit1LayoutController setLayoutManagerDelegate:];
-[_UITextKit1LayoutController documentRange];
-[_UITextKit1LayoutController positionWithOffset:affinity:];
-[_UITextKit1LayoutController textRangeForLineEnclosingPosition:];
-[_UITextKit1LayoutController textRangeForLineEnclosingPosition:effectiveAffinity:];
-[_UITextKit1LayoutController cursorPositionAtPoint:inContainer:];
-[_UITextKit1LayoutController textRangeForCharacterRanges:];
-[_UITextKit1LayoutController removeAnnotationAttribute:forRange:];
-[_UITextKit1LayoutController _visualSelectionRangeForExtent:forPoint:fromPosition:inDirection:];
-[_UITextKit1LayoutController textRangeForTextKit2Ranges:];
-[_UITextKit1LayoutController maxTileHeight];
-[_UITextKit1LayoutController affinityForPosition:];
-[_UITextKit1LayoutController baselineOffsetForFirstGlyph];
```
