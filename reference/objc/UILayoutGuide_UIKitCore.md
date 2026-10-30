# `UILayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPopoverPresentationControllerSourceItem_Internal`, `UILayoutItem_Internal`, `_UILayoutItem`, `NSISVariableDelegate`, `NSCoding`
- 28 instance variables, 57 properties, 116 instance methods, 1 class methods

## Instance variables

```
@"NSLayoutRect" _layoutRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _layoutFrame;
B _isLayoutFrameValid;
@"NSMutableArray" _constraintsToBeProcessedAfterDecoding;
@"UIView" _unsafeUnretainedOwningView;
B _allowOwningViewSetting;
B _isLockedToOwningView;
B _useManualLayoutFrame;
B __allowsNegativeDimensions;
B __shouldBeArchived;
@"UIView" _owningView;
@"NSString" _identifier;
@"NSISVariable" _minXVariable;
@"NSISVariable" _minYVariable;
@"NSISVariable" _boundsWidthVariable;
@"NSISVariable" _boundsHeightVariable;
@"NSArray" _systemConstraints;
@"NSMapTable" _stashedLayoutVariableObservations;
@"NSLayoutXAxisAnchor" _leadingAnchor;
@"NSLayoutXAxisAnchor" _trailingAnchor;
@"NSLayoutXAxisAnchor" _leftAnchor;
@"NSLayoutXAxisAnchor" _rightAnchor;
@"NSLayoutYAxisAnchor" _topAnchor;
@"NSLayoutYAxisAnchor" _bottomAnchor;
@"NSLayoutDimension" _widthAnchor;
@"NSLayoutDimension" _heightAnchor;
@"NSLayoutXAxisAnchor" _centerXAnchor;
@"NSLayoutYAxisAnchor" _centerYAnchor;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _ui_bounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) _ui_frame;
@property (T@"UIView",R,N) _ui_superview;
@property (T@"UIView",R,N) _ui_view;
@property (TB,N) _ui_usesManualLayout;
@property (T@"NSLayoutXAxisAnchor",R,N) leadingAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) trailingAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) leftAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) rightAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) topAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) bottomAnchor;
@property (T@"NSLayoutDimension",R,N) widthAnchor;
@property (T@"NSLayoutDimension",R,N) heightAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N) centerXAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) centerYAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) firstBaselineAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N) lastBaselineAnchor;
@property (T@"UITraitCollection",R,N) traitCollection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasAmbiguousLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSISVariable",R,&,N,V_minXVariable) _minXVariable;
@property (T@"NSISVariable",R,&,N,V_minYVariable) _minYVariable;
@property (T@"NSISVariable",R,&,N,V_boundsWidthVariable) _boundsWidthVariable;
@property (T@"NSISVariable",R,&,N,V_boundsHeightVariable) _boundsHeightVariable;
@property (T@"NSMapTable",R,&,N,V_stashedLayoutVariableObservations) _stashedLayoutVariableObservations;
@property (TB,N,S_setAllowsNegativeDimensions:,V__allowsNegativeDimensions) _allowsNegativeDimensions;
@property (TB,N,S_setShouldBeArchived:,V__shouldBeArchived) _shouldBeArchived;
@property (TB,N,G_isLockedToOwningView,S_setLockedToOwningView:,V_isLockedToOwningView) _lockedToOwningView;
@property (T@"NSArray",&,N,S_setSystemConstraints:,V_systemConstraints) _systemConstraints;
@property (TB,N,S_setAllowOwningViewSetting:,V_allowOwningViewSetting) _allowOwningViewSetting;
@property (TB,R,N) _isSafeAreaAspectFitLayoutGuide;
@property (TB,R,N,V_useManualLayoutFrame) _useManualLayoutFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) layoutFrame;
@property (T@"UIView",W,N,V_owningView) owningView;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSLayoutXAxisAnchor",R,N,V_leadingAnchor) leadingAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N,V_trailingAnchor) trailingAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N,V_leftAnchor) leftAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N,V_rightAnchor) rightAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N,V_topAnchor) topAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N,V_bottomAnchor) bottomAnchor;
@property (T@"NSLayoutDimension",R,N,V_widthAnchor) widthAnchor;
@property (T@"NSLayoutDimension",R,N,V_heightAnchor) heightAnchor;
@property (T@"NSLayoutXAxisAnchor",R,N,V_centerXAnchor) centerXAnchor;
@property (T@"NSLayoutYAxisAnchor",R,N,V_centerYAnchor) centerYAnchor;
@property (TQ,?,Snsli_setPiercingToken:) nsli_piercingToken;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UILayoutGuide _defaultSpacingBetweenGuidesForResolvingSymbolicConstant];
```

## Instance methods

```
-[UILayoutGuide traitCollection];
-[UILayoutGuide _setOwningView:];
-[UILayoutGuide identifier];
-[UILayoutGuide init];
-[UILayoutGuide layoutFrame];
-[UILayoutGuide dealloc];
-[UILayoutGuide _nearestViewController];
-[UILayoutGuide _frameInCoordinateSpace:window:];
-[UILayoutGuide nsli_boundsHeightVariable];
-[UILayoutGuide nsli_minYVariable];
-[UILayoutGuide _uili_requiresObservationForVariable:];
-[UILayoutGuide _prefersZoomTransitionsForPopoverPresentationController:];
-[UILayoutGuide _sourceRectForPresentationInWindow:];
-[UILayoutGuide _sourceViewForPresentationInWindow:];
-[UILayoutGuide nsli_boundsWidthVariable];
-[UILayoutGuide setIdentifier:];
-[UILayoutGuide owningView];
-[UILayoutGuide _uili_isFocusGuide];
-[UILayoutGuide nsis_orientationHintForVariable:];
-[UILayoutGuide _boundsHeightVariable];
-[UILayoutGuide lastBaselineAnchor];
-[UILayoutGuide encodeWithCoder:];
-[UILayoutGuide nsis_valueOfVariableIsUserObservable:];
-[UILayoutGuide methodSignatureForSelector:];
-[UILayoutGuide description];
-[UILayoutGuide initWithCoder:];
-[UILayoutGuide traitCollectionDidChange:];
-[UILayoutGuide setOwningView:];
-[UILayoutGuide nsli_minXVariable];
-[UILayoutGuide nsis_valueOfVariable:didChangeInEngine:];
-[UILayoutGuide _minXVariable];
-[UILayoutGuide firstBaselineAnchor];
-[UILayoutGuide _boundsWidthVariable];
-[UILayoutGuide forwardInvocation:];
-[UILayoutGuide frameInView:];
-[UILayoutGuide _minYVariable];
-[UILayoutGuide nsis_descriptionOfVariable:];
-[UILayoutGuide _isSafeAreaAspectFitLayoutGuide];
-[UILayoutGuide _uili_removeLayoutVariableObservationsOnlyToSupportTAMICChange:];
-[UILayoutGuide nsis_shouldIntegralizeVariable:];
-[UILayoutGuide nsli_descriptionIncludesPointer];
-[UILayoutGuide _addConstraintToBeProcessedAfterDecoding:];
-[UILayoutGuide _allowOwningViewSetting];
-[UILayoutGuide _allowsNegativeDimensions];
-[UILayoutGuide _autolayoutTraceAtLevel:recursively:];
-[UILayoutGuide _createAnchorWithClass:attribute:];
-[UILayoutGuide _descriptionForLayoutTrace];
-[UILayoutGuide _invalidateLayoutFrame];
-[UILayoutGuide _isLockedToOwningView];
-[UILayoutGuide _layoutRect];
-[UILayoutGuide _owningViewIsDeallocating];
-[UILayoutGuide _referenceView];
-[UILayoutGuide _setAllowOwningViewSetting:];
-[UILayoutGuide _setAllowsNegativeDimensions:];
-[UILayoutGuide _setLockedToOwningView:];
-[UILayoutGuide _setManualLayoutFrame:];
-[UILayoutGuide _setShouldBeArchived:];
-[UILayoutGuide _setSystemConstraints:];
-[UILayoutGuide _shouldBeArchived];
-[UILayoutGuide _snipReferencingConstraints];
-[UILayoutGuide _stashedLayoutVariableObservations];
-[UILayoutGuide _systemConstraints];
-[UILayoutGuide _ui_addSubLayoutItem:];
-[UILayoutGuide _ui_addToView:atIndex:];
-[UILayoutGuide _ui_bounds];
-[UILayoutGuide _ui_frame];
-[UILayoutGuide _ui_insertSubLayoutItem:atIndex:];
-[UILayoutGuide _ui_removeFromParentLayoutItem];
-[UILayoutGuide _ui_superview];
-[UILayoutGuide _ui_usesManualLayout];
-[UILayoutGuide _ui_view];
-[UILayoutGuide _uili_existingBaseFrameVariables];
-[UILayoutGuide _uili_existingObservationEligibleLayoutVariables];
-[UILayoutGuide _uili_observableLayoutEngineForBaseFrameVariables:];
-[UILayoutGuide _uili_stashLayoutVariableObservation:forVariable:];
-[UILayoutGuide _updateLayoutFrameInOwningView:fromEngine:];
-[UILayoutGuide _useManualLayoutFrame];
-[UILayoutGuide bottomAnchor];
-[UILayoutGuide centerXAnchor];
-[UILayoutGuide centerYAnchor];
-[UILayoutGuide constraintsAffectingLayoutForAxis:];
-[UILayoutGuide hasAmbiguousLayout];
-[UILayoutGuide heightAnchor];
-[UILayoutGuide leadingAnchor];
-[UILayoutGuide leftAnchor];
-[UILayoutGuide nsli_addConstraint:];
-[UILayoutGuide nsli_autoresizingMask];
-[UILayoutGuide nsli_constraintWithAnchor:relatedBy:toAnchor:withSystemSpacingMultipliedBy:];
-[UILayoutGuide nsli_contentHeightVariable];
-[UILayoutGuide nsli_contentWidthVariable];
-[UILayoutGuide nsli_convertSizeFromEngineSpace:];
-[UILayoutGuide nsli_convertSizeToEngineSpace:];
-[UILayoutGuide nsli_defaultResolvedValue:forSymbolicConstant:inConstraint:error:];
-[UILayoutGuide nsli_description];
-[UILayoutGuide nsli_engineToUserScalingCoefficients];
-[UILayoutGuide nsli_heightVariable];
-[UILayoutGuide nsli_installedConstraints];
-[UILayoutGuide nsli_isCollectingConstraintChangesForLaterCoordinatedFlush:];
-[UILayoutGuide nsli_isFlipped];
-[UILayoutGuide nsli_isLegalConstraintItem];
-[UILayoutGuide nsli_isRTL];
-[UILayoutGuide nsli_layoutEngine];
-[UILayoutGuide nsli_layoutMarginsItem];
-[UILayoutGuide nsli_lowerAttribute:intoExpression:withCoefficient:container:];
-[UILayoutGuide nsli_lowerAttribute:intoExpression:withCoefficient:forConstraint:];
-[UILayoutGuide nsli_marginOffsetForAttribute:];
-[UILayoutGuide nsli_removeConstraint:];
-[UILayoutGuide nsli_resolvedValue:forSymbolicConstant:inConstraint:error:];
-[UILayoutGuide nsli_superitem];
-[UILayoutGuide nsli_widthVariable];
-[UILayoutGuide rightAnchor];
-[UILayoutGuide set_ui_frame:];
-[UILayoutGuide set_ui_usesManualLayout:];
-[UILayoutGuide topAnchor];
-[UILayoutGuide trailingAnchor];
-[UILayoutGuide widthAnchor];
```
