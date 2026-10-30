# `_UITextUnderlineView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITextSelectionHighlightView`
- 4 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _underlineViews;
@"NSMutableArray" _trackedUnderlineRects;
@"UIVisualEffectView" _baseView;
B _useDirectionalLightEffect;
```

## Properties

```
@property (T@"NSArray",&,N) underlineRects;
@property (TB,N,V_useDirectionalLightEffect) useDirectionalLightEffect;
```

## Instance methods

```
-[_UITextUnderlineView setUseDirectionalLightEffect:];
-[_UITextUnderlineView clearAllUnderlinesAnimated:];
-[_UITextUnderlineView useDirectionalLightEffect];
-[_UITextUnderlineView layoutSubviews];
-[_UITextUnderlineView effectForProofreadingUnderlines];
-[_UITextUnderlineView underlineFrameFromRect:underlineHeight:];
-[_UITextUnderlineView setUnderlineRects:];
-[_UITextUnderlineView addUnderlines:animated:];
-[_UITextUnderlineView removeUnderlines:animated:];
-[_UITextUnderlineView initWithFrame:];
-[_UITextUnderlineView underlineRects];
```
