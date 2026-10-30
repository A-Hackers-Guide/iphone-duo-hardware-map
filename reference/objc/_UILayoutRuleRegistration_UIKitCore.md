# `_UILayoutRuleRegistration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UILayoutRuleEvaluationContext`
- 4 instance variables, 9 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@? _evaluationHandler;
{?="layoutMargins"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"reversesLayoutDirection"B"safeAreaInsets"{UIEdgeInsets="top"d"left"d"bottom"d"right"d}"size"{CGSize="width"d"height"d}} _layoutInfo;
@"UITraitCollection" _parentTraitCollection;
```

## Properties

```
@property (T{CGSize=dd},R,N) size;
@property (T@"UITraitCollection",R,N) traitCollection;
@property (T{NSDirectionalEdgeInsets=dddd},R,N) directionalLayoutMargins;
@property (T{UIEdgeInsets=dddd},R,N) layoutMargins;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UILayoutRuleRegistration layoutMargins];
-[_UILayoutRuleRegistration directionalLayoutMargins];
-[_UILayoutRuleRegistration safeAreaInsets];
-[_UILayoutRuleRegistration traitCollection];
-[_UILayoutRuleRegistration size];
```
