# `_UITextLayoutCanvasView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIGeometryChangeObserver`, `_NSTextLayoutManagerPlatformDelegate`, `_UITextKit2Canvas`
- 24 instance variables, 14 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"NSTextViewportLayoutController" _viewportLayoutController;
@"NSMutableSet" _renderingSurfaceKeysToRemove;
@"NSMapTable" _textViewportViews;
@"NSMutableSet" _textAttachmentViews;
@"NSMutableSet" _newTextAttachmentViews;
@"NSMutableSet" _currentClientAuxiliaryViews;
@"NSMutableSet" _oldClientAuxiliaryViews;
@"NSTextParagraphAnchoredAttachment" _incomingAnchoredAttachment;
Q _textContainerIndex;
{CGSize="width"d"height"d} _contentSize;
B _inLayout;
@"_UITextLayoutCanvasViewHoverEffectContainerLayer" _hoverEffectsLayer;
B _isTextViewScrolling;
@"_UITextAttachmentViewProviderCache" _viewProviderCache;
@"<NSCustomTextRendering>" _lastCustomRenderController;
@"<UITraitChangeRegistration>" _traitChangeToken;
{?="customRenderControllerSupportsSetContentsScale"b1"customRenderControllerSupportsSetNeedsDisplay"b1"customRenderControllerSupportsInvalidateTemporaryAttributes"b1"customRenderControllerSupportPrePostNotify"b1} _canvasViewFlags;
B _layoutFragmentViewsNeedDisplay;
@"NSTextLayoutManager" _textLayoutManager;
@"<_UITextCanvasContext>" _context;
@"NSTextContainer" _textContainer;
@"UIView" _selectionContainerView;
@"_UITextEmphasisBackgroundView" _textEmphasisBackgroundView;
@"_UIAnimatedTextLayoutInfo" _uniqueWritingToolsAnimatedLayoutInfo;
```

## Properties

```
@property (T@"NSTextLayoutManager",R,N,V_textLayoutManager) textLayoutManager;
@property (T@"NSTextContainer",R,N,V_textContainer) textContainer;
@property (T@"<NSCustomTextRendering>",R,N) customRenderController;
@property (T@"UIView",&,N,V_selectionContainerView) selectionContainerView;
@property (T@"_UITextEmphasisBackgroundView",R,N,V_textEmphasisBackgroundView) textEmphasisBackgroundView;
@property (T@"_UIAnimatedTextLayoutInfo",&,N,V_uniqueWritingToolsAnimatedLayoutInfo) uniqueWritingToolsAnimatedLayoutInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UITextCanvasContext>",W,N,V_context) context;
@property (TB,V_layoutFragmentViewsNeedDisplay) layoutFragmentViewsNeedDisplay;
@property (T{CGPoint=dd},?,R) viewportAnchor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R) viewport;
```

## Instance methods

```
-[_UITextLayoutCanvasView setNeedsLayout];
-[_UITextLayoutCanvasView platformDelegateForTextLayoutManager:cacheTextAttachmentViewProvider:forTextAttachment:];
-[_UITextLayoutCanvasView textContainer];
-[_UITextLayoutCanvasView setNeedsDisplay];
-[_UITextLayoutCanvasView layoutFragmentViewsNeedDisplay];
-[_UITextLayoutCanvasView _updateRenderingSurfaceViewsForTextRange:inTextView:bounds:];
-[_UITextLayoutCanvasView uniqueWritingToolsAnimatedLayoutInfo];
-[_UITextLayoutCanvasView viewportBoundsDidChange];
-[_UITextLayoutCanvasView isEditingDidChange];
-[_UITextLayoutCanvasView _performViewportLayout:];
-[_UITextLayoutCanvasView textViewportLayoutControllerDidLayout:];
-[_UITextLayoutCanvasView initWithTextLayoutManager:textContainer:];
-[_UITextLayoutCanvasView flushElementViews];
-[_UITextLayoutCanvasView dealloc];
-[_UITextLayoutCanvasView viewportBoundsForTextViewportLayoutController:];
-[_UITextLayoutCanvasView invalidateTemporaryAttributesInRange:];
-[_UITextLayoutCanvasView textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:];
-[_UITextLayoutCanvasView layoutSubviews];
-[_UITextLayoutCanvasView setViewportLayoutControllerDelegate:];
-[_UITextLayoutCanvasView hitTest:withEvent:];
-[_UITextLayoutCanvasView textViewportLayoutController:retrieveCachedRenderingSurfaceForKey:];
-[_UITextLayoutCanvasView observeEnclosingScrollView];
-[_UITextLayoutCanvasView textViewportLayoutControllerReceivedSetNeedsLayout:];
-[_UITextLayoutCanvasView _viewportWillLayout];
-[_UITextLayoutCanvasView _geometryChanged:forAncestor:];
-[_UITextLayoutCanvasView _viewportDidLayout];
-[_UITextLayoutCanvasView textViewportLayoutController:presentationLayoutFragmentFrameForTextLayoutFragment:proposedOrigin:];
-[_UITextLayoutCanvasView updateContentSizeIfNeeded];
-[_UITextLayoutCanvasView requestHoverEffectsUpdate];
-[_UITextLayoutCanvasView setTextEmphasisBackgroundView:withTextView:];
-[_UITextLayoutCanvasView frameForAnchoredTextAttachment:associatedLayoutFragment:];
-[_UITextLayoutCanvasView setContext:];
-[_UITextLayoutCanvasView setUniqueWritingToolsAnimatedLayoutInfo:];
-[_UITextLayoutCanvasView _updateTraitsForCustomTextRenderer:];
-[_UITextLayoutCanvasView setSelectionContainerView:];
-[_UITextLayoutCanvasView textViewportLayoutController:addRenderingSurface:group:placement:];
-[_UITextLayoutCanvasView textLayoutManager];
-[_UITextLayoutCanvasView customRenderController];
-[_UITextLayoutCanvasView textViewportLayoutController:renderingSurfaceForTextLayoutFragment:];
-[_UITextLayoutCanvasView setNeedsDisplayInRect:];
-[_UITextLayoutCanvasView textRangeForBounds:layoutIfNeeded:];
-[_UITextLayoutCanvasView _internalTextLayoutController];
-[_UITextLayoutCanvasView textViewportLayoutController:cacheRenderingSurface:forKey:];
-[_UITextLayoutCanvasView _registerTextAttachmentViewProviderReusePolicy:forTextAttachmentViewProviderType:];
-[_UITextLayoutCanvasView textEmphasisBackgroundView];
-[_UITextLayoutCanvasView _updateContentsScaleForCustomRenderController:];
-[_UITextLayoutCanvasView drawTextInRect:];
-[_UITextLayoutCanvasView _traitsChanged];
-[_UITextLayoutCanvasView isScrollingChangedTo:];
-[_UITextLayoutCanvasView context];
-[_UITextLayoutCanvasView locationForPositionInViewport:offset:];
-[_UITextLayoutCanvasView setLayoutFragmentViewsNeedDisplay:];
-[_UITextLayoutCanvasView textViewportLayoutControllerWillLayout:];
-[_UITextLayoutCanvasView selectionContainerView];
-[_UITextLayoutCanvasView platformDelegateForTextLayoutManager:retrieveCachedTextAttachmentViewProviderForTextAttachment:];
-[_UITextLayoutCanvasView _removeUnusedElementViews];
-[_UITextLayoutCanvasView configureCustomTextRenderer];
```
