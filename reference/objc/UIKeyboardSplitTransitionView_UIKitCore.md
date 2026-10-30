# `UIKeyboardSplitTransitionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 15 instance variables, 5 properties, 35 instance methods, 0 class methods

## Instance variables

```
d _currentProgress;
d _liftOffProgress;
d _finishProgress;
d _finishDuration;
d _finalTransitionStartTime;
@"CADisplayLink" _displayLink;
@? _completionBlock;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endFrame;
@"<UIKeyboardKeyplaneTransitionDelegate>" _transitionDelegate;
@"<UIKeyboardSplitTransitionDataSource>" _transitionDataSource;
B _centerFilled;
B _isRebuilding;
B _isSplitTranslation;
@"UIKeyboardSliceSet" _sliceSet;
```

## Properties

```
@property (T@?,C,V_completionBlock) completionBlock;
@property (T@"<UIKeyboardKeyplaneTransitionDelegate>",W,N,V_transitionDelegate) splitTransitionDelegate;
@property (T@"<UIKeyboardSplitTransitionDataSource>",W,N,V_transitionDataSource) splitTransitionDataSource;
@property (T@"NSArray",R) shadowLayers;
@property (T@"NSArray",R) backgroundLayers;
```

## Instance methods

```
-[UIKeyboardSplitTransitionView updateWithProgress:];
-[UIKeyboardSplitTransitionView didMoveToWindow];
-[UIKeyboardSplitTransitionView setCompletionBlock:];
-[UIKeyboardSplitTransitionView completionBlock];
-[UIKeyboardSplitTransitionView dealloc];
-[UIKeyboardSplitTransitionView setFrame:];
-[UIKeyboardSplitTransitionView backgroundLayers];
-[UIKeyboardSplitTransitionView bottomDropShadow];
-[UIKeyboardSplitTransitionView canDisplayTransition];
-[UIKeyboardSplitTransitionView centerDropShadow];
-[UIKeyboardSplitTransitionView colorsForBackgroundLayer:];
-[UIKeyboardSplitTransitionView defaultKeyboardImage];
-[UIKeyboardSplitTransitionView finalizeTransition];
-[UIKeyboardSplitTransitionView finishWithProgress:completionBlock:];
-[UIKeyboardSplitTransitionView initializeLayers];
-[UIKeyboardSplitTransitionView keyImageWithToken:];
-[UIKeyboardSplitTransitionView outerCenterDropShadow];
-[UIKeyboardSplitTransitionView rebuildControlKeys:];
-[UIKeyboardSplitTransitionView rebuildFromKeyplane:toKeyplane:startToken:endToken:keyboardType:orientation:];
-[UIKeyboardSplitTransitionView rebuildTransitionForSplitStyleChange:];
-[UIKeyboardSplitTransitionView rectEnclosingKeyplane:];
-[UIKeyboardSplitTransitionView setSplitTransitionDataSource:];
-[UIKeyboardSplitTransitionView setSplitTransitionDelegate:];
-[UIKeyboardSplitTransitionView shadowLayers];
-[UIKeyboardSplitTransitionView shouldAllowRubberiness];
-[UIKeyboardSplitTransitionView showDictationKey];
-[UIKeyboardSplitTransitionView showIntlKey];
-[UIKeyboardSplitTransitionView sizeForShadowLayer:];
-[UIKeyboardSplitTransitionView splitKeyboardImage];
-[UIKeyboardSplitTransitionView splitTransitionDataSource];
-[UIKeyboardSplitTransitionView splitTransitionDelegate];
-[UIKeyboardSplitTransitionView topDropShadow];
-[UIKeyboardSplitTransitionView transformForProgress:];
-[UIKeyboardSplitTransitionView transitionIsVisible];
-[UIKeyboardSplitTransitionView transitionToFinalState:];
```
