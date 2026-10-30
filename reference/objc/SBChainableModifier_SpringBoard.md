# `SBChainableModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBChainableModifierQuery`, `SBChainableModifierContext`, `NSCopying`
- 11 instance variables, 14 properties, 59 instance methods, 17 class methods

## Instance variables

```
B _hasNotifiedChildrenDidMoveToParent;
@"SBChainableModifierMethodCache" _queryCache;
@"SBChainableModifierMethodCache" _contextCache;
@"SBChainableModifierMethodCache" _eventCache;
@"SBChainableModifier" _parentModifier;
@"<SBChainableModifierDelegate>" _delegate;
q _state;
@"SBChainableModifier" _previousContextModifier;
@"SBChainableModifier" _nextQueryModifier;
q _modifierLevel;
@"NSString" _key;
```

## Properties

```
@property (T@"SBChainableModifier",N,V_parentModifier) parentModifier;
@property (T@"SBChainableModifier",N,V_previousContextModifier) previousContextModifier;
@property (T@"SBChainableModifier",&,N,V_nextQueryModifier) nextQueryModifier;
@property (T@"SBModifierCacheCoordinator",&,N) queryCacheCoordinator;
@property (T@"SBModifierCacheCoordinator",&,N) contextCacheCoordinator;
@property (T@"SBModifierCacheCoordinator",&,N) eventCacheCoordinator;
@property (Tq,N,V_state) state;
@property (Tq,N,V_modifierLevel) modifierLevel;
@property (T@"NSString",C,N,V_key) key;
@property (T@"<SBChainableModifierDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBChainableModifier initialize];
+[SBChainableModifier newContextCache];
+[SBChainableModifier contextProtocol];
+[SBChainableModifier _initalizeIMPCaching];
+[SBChainableModifier baseClassForQueryProtocol];
+[SBChainableModifier contextSelectors];
+[SBChainableModifier eventSelectors];
+[SBChainableModifier makeDynamicSubclassWithDescriptor:implementation:forSelector:ofProtocol:];
+[SBChainableModifier modifierUnderTest:containsChildModifierKindOfClass:];
+[SBChainableModifier newCacheWithSelectorList:subsequentMethodCacheFunc:cachingDictionary:];
+[SBChainableModifier newEventCache];
+[SBChainableModifier newEventResponse];
+[SBChainableModifier newQueryCache];
+[SBChainableModifier queryProtocol];
+[SBChainableModifier querySelectors];
+[SBChainableModifier updateProtocol];
+[SBChainableModifier verifyModifierImplements:methodsOfProtocol:];
```

## Instance methods

```
-[SBChainableModifier handleEvent:];
-[SBChainableModifier didMoveToParentModifier:];
-[SBChainableModifier setState:];
-[SBChainableModifier _handleEvent:];
-[SBChainableModifier succinctDescriptionBuilder];
-[SBChainableModifier init];
-[SBChainableModifier dealloc];
-[SBChainableModifier descriptionWithMultilinePrefix:];
-[SBChainableModifier setKey:];
-[SBChainableModifier completesWhenChildrenComplete];
-[SBChainableModifier succinctDescription];
-[SBChainableModifier loggingCategory];
-[SBChainableModifier setDelegate:];
-[SBChainableModifier delegate];
-[SBChainableModifier description];
-[SBChainableModifier copyWithZone:];
-[SBChainableModifier key];
-[SBChainableModifier state];
-[SBChainableModifier descriptionBuilderWithMultilinePrefix:];
-[SBChainableModifier enumerateChildModifiersWithBlock:];
-[SBChainableModifier _addChildModifier:atLevel:key:queryResponse:contextResponse:eventResponse:];
-[SBChainableModifier _anyDescendentImplementsAnyContextMethod];
-[SBChainableModifier _anyDescendentImplementsAnyEventMethod];
-[SBChainableModifier _anyDescendentImplementsAnyQueryMethod];
-[SBChainableModifier _forwardEvent:toChildModifier:];
-[SBChainableModifier _insertModifier:afterModifier:queryResponse:contextResponse:eventResponse:];
-[SBChainableModifier _lastDeepChildModifier];
-[SBChainableModifier _notifyChildrenDidMoveToParentIfNeeded];
-[SBChainableModifier _removeChildModifier:queryResponse:contextResponse:eventResponse:];
-[SBChainableModifier addChildModifier:];
-[SBChainableModifier addChildModifier:atLevel:key:];
-[SBChainableModifier childModifierByKey:];
-[SBChainableModifier childModifierCount];
-[SBChainableModifier containsChildModifier:];
-[SBChainableModifier contextCacheCoordinator];
-[SBChainableModifier debugPotentialChildModifiers];
-[SBChainableModifier eventCacheCoordinator];
-[SBChainableModifier isSwitcherModifier];
-[SBChainableModifier isWindowingModifier];
-[SBChainableModifier modifierLevel];
-[SBChainableModifier nextQueryModifier];
-[SBChainableModifier parentModifier];
-[SBChainableModifier performTransactionWithTemporaryChildModifier:usingBlock:];
-[SBChainableModifier previousContextModifier];
-[SBChainableModifier provideNextQueryImplementation:forSelector:];
-[SBChainableModifier providePreviousContextImplementation:forSelector:];
-[SBChainableModifier queryCacheCoordinator];
-[SBChainableModifier recomputeQueryCache];
-[SBChainableModifier removeChildModifier:];
-[SBChainableModifier responseForProposedChildResponse:childModifier:event:];
-[SBChainableModifier setContextCacheCoordinator:];
-[SBChainableModifier setEventCacheCoordinator:];
-[SBChainableModifier setModifierLevel:];
-[SBChainableModifier setNextQueryModifier:];
-[SBChainableModifier setParentModifier:];
-[SBChainableModifier setPreviousContextModifier:];
-[SBChainableModifier setQueryCacheCoordinator:];
-[SBChainableModifier verifyInternalIntegrityAfterHandlingEvent:];
-[SBChainableModifier willPerformAsTemporaryChildModifier];
```
