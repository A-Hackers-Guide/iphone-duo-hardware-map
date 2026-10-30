# `SBChainableModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 2 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _handled;
@"NSString" _handledReason;
```

## Properties

```
@property (TB,R,N,GisHandled,V_handled) handled;
@property (T@"NSString",R,C,N,V_handledReason) handledReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBChainableModifierEvent succinctDescriptionBuilder];
-[SBChainableModifierEvent descriptionWithMultilinePrefix:];
-[SBChainableModifierEvent succinctDescription];
-[SBChainableModifierEvent loggingCategory];
-[SBChainableModifierEvent description];
-[SBChainableModifierEvent copyWithZone:];
-[SBChainableModifierEvent descriptionBuilderWithMultilinePrefix:];
-[SBChainableModifierEvent handleWithReason:];
-[SBChainableModifierEvent handledReason];
-[SBChainableModifierEvent isHandled];
-[SBChainableModifierEvent isSwitcherModifierEvent];
-[SBChainableModifierEvent isWindowingModifierActivity];
-[SBChainableModifierEvent switcherModifierEvent];
-[SBChainableModifierEvent unhandledCopy];
-[SBChainableModifierEvent windowingModifierActivity];
```
