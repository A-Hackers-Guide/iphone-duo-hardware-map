# `_UIPortalView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIViewMultiLayerDelegate`
- 6 instance variables, 20 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _forwardsClientHitTestingToSourceView;
B __geometryFrozen;
B __prefersClientLayer;
@"UIView" _sourceView;
@"NSString" _name;
@"NSSet" __additionalAnimatableKeyPaths;
```

## Properties

```
@property (TB,N,G_isGeometryFrozen,S_setGeometryFrozen:,V__geometryFrozen) _geometryFrozen;
@property (T@"NSSet",&,N,G_additionalAnimatableKeyPaths,S_setAdditionalAnimatableKeypaths:,V__additionalAnimatableKeyPaths) _additionalAnimatableKeyPaths;
@property (TB,N,G_prefersClientLayer,S_setPrefersClientLayer:,V__prefersClientLayer) _prefersClientLayer;
@property (TB,N,S_setAllowedInContextTransform:) _allowedInContextTransform;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (T@"NSString",C,N,V_name) name;
@property (TB,D,N) hidesSourceView;
@property (TB,D,N) matchesAlpha;
@property (TB,D,N) matchesTransform;
@property (TB,D,N) matchesPosition;
@property (TB,D,N) allowsBackdropGroups;
@property (TB,N) hidesSourceLayerInOtherPortals;
@property (TB,D,N) allowsHitTesting;
@property (TB,N,V_forwardsClientHitTestingToSourceView) forwardsClientHitTestingToSourceView;
@property (Td,N) sourceViewAlphaScale;
@property (T@"CAPortalLayer",R,D,N) portalLayer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPortalView layerClass];
```

## Instance methods

```
-[_UIPortalView matchesTransform];
-[_UIPortalView setMatchesTransform:];
-[_UIPortalView hidesSourceView];
-[_UIPortalView setHidden:];
-[_UIPortalView _isGeometryFrozen];
-[_UIPortalView setSourceViewAlphaScale:];
-[_UIPortalView _allowedInContextTransform];
-[_UIPortalView initWithSourceView:];
-[_UIPortalView portalLayer];
-[_UIPortalView _prefersClientLayer];
-[_UIPortalView setCenter:];
-[_UIPortalView hitTest:withEvent:];
-[_UIPortalView _pointInSourceViewForPoint:];
-[_UIPortalView setBounds:];
-[_UIPortalView setMatchesAlpha:];
-[_UIPortalView sourceViewAlphaScale];
-[_UIPortalView matchesPosition];
-[_UIPortalView _setAdditionalAnimatableKeypaths:];
-[_UIPortalView _outermostLayerDidChange:];
-[_UIPortalView allowsHitTesting];
-[_UIPortalView setHidesSourceLayerInOtherPortals:];
-[_UIPortalView _updateSourceLayer];
-[_UIPortalView setSourceView:];
-[_UIPortalView _sourceViewIfPortal];
-[_UIPortalView _setPrefersClientLayer:];
-[_UIPortalView setHidesSourceView:];
-[_UIPortalView _setGeometryFrozen:];
-[_UIPortalView setFrame:];
-[_UIPortalView allowsBackdropGroups];
-[_UIPortalView description];
-[_UIPortalView setName:];
-[_UIPortalView setForwardsClientHitTestingToSourceView:];
-[_UIPortalView hidesSourceLayerInOtherPortals];
-[_UIPortalView _setAllowedInContextTransform:];
-[_UIPortalView setMatchesPosition:];
-[_UIPortalView setAllowsBackdropGroups:];
-[_UIPortalView pointInside:withEvent:];
-[_UIPortalView forwardsClientHitTestingToSourceView];
-[_UIPortalView _shouldAnimatePropertyWithKey:];
-[_UIPortalView initWithFrame:];
-[_UIPortalView name];
-[_UIPortalView _additionalAnimatableKeyPaths];
-[_UIPortalView setAllowsHitTesting:];
-[_UIPortalView matchesAlpha];
-[_UIPortalView sourceView];
```
