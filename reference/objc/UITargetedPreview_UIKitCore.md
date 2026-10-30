# `UITargetedPreview`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMorphableInternal`, `NSCopying`
- 19 instance variables, 29 properties, 59 instance methods, 1 class methods

## Instance variables

```
@"CALayer" _layer;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _cropInsets;
B _sourceViewIsInViewHierarchy;
B _hasCustomTarget;
B _hasCustomParameters;
B _defaultPreview;
B __captureHierarchyBelowSourceView;
Q _sourceHostingBehavior;
@"_UITypedStorage" _typedStorage;
@"UIPreviewTarget" _target;
@"UIView" _view;
@"UIPreviewParameters" _parameters;
@"UIView" _viewToSnapshot;
@"<_UIPreviewProvider>" __PreviewProvider;
@"<NSCopying><NSObject>" __internalIdentifier;
@"NSArray" __transferrableAnimationKeys;
@"NSArray" __matchableProperties;
@"UIView" _overridePositionTrackingView;
@"NSArray" __accessoryViews;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,G_isDefaultPreview,S_setDefaultPreview:,V_defaultPreview) defaultPreview;
@property (T@"UIView",W,N,G_viewToSnapshot,S_setViewToSnapshot:,V_viewToSnapshot) viewToSnapshot;
@property (T@"<_UIPreviewProvider>",R,N,V__PreviewProvider) _PreviewProvider;
@property (TB,R,N,G_sourceViewIsInViewHierarchy,V_sourceViewIsInViewHierarchy) _sourceViewIsInViewHierarchy;
@property (TQ,N,S_setSourceHostingBehavior:,V_sourceHostingBehavior) _sourceHostingBehavior;
@property (TB,R,N) _shouldHostSourceView;
@property (TB,R,N,V_hasCustomTarget) _hasCustomTarget;
@property (TB,R,N,V_hasCustomParameters) _hasCustomParameters;
@property (TB,R,N,G_isVisible) _visible;
@property (TB,R,N,G_isLikelyOpaque) _isLikelyOpaque;
@property (Tq,N,G_previewMode,S_setPreviewMode:) previewMode;
@property (T@"<NSCopying><NSObject>",&,N,V__internalIdentifier) _internalIdentifier;
@property (T@"NSArray",&,N,V__transferrableAnimationKeys) _transferrableAnimationKeys;
@property (T@"NSArray",&,N,V__matchableProperties) _matchableProperties;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _frame;
@property (T@"_UIShape",R,N) _outlineShape;
@property (TB,N,V__captureHierarchyBelowSourceView) _captureHierarchyBelowSourceView;
@property (TB,N) _springboardPlatterStyle;
@property (T@"UIView",&,N,S_setOverridePositionTrackingView:,V_overridePositionTrackingView) overridePositionTrackingView;
@property (TB,N,G_prefersUnmaskedPlatterStyle,S_setPrefersUnmaskedPlatterStyle:) _prefersUnmaskedPlatterStyle;
@property (T@"NSArray",&,N,G_accessoryViews,S_setAccessoryViews:,V__accessoryViews) _accessoryViews;
@property (T@"UIPreviewTarget",R,N,V_target) target;
@property (T@"UIView",R,N,V_view) view;
@property (T@"UIPreviewParameters",R,C,N,V_parameters) parameters;
@property (T{CGSize=dd},R,N) size;
```

## Class methods

```
+[UITargetedPreview new];
```

## Instance methods

```
-[UITargetedPreview _isVisible];
-[UITargetedPreview parameters];
-[UITargetedPreview _isVisibleIncludingAlpha:];
-[UITargetedPreview _transferAnimationsToView:];
-[UITargetedPreview _PreviewProvider];
-[UITargetedPreview overridePositionTrackingView];
-[UITargetedPreview _hasCustomParameters];
-[UITargetedPreview set_captureHierarchyBelowSourceView:];
-[UITargetedPreview _initWithView:fromCurrentState:fallbackBackgroundColor:contentScale:];
-[UITargetedPreview _setAccessoryViews:];
-[UITargetedPreview init];
-[UITargetedPreview set_matchableProperties:];
-[UITargetedPreview set_transferrableAnimationKeys:];
-[UITargetedPreview _sourceHostingBehavior];
-[UITargetedPreview initWithView:];
-[UITargetedPreview _accessoryViews];
-[UITargetedPreview _setPreviewMode:];
-[UITargetedPreview _frame];
-[UITargetedPreview _isLikelyOpaque];
-[UITargetedPreview set_internalIdentifier:];
-[UITargetedPreview containsPoint:fromView:];
-[UITargetedPreview _morphView];
-[UITargetedPreview _setPrefersUnmaskedPlatterStyle:];
-[UITargetedPreview size];
-[UITargetedPreview _matchableProperties];
-[UITargetedPreview view];
-[UITargetedPreview _resolvedMorphablePreview];
-[UITargetedPreview _isDefaultPreview];
-[UITargetedPreview _morphPreviewFromCurrentState:fallbackBackgroundColor:contentScale:];
-[UITargetedPreview _effectiveBackgroundColorResolvesToMaterial];
-[UITargetedPreview _hasCustomTarget];
-[UITargetedPreview _springboardPlatterStyle];
-[UITargetedPreview _internalIdentifier];
-[UITargetedPreview _shouldHostSourceView];
-[UITargetedPreview _captureHierarchyBelowSourceView];
-[UITargetedPreview retargetedPreviewWithTarget:];
-[UITargetedPreview _isRoughlyEqualToPreview:];
-[UITargetedPreview _setViewToSnapshot:];
-[UITargetedPreview _sourceViewIsInViewHierarchy];
-[UITargetedPreview description];
-[UITargetedPreview _defaultTargetForView:withCenter:version:];
-[UITargetedPreview _previewMode];
-[UITargetedPreview _trueSourceViewIfPortal];
-[UITargetedPreview _resolvedBackgroundMaterial];
-[UITargetedPreview _transferrableAnimationKeys];
-[UITargetedPreview target];
-[UITargetedPreview copyWithZone:];
-[UITargetedPreview _viewToSnapshot];
-[UITargetedPreview _setOverridePositionTrackingView:];
-[UITargetedPreview isEqual:];
-[UITargetedPreview _mayInferCornerRadiusFromVisiblePath];
-[UITargetedPreview _prefersUnmaskedPlatterStyle];
-[UITargetedPreview _setSourceHostingBehavior:];
-[UITargetedPreview _setDefaultPreview:];
-[UITargetedPreview initWithView:parameters:target:];
-[UITargetedPreview _outlineShape];
-[UITargetedPreview set_springboardPlatterStyle:];
-[UITargetedPreview _sizeUsingPresentationLayer:];
-[UITargetedPreview initWithView:parameters:];
```
