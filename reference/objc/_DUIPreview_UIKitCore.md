# `_DUIPreview`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 22 instance variables, 36 properties, 66 instance methods, 3 class methods

## Instance variables

```
{?="width"d"height"d"depth"d} _contentSize;
{CAPoint3D="x"d"y"d"z"d} _originalCenterInCoordinateSpace;
B _hidesSourceView;
B _hiddenDuringDrag;
B _hasCustomOutline;
B _avoidAnimation;
B _wantsSuppressedMask;
@"UIColor" _backgroundColor;
@"UIBezierPath" _outline;
@"UIBezierPath" _shadowPath;
@"_UIDragPreviewShadowProperties" _shadowProperties;
@"_DUITargetLayerDescriptor" _coordinateSpaceSourceLayerContext;
d _originalRotation;
q _previewMode;
q _preferredStackOrder;
{CGPoint="x"d"y"d} _contentOffset;
{CGPoint="x"d"y"d} _initialBadgeLocation;
{CGPoint="x"d"y"d} _originalCenter;
{CGPoint="x"d"y"d} _liftAnchorPoint;
{CGSize="width"d"height"d} _viewScaleFactor;
{?="width"d"height"d"depth"d} _placeholderContentSize3D;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _overrideStackTransform;
```

## Properties

```
@property (T{CGSize=dd},R,N,V_viewScaleFactor) viewScaleFactor;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
@property (T{CGSize=dd},R,N) boundingSize;
@property (T{CGPoint=dd},R,N,V_contentOffset) contentOffset;
@property (T{CGSize=dd},R,D,N) contentSize;
@property (T{CGSize=dd},R,N) croppedScaledSize;
@property (Td,R,N) liftAlpha;
@property (T{CGAffineTransform=dddddd},R,N) liftTransform;
@property (TB,N,V_hidesSourceView) hidesSourceView;
@property (T@"UIBezierPath",C,N,V_outline) outline;
@property (T@"UIBezierPath",C,N,V_shadowPath) shadowPath;
@property (T@"UIBezierPath",R,N) effectiveShadowPath;
@property (T@"_UIDragPreviewShadowProperties",C,N,V_shadowProperties) shadowProperties;
@property (T{CGAffineTransform=dddddd},N,V_overrideStackTransform) overrideStackTransform;
@property (T{CGPoint=dd},N,V_initialBadgeLocation) initialBadgeLocation;
@property (T{CGPoint=dd},N,V_originalCenter) originalCenter;
@property (T{CGPoint=dd},D,N) originalCenterInCoordinateSpace;
@property (T@"_DUITargetLayerDescriptor",&,N,V_coordinateSpaceSourceLayerContext) coordinateSpaceSourceLayerContext;
@property (TB,R,N,GisHiddenDuringDrag,V_hiddenDuringDrag) hiddenDuringDrag;
@property (T{?=ddd},R,N,V_placeholderContentSize3D) placeholderContentSize3D;
@property (Td,N,V_originalRotation) originalRotation;
@property (TB,R,N,GisOversized) oversized;
@property (Td,R,N) scaleFactor;
@property (T{CGSize=dd},R,N) scaledSize;
@property (Td,R,N) stackAlpha;
@property (TB,N) textMode;
@property (Tq,N,V_previewMode) previewMode;
@property (Td,R,N) topAlpha;
@property (T{CGPoint=dd},R,N) unscaledAnchorPoint;
@property (T{CGSize=dd},R,N) unscaledSize;
@property (T@"UIDragPreviewParameters",R,N) parameters;
@property (T{CGPoint=dd},N,V_liftAnchorPoint) liftAnchorPoint;
@property (TB,N,V_hasCustomOutline) hasCustomOutline;
@property (TB,N,V_avoidAnimation) avoidAnimation;
@property (TB,N,V_wantsSuppressedMask) wantsSuppressedMask;
@property (Tq,N,V_preferredStackOrder) preferredStackOrder;
```

## Class methods

```
+[_DUIPreview supportsSecureCoding];
+[_DUIPreview defaultPreviewWithFrame:];
+[_DUIPreview defaultStackAlpha];
```

## Instance methods

```
-[_DUIPreview setShadowPath:];
-[_DUIPreview parameters];
-[_DUIPreview hidesSourceView];
-[_DUIPreview shadowProperties];
-[_DUIPreview contentOffset];
-[_DUIPreview init];
-[_DUIPreview setShadowProperties:];
-[_DUIPreview liftAnchorPoint];
-[_DUIPreview contentSize];
-[_DUIPreview shadowPath];
-[_DUIPreview setBackgroundColor:];
-[_DUIPreview initialBadgeLocation];
-[_DUIPreview scaleFactor];
-[_DUIPreview encodeWithCoder:];
-[_DUIPreview setHidesSourceView:];
-[_DUIPreview backgroundColor];
-[_DUIPreview initWithCoder:];
-[_DUIPreview copyWithZone:];
-[_DUIPreview isEqual:];
-[_DUIPreview setLiftAnchorPoint:];
-[_DUIPreview outline];
-[_DUIPreview scaledSize];
-[_DUIPreview originalCenterInCoordinateSpace];
-[_DUIPreview setPreviewMode:];
-[_DUIPreview viewScaleFactor];
-[_DUIPreview _applyPropertiesFromPreviewParameters:];
-[_DUIPreview _initWithView:container:parameters:platformCenter:];
-[_DUIPreview _topOffset];
-[_DUIPreview avoidAnimation];
-[_DUIPreview backAlpha];
-[_DUIPreview boundingSize];
-[_DUIPreview coordinateSpaceSourceLayerContext];
-[_DUIPreview croppedScaledSize];
-[_DUIPreview effectiveShadowPath];
-[_DUIPreview hasCustomOutline];
-[_DUIPreview initWithBounds:outline:];
-[_DUIPreview initWithView:container:parameters:];
-[_DUIPreview initWithView:container:parameters:center:];
-[_DUIPreview isHiddenDuringDrag];
-[_DUIPreview isOversized];
-[_DUIPreview liftAlpha];
-[_DUIPreview liftTransform];
-[_DUIPreview originalCenter];
-[_DUIPreview originalRotation];
-[_DUIPreview overrideStackTransform];
-[_DUIPreview placeholderContentSize3D];
-[_DUIPreview preferredStackOrder];
-[_DUIPreview previewMode];
-[_DUIPreview setAvoidAnimation:];
-[_DUIPreview setCoordinateSpaceSourceLayerContext:];
-[_DUIPreview setHasCustomOutline:];
-[_DUIPreview setInitialBadgeLocation:];
-[_DUIPreview setOriginalCenter:];
-[_DUIPreview setOriginalCenterInCoordinateSpace:];
-[_DUIPreview setOriginalRotation:];
-[_DUIPreview setOutline:];
-[_DUIPreview setOverrideStackTransform:];
-[_DUIPreview setPreferredStackOrder:];
-[_DUIPreview setTextMode:];
-[_DUIPreview setWantsSuppressedMask:];
-[_DUIPreview stackAlpha];
-[_DUIPreview textMode];
-[_DUIPreview topAlpha];
-[_DUIPreview unscaledAnchorPoint];
-[_DUIPreview unscaledSize];
-[_DUIPreview wantsSuppressedMask];
```
