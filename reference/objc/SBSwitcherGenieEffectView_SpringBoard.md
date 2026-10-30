# `SBSwitcherGenieEffectView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `BSInvalidatable`
- 22 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"_SBSwitcherGenieEffectContainerView" _containerView;
@"_SBSwitcherGenieEffectContentView" _contentView;
@"NSMutableArray" _contentPortalViews;
@"NSMutableArray" _contentNotificationBadgePortalViews;
{SBSwitcherGenieGlassHighlight="style"Q"direction"{SBSwitcherGenieGlassHighlightDirection="x"d"y"d"z"d}"intensity"d} _glassHighlight;
@"_SBSDFView" _keyFillHighlightSDFView;
@"_SBSDFView" _diffuseHighlightSDFView;
@"_SBSDFView" _darklightSDFView;
@"_SBSDFElementView" _sdfElementView;
@"NSArray" _animatableProperties;
@"UIViewFloatAnimatableProperty" _boundsProperty;
q _generationCount;
q _lastCompletedGenerationCount;
B _pendingCompletion;
B _modelUpdatesPaused;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _c2_lock;
B _c2_presentationUpdatePaused;
@"UIView" _childContentView;
d _displayScale;
B _portaledContentShouldMatchSource;
@"<SBSwitcherGenieEffectViewDelegate>" _delegate;
@"SBSwitcherGenieAttributes" _attributes;
```

## Properties

```
@property (T@"<SBSwitcherGenieEffectViewDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_portaledContentShouldMatchSource) portaledContentShouldMatchSource;
@property (T@"SBSwitcherGenieAttributes",R,N,V_attributes) attributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherGenieEffectView addPortaledContentView:];
-[SBSwitcherGenieEffectView setAttributes:mode:completion:];
-[SBSwitcherGenieEffectView _iconBadgeViewIfAnyInView:];
-[SBSwitcherGenieEffectView _addPortaledNotificationBadgeForContentViewIfNeeded:];
-[SBSwitcherGenieEffectView _invalidateGenie];
-[SBSwitcherGenieEffectView portaledContentShouldMatchSource];
-[SBSwitcherGenieEffectView layoutSubviews];
-[SBSwitcherGenieEffectView hitTest:withEvent:];
-[SBSwitcherGenieEffectView _setGlassHighlight:];
-[SBSwitcherGenieEffectView _continuousCornerRadius];
-[SBSwitcherGenieEffectView setPortaledContentViews:];
-[SBSwitcherGenieEffectView invalidate];
-[SBSwitcherGenieEffectView _layoutContentAndContainerViewWithAttributes:];
-[SBSwitcherGenieEffectView _setContinuousCornerRadius:];
-[SBSwitcherGenieEffectView _invalidateContentViewPortalsIfNeeded];
-[SBSwitcherGenieEffectView delegate];
-[SBSwitcherGenieEffectView _updateGenieMeshTransformForPresentationLayer:properties:boundsProperty:attributes:];
-[SBSwitcherGenieEffectView _performGenieWithAttributes:mode:completion:];
-[SBSwitcherGenieEffectView initWithCoder:];
-[SBSwitcherGenieEffectView _iconViewIfAnyInView:];
-[SBSwitcherGenieEffectView attributes];
-[SBSwitcherGenieEffectView pointInside:withEvent:];
-[SBSwitcherGenieEffectView _addAndReturnPortaledContentView:];
-[SBSwitcherGenieEffectView setPortaledContentShouldMatchSource:];
-[SBSwitcherGenieEffectView initWithFrame:delegate:];
-[SBSwitcherGenieEffectView setChildContentView:];
```
