# `_UIPopoverHostManagerPopoverUpdateConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _showsArrow;
B _isRTL;
q _preferredHorizontalAlignment;
{CGSize="width"d"height"d} _contentSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRectInParentUIWindow;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRectInParentUIWindow) sourceRectInParentUIWindow;
@property (T{CGSize=dd},N,V_contentSize) contentSize;
@property (Tq,N,V_preferredHorizontalAlignment) preferredHorizontalAlignment;
@property (TB,N,V_showsArrow) showsArrow;
@property (TB,N,V_isRTL) isRTL;
```

## Instance methods

```
-[_UIPopoverHostManagerPopoverUpdateConfiguration contentSize];
-[_UIPopoverHostManagerPopoverUpdateConfiguration setContentSize:];
-[_UIPopoverHostManagerPopoverUpdateConfiguration setPreferredHorizontalAlignment:];
-[_UIPopoverHostManagerPopoverUpdateConfiguration setIsRTL:];
-[_UIPopoverHostManagerPopoverUpdateConfiguration preferredHorizontalAlignment];
-[_UIPopoverHostManagerPopoverUpdateConfiguration isRTL];
-[_UIPopoverHostManagerPopoverUpdateConfiguration setShowsArrow:];
-[_UIPopoverHostManagerPopoverUpdateConfiguration setSourceRectInParentUIWindow:];
-[_UIPopoverHostManagerPopoverUpdateConfiguration showsArrow];
-[_UIPopoverHostManagerPopoverUpdateConfiguration sourceRectInParentUIWindow];
```
