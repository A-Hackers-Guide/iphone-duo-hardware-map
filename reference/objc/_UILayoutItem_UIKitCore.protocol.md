# `_UILayoutItem` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSLayoutItem`
- 0 instance variables, 10 properties, 34 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[_UILayoutItem nsli_boundsHeightVariable];
-[_UILayoutItem nsli_minYVariable];
-[_UILayoutItem _uili_requiresObservationForVariable:];
-[_UILayoutItem nsli_boundsWidthVariable];
-[_UILayoutItem _uili_isFocusGuide];
-[_UILayoutItem _boundsHeightVariable];
-[_UILayoutItem nsli_minXVariable];
-[_UILayoutItem _minXVariable];
-[_UILayoutItem _boundsWidthVariable];
-[_UILayoutItem _minYVariable];
-[_UILayoutItem _uili_removeLayoutVariableObservationsOnlyToSupportTAMICChange:];
-[_UILayoutItem _faultInGuidesForConstraint:];
-[_UILayoutItem _referenceView];
-[_UILayoutItem _uili_existingBaseFrameVariables];
-[_UILayoutItem _uili_existingObservationEligibleLayoutVariables];
-[_UILayoutItem _uili_observableLayoutEngineForBaseFrameVariables:];
-[_UILayoutItem _uili_stashLayoutVariableObservation:forVariable:];
-[_UILayoutItem bottomAnchor];
-[_UILayoutItem centerXAnchor];
-[_UILayoutItem centerYAnchor];
-[_UILayoutItem heightAnchor];
-[_UILayoutItem leadingAnchor];
-[_UILayoutItem leftAnchor];
-[_UILayoutItem nsli_defaultResolvedValue:forSymbolicConstant:inConstraint:error:];
-[_UILayoutItem nsli_heightVariable];
-[_UILayoutItem nsli_widthVariable];
-[_UILayoutItem rightAnchor];
-[_UILayoutItem topAnchor];
-[_UILayoutItem trailingAnchor];
-[_UILayoutItem widthAnchor];
-[_UILayoutItem _contentHeightVariable];
-[_UILayoutItem _contentWidthVariable];
-[_UILayoutItem nsli_contentHeightVariable];
-[_UILayoutItem nsli_contentWidthVariable];
```
