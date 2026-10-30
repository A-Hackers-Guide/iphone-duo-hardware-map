# `UIKeyboardFlipTransitionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardSplitTransitionView`
- 12 instance variables, 1 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"CALayer" _container;
@"CALayer" _frontFace;
@"CALayer" _backFace;
@"CALayer" _frontDarkening;
@"CALayer" _backDarkening;
@"CALayer" _backDarkeningLeft;
@"CALayer" _backDarkeningRight;
B _showingFrontFace;
@"UIKBCacheToken" _startKeyplaneToken;
@"UIKBCacheToken" _endKeyplaneToken;
@"NSMutableDictionary" _controlKeys;
{?="shiftKeys"b1"returnKeys"b1"moreIntlKeys"b1} _rebuildFlags;
```

## Properties

```
@property (TB,N,GisShowingFrontFace,V_showingFrontFace) showingFrontFace;
```

## Instance methods

```
-[UIKeyboardFlipTransitionView setFrame:];
-[UIKeyboardFlipTransitionView initWithFrame:];
-[UIKeyboardFlipTransitionView rebuildControlSlicesForKeyName:];
-[UIKeyboardFlipTransitionView _delayedUpdateTransition];
-[UIKeyboardFlipTransitionView _flipToFront:animated:];
-[UIKeyboardFlipTransitionView defaultKeyboardImage];
-[UIKeyboardFlipTransitionView isShowingFrontFace];
-[UIKeyboardFlipTransitionView rebuildBackgroundTransition];
-[UIKeyboardFlipTransitionView rebuildControlKeys:];
-[UIKeyboardFlipTransitionView rebuildFromKeyplane:toKeyplane:startToken:endToken:keyboardType:orientation:];
-[UIKeyboardFlipTransitionView rebuildMoreIntlKeys];
-[UIKeyboardFlipTransitionView rebuildReturnSlices];
-[UIKeyboardFlipTransitionView rebuildShiftSlices];
-[UIKeyboardFlipTransitionView rebuildTransition];
-[UIKeyboardFlipTransitionView rebuildTransitionForSplitStyleChange:];
-[UIKeyboardFlipTransitionView setShowingFrontFace:];
-[UIKeyboardFlipTransitionView splitKeyboardImage];
-[UIKeyboardFlipTransitionView transitionIsVisible];
-[UIKeyboardFlipTransitionView updateMoreIntlKey:asStart:withRect:showIntl:showDictKey:];
-[UIKeyboardFlipTransitionView updateTransition];
```
