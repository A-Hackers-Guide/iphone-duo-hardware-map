# `_UITextKit2LayoutController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextLayoutControllerBase`
- Protocols: `NSTextLayoutManagerDelegate`, `_UITextLayoutControllerInternal`
- 8 instance variables, 19 properties, 92 instance methods, 1 class methods

## Instance variables

```
@"UITextView" _textView;
@"NSTextContentStorage" _textContentStorage;
@"NSTextLayoutManager" _textLayoutManager;
@"NSMutableSet" _ghostedRanges;
@"NSMutableSet" _invisibleRanges;
@"NSMapTable" _textCanvasViews;
B _editable;
B _drawsDebugBaselines;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
@property (TB,N,V_drawsDebugBaselines) drawsDebugBaselines;
@property (T@"NSLayoutManager",R,N) layoutManager;
@property (T@"<NSLayoutManagerDelegate>",W,N) layoutManagerDelegate;
@property (TB,?,GisEditable,V_editable) editable;
@property (TB,?,R,N) includesTextListMarkers;
```

## Class methods

```
+[_UITextKit2LayoutController coordinateSystemCompatibilityFor2022AndEarlierSDKEnabled];
```

## Instance methods

```
-[_UITextKit2LayoutController textContainers];
-[_UITextKit2LayoutController offsetFromPosition:toPosition:];
-[_UITextKit2LayoutController endOfDocument];
-[_UITextKit2LayoutController comparePosition:toPosition:];
-[_UITextKit2LayoutController isEditable];
-[_UITextKit2LayoutController textStorage];
-[_UITextKit2LayoutController textRangeFromPosition:toPosition:];
-[_UITextKit2LayoutController emptyTextRangeAtPosition:];
-[_UITextKit2LayoutController includesTextListMarkers];
-[_UITextKit2LayoutController searchableObject];
-[_UITextKit2LayoutController unionRectForCharacterRange:bottomInset:];
-[_UITextKit2LayoutController ensureLayoutForTextContainer:];
-[_UITextKit2LayoutController beginningOfDocument];
-[_UITextKit2LayoutController invalidateLayoutForRange:];
-[_UITextKit2LayoutController setUnobscuredRange:];
-[_UITextKit2LayoutController setMaxTileHeight:];
-[_UITextKit2LayoutController ensureLayoutForBounds:inTextContainer:];
-[_UITextKit2LayoutController annotatedSubstringForRange:];
-[_UITextKit2LayoutController addRenderingAttributes:forRange:];
-[_UITextKit2LayoutController updateLayoutForSizeChangeOfTextContainer:];
-[_UITextKit2LayoutController insertionRectForPosition:typingAttributes:placeholderAttachment:textContainer:];
-[_UITextKit2LayoutController invalidateDisplayForCharacterRange:];
-[_UITextKit2LayoutController enumerateTextLineFragmentsInRange:usingBlock:];
-[_UITextKit2LayoutController enumerateTextSegmentsInRange:inTextContainer:usingBlock:];
-[_UITextKit2LayoutController drawsDebugBaselines];
-[_UITextKit2LayoutController layoutManager];
-[_UITextKit2LayoutController styleEffectConfiguration];
-[_UITextKit2LayoutController initWithTextView:textContentStorage:textContainer:];
-[_UITextKit2LayoutController dequeueCanvasViewForTextContainer:];
-[_UITextKit2LayoutController _updateSelectionWithTextRange:affinity:typingAttributes:];
-[_UITextKit2LayoutController usedRectForTextContainer:];
-[_UITextKit2LayoutController textLayoutManager:renderingAttributesForLink:atLocation:defaultAttributes:];
-[_UITextKit2LayoutController dealloc];
-[_UITextKit2LayoutController resetTextViewportLayoutControllerLayoutForPosition:];
-[_UITextKit2LayoutController usesTiledViews];
-[_UITextKit2LayoutController _invalidateTemporaryAttributesInRange:];
-[_UITextKit2LayoutController initWithTextView:textContainer:];
-[_UITextKit2LayoutController viewportRangeForTextContainer:];
-[_UITextKit2LayoutController textContainerForPosition:];
-[_UITextKit2LayoutController addInvisibleRange:];
-[_UITextKit2LayoutController annotationAttribute:atPosition:];
-[_UITextKit2LayoutController ensureLayoutForRange:];
-[_UITextKit2LayoutController setUsesTiledViews:];
-[_UITextKit2LayoutController textRangeForBounds:inTextContainer:layoutIfNeeded:];
-[_UITextKit2LayoutController resumeTiling];
-[_UITextKit2LayoutController addGhostedRange:];
-[_UITextKit2LayoutController boundingRectForCharacterRange:];
-[_UITextKit2LayoutController previewRendererForRange:unifyRects:];
-[_UITextKit2LayoutController _writingToolsMinimumContextualRangeForRange:];
-[_UITextKit2LayoutController _textContentStorageAddedUnsupportedAttribute:];
-[_UITextKit2LayoutController _rangeForCharacterRange:];
-[_UITextKit2LayoutController baseWritingDirectionAtPosition:];
-[_UITextKit2LayoutController removeAllGhostedRanges];
-[_UITextKit2LayoutController setStyleEffectConfiguration:];
-[_UITextKit2LayoutController canAccessLayoutManager];
-[_UITextKit2LayoutController textRangeForCharacterRange:];
-[_UITextKit2LayoutController resetFontForExtraBulletRendering];
-[_UITextKit2LayoutController characterRangeForTextRange:];
-[_UITextKit2LayoutController characterRangesForTextRange:clippedToDocument:];
-[_UITextKit2LayoutController setDrawsDebugBaselines:];
-[_UITextKit2LayoutController addAnnotationAttribute:value:forRange:];
-[_UITextKit2LayoutController removeInvisibleRange:];
-[_UITextKit2LayoutController requestTextGeometryAtPosition:typingAttributes:resultBlock:];
-[_UITextKit2LayoutController rangeOfCharacterClusterAtIndex:type:];
-[_UITextKit2LayoutController setEditable:];
-[_UITextKit2LayoutController suspendTiling];
-[_UITextKit2LayoutController attributedTextInRange:];
-[_UITextKit2LayoutController characterRangeForTextRange:clippedToDocument:];
-[_UITextKit2LayoutController nearestPositionAtPoint:inContainer:];
-[_UITextKit2LayoutController removeRenderingAttributes:forRange:];
-[_UITextKit2LayoutController attributesAtPosition:inDirection:];
-[_UITextKit2LayoutController positionFromPosition:offset:affinity:];
-[_UITextKit2LayoutController boundingRectForRange:];
-[_UITextKit2LayoutController layoutManagerDelegate];
-[_UITextKit2LayoutController extraLineFragmentRect];
-[_UITextKit2LayoutController selectionRectsForRange:fromView:forContainerPassingTest:];
-[_UITextKit2LayoutController setLayoutManagerDelegate:];
-[_UITextKit2LayoutController documentRange];
-[_UITextKit2LayoutController setDocumentObscured:];
-[_UITextKit2LayoutController positionWithOffset:affinity:];
-[_UITextKit2LayoutController textRangeForLineEnclosingPosition:];
-[_UITextKit2LayoutController textRangeForLineEnclosingPosition:effectiveAffinity:];
-[_UITextKit2LayoutController cursorPositionAtPoint:inContainer:];
-[_UITextKit2LayoutController textRangeForCharacterRanges:];
-[_UITextKit2LayoutController removeAnnotationAttribute:forRange:];
-[_UITextKit2LayoutController _visualSelectionRangeForExtent:forPoint:fromPosition:inDirection:];
-[_UITextKit2LayoutController positionFromPosition:inDirection:offset:affinity:anchorPositionOffset:];
-[_UITextKit2LayoutController textRangeForTextKit2Ranges:];
-[_UITextKit2LayoutController _locationWithOffset:];
-[_UITextKit2LayoutController maxTileHeight];
-[_UITextKit2LayoutController affinityForPosition:];
-[_UITextKit2LayoutController baselineOffsetForFirstGlyph];
```
