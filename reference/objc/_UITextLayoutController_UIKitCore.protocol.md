# `_UITextLayoutController` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 15 properties, 81 instance methods, 0 class methods

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
```

## Instance methods

```
-[_UITextLayoutController textContainers];
-[_UITextLayoutController offsetFromPosition:toPosition:];
-[_UITextLayoutController endOfDocument];
-[_UITextLayoutController comparePosition:toPosition:];
-[_UITextLayoutController textStorage];
-[_UITextLayoutController textRangeFromPosition:toPosition:];
-[_UITextLayoutController emptyTextRangeAtPosition:];
-[_UITextLayoutController unionRectForCharacterRange:bottomInset:];
-[_UITextLayoutController ensureLayoutForTextContainer:];
-[_UITextLayoutController beginningOfDocument];
-[_UITextLayoutController invalidateLayoutForRange:];
-[_UITextLayoutController setMaxTileHeight:];
-[_UITextLayoutController ensureLayoutForBounds:inTextContainer:];
-[_UITextLayoutController annotatedSubstringForRange:];
-[_UITextLayoutController addRenderingAttributes:forRange:];
-[_UITextLayoutController updateLayoutForSizeChangeOfTextContainer:];
-[_UITextLayoutController insertionRectForPosition:typingAttributes:placeholderAttachment:textContainer:];
-[_UITextLayoutController invalidateDisplayForCharacterRange:];
-[_UITextLayoutController enumerateTextLineFragmentsInRange:usingBlock:];
-[_UITextLayoutController enumerateTextSegmentsInRange:inTextContainer:usingBlock:];
-[_UITextLayoutController drawsDebugBaselines];
-[_UITextLayoutController layoutManager];
-[_UITextLayoutController styleEffectConfiguration];
-[_UITextLayoutController dequeueCanvasViewForTextContainer:];
-[_UITextLayoutController usedRectForTextContainer:];
-[_UITextLayoutController usesTiledViews];
-[_UITextLayoutController viewportRangeForTextContainer:];
-[_UITextLayoutController textContainerForPosition:];
-[_UITextLayoutController addInvisibleRange:];
-[_UITextLayoutController annotationAttribute:atPosition:];
-[_UITextLayoutController ensureLayoutForRange:];
-[_UITextLayoutController setUsesTiledViews:];
-[_UITextLayoutController textRangeForBounds:inTextContainer:layoutIfNeeded:];
-[_UITextLayoutController resumeTiling];
-[_UITextLayoutController addGhostedRange:];
-[_UITextLayoutController boundingRectForCharacterRange:];
-[_UITextLayoutController previewRendererForRange:unifyRects:];
-[_UITextLayoutController baseWritingDirectionAtPosition:];
-[_UITextLayoutController removeAllGhostedRanges];
-[_UITextLayoutController setStyleEffectConfiguration:];
-[_UITextLayoutController canAccessLayoutManager];
-[_UITextLayoutController textRangeForCharacterRange:];
-[_UITextLayoutController firstTextContainer];
-[_UITextLayoutController resetFontForExtraBulletRendering];
-[_UITextLayoutController characterRangeForTextRange:];
-[_UITextLayoutController characterRangesForTextRange:clippedToDocument:];
-[_UITextLayoutController setDrawsDebugBaselines:];
-[_UITextLayoutController addAnnotationAttribute:value:forRange:];
-[_UITextLayoutController removeInvisibleRange:];
-[_UITextLayoutController requestTextGeometryAtPosition:typingAttributes:resultBlock:];
-[_UITextLayoutController rangeOfCharacterClusterAtIndex:type:];
-[_UITextLayoutController suspendTiling];
-[_UITextLayoutController attributedTextInRange:];
-[_UITextLayoutController characterRangeForTextRange:clippedToDocument:];
-[_UITextLayoutController nearestPositionAtPoint:inContainer:];
-[_UITextLayoutController removeRenderingAttributes:forRange:];
-[_UITextLayoutController attributesAtPosition:inDirection:];
-[_UITextLayoutController positionFromPosition:offset:affinity:];
-[_UITextLayoutController boundingRectForRange:];
-[_UITextLayoutController layoutManagerDelegate];
-[_UITextLayoutController extraLineFragmentRect];
-[_UITextLayoutController selectionRectsForRange:fromView:forContainerPassingTest:];
-[_UITextLayoutController setLayoutManagerDelegate:];
-[_UITextLayoutController documentRange];
-[_UITextLayoutController positionWithOffset:affinity:];
-[_UITextLayoutController textRangeForLineEnclosingPosition:];
-[_UITextLayoutController textRangeForLineEnclosingPosition:effectiveAffinity:];
-[_UITextLayoutController cursorPositionAtPoint:inContainer:];
-[_UITextLayoutController textRangeForCharacterRanges:];
-[_UITextLayoutController removeAnnotationAttribute:forRange:];
-[_UITextLayoutController _visualSelectionRangeForExtent:forPoint:fromPosition:inDirection:];
-[_UITextLayoutController textRangeForTextKit2Ranges:];
-[_UITextLayoutController maxTileHeight];
-[_UITextLayoutController affinityForPosition:];
-[_UITextLayoutController baselineOffsetForFirstGlyph];
-[_UITextLayoutController isEditable];
-[_UITextLayoutController includesTextListMarkers];
-[_UITextLayoutController resetTextViewportLayoutControllerLayoutForPosition:];
-[_UITextLayoutController _writingToolsMinimumContextualRangeForRange:];
-[_UITextLayoutController setEditable:];
-[_UITextLayoutController positionFromPosition:inDirection:offset:affinity:anchorPositionOffset:];
```
