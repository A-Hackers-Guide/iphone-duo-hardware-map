# `UIInputView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UISplittableInputView`
- 24 instance variables, 17 properties, 58 instance methods, 1 class methods

## Instance variables

```
q _style;
@"UIKBRenderConfig" _renderConfig;
B _suppressBackgroundStyling;
B _disableSplitSupport;
@"_UIInputViewContent" _leftContentView;
@"_UIInputViewContent" _rightContentView;
d _contentRatio;
{CGSize="width"d"height"d} _leftContentSize;
{CGSize="width"d"height"d} _rightContentSize;
d _gapWidth;
d _leftOffset;
B _isTransitioning;
d _transitionGap;
d _transitionLeftOffset;
d _transitionRatio;
@"UIImage" _mergedImage;
@"UIImage" _splitImage;
@"NSMutableDictionary" _mergedSliceMap;
@"NSMutableDictionary" _splitSliceMap;
@"NSArray" _visibleLayers;
@"CALayer" _transitionLayer;
B _allowsSelfSizing;
B _assertSizingWithPredictionBar;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _backgroundEdgeInsets;
```

## Properties

```
@property (T@"UIImage",&,N,V_mergedImage) _mergedImage;
@property (T@"UIImage",&,N,V_splitImage) _splitImage;
@property (T@"NSMutableDictionary",&,N,V_mergedSliceMap) _mergedSliceMap;
@property (T@"NSMutableDictionary",&,N,V_splitSliceMap) _splitSliceMap;
@property (T{UIEdgeInsets=dddd},N,V_backgroundEdgeInsets) backgroundEdgeInsets;
@property (TB,N,V_assertSizingWithPredictionBar) assertSizingWithPredictionBar;
@property (T@"UIView",R,N,V_leftContentView) leftContentView;
@property (T@"UIView",R,N,V_rightContentView) rightContentView;
@property (Td,N,V_contentRatio) contentRatio;
@property (T{CGSize=dd},N,V_leftContentSize) leftContentViewSize;
@property (T{CGSize=dd},N,V_rightContentSize) rightContentViewSize;
@property (Tq,R,N,V_style) inputViewStyle;
@property (TB,N,V_allowsSelfSizing) allowsSelfSizing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInputView _setupAppearanceIfNecessary];
```

## Instance methods

```
-[UIInputView _clipCornersOfView:];
-[UIInputView _isTransitioning];
-[UIInputView _setRenderConfig:];
-[UIInputView _setLeftOffset:gapWidth:];
-[UIInputView _beginSplitTransitionIfNeeded:gapWidth:];
-[UIInputView didEndSplitTransition];
-[UIInputView setBounds:];
-[UIInputView updateSplitSubviewContraintsWithLeftContentSize:rightContentSize:];
-[UIInputView layoutMergedSubviews];
-[UIInputView willBeginSplitTransition];
-[UIInputView leftContentViewSize];
-[UIInputView setFrame:];
-[UIInputView tintColor];
-[UIInputView initWithCoder:];
-[UIInputView updateMergedSubviewConstraints];
-[UIInputView _setProgress:boundedBy:];
-[UIInputView pointInside:withEvent:];
-[UIInputView _endSplitTransitionIfNeeded:];
-[UIInputView initWithFrame:];
-[UIInputView layoutSplitSubviewsWithLeftContentSize:rightContentSize:];
-[UIInputView rightContentViewSize];
-[UIInputView leftContentView];
-[UIInputView set_splitImage:];
-[UIInputView _mergedSliceMap];
-[UIInputView _additionalClipHeight];
-[UIInputView _defaultSize];
-[UIInputView _disableSplitSupport];
-[UIInputView _isSplit];
-[UIInputView _isToolbars];
-[UIInputView _mergedImage];
-[UIInputView _setDisableSplitSupport:];
-[UIInputView _setNeedsContentSizeUpdate];
-[UIInputView _setSuppressBackgroundStyling:];
-[UIInputView _splitBorderedBackgroundWithCorners:];
-[UIInputView _splitImage];
-[UIInputView _splitSliceMap];
-[UIInputView _supportsSplit];
-[UIInputView _suppressBackgroundStyling];
-[UIInputView _toolbarBorderedBackground];
-[UIInputView _updateClipCorners];
-[UIInputView _updateWithSize:];
-[UIInputView allowsSelfSizing];
-[UIInputView assertSizingWithPredictionBar];
-[UIInputView backgroundEdgeInsets];
-[UIInputView contentRatio];
-[UIInputView initWithFrame:inputViewStyle:];
-[UIInputView inputViewStyle];
-[UIInputView rightContentView];
-[UIInputView setAllowsSelfSizing:];
-[UIInputView setAssertSizingWithPredictionBar:];
-[UIInputView setBackgroundEdgeInsets:];
-[UIInputView setContentRatio:];
-[UIInputView setInputViewStyle:];
-[UIInputView setLeftContentViewSize:];
-[UIInputView setRightContentViewSize:];
-[UIInputView set_mergedImage:];
-[UIInputView set_mergedSliceMap:];
-[UIInputView set_splitSliceMap:];
```
