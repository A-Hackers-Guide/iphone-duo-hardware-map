# `_UITextLayoutFragmentViewBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIMutableTextLayoutFragmentView`, `_UITextViewportRenderingSurface`
- 7 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _textAttachmentGeometryNeedsUpdate;
B _cacheAndRetainInViewHierarchy;
@"NSTextLayoutFragment" _layoutFragment;
{CGPoint="x"d"y"d} _containerOrigin;
{CGSize="width"d"height"d} _containerSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _clipRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _clipFrame;
```

## Properties

```
@property (T{CGPoint=dd},N,V_containerOrigin) containerOrigin;
@property (T{CGSize=dd},N,V_containerSize) containerSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_clipRect) clipRect;
@property (T@"NSTextLayoutFragment",R,N,V_layoutFragment) layoutFragment;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_clipFrame) clipFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) isLayoutFragmentView;
@property (TB,N,V_cacheAndRetainInViewHierarchy) cacheAndRetainInViewHierarchy;
```

## Instance methods

```
-[_UITextLayoutFragmentViewBase containerSize];
-[_UITextLayoutFragmentViewBase _updateGeometry];
-[_UITextLayoutFragmentViewBase setContainerSize:];
-[_UITextLayoutFragmentViewBase performChanges:];
-[_UITextLayoutFragmentViewBase layoutSubviews];
-[_UITextLayoutFragmentViewBase hitTest:withEvent:];
-[_UITextLayoutFragmentViewBase _activeContainerOrigin];
-[_UITextLayoutFragmentViewBase _activeClipRect];
-[_UITextLayoutFragmentViewBase didMoveToSuperview];
-[_UITextLayoutFragmentViewBase teardown];
-[_UITextLayoutFragmentViewBase _activeLayoutFragmentFrame];
-[_UITextLayoutFragmentViewBase containerOrigin];
-[_UITextLayoutFragmentViewBase _updateTextAttachmentGeometry];
-[_UITextLayoutFragmentViewBase cacheAndRetainInViewHierarchy];
-[_UITextLayoutFragmentViewBase clipFrame];
-[_UITextLayoutFragmentViewBase clipRect];
-[_UITextLayoutFragmentViewBase enumerateTextAttachmentViewsUsingBlock:];
-[_UITextLayoutFragmentViewBase initWithLayoutFragment:containerOrigin:containerSize:clipRect:];
-[_UITextLayoutFragmentViewBase isLayoutFragmentView];
-[_UITextLayoutFragmentViewBase layoutFragment];
-[_UITextLayoutFragmentViewBase setCacheAndRetainInViewHierarchy:];
-[_UITextLayoutFragmentViewBase setClipRect:];
-[_UITextLayoutFragmentViewBase setContainerOrigin:];
```
