# `SBRequestSystemApertureElementSuppressionEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _wantsGlobalSuppression;
B _wantsKeyLineEnabled;
@"SBAppLayout" _appLayout;
@"NSUUID" _invalidationIdentifier;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (T@"NSUUID",R,N,V_invalidationIdentifier) invalidationIdentifier;
@property (TB,R,N,V_wantsGlobalSuppression) wantsGlobalSuppression;
@property (TB,R,N,V_wantsKeyLineEnabled) wantsKeyLineEnabled;
```

## Instance methods

```
-[SBRequestSystemApertureElementSuppressionEventResponse appLayout];
-[SBRequestSystemApertureElementSuppressionEventResponse type];
-[SBRequestSystemApertureElementSuppressionEventResponse descriptionBuilderWithMultilinePrefix:];
-[SBRequestSystemApertureElementSuppressionEventResponse initWithAppLayout:wantsGlobalSuppression:wantsKeyLineEnabled:invalidationIdentifier:];
-[SBRequestSystemApertureElementSuppressionEventResponse invalidationIdentifier];
-[SBRequestSystemApertureElementSuppressionEventResponse wantsGlobalSuppression];
-[SBRequestSystemApertureElementSuppressionEventResponse wantsKeyLineEnabled];
```
