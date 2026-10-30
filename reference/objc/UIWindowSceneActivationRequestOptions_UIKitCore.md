# `UIWindowSceneActivationRequestOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISceneActivationRequestOptions`
- Protocols: `NSCopying`
- 6 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
B __preserveLayout;
@"UISceneConfiguration" _quickLookSceneConfiguration;
Q _preferredPresentationStyle;
@"UIWindowScenePlacement" _placement;
@"NSString" __interactionIdentifier;
Q __preferredSizeCategory;
```

## Properties

```
@property (T@"NSString",C,N,S_setInteractionIdentifier:,V__interactionIdentifier) _interactionIdentifier;
@property (TB,R,N) _effectivelyWantsProminence;
@property (TB,R,N) _effectivelyWantsFullscreen;
@property (TB,R,N) _effectivelyWantsPreservedLayout;
@property (TB,R,N) _effectivelyWantsBackground;
@property (T@"_UIWindowScenePlacement",C,N,S_setPlacement:) _placement;
@property (T@"UISceneConfiguration",&,N,S_setQuickLookSceneConfiguration:,V_quickLookSceneConfiguration) _quickLookSceneConfiguration;
@property (TQ,N,S_setPreferredSizeCategory:,V__preferredSizeCategory) _preferredSizeCategory;
@property (TB,N,S_setPreserveLayout:,V__preserveLayout) _preserveLayout;
@property (TQ,N,V_preferredPresentationStyle) preferredPresentationStyle;
@property (T@"UIWindowScenePlacement",C,N,V_placement) placement;
```

## Instance methods

```
-[UIWindowSceneActivationRequestOptions setPlacement:];
-[UIWindowSceneActivationRequestOptions placement];
-[UIWindowSceneActivationRequestOptions copyWithZone:];
-[UIWindowSceneActivationRequestOptions descriptionBuilderWithMultilinePrefix:];
-[UIWindowSceneActivationRequestOptions _preserveLayout];
-[UIWindowSceneActivationRequestOptions _effectivelyWantsBackground];
-[UIWindowSceneActivationRequestOptions _effectivelyWantsFullscreen];
-[UIWindowSceneActivationRequestOptions _effectivelyWantsPreservedLayout];
-[UIWindowSceneActivationRequestOptions _effectivelyWantsProminence];
-[UIWindowSceneActivationRequestOptions _interactionIdentifier];
-[UIWindowSceneActivationRequestOptions _placement];
-[UIWindowSceneActivationRequestOptions _preferredSizeCategory];
-[UIWindowSceneActivationRequestOptions _quickLookSceneConfiguration];
-[UIWindowSceneActivationRequestOptions _setInteractionIdentifier:];
-[UIWindowSceneActivationRequestOptions _setPlacement:];
-[UIWindowSceneActivationRequestOptions _setPreferredSizeCategory:];
-[UIWindowSceneActivationRequestOptions _setPreserveLayout:];
-[UIWindowSceneActivationRequestOptions _setQuickLookSceneConfiguration:];
-[UIWindowSceneActivationRequestOptions preferredPresentationStyle];
-[UIWindowSceneActivationRequestOptions setPreferredPresentationStyle:];
```
