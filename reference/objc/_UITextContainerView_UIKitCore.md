# `_UITextContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `NSUITextViewCommonMethods`, `_UITextViewCanvasViewContext`
- 15 instance variables, 32 properties, 81 instance methods, 0 class methods

## Instance variables

```
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _textContainerInset;
{CGPoint="x"d"y"d} _textContainerOrigin;
{CGSize="width"d"height"d} _minSize;
{CGSize="width"d"height"d} _maxSize;
@"NSTextContainer" _textContainer;
@"NSDictionary" _linkTextAttributes;
Q _invalidationSeqNo;
q _invalidationSeqClipsToBounds;
@"UIScrollView" _enclosingScrollView;
{?="textContainerOriginInvalid"b1"verticalLayout"b2"horizontallyResizable"b1"verticallyResizable"b1"freezeTextContainerSize"b1"usesStandardTextScaling"b1} _tcvFlags;
@"UITextView" _textView;
@"NSDictionary" _textHighlightAttributes;
@"_UITextLayoutControllerBase<_UITextLayoutController>" _textLayoutController;
@"<_UITextContainerViewDelegate>" _delegate;
@"UIView<_UITextCanvas>" _canvasView;
```

## Properties

```
@property (T@"NSTextContainer",W,N,V_textContainer) textContainer;
@property (T@"_UITextLayoutControllerBase<_UITextLayoutController>",R,N,V_textLayoutController) textLayoutController;
@property (T@"<_UITextContainerViewDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,N) selectionContainerView;
@property (T@"_UITextEmphasisBackgroundView",R,N) textEmphasisBackgroundView;
@property (T@"NSDictionary",C,N,V_textHighlightAttributes) textHighlightAttributes;
@property (T@"_UIAnimatedTextLayoutInfo",&,N) uniqueWritingToolsAnimatedLayoutInfo;
@property (T{CGPoint=dd},R,N) textContainerOrigin;
@property (T{UIEdgeInsets=dddd},N) textContainerInset;
@property (TB,N,GisHorizontallyResizable) horizontallyResizable;
@property (TB,N,GisVerticallyResizable) verticallyResizable;
@property (T{CGSize=dd},N,V_minSize) minSize;
@property (T{CGSize=dd},N,V_maxSize) maxSize;
@property (T@"UIView<_UITextCanvas>",R,N,V_canvasView) canvasView;
@property (TB,N) usesStandardTextScaling;
@property (T@"UIScrollView",W,N) enclosingScrollView;
@property (TB,N,G_freezeTextContainerSize,S_setFreezeTextContainerSize:) freezeTextContainerSize;
@property (T@"NSLayoutManager",R,N) layoutManager;
@property (T{_NSRange=QQ},?,N) markedRange;
@property (T@"NSDictionary",?,R,N) markedTextStyle;
@property (Tq,R,N) layoutOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIColor",R,N) textColor;
@property (TB,R,N) hasOverriddenEnclosingScrollView;
@property (TB,R,N,GisEditable) editable;
@property (TB,R,N,GisEditing) editing;
@property (T{CGPoint=dd},R,N) drawingScale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _clipRectForFadedEdges;
@property (T@"<NSCustomTextRendering>",?,R,N) customRenderController;
```

## Instance methods

```
-[_UITextContainerView markedTextStyle];
-[_UITextContainerView markedRange];
-[_UITextContainerView minSize];
-[_UITextContainerView isEditable];
-[_UITextContainerView _clipRectForFadedEdges];
-[_UITextContainerView setTextContainer:];
-[_UITextContainerView textContainer];
-[_UITextContainerView textContainerUsageDidChangeToSize:];
-[_UITextContainerView setNeedsDisplay];
-[_UITextContainerView visibleRect];
-[_UITextContainerView _ensureLayoutCompleteForRect:];
-[_UITextContainerView usesStandardTextScaling];
-[_UITextContainerView uniqueWritingToolsAnimatedLayoutInfo];
-[_UITextContainerView willMoveToSuperview:];
-[_UITextContainerView _ensureLayoutForCappedSize];
-[_UITextContainerView sizeToFit];
-[_UITextContainerView textHighlightRenderingAttributesForAttributes:];
-[_UITextContainerView textColor];
-[_UITextContainerView textHighlightAttributes];
-[_UITextContainerView _setNeedsContentsFormatUpdate];
-[_UITextContainerView layoutManager];
-[_UITextContainerView enclosingScrollView];
-[_UITextContainerView isHorizontallyResizable];
-[_UITextContainerView maxSize];
-[_UITextContainerView layoutSubviews];
-[_UITextContainerView isVerticallyResizable];
-[_UITextContainerView drawTextInRectIfNeeded:];
-[_UITextContainerView setUsesStandardTextScaling:];
-[_UITextContainerView linkTextAttributes];
-[_UITextContainerView setBounds:];
-[_UITextContainerView textLayoutController];
-[_UITextContainerView setBackgroundColor:];
-[_UITextContainerView layoutOrientation];
-[_UITextContainerView setTextEmphasisBackgroundView:withTextView:];
-[_UITextContainerView attributedSubstringForMarkedRange];
-[_UITextContainerView setDelegate:];
-[_UITextContainerView tintColorDidChange];
-[_UITextContainerView _ensureMinAndMaxSizesConsistentWithBounds];
-[_UITextContainerView initWithFrame:textLayoutController:textContainer:delegate:];
-[_UITextContainerView setMinSize:];
-[_UITextContainerView updateInsertionPointStateAndRestartTimer:];
-[_UITextContainerView _ensureLayoutCompleteToEndOfCharacterRange:];
-[_UITextContainerView _setFrameOrBounds:oldRect:isFrameRect:settingAction:];
-[_UITextContainerView setVerticallyResizable:];
-[_UITextContainerView setUniqueWritingToolsAnimatedLayoutInfo:];
-[_UITextContainerView drawingScale];
-[_UITextContainerView textContainerOrigin];
-[_UITextContainerView setSelectionContainerView:];
-[_UITextContainerView setHorizontallyResizable:];
-[_UITextContainerView setMaxSize:];
-[_UITextContainerView customRenderController];
-[_UITextContainerView delegate];
-[_UITextContainerView setConstrainedFrameSize:];
-[_UITextContainerView setFrame:];
-[_UITextContainerView setEnclosingScrollView:];
-[_UITextContainerView layoutManager:effectiveCUICatalogForTextEffect:];
-[_UITextContainerView setNeedsDisplayInRect:];
-[_UITextContainerView description];
-[_UITextContainerView _shouldCapSizeToFitLayoutRange:];
-[_UITextContainerView setTextHighlightAttributes:];
-[_UITextContainerView didAddTextAttachmentViews:];
-[_UITextContainerView canvasView];
-[_UITextContainerView textEmphasisBackgroundView];
-[_UITextContainerView didLayoutTextAttachmentView:inFragmentRect:];
-[_UITextContainerView reconfigureWithLayoutManager:triggeredBySelector:];
-[_UITextContainerView hasOverriddenEnclosingScrollView];
-[_UITextContainerView _setFreezeTextContainerSize:];
-[_UITextContainerView didRemoveTextAttachmentViews:];
-[_UITextContainerView setTextContainerInset:];
-[_UITextContainerView isEditing];
-[_UITextContainerView initWithFrame:];
-[_UITextContainerView setNeedsDisplayInRect:avoidAdditionalLayout:];
-[_UITextContainerView setLayoutOrientation:];
-[_UITextContainerView _sizeToConstrainedContainerUsedRect];
-[_UITextContainerView _updateInteractionGeometry];
-[_UITextContainerView linkAttributesForLink:forCharacterAtIndex:];
-[_UITextContainerView selectionContainerView];
-[_UITextContainerView invalidateTextContainerOrigin];
-[_UITextContainerView _textKit2CanvasDidLayout];
-[_UITextContainerView textContainerInset];
-[_UITextContainerView _freezeTextContainerSize];
```
