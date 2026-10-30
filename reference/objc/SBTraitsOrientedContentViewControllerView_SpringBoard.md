# `SBTraitsOrientedContentViewControllerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- Protocols: `BSDescriptionProviding`
- 10 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UIView" _contentView;
@"UIView" _backgroundView;
@"UIView" _overlayView;
@"UILabel" _placeholderLabel;
q _previousContainerLayoutOrientation;
q _previousContentLayoutOrientation;
@"SBTraitsDirectionalRotationView" _contentRotationView;
q _contentOrientation;
q _containerOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentViewBoundsInReferenceSpace;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentViewBoundsInReferenceSpace) contentViewBoundsInReferenceSpace;
@property (Tq,N,V_contentOrientation) contentOrientation;
@property (Tq,N,V_containerOrientation) containerOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsOrientedContentViewControllerView setClipsToBounds:];
-[SBTraitsOrientedContentViewControllerView containerOrientation];
-[SBTraitsOrientedContentViewControllerView setContentView:];
-[SBTraitsOrientedContentViewControllerView succinctDescriptionBuilder];
-[SBTraitsOrientedContentViewControllerView setContainerOrientation:];
-[SBTraitsOrientedContentViewControllerView contentOrientation];
-[SBTraitsOrientedContentViewControllerView setContentOrientation:];
-[SBTraitsOrientedContentViewControllerView layoutSubviews];
-[SBTraitsOrientedContentViewControllerView descriptionWithMultilinePrefix:];
-[SBTraitsOrientedContentViewControllerView succinctDescription];
-[SBTraitsOrientedContentViewControllerView _setContinuousCornerRadius:];
-[SBTraitsOrientedContentViewControllerView contentView];
-[SBTraitsOrientedContentViewControllerView backgroundView];
-[SBTraitsOrientedContentViewControllerView description];
-[SBTraitsOrientedContentViewControllerView initWithFrame:];
-[SBTraitsOrientedContentViewControllerView setBackgroundView:];
-[SBTraitsOrientedContentViewControllerView descriptionBuilderWithMultilinePrefix:];
-[SBTraitsOrientedContentViewControllerView addOverlayView:];
-[SBTraitsOrientedContentViewControllerView _counterTransformedToIdentityForContainerChange];
-[SBTraitsOrientedContentViewControllerView _setDebugColorsEnabled:];
-[SBTraitsOrientedContentViewControllerView contentViewBoundsInReferenceSpace];
-[SBTraitsOrientedContentViewControllerView setContentViewBoundsInReferenceSpace:];
```
