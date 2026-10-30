# `UIStatusBarItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 6 properties, 60 instance methods, 1 class methods

## Instance variables

```
d _currentOverlap;
^{CGContext=} _imageContext;
d _imageContextScale;
@"_UILegibilityView" _legibilityView;
@"_UILegibilityImageSet" _lastGeneratedTextImage;
d _lastGeneratedTextImageLetterSpacing;
@"NSString" _lastGeneratedTextImageText;
B _visible;
B _allowsUpdates;
B _shouldTintContentImage;
@"UIStatusBarItem" _item;
@"UIStatusBarLayoutManager" _layoutManager;
@"UIStatusBarForegroundStyleAttributes" _foregroundStyle;
```

## Properties

```
@property (T@"UIStatusBarItem",R,N,V_item) item;
@property (T@"UIStatusBarLayoutManager",W,N,V_layoutManager) layoutManager;
@property (T@"UIStatusBarForegroundStyleAttributes",R,N,V_foregroundStyle) foregroundStyle;
@property (TB,N,GisVisible,V_visible) visible;
@property (TB,N,V_allowsUpdates) allowsUpdates;
@property (TB,R,N,V_shouldTintContentImage) shouldTintContentImage;
```

## Class methods

```
+[UIStatusBarItemView createViewForItem:withData:actions:foregroundStyle:];
```

## Instance methods

```
-[UIStatusBarItemView accessibilityHUDRepresentation];
-[UIStatusBarItemView setVisible:];
-[UIStatusBarItemView setContentMode:];
-[UIStatusBarItemView textAlignment];
-[UIStatusBarItemView foregroundView];
-[UIStatusBarItemView _shouldReverseLayoutDirection];
-[UIStatusBarItemView layoutManager];
-[UIStatusBarItemView dealloc];
-[UIStatusBarItemView isVisible];
-[UIStatusBarItemView contentsImage];
-[UIStatusBarItemView legibilityStrength];
-[UIStatusBarItemView item];
-[UIStatusBarItemView textFont];
-[UIStatusBarItemView willMoveToWindow:];
-[UIStatusBarItemView legibilityStyle];
-[UIStatusBarItemView description];
-[UIStatusBarItemView _shouldAnimatePropertyWithKey:];
-[UIStatusBarItemView textStyle];
-[UIStatusBarItemView allowsUserInteraction];
-[UIStatusBarItemView setLayoutManager:];
-[UIStatusBarItemView endImageContext];
-[UIStatusBarItemView foregroundStyle];
-[UIStatusBarItemView setPersistentAnimationsEnabled:];
-[UIStatusBarItemView standardPadding];
-[UIStatusBarItemView _tintContentLayerIfNeeded];
-[UIStatusBarItemView addContentOverlap:];
-[UIStatusBarItemView adjustFrameToNewSize:];
-[UIStatusBarItemView allowsUpdates];
-[UIStatusBarItemView animatesDataChange];
-[UIStatusBarItemView beginDisablingRasterization];
-[UIStatusBarItemView beginImageContextWithMinimumWidth:];
-[UIStatusBarItemView cachedImageWithText:truncatedWithEllipsesAtMaxWidth:letterSpacing:];
-[UIStatusBarItemView clearCachedTextImage];
-[UIStatusBarItemView contentsIOSurface];
-[UIStatusBarItemView currentLeftOverlap];
-[UIStatusBarItemView currentOverlap];
-[UIStatusBarItemView currentRightOverlap];
-[UIStatusBarItemView endDisablingRasterization];
-[UIStatusBarItemView extraLeftPadding];
-[UIStatusBarItemView extraRightPadding];
-[UIStatusBarItemView imageFromImageContextClippedToWidth:];
-[UIStatusBarItemView imageWithShadowNamed:];
-[UIStatusBarItemView imageWithText:];
-[UIStatusBarItemView imageWithText:shouldCache:];
-[UIStatusBarItemView initWithItem:data:actions:style:];
-[UIStatusBarItemView maximumOverlap];
-[UIStatusBarItemView neededSizeForImageSet:];
-[UIStatusBarItemView performPendedActions];
-[UIStatusBarItemView resetContentOverlap];
-[UIStatusBarItemView setAllowsUpdates:];
-[UIStatusBarItemView setCurrentOverlap:];
-[UIStatusBarItemView setLayerContentsImage:];
-[UIStatusBarItemView setStatusBarData:actions:];
-[UIStatusBarItemView setVisible:frame:duration:];
-[UIStatusBarItemView setVisible:settingAlpha:];
-[UIStatusBarItemView shadowPadding];
-[UIStatusBarItemView shouldTintContentImage];
-[UIStatusBarItemView updateContentsAndWidth];
-[UIStatusBarItemView updateForNewData:actions:];
-[UIStatusBarItemView updateForNewStyle:];
```
