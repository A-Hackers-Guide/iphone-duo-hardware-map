# `SBChainableModifierEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 7 properties, 25 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _childResponses;
B _consumed;
d _delay;
@? _validator;
```

## Properties

```
@property (TB,R,N,GisValid) valid;
@property (Td,R,N,V_delay) delay;
@property (T@"NSArray",C,N) childResponses;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBChainableModifierEventResponse newEventResponse];
+[SBChainableModifierEventResponse responseByAppendingResponse:toResponse:];
```

## Instance methods

```
-[SBChainableModifierEventResponse succinctDescriptionBuilder];
-[SBChainableModifierEventResponse init];
-[SBChainableModifierEventResponse descriptionWithMultilinePrefix:];
-[SBChainableModifierEventResponse succinctDescription];
-[SBChainableModifierEventResponse delay];
-[SBChainableModifierEventResponse loggingCategory];
-[SBChainableModifierEventResponse isValid];
-[SBChainableModifierEventResponse description];
-[SBChainableModifierEventResponse descriptionBuilderWithMultilinePrefix:];
-[SBChainableModifierEventResponse isSwitcherModifierEventResponse];
-[SBChainableModifierEventResponse _initWithChildResponses:];
-[SBChainableModifierEventResponse addChildResponse:];
-[SBChainableModifierEventResponse addChildResponses:];
-[SBChainableModifierEventResponse childResponses];
-[SBChainableModifierEventResponse consumeWithReason:];
-[SBChainableModifierEventResponse enumerateChildResponsesUsingBlock:];
-[SBChainableModifierEventResponse enumerateResponseTreeUsingBlock:];
-[SBChainableModifierEventResponse enumerateResponseTreeUsingBlock:stop:];
-[SBChainableModifierEventResponse insertChildResponse:atIndex:];
-[SBChainableModifierEventResponse isWindowingModifierResponse];
-[SBChainableModifierEventResponse responseByTransformingResponseWithTransformer:];
-[SBChainableModifierEventResponse setChildResponses:];
-[SBChainableModifierEventResponse setDelay:withValidator:];
-[SBChainableModifierEventResponse switcherModifierEventResponse];
-[SBChainableModifierEventResponse windowingModifierResponse];
```
