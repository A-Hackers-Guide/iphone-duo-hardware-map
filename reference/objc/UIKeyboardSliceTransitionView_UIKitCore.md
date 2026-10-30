# `UIKeyboardSliceTransitionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardSplitTransitionView`
- 10 instance variables, 0 properties, 31 instance methods, 0 class methods

## Instance variables

```
^{CGImage=} _defaultKeyplaneImage;
^{CGImage=} _splitKeyplaneImage;
@"CALayer" _leftKeys;
@"CALayer" _rightKeys;
@"CALayer" _spaceFill;
@"NSMutableDictionary" _controlKeys;
@"CALayer" _topEdgeHighlight;
@"UIKBCacheToken" _keyplaneToken;
q _orientation;
{?="position"b1"slices"b1"backgroundAndShadows"b1"backgroundGradients"b1"topEdgeHighlight"b1"shiftKeys"b1"returnKeys"b1"moreIntlKeys"b1} _rebuildFlags;
```

## Instance methods

```
-[UIKeyboardSliceTransitionView updateWithProgress:];
-[UIKeyboardSliceTransitionView setHidden:];
-[UIKeyboardSliceTransitionView dealloc];
-[UIKeyboardSliceTransitionView setFrame:];
-[UIKeyboardSliceTransitionView initWithFrame:];
-[UIKeyboardSliceTransitionView setRebuildFlags];
-[UIKeyboardSliceTransitionView _delayedUpdateTransition];
-[UIKeyboardSliceTransitionView adjustedLeftWidthAtMergePoint];
-[UIKeyboardSliceTransitionView adjustedRightWidthAtMergePoint];
-[UIKeyboardSliceTransitionView canDisplayTransition];
-[UIKeyboardSliceTransitionView crossfadeOpacityAnimation];
-[UIKeyboardSliceTransitionView defaultKeyboardImage];
-[UIKeyboardSliceTransitionView getKeyboardImageAsSplit:];
-[UIKeyboardSliceTransitionView initializeLayers];
-[UIKeyboardSliceTransitionView meshTransformForProgress:];
-[UIKeyboardSliceTransitionView rebuildBackgroundAndShadowTransitions];
-[UIKeyboardSliceTransitionView rebuildBackgroundGradientTransitions];
-[UIKeyboardSliceTransitionView rebuildControlKeys:];
-[UIKeyboardSliceTransitionView rebuildFromKeyplane:toKeyplane:startToken:endToken:keyboardType:orientation:];
-[UIKeyboardSliceTransitionView rebuildMoreIntlKeys];
-[UIKeyboardSliceTransitionView rebuildReturnSlices];
-[UIKeyboardSliceTransitionView rebuildShadows];
-[UIKeyboardSliceTransitionView rebuildShiftSlices];
-[UIKeyboardSliceTransitionView rebuildSliceTransitions];
-[UIKeyboardSliceTransitionView rebuildTopEdgeHighlightTransition];
-[UIKeyboardSliceTransitionView rebuildTransitionForSplitStyleChange:];
-[UIKeyboardSliceTransitionView refreshKeyplaneImages];
-[UIKeyboardSliceTransitionView splitKeyboardImage];
-[UIKeyboardSliceTransitionView transformForProgress:];
-[UIKeyboardSliceTransitionView updateTransition];
-[UIKeyboardSliceTransitionView updateTransitionForSlice:withStart:startContents:end:endContents:updateContents:];
```
