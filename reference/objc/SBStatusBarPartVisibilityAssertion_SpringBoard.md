# `SBStatusBarPartVisibilityAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSSimpleAssertion`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIStatusBar" _statusBar;
@"NSMutableSet" _hiddenParts;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStatusBarPartVisibilityAssertion succinctDescriptionBuilder];
-[SBStatusBarPartVisibilityAssertion descriptionWithMultilinePrefix:];
-[SBStatusBarPartVisibilityAssertion succinctDescription];
-[SBStatusBarPartVisibilityAssertion descriptionBuilderWithMultilinePrefix:];
-[SBStatusBarPartVisibilityAssertion _setStatusBarPartWithIdentifier:hidden:animatedWithDuration:];
-[SBStatusBarPartVisibilityAssertion initWithIdentifier:statusBar:forReason:];
-[SBStatusBarPartVisibilityAssertion isHidingStatusBarPartWithIdentifier:];
-[SBStatusBarPartVisibilityAssertion setStatusBarPartWithIdentifier:hidden:animated:];
-[SBStatusBarPartVisibilityAssertion setStatusBarPartWithIdentifier:hidden:animatedWithDuration:];
```
