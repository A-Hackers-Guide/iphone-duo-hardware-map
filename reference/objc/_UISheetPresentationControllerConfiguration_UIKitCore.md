# `_UISheetPresentationControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSXPCSecureCoding`
- 34 instance variables, 38 properties, 77 instance methods, 3 class methods

## Instance variables

```
B __shouldScaleDownBehindDescendantSheets;
B __peeksWhenFloating;
B __wantsFullScreen;
B __wantsBottomAttached;
B __wantsEdgeAttachedInCompactHeight;
B __widthFollowsPreferredContentSizeWhenEdgeAttached;
B __prefersGrabberVisible;
B __insetsPresentedViewForGrabber;
B __prefersScrollingResizesWhenDetentDirectionIsDown;
B __prefersScrollingExpandsToLargerDetentWhenScrolledToEdge;
B __shouldAdaptToInactiveDivisions;
B __hostParentIsFunctionallyFullScreen;
B __hostParentScalesDownBehindDescendants;
d __grabberTopSpacing;
d __additionalMinimumTopInset;
q __mode;
d __cornerRadiusForPresentationAndDismissal;
d __preferredCornerRadius;
d __preferredShadowOpacity;
d __shadowRadius;
@"NSArray" __detents;
@"NSString" __selectedDetentIdentifier;
@"_UISheetPresentationControllerAppearance" __standardAppearance;
@"_UISheetPresentationControllerAppearance" __edgeAttachedCompactHeightAppearance;
@"_UISheetPresentationControllerAppearance" __floatingAppearance;
q __preferredPlacement;
q __divisionHorizontalAlignment;
q __detentDirectionWhenFloating;
@"UIVisualEffect" __backgroundEffect;
d __hostParentDepthLevel;
d __hostParentRecedingStackOffset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __minimumInsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __hostParentStackAlignmentFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __hostParentFullHeightUntransformedFrameForDepthLevel;
```

## Properties

```
@property (TB,N,S_setShouldScaleDownBehindDescendantSheets:,V__shouldScaleDownBehindDescendantSheets) _shouldScaleDownBehindDescendantSheets;
@property (TB,N,S_setPeeksWhenFloating:,V__peeksWhenFloating) _peeksWhenFloating;
@property (TB,N,S_setWantsFullScreen:,V__wantsFullScreen) _wantsFullScreen;
@property (TB,N,S_setWantsBottomAttached:,V__wantsBottomAttached) _wantsBottomAttached;
@property (TB,N,S_setWantsEdgeAttachedInCompactHeight:,V__wantsEdgeAttachedInCompactHeight) _wantsEdgeAttachedInCompactHeight;
@property (TB,N,S_setWidthFollowsPreferredContentSizeWhenEdgeAttached:,V__widthFollowsPreferredContentSizeWhenEdgeAttached) _widthFollowsPreferredContentSizeWhenEdgeAttached;
@property (TB,N,S_prefersGrabberVisible:,V__prefersGrabberVisible) _prefersGrabberVisible;
@property (Td,N,S_setGrabberTopSpacing:,V__grabberTopSpacing) _grabberTopSpacing;
@property (Td,N,S_setAdditionalMinimumTopInset:,V__additionalMinimumTopInset) _additionalMinimumTopInset;
@property (T{UIEdgeInsets=dddd},N,S_setMinimumInsets:,V__minimumInsets) _minimumInsets;
@property (TB,N,S_setInsetsPresentedViewForGrabber:,V__insetsPresentedViewForGrabber) _insetsPresentedViewForGrabber;
@property (Tq,N,S_setMode:,V__mode) _mode;
@property (Td,N,S_setCornerRadiusForPresentationAndDismissal:,V__cornerRadiusForPresentationAndDismissal) _cornerRadiusForPresentationAndDismissal;
@property (Td,N,S_setPreferredCornerRadius:,V__preferredCornerRadius) _preferredCornerRadius;
@property (Td,N,S_setPreferredShadowOpacity:,V__preferredShadowOpacity) _preferredShadowOpacity;
@property (Td,N,S_setShadowRadius:,V__shadowRadius) _shadowRadius;
@property (T@"NSArray",C,N,S_setDetents:,V__detents) _detents;
@property (T@"NSString",C,N,S_setSelectedDetentIdentifier:,V__selectedDetentIdentifier) _selectedDetentIdentifier;
@property (T@"_UISheetPresentationControllerAppearance",&,N,S_setStandardAppearance:,V__standardAppearance) _standardAppearance;
@property (T@"_UISheetPresentationControllerAppearance",&,N,S_setEdgeAttachedCompactHeightAppearance:,V__edgeAttachedCompactHeightAppearance) _edgeAttachedCompactHeightAppearance;
@property (T@"_UISheetPresentationControllerAppearance",&,N,S_setFloatingAppearance:,V__floatingAppearance) _floatingAppearance;
@property (Tq,N,S_setPreferredPlacement:,V__preferredPlacement) _preferredPlacement;
@property (Tq,N,S_setDivisionHorizontalAlignment:,V__divisionHorizontalAlignment) _divisionHorizontalAlignment;
@property (Tq,N,S_setDetentDirectionWhenFloating:,V__detentDirectionWhenFloating) _detentDirectionWhenFloating;
@property (TB,N,S_setPrefersScrollingResizesWhenDetentDirectionIsDown:,V__prefersScrollingResizesWhenDetentDirectionIsDown) _prefersScrollingResizesWhenDetentDirectionIsDown;
@property (TB,N,S_setPrefersScrollingExpandsToLargerDetentWhenScrolledToEdge:,V__prefersScrollingExpandsToLargerDetentWhenScrolledToEdge) _prefersScrollingExpandsToLargerDetentWhenScrolledToEdge;
@property (T@"UIVisualEffect",&,N,V__backgroundEffect) _backgroundEffect;
@property (TB,N,S_setShouldAdaptToInactiveDivisions:,V__shouldAdaptToInactiveDivisions) _shouldAdaptToInactiveDivisions;
@property (Td,N,S_setHostParentDepthLevel:,V__hostParentDepthLevel) _hostParentDepthLevel;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setHostParentStackAlignmentFrame:,V__hostParentStackAlignmentFrame) _hostParentStackAlignmentFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setHostParentFullHeightUntransformedFrameForDepthLevel:,V__hostParentFullHeightUntransformedFrameForDepthLevel) _hostParentFullHeightUntransformedFrameForDepthLevel;
@property (TB,N,S_setHostParentIsFunctionallyFullScreen:,V__hostParentIsFunctionallyFullScreen) _hostParentIsFunctionallyFullScreen;
@property (TB,N,S_setHostParentScalesDownBehindDescendants:,V__hostParentScalesDownBehindDescendants) _hostParentScalesDownBehindDescendants;
@property (Td,N,S_setHostParentRecedingStackOffset:,V__hostParentRecedingStackOffset) _hostParentRecedingStackOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISheetPresentationControllerConfiguration supportsBSXPCSecureCoding];
+[_UISheetPresentationControllerConfiguration supportsSecureCoding];
+[_UISheetPresentationControllerConfiguration _fullScreenConfiguration];
```

## Instance methods

```
-[_UISheetPresentationControllerConfiguration _preferredPlacement];
-[_UISheetPresentationControllerConfiguration _standardAppearance];
-[_UISheetPresentationControllerConfiguration _setDetents:];
-[_UISheetPresentationControllerConfiguration _shadowRadius];
-[_UISheetPresentationControllerConfiguration _mode];
-[_UISheetPresentationControllerConfiguration _setPreferredPlacement:];
-[_UISheetPresentationControllerConfiguration _additionalMinimumTopInset];
-[_UISheetPresentationControllerConfiguration _backgroundEffect];
-[_UISheetPresentationControllerConfiguration _hostParentRecedingStackOffset];
-[_UISheetPresentationControllerConfiguration _preferredCornerRadius];
-[_UISheetPresentationControllerConfiguration _hostParentDepthLevel];
-[_UISheetPresentationControllerConfiguration _hostParentScalesDownBehindDescendants];
-[_UISheetPresentationControllerConfiguration _hostParentIsFunctionallyFullScreen];
-[_UISheetPresentationControllerConfiguration _preferredShadowOpacity];
-[_UISheetPresentationControllerConfiguration _wantsFullScreen];
-[_UISheetPresentationControllerConfiguration _edgeAttachedCompactHeightAppearance];
-[_UISheetPresentationControllerConfiguration _detents];
-[_UISheetPresentationControllerConfiguration _setAdditionalMinimumTopInset:];
-[_UISheetPresentationControllerConfiguration _setHostParentStackAlignmentFrame:];
-[_UISheetPresentationControllerConfiguration _selectedDetentIdentifier];
-[_UISheetPresentationControllerConfiguration _setPreferredShadowOpacity:];
-[_UISheetPresentationControllerConfiguration _setHostParentScalesDownBehindDescendants:];
-[_UISheetPresentationControllerConfiguration _hostParentFullHeightUntransformedFrameForDepthLevel];
-[_UISheetPresentationControllerConfiguration _setHostParentDepthLevel:];
-[_UISheetPresentationControllerConfiguration _widthFollowsPreferredContentSizeWhenEdgeAttached];
-[_UISheetPresentationControllerConfiguration _hostParentStackAlignmentFrame];
-[_UISheetPresentationControllerConfiguration _divisionHorizontalAlignment];
-[_UISheetPresentationControllerConfiguration _setPreferredCornerRadius:];
-[_UISheetPresentationControllerConfiguration _setWantsFullScreen:];
-[_UISheetPresentationControllerConfiguration _setStandardAppearance:];
-[_UISheetPresentationControllerConfiguration _setShouldAdaptToInactiveDivisions:];
-[_UISheetPresentationControllerConfiguration _setHostParentFullHeightUntransformedFrameForDepthLevel:];
-[_UISheetPresentationControllerConfiguration _setWidthFollowsPreferredContentSizeWhenEdgeAttached:];
-[_UISheetPresentationControllerConfiguration _setPeeksWhenFloating:];
-[_UISheetPresentationControllerConfiguration _shouldAdaptToInactiveDivisions];
-[_UISheetPresentationControllerConfiguration _wantsEdgeAttachedInCompactHeight];
-[_UISheetPresentationControllerConfiguration _setDivisionHorizontalAlignment:];
-[_UISheetPresentationControllerConfiguration _setMinimumInsets:];
-[_UISheetPresentationControllerConfiguration _setWantsEdgeAttachedInCompactHeight:];
-[_UISheetPresentationControllerConfiguration _floatingAppearance];
-[_UISheetPresentationControllerConfiguration _peeksWhenFloating];
-[_UISheetPresentationControllerConfiguration _setMode:];
-[_UISheetPresentationControllerConfiguration _setFloatingAppearance:];
-[_UISheetPresentationControllerConfiguration _prefersScrollingResizesWhenDetentDirectionIsDown];
-[_UISheetPresentationControllerConfiguration _setEdgeAttachedCompactHeightAppearance:];
-[_UISheetPresentationControllerConfiguration _minimumInsets];
-[_UISheetPresentationControllerConfiguration _setHostParentRecedingStackOffset:];
-[_UISheetPresentationControllerConfiguration _prefersScrollingExpandsToLargerDetentWhenScrolledToEdge];
-[_UISheetPresentationControllerConfiguration _setPrefersScrollingExpandsToLargerDetentWhenScrolledToEdge:];
-[_UISheetPresentationControllerConfiguration _setHostParentIsFunctionallyFullScreen:];
-[_UISheetPresentationControllerConfiguration _setSelectedDetentIdentifier:];
-[_UISheetPresentationControllerConfiguration _setShadowRadius:];
-[_UISheetPresentationControllerConfiguration _detentDirectionWhenFloating];
-[_UISheetPresentationControllerConfiguration init];
-[_UISheetPresentationControllerConfiguration _isEqual:onlyCheckPropertiesRequiringFencing:];
-[_UISheetPresentationControllerConfiguration _setGrabberTopSpacing:];
-[_UISheetPresentationControllerConfiguration _grabberTopSpacing];
-[_UISheetPresentationControllerConfiguration _shouldScaleDownBehindDescendantSheets];
-[_UISheetPresentationControllerConfiguration _setDetentDirectionWhenFloating:];
-[_UISheetPresentationControllerConfiguration _prefersGrabberVisible];
-[_UISheetPresentationControllerConfiguration _setInsetsPresentedViewForGrabber:];
-[_UISheetPresentationControllerConfiguration _setShouldScaleDownBehindDescendantSheets:];
-[_UISheetPresentationControllerConfiguration _cornerRadiusForPresentationAndDismissal];
-[_UISheetPresentationControllerConfiguration encodeWithCoder:];
-[_UISheetPresentationControllerConfiguration _wantsBottomAttached];
-[_UISheetPresentationControllerConfiguration set_backgroundEffect:];
-[_UISheetPresentationControllerConfiguration description];
-[_UISheetPresentationControllerConfiguration _setCornerRadiusForPresentationAndDismissal:];
-[_UISheetPresentationControllerConfiguration _prefersGrabberVisible:];
-[_UISheetPresentationControllerConfiguration initWithCoder:];
-[_UISheetPresentationControllerConfiguration encodeWithBSXPCCoder:];
-[_UISheetPresentationControllerConfiguration _setWantsBottomAttached:];
-[_UISheetPresentationControllerConfiguration initWithBSXPCCoder:];
-[_UISheetPresentationControllerConfiguration _insetsPresentedViewForGrabber];
-[_UISheetPresentationControllerConfiguration _setPrefersScrollingResizesWhenDetentDirectionIsDown:];
-[_UISheetPresentationControllerConfiguration isEqual:];
-[_UISheetPresentationControllerConfiguration _shouldFenceChangeToConfiguration:];
```
